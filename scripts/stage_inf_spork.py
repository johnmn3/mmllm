"""Stage harvested artifacts into inf-spork-r${TARGET}.{fim,bank} layout
so run_eval_battery.py can target them via MMLLM_INF_BASE / MMLLM_INF_BANK.

Input:
  /tmp/mmllm-cpu/harvested-r${TARGET}.dense.pt
  /tmp/mmllm-cpu/harvested-r${TARGET}.bank-net.{0..31}.bin
  /tmp/mmllm-cpu/harvested-r${TARGET}.bank.{i}.bin     (V_local, 8 layers)

Output:
  /tmp/mmllm-cpu/inf-spork-r${TARGET}.fim.ckpts/step-1/dense.pt
  /tmp/mmllm-cpu/inf-spork-r${TARGET}.bank-net.{i}.bin    (symlinks)
  /tmp/mmllm-cpu/inf-spork-r${TARGET}.bank.{i}.bin        (symlinks)

Usage:
  python3 scripts/stage_inf_spork.py <target_round>
"""
import argparse, os, shutil, sys
from pathlib import Path

LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target_round", type=int)
    args = ap.parse_args()
    target = args.target_round

    src_dense = Path(f"/tmp/mmllm-cpu/harvested-r{target}.dense.pt")
    src_bank_prefix = f"/tmp/mmllm-cpu/harvested-r{target}.bank"
    if not src_dense.exists():
        print(f"ERROR: {src_dense} missing — run harvest_chain.py first.", file=sys.stderr)
        sys.exit(2)

    inf_base = f"/tmp/mmllm-cpu/inf-spork-r{target}.fim"
    inf_bank = f"/tmp/mmllm-cpu/inf-spork-r{target}.bank"

    ckpt_dir = Path(f"{inf_base}.ckpts/step-1")
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_dense, ckpt_dir / "dense.pt")
    print(f"staged dense → {ckpt_dir/'dense.pt'}")

    for i in range(32):
        src = f"{src_bank_prefix}-net.{i}.bin"
        dst = f"{inf_bank}-net.{i}.bin"
        if os.path.exists(dst): os.remove(dst)
        os.symlink(src, dst)
    for i in LOCAL_LAYERS:
        src = f"{src_bank_prefix}.{i}.bin"
        dst = f"{inf_bank}.{i}.bin"
        if os.path.exists(dst): os.remove(dst)
        os.symlink(src, dst)
    print(f"staged 32× V_net + 8× V_local symlinks → {inf_bank}.*")
    print()
    print(f"Run battery with:")
    print(f"  MMLLM_INF_BASE={inf_base} MMLLM_INF_BANK={inf_bank} \\")
    print(f"    MMLLM_BATTERY_OUT=workers/dispatcher/harvest-Nway-r{target}/eval_battery.jsonl \\")
    print(f"    python3 scripts/run_eval_battery.py")

if __name__ == "__main__":
    main()
