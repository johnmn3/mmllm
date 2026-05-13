"""Inf-spork eval: bpc quality + TPS bench against the chain end-state.

Loads cpu-mini config, mmap-binds the V_local + V_net banks, loads
dense.pt from the chain end. Then:
  1. Runs eval-bpc on val data (quality)
  2. Runs warmup + timed batched-decode for B in {1, 16} (tps)

Invoked from scripts/build_inf_spork.sh after staging.

Args:
  argv[1]: base path (e.g. /tmp/mmllm-cpu/inf-spork.fim)
  argv[2]: bank path (e.g. /tmp/mmllm-cpu/inf-spork.bank)
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

# Bootstrap basilisp so mmllm.core compiles.
from mmllm._entry import _patch_torch
_patch_torch()
from basilisp.main import init
init()

import torch
import torch.nn.functional as F

# Now mmllm.core is a real Python module (basilisp-compiled).
import mmllm.core as core
import basilisp.lang.keyword as bkw


def K(s):
    return bkw.keyword(s)


def main():
    base = sys.argv[1]
    bank = sys.argv[2]

    # cpu-mini config + mmap bank (basilisp PersistentMap)
    cfg = core.default_config_cpu_mini
    cfg = cfg.assoc(K("memory-mmap-path"), bank)
    cfg = cfg.assoc(K("device"), "cpu")
    cfg = cfg.assoc(K("bank-on-gpu"), False)
    cfg = cfg.assoc(K("net-bank-on-gpu"), False)

    print(f"  Building cpu-mini model (mmap bank={bank})…")
    m = core.build_model(cfg)
    device = m.val_at(K("device"))

    # Load dense from chain end
    ckpt_path = f"{base}.ckpts/step-1/dense.pt"
    saved = list(torch.load(ckpt_path, map_location=device, weights_only=False))
    print(f"  Loaded {ckpt_path}: {len(saved)} dense tensors")
    params = list(core.parameters(m))
    print(f"  Model has {len(params)} dense param tensors")
    n_loaded = 0
    n_skipped = 0
    for p, s in zip(params, saved):
        if p.data.shape == s.shape:
            p.data.copy_(s)
            n_loaded += 1
        else:
            n_skipped += 1
    print(f"  Loaded {n_loaded} / skipped {n_skipped} param tensors (shape mismatches)")

    core.set_eval_mode__BANG__(m)
    torch.set_grad_enabled(False)

    # ---------- Quality: eval-bpc (basilisp path — single-shot eval) ----------
    print("\n  ── eval-bpc on val ──")
    val_path = f"{base}.val.bin"
    import mmllm.corpus as corp
    val_data = corp.load_as_tensor(val_path)
    t0 = time.time()
    # eval-bpc args: m val-data T B max-toks
    r = core.eval_bpc(m, val_data, 128, 16, 25000)
    dt_eval = time.time() - t0
    bpc = r.val_at(K("bpc"))
    ppl = r.val_at(K("ppl"))
    print(f"  eval bpc={bpc:.4f}  ppl={ppl:.4f}  over 25000 tokens  wall={dt_eval:.1f}s")

    # ---------- TPS benchmark: TWO paths for comparison ----------
    # 1. basilisp sample_batch (the existing CLI path)
    # 2. pure-Python forward via mmllm.inference (skips basilisp dispatch)
    from mmllm.inference import unpack_model, bench_decode
    bundle = unpack_model(m)
    prompt = "the quick brown fox jumps over the lazy dog. "

    for B, n_warm, n_time in [(1, 20, 100), (16, 10, 50)]:
        print(f"\n  ── TPS bench B={B}  warm={n_warm} time={n_time} ──")

        # --- basilisp path
        core.sample_batch(m, prompt, n_warm, B)
        t0 = time.time()
        core.sample_batch(m, prompt, n_time, B)
        dt_bas = time.time() - t0
        per_bas = n_time / dt_bas
        agg_bas = B * per_bas
        print(f"  basilisp:    per_seq={per_bas:7.2f} tok/s  agg={agg_bas:8.2f} tok/s  ({1000*dt_bas/n_time:5.1f} ms/tok)")

        # --- pure-Python path
        r = bench_decode(bundle, prompt, n_warm, n_time, B)
        speedup = r["per_seq_tps"] / per_bas
        print(f"  pure-Python: per_seq={r['per_seq_tps']:7.2f} tok/s  agg={r['aggregate_tps']:8.2f} tok/s  ({r['ms_per_tok']:5.1f} ms/tok)  → {speedup:.2f}× basilisp")


if __name__ == "__main__":
    main()
