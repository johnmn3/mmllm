"""Capture per-layer NetBank input queries from the merged student model.

The naive distillation harvest used random Gaussian queries, which don't
match the distribution the real model produces. Result: student over-fit
to "teacher output at noise" and *regressed* format_validity (0.110 →
0.080) despite a 4× distill loss reduction.

This script forwards the merged student through FIM val.bin and records
the q_long_flat tensors at each layer's NetBank input via forward
pre-hooks. The output is a list-of-tensors-per-layer suitable for
sampling during distillation.

Output format:
  torch.save([torch.cat(layer_chunks_0, dim=0),
              torch.cat(layer_chunks_1, dim=0),
              ...], out_path)

  Each entry: (N_batches × B, T, q_dim) tensor of real q_long_flat values
  observed at that layer during the capture run.

Usage:
  python scripts/capture_queries.py \\
      --ckpt-dir /tmp/mmllm-cpu/eval-merged.ckpts \\
      --ckpt-step 5000 \\
      --bank-path /tmp/mmllm-cpu/fim-eval-bank \\
      --val-path  /tmp/mmllm-cpu/fim-json.val.bin \\
      --n-batches 100 \\
      --out /tmp/mmllm-cpu/captured-queries.pt
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Match the env contract the basilisp side reads.
os.environ.setdefault("MMLLM_NETBANK_ENABLED", "true")
os.environ.setdefault("MMLLM_NET_SQRT_N",      "1024")
os.environ.setdefault("MMLLM_NET_C_NET",       "32")
os.environ.setdefault("MMLLM_LONG_TIER_MIX",   "switch")
os.environ.setdefault("MMLLM_ALPHA_NET",       "true")
os.environ.setdefault("MMLLM_DEVICE",          "cpu")
os.environ.setdefault("MMLLM_BANK_ON_GPU",     "false")
os.environ.setdefault("MMLLM_NETBANK_ON_GPU",  "false")
os.environ.setdefault("MMLLM_NET_DTYPE",       "fp32")
os.environ.setdefault("MMLLM_NET_DELAY_MS_MIN", "0.0")
os.environ.setdefault("MMLLM_NET_DELAY_MS_MAX", "0.0")
os.environ.setdefault("MMLLM_NUM_THREADS",     "4")

import basilisp.main as bm
bm.init()
import basilisp.lang.keyword as kw
import basilisp.lang.runtime as rt

import torch

# This loads core.lpy and exposes its top-level defs as python attrs
# (kebab-case is converted; ! becomes __BANG__, ? becomes __Q__).
import mmllm.core as mc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--ckpt-dir",  required=True, type=Path,
                    help="checkpoint directory containing step-<N>/dense.pt")
    ap.add_argument("--ckpt-step", required=True, type=int,
                    help="step number inside ckpt-dir to load")
    ap.add_argument("--bank-path", required=True, type=str,
                    help="bank path prefix (Local V at <prefix>.<i>.bin, "
                         "NetBank V at <prefix>-net.<i>.bin)")
    ap.add_argument("--val-path",  required=True, type=Path,
                    help="FIM val.bin file to sample from")
    ap.add_argument("--n-batches", type=int, default=100)
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--seq-len",   type=int, default=128)
    ap.add_argument("--out",       required=True, type=Path,
                    help="output .pt file: list[Tensor] per layer")
    ap.add_argument("--seed",      type=int, default=42)
    args = ap.parse_args()

    torch.manual_seed(args.seed)

    # Construct cpu-tiny config with our memory-mmap-path
    # default_config_cpu_tiny is a basilisp PersistentMap.
    cfg = mc.default_config_cpu_tiny
    # Override :memory-mmap-path so the model mmaps at our bank-path.
    cfg = cfg.assoc(kw.keyword("memory-mmap-path"), args.bank_path)

    # Build model
    print(f"== capture-queries ==")
    print(f"  ckpt={args.ckpt_dir}/step-{args.ckpt_step}")
    print(f"  bank={args.bank_path}  val={args.val_path}")
    print(f"  n_batches={args.n_batches}  B={args.batch_size}  T={args.seq_len}")

    m = mc.build_model(cfg)

    # Build optimizers (load_checkpoint needs them as arguments to slot
    # the saved state into; we discard after loading).
    import torch.optim as optim
    opt_d  = optim.AdamW(list(mc.parameters(m)),                lr=1e-3)
    opt_s  = optim.SparseAdam(list(mc.sparse_parameters(m)),    lr=1e-3)
    opt_sn = None
    try:
        nbsps = list(mc.netbank_sparse_parameters(m))
        if nbsps:
            opt_sn = optim.SparseAdam(nbsps, lr=1e-3)
    except Exception as e:
        print(f"  (no NetBank sparse params? {e})")

    # Load checkpoint: load_checkpoint! signature is
    #   (m opt-dense opt-sparse [opt-sparse-net] ckpt-dir step)
    if opt_sn is not None:
        mc.load_checkpoint__BANG__(m, opt_d, opt_s, opt_sn,
                                   str(args.ckpt_dir), args.ckpt_step)
    else:
        mc.load_checkpoint__BANG__(m, opt_d, opt_s,
                                   str(args.ckpt_dir), args.ckpt_step)
    print(f"  loaded checkpoint")

    # Set eval mode — disables training-only paths (dropout, q-z-loss, etc.)
    mc.set_eval_mode__BANG__(m) if hasattr(mc, "set_eval_mode__BANG__") else None
    # Fallback if eval-mode setter isn't exposed: walk modules.
    # The model dict has :blocks etc. We need the actual python modules.
    # Easiest: iterate :blocks and call .eval() on the contained nn.Modules.
    # But m is a PersistentMap. Access via mc-side kw lookup:
    blocks_kw = kw.keyword("blocks")
    blocks = m.val_at(blocks_kw)
    n_layers = len(list(blocks))
    print(f"  model has {n_layers} blocks")

    # Register forward pre-hooks on each NetBank to capture inputs.
    captured = [[] for _ in range(n_layers)]
    netbank_kw = kw.keyword("netbank")
    handles = []
    for i, b in enumerate(blocks):
        nb = b.val_at(netbank_kw)
        if nb is None:
            print(f"  WARN block {i}: no :netbank — skip")
            continue
        nb.eval()
        # Also eval the other modules in the block for consistency
        for k_name in ("memory", "norm1", "norm2", "q-proj", "k-proj-s",
                       "v-proj-s", "k-proj-l", "v-proj-l", "o-proj",
                       "gate-proj", "up-proj", "down-proj",
                       "bank-query", "bank-feedback", "long-gate"):
            sub = b.val_at(kw.keyword(k_name))
            if sub is not None and hasattr(sub, "eval"):
                sub.eval()
        def make_hook(layer):
            def hook(module, args):
                # args is (q,). Capture q.
                q = args[0].detach().cpu().clone()
                captured[layer].append(q)
            return hook
        h = nb.register_forward_pre_hook(make_hook(i))
        handles.append(h)

    # Eval tok-emb / norm-final
    for k_name in ("tok-emb", "norm-final"):
        sub = m.val_at(kw.keyword(k_name))
        if sub is not None and hasattr(sub, "eval"):
            sub.eval()

    # Load val.bin as a uint8 tensor
    val_bytes = args.val_path.read_bytes()
    val_tensor = torch.frombuffer(bytearray(val_bytes), dtype=torch.uint8)
    n_tokens = val_tensor.numel()
    T = args.seq_len
    B = args.batch_size
    print(f"  val.bin: {n_tokens} tokens")

    # Forward N batches with grad disabled
    n_positions = n_tokens - T - 1
    torch.set_grad_enabled(False)
    try:
        import time
        t0 = time.time()
        for step in range(args.n_batches):
            offsets = torch.randint(0, n_positions, (B,))
            inputs = torch.stack(
                [val_tensor[off:off + T].long() for off in offsets.tolist()],
                dim=0,
            )
            _ = mc.forward(m, inputs)
            if (step + 1) % 20 == 0 or step == 0:
                el = time.time() - t0
                print(f"  step {step+1}/{args.n_batches}  ({el:.1f}s)")
    finally:
        torch.set_grad_enabled(True)

    # Remove hooks
    for h in handles:
        h.remove()

    # Concatenate per-layer captures
    print(f"  per-layer capture chunks: {[len(c) for c in captured]}")
    consolidated = []
    for layer, chunks in enumerate(captured):
        if not chunks:
            consolidated.append(None)
            continue
        t = torch.cat(chunks, dim=0)   # (N_batches * B, T, q_dim)
        consolidated.append(t)
        print(f"  layer {layer}: {tuple(t.shape)}  norm={t.norm().item():.2f}  "
              f"std={t.std().item():.4f}  mean={t.mean().item():.4f}")

    # Save
    args.out.parent.mkdir(parents=True, exist_ok=True)
    torch.save(consolidated, args.out)
    print(f"  wrote {args.out} ({args.out.stat().st_size / 1024**2:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
