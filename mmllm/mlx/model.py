"""MLX model forward: token embedding -> N blocks -> final RMSNorm -> weight-tied
LM head. Mirrors core.lpy `forward` (eval/no-cache path). Pure function of
(params, tokens) so it composes with mx.value_and_grad in Stage 2.

`params` is a dict:
  {"tok_emb": (vocab,d_model), "norm_final_w": (d_model,), "norm_final_eps": f,
   "rope_cos","rope_sin": (max_pos,head_dim), "blocks": [block_param_dict, ...]}
Each block_param_dict is what blocks.block_forward consumes.
"""
from __future__ import annotations

import mlx.core as mx

from mmllm.mlx import blocks
from mmllm.mlx import ngram as _ngram
from mmllm.mlx import mamba as _mamba
from mmllm.mlx import chunker as _chunker


def _embed(params, tokens):
    """Byte embedding + (Phase C) n-gram hash features. No "ngram" key in
    params (MMLLM_NGRAM_HASH unset) -> returns the plain lookup, byte-identical
    to the pre-Phase-C path."""
    x = params["tok_emb"][tokens]
    ng = params.get("ngram")
    if ng is not None:
        x = x + _ngram.ngram_embed(ng["tables"], ng["specs"], tokens)
    return x


def mtp_loss(mtp_logits, yb, n_heads, coef, decay, vocab, loss_mask=None):
    """Phase C MTP loss (MLX, source of truth). Mirrors core.lpy collect-mtp-loss:
    head k (k=0..n-1) predicts the byte at offset t+(k+2); per-head CE summed with
    geometric decay coef·γ^k. At n_heads=1 this is the legacy single t+2 head.

    mtp_logits: (B,T,n*vocab). yb: (B,T) int. Returns a scalar mx.array."""
    if mtp_logits is None or not coef:
        return mx.array(0.0)
    B, T, _ = mtp_logits.shape
    aux = mtp_logits.reshape(B, T, n_heads, vocab)
    total = mx.array(0.0)
    for k in range(n_heads):
        win = T - 1 - k                                  # valid positions 0..T-2-k
        if win <= 0:
            break
        a_k = aux[:, :win, k, :].reshape(-1, vocab).astype(mx.float32)
        y_k = yb[:, k + 1:k + 1 + win].reshape(-1)
        logp = a_k - mx.logsumexp(a_k, axis=-1, keepdims=True)
        ce_tok = -mx.take_along_axis(logp, y_k[:, None], axis=-1)[:, 0]   # (B*win,)
        if loss_mask is not None:
            mk = loss_mask[:, :win].reshape(-1)
            ce = (ce_tok * mk).sum() / mx.maximum(mk.sum(), mx.array(1.0))
        else:
            ce = ce_tok.mean()
        total = total + coef * (decay ** k) * ce
    return total


def _hnet_encode(params, x):
    """Phase B spine — bytes->Mamba enc->cosine chunker. Returns
    (seq, hn) where seq is the chunk-rate residual stream the transformer runs on
    and hn carries the dechunk bookkeeping (chunk_id, confidence, p/b stats).
    No "hnet" key (MMLLM_HNET unset) -> (x, None): byte-identical bypass."""
    hnet = params.get("hnet")
    if hnet is None:
        return x, None
    xhat = _mamba.mamba_stack(hnet.get("enc", []), x)            # full byte rate
    z, keep_idx, valid, chunk_id, p, b, c = _chunker.chunk(xhat, hnet["W_q"], hnet["W_k"])
    if hnet.get("conf_gate"):                                    # down-weight low-conf chunks
        c_chunk = mx.take_along_axis(c, keep_idx, axis=1)        # per-chunk confidence
        z = z * c_chunk[..., None]
    hn = {"chunk_id": chunk_id, "c": c, "p": p, "b": b,
          "smooth": bool(hnet.get("smooth")), "dec": hnet.get("dec", [])}
    # stash ratio loss + boundary stats so the caller (loss_fn / harness) can read
    # them without changing the forward's return arity (mirrors mtp's in-tuple add).
    N = float(hnet.get("target_n", 6))
    hnet["ratio_loss"] = _chunker.ratio_loss(p, b, N)
    hnet["cut_rate"] = mx.mean(b)
    # Static-bound bookkeeping: #rows whose real boundary count exceeded the
    # static max_chunks bound (clamped+masked gracefully in the chunker). Stashed
    # as a LAZY scalar (no host-sync in the trace). Only float()'d when the
    # MMLLM_HNET_DEBUG diagnostic is explicitly enabled — default path stays
    # sync-free and byte-identical to the old dynamic gather.
    hnet["chunk_overflow"] = _chunker.overflow_count(b)
    import os as _os
    if _os.environ.get("MMLLM_HNET_DEBUG", "").lower() in ("1", "true", "yes"):
        _ov = int(hnet["chunk_overflow"].item())
        if _ov:
            print(f"  [HNET] chunk overflow: {_ov} row(s) exceeded static "
                  f"max_chunks={_chunker.max_chunks_bound(xhat.shape[1])} "
                  f"(clamped+masked)", flush=True)
    return z, hn


