"""Inference test for f256round100 — the head of the last chain.

Two things:
  (1) PROSE QUALITY per skill-module — generate ~120 bytes autoregressively
      routed to each of [text, math, agentic, code] in turn (by pinning the
      modular NetBank's active set to a single module), decode bytes->text,
      print labeled samples.
  (2) TOKEN SPEED — warm decode tok/s (single-stream autoregressive) and a
      prefill throughput probe (B=1, T=1024), like scripts/inf_speed.py.

Loads f256round100 with its TRAINED dense weights (dense_named.pt, by NAME —
the trunk/router/embeddings/attn/gates/norms; WITHOUT this the prose is
garbage) and streams its on-disk modular NetBanks (f256round100-bank-net.*.bin)
via VSTREAM. Drives the MLX `model.forward` autoregressively (no KV-cache in
the MLX eval path — re-runs forward on the growing sequence; fine for ~120 tok).

Run (PAUSE TRAINING FIRST — this contends for RAM/disk with the running chain):
  PYTHONPATH=/Users/john/models/genesis/mmllm-src \
    /Users/john/src/mmllm/.venv/bin/python3 \
    /Users/john/models/genesis/scripts/inf_test_f256.py
"""
import os, sys, time, glob
import numpy as np

G = os.path.expanduser("~/models/genesis")
MODS = "text,math,agentic,code"
# Which round to test — pass as argv[1] or $INF_ROUND; defaults to the last chain head.
# e.g.  inf_test_f256.py f256xround50   (re-run on a later round as the chain progresses)
ROUND = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("INF_ROUND", "f256round100")
# <ROUND> training config (the config it was trained with).
os.environ.update({
    "MMLLM_DEVICE": "cpu", "MMLLM_NETBANK_ENABLED": "true", "MMLLM_NET_MODULES": MODS,
    "MMLLM_NET_SQRT_N": "256", "MMLLM_NET_N_BLOCKS": "160",
    "MMLLM_NET_VQ": "true", "MMLLM_NET_VSTREAM": "true",
    "MMLLM_NET_C_NET": "8", "MMLLM_NET_TOP_K": "128", "MMLLM_NET_SUB_TOP_K": "16",
    "MMLLM_BANK_ON_GPU": "false", "MMLLM_NET_BANK_ON_GPU": "false",
    "MMLLM_NET_ROUTER": "true", "MMLLM_NET_ROUTER_DRIVE": "true",
    # 0 = ALL modules live at inference (per design); K_TOK=2 per-token Level-2.
    "MMLLM_NET_ROUTER_K_LOAD": "0", "MMLLM_NET_ROUTER_K_TOK": "2",
    "MMLLM_NET_STREAM_LR": "0.003", "MMLLM_NET_Z_COEF": "0.1",
})

import basilisp.main; basilisp.main.init()
import mmllm.core as C, mmllm.mlx.trainer as TR, mmllm.mlx.model as MD
import mlx.core as mx, basilisp.lang.keyword as kw, torch
K = kw.keyword
mx.set_cache_limit(1 << 30)

# ---- build the model: WIDE trunk d_model=256 d_ff=768, banks mmap'd at the
#      f256round100-bank prefix (-> f256round100-bank-net.<layer>.bin) ----
cfg = (C.default_config_cpu_mini
       .assoc(K("d-model"), 256).assoc(K("d-ff"), 768)
       .assoc(K("memory-mmap-path"), f"{G}/{ROUND}-bank"))
m = C.build_model(cfg)

# ---- load the TRAINED dense weights BY NAME (module-growth-safe; mirrors
#      trainer.py ~575-591 resume path). dense_named.pt is torch-saved. ----
_cks = sorted(glob.glob(f"{G}/{ROUND}.ckpts/step-*/dense_named.pt"))   # latest step for this round
if not _cks: sys.exit(f"no ckpt for round {ROUND} ({G}/{ROUND}.ckpts/step-*/dense_named.pt)")
ckpt = _cks[-1]
nd = torch.load(ckpt, map_location="cpu", weights_only=False)
nl = sk = 0
for n, p in TR._named_params(m, K).items():
    s = nd.get(n)
    if s is not None and tuple(p.shape) == tuple(s.shape):
        p.data.copy_(s.to(p.dtype)); nl += 1
    else:
        sk += 1
print(f"[load] {nl} dense params BY NAME from {os.path.relpath(ckpt, G)} "
      f"({sk} unmatched/new) | banks={len(glob.glob(f'{G}/{ROUND}-bank-net.*.bin'))}",
      flush=True)

