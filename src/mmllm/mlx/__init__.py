"""MLX backend for mmllm — Apple-Silicon training/inference acceleration.

This package is an OPTIONAL sibling to the canonical PyTorch path. It is only
imported when MMLLM_BACKEND=mlx is requested AND `mlx` is installed (Apple
Silicon only). On Linux CI birds `mlx` is absent, so `HAS_MLX` is False and the
torch path is used unconditionally — the import here must never raise.

The MLX backend fuses lazily on Metal (the spike measured 4.5x over torch-MPS on
the PKM/NetBank forward, 3.2x on the dense block) — past the torch-MPS 3.8x
ceiling that torch.compile cannot lift (inductor-MPS is 0.90x). It takes a whole
bird *round* (build -> load ckpt -> train -> eval -> ablate -> save); the only
torch touch-point is checkpoint I/O, bridged via numpy in `bridge.py`. The torch
trainer is untouched — this is a permanent dual-backend split (CI stays torch).
"""

try:
    import mlx.core as _mx  # noqa: F401

    HAS_MLX = True
except Exception:  # ImportError on Linux, or any load failure — degrade quietly
    HAS_MLX = False


def backend_requested() -> bool:
    """True iff the operator asked for the MLX backend via MMLLM_BACKEND=mlx."""
    import os

    return os.environ.get("MMLLM_BACKEND", "").strip().lower() == "mlx"


def active() -> bool:
    """True iff the MLX backend should actually drive this run (requested AND
    importable). The dispatch seam in core.lpy gates on this; anything False
    falls through to the torch `train-long`."""
    return backend_requested() and HAS_MLX


def run_round(cfg, train_path, val_path, ckpt_dir, log_path,
              total, eval_every, ckpt_every):
    """Entry point the core.lpy dispatch seam calls when `active()`. Imports the
    MLX trainer LAZILY (so `import mmllm.mlx` stays safe on Linux where mlx is
    absent — the trainer module imports mlx.core at top) and runs one bird round.
    Signature mirrors core.lpy's `train-long`."""
    from mmllm.mlx import trainer

    return trainer.train_round(
        cfg, train_path, val_path, ckpt_dir, log_path,
        total, eval_every, ckpt_every,
    )
