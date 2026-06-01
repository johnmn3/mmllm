"""The torch <-> MLX checkpoint bridge — the ONLY file in mmllm/mlx that touches
torch. Everything else in the round runs in pure MLX.

The federated harvest (harvester.py, scripts/_delta_sparse_net.py,
scripts/_opt_sparse_net_chunk.py) consumes/produces torch artifacts; an MLX bird
must read/write the identical formats so it is interchangeable with a torch bird:

  - dense.pt              = list[torch.Tensor] in the EXACT positional order of
                            core.lpy's (parameters m). FedAvg merges by position,
                            so order + dtype must be preserved round-trip.
  - V_net.{i}.bin /       = raw numpy memmap (fp32) — no torch at all.
    V_local.{i}.bin
  - opt-sparse-net.{pid}.pt = {step, m_buf(R,c_net) fp32, v_buf fp32, row_to_buf}
                            (emitted in Stage 5; see sparse_adam.py)

Conversion goes through numpy. For fp32 (the common case for dense params and the
mandatory dtype for banks/optimizer moments) the round-trip is bit-exact, which
is what the Stage-0 gate asserts. Lower-precision dtypes (bf16/fp16) are carried
through float32 numpy and cast back to the recorded torch dtype on save — exact
for the values MLX actually held, since MLX computed them.
"""
from __future__ import annotations

import numpy as np

# torch is imported lazily inside functions: this module may be imported on a
# pure-MLX code path where we still want `import`-safety, and torch is only ever
# needed at the checkpoint boundary, not in the hot loop.


# --- numpy dtype <-> torch dtype, restricted to what the chain actually uses ---
def _np_dtype_for(torch_dtype) -> np.dtype:
    import torch

    # MLX has no bf16<->numpy path; bf16/fp16 params are bridged as fp32 and the
    # original torch dtype is restored on save (see torch_list_from_mx).
    if torch_dtype in (torch.bfloat16, torch.float16, torch.float32, torch.float64):
        return np.float32
    if torch_dtype == torch.int64:
        return np.int64
    if torch_dtype == torch.int32:
        return np.int32
    if torch_dtype == torch.int8:
        return np.int8
    return np.float32


def mx_from_torch(t):
    """torch.Tensor -> mx.array, via a numpy bridge. fp32 is bit-exact."""
    import mlx.core as mx
    import torch

    t = t.detach().to("cpu")
    np_dt = _np_dtype_for(t.dtype)
    # bf16/fp16 can't view as numpy directly; promote to fp32 first.
    if t.dtype in (torch.bfloat16, torch.float16):
        arr = t.to(torch.float32).numpy().astype(np_dt, copy=False)
    else:
        arr = t.numpy().astype(np_dt, copy=False)
    return mx.array(arr)


def torch_from_mx(a, torch_dtype=None):
    """mx.array -> torch.Tensor. If torch_dtype is given, cast to it (restores the
    original dense.pt dtype on save). fp32->fp32 is bit-exact."""
    import torch

    np_arr = np.array(a)  # MLX -> numpy (host copy)
    t = torch.from_numpy(np_arr)
    if torch_dtype is not None and t.dtype != torch_dtype:
        t = t.to(torch_dtype)
    return t


# ----------------------------- dense.pt ----------------------------------------
def load_dense_pt(path: str):
    """Load dense.pt -> (list[mx.array], list[torch.dtype]).

    The dtype list records each param's original torch dtype so save_dense_pt can
    restore it position-for-position (preserving the FedAvg-by-position contract).
    """
    import torch

    tensors = torch.load(path, map_location="cpu", weights_only=False)
    tensors = list(tensors)  # dense.pt is a positional list, never a state_dict
    arrays = [mx_from_torch(t) for t in tensors]
    dtypes = [t.dtype for t in tensors]
    return arrays, dtypes


def torch_list_from_mx(arrays, dtypes):
    """list[mx.array] (+ recorded dtypes) -> list[torch.Tensor], in order."""
    if dtypes is None:
        dtypes = [None] * len(arrays)
    assert len(arrays) == len(dtypes), (
        f"dense param count drift: {len(arrays)} arrays vs {len(dtypes)} dtypes "
        f"— this would corrupt the FedAvg-by-position contract"
    )
    return [torch_from_mx(a, dt) for a, dt in zip(arrays, dtypes)]


def save_dense_pt(arrays, dtypes, path: str):
    """Write list[mx.array] back to a torch dense.pt (positional list)."""
    import torch

    torch.save(torch_list_from_mx(arrays, dtypes), path)


# ----------------------------- V_*.bin (numpy) ---------------------------------
def load_bin(path: str, shape, dtype=np.float32):
    """Load a V_net/V_local .bin (raw numpy memmap) -> mx.array."""
    import mlx.core as mx

    mm = np.memmap(path, dtype=dtype, mode="r", shape=tuple(shape))
    return mx.array(np.ascontiguousarray(mm))


def save_bin(a, path: str, dtype=np.float32):
    """Write an mx.array V table back to a raw .bin (fp32 by default)."""
    np.asarray(np.array(a), dtype=dtype).tofile(path)