# ---- extract -> reassemble into the MLX functional param tree ----
trainable, static, meta = TR._extract(m, K, mx.array(np.zeros(1, np.int64)))
static = dict(static)
vocab = m.get(K("tok-emb")).weight.shape[0]
print(f"[load] vocab={vocab} (byte-level) | n_blocks={len(meta.get('blocks', [])) if isinstance(meta, dict) else '?'}",
      flush=True)


def reassemble(net_active):
    """Rebuild P with the modular NetBank pinned to `net_active`
    (None=all modules composed; [name]=route ONLY to that module)."""
    s = dict(static); s["_net_active"] = net_active
    return TR._reassemble(trainable, s, meta)


def generate(P, prompt, n, greedy=True, temp=0.7):
    """Autoregressive byte generation against MLX model.forward (no KV cache:
    re-runs the full growing sequence each step)."""
    ids = np.frombuffer(prompt.encode("utf-8"), dtype=np.uint8).astype(np.int64)
    cur = mx.array(ids[None, :])
    out = []
    for _ in range(n):
        logits = MD.forward(P, cur)            # (1, T, vocab)
        last = logits[:, -1, :]                # (1, vocab)
        if greedy:
            nxt = mx.argmax(last, axis=-1)
        else:
            nxt = mx.random.categorical(last * (1.0 / temp))
        mx.eval(nxt)
        tok = int(np.array(nxt).reshape(-1)[0])
        out.append(tok)
        cur = mx.concatenate([cur, mx.array(np.array([[tok]], dtype=np.int64))], axis=1)
    return bytes(bytearray(out)).decode("utf-8", errors="replace")


# ============================== (1) PROSE =================================
PROMPTS = {
    "text":    "<|im_start|>user\nWrite a short story about a lighthouse keeper.<|im_end|>\n<|im_start|>assistant\n",
    "math":    "<|im_start|>user\nWhat is 17 + 25? Explain step by step.<|im_end|>\n<|im_start|>assistant\n",
    "agentic": "<|im_start|>user\nPlan the steps to book a flight from a CLI tool.<|im_end|>\n<|im_start|>assistant\n",
    "code":    "<|im_start|>user\nWrite a Python function to reverse a string.<|im_end|>\n<|im_start|>assistant\n",
}
print("\n=== (1) PROSE QUALITY — per skill-module (routed to single module) ===", flush=True)
for mod in ["text", "math", "agentic", "code"]:
    P = reassemble([mod])                      # pin active set to ONLY this module
    pr = PROMPTS[mod]
    t0 = time.time()
    g = generate(P, pr, 120, greedy=True)
    s = generate(P, pr, 120, greedy=False, temp=0.7)
    print("-" * 72, flush=True)
    print(f"[module={mod}]  ({time.time()-t0:.1f}s for 2x120 tok)", flush=True)
    print(f"  prompt: {pr.splitlines()[1]!r}", flush=True)
    print(f"  greedy: {g!r}", flush=True)
    print(f"  temp07: {s!r}", flush=True)

# ============================== (2) SPEED ================================
print("\n=== (2) TOKEN SPEED — all modules live (net_active=None) ===", flush=True)
P = reassemble(None)

# decode tok/s (single-stream autoregressive, warm)
generate(P, "Hello", 8, greedy=True)           # warm: page-in banks / JIT
t0 = time.time(); N = 64
generate(P, "The quick brown fox", N, greedy=True)
dt = time.time() - t0
print(f"  decode (B=1, autoregressive): {N} tok in {dt:.2f}s = {N/dt:.1f} tok/s (warm)", flush=True)

# prefill throughput (B=1, T=1024), like inf_speed.py
rng = np.random.default_rng(0)
xb = mx.array(rng.integers(0, vocab, size=(1, 1024)).astype(np.int64))
o = MD.forward(P, xb); mx.eval(o)              # warm
ts = []
for _ in range(3):
    xb = mx.array(rng.integers(0, vocab, size=(1, 1024)).astype(np.int64))
    t0 = time.time(); o = MD.forward(P, xb); mx.eval(o); ts.append(time.time() - t0)
print(f"  prefill (B=1, T=1024): warm={np.median(ts)*1000:.0f}ms "
      f"({1024/np.median(ts):.0f} tok/s)", flush=True)
print("=== DONE ===", flush=True)