def _hnet_decode(params, seq, hn):
    """STE dechunk chunk-rate seq -> byte rate, then Mamba decoder. Identity when
    hn is None (no hnet)."""
    if hn is None:
        return seq
    seq = _chunker.dechunk(seq, hn["chunk_id"], hn["c"], smooth=hn["smooth"])
    return _mamba.mamba_stack(hn["dec"], seq)


def forward(params, tokens, collect_aux=False):
    """tokens: int array (B,T) -> logits (B,T,vocab). Weight-tied LM head.
    When collect_aux, returns
      (logits, distill_total, z_total, net_z_total, router_logits, n_distill,
       mtp_logits) where the totals SUM the per-block aux terms (n_distill =
    #blocks contributing a distill term). mtp_logits (Phase C) is (B,T,n*vocab)
    when an MTP head is present in params, else None.

    Phase B (MMLLM_HNET): when params carries an "hnet" dict, the byte stream is
    Mamba-encoded, cosine-chunked, the transformer block loop runs on CHUNKS, then
    STE-dechunked + Mamba-decoded back to byte rate before the final norm + LM
    head. No "hnet" key -> byte-identical to the pre-Phase-B transformer path."""
    x = _embed(params, tokens)                          # embedding lookup (+ n-gram)
    cos = params["rope_cos"]; sin = params["rope_sin"]
    seq, hn = _hnet_encode(params, x)                   # Phase B encode+chunk (or bypass)
    if not collect_aux:
        for b in params["blocks"]:
            seq = blocks.block_forward(b, seq, cos, sin)
        seq = _hnet_decode(params, seq, hn)             # Phase B dechunk+decode (or bypass)
        seq = blocks._rms_norm(seq, params["norm_final_w"], params["norm_final_eps"])
        return seq @ params["tok_emb"].T
    distill_total = mx.array(0.0); z_total = mx.array(0.0)
    net_z_total = mx.array(0.0); n_distill = 0
    router_logits_total = None       # Σ per-block module logits (B,T,N) for the aux loss
    # Gradient checkpointing: recompute each block's forward during the backward
    # instead of retaining all intermediates (the backward graph was ~20× the
    # forward — that's the real memory hog). Only the residual handoff between
    # blocks is kept. The netbank stream_combine's disk side-effect lives in its
    # VJP (fires once in backward); the recomputed forward only re-READS rows
    # (idempotent), so checkpointing is safe here. Gated by MMLLM_MLX_GRAD_CKPT.
    import os as _os
    _ck = _os.environ.get("MMLLM_MLX_GRAD_CKPT", "").lower() in ("1", "true", "yes")
    _bf = (mx.checkpoint(lambda bb, xx, c, s: blocks.block_forward(bb, xx, c, s, collect_aux=True))
           if _ck else None)
    for b in params["blocks"]:
        if _ck:
            seq, distill, z, net_z, rlogits = _bf(b, seq, cos, sin)
        else:
            seq, distill, z, net_z, rlogits = blocks.block_forward(b, seq, cos, sin, collect_aux=True)
        if distill is not None:
            distill_total = distill_total + distill; n_distill += 1
        if z is not None:
            z_total = z_total + z
        if net_z is not None:
            net_z_total = net_z_total + net_z
        if rlogits is not None:
            router_logits_total = rlogits if router_logits_total is None else router_logits_total + rlogits
    seq = _hnet_decode(params, seq, hn)                 # Phase B dechunk+decode (or bypass)
    x = blocks._rms_norm(seq, params["norm_final_w"], params["norm_final_eps"])
    logits = x @ params["tok_emb"].T
    # Phase C: MTP byte heads on the post-decoder hidden state. mtp_head_w is
    # (n*vocab, d_model) (a torch Linear weight) -> mtp_logits (B,T,n*vocab).
    # No head in params -> None (unchanged loss path).
    mtp_w = params.get("mtp_head_w")
    mtp_logits = (x @ mtp_w.T) if mtp_w is not None else None
    return logits, distill_total, z_total, net_z_total, router_logits_total, n_distill, mtp_logits
