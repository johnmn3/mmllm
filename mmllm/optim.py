"""Custom optimizer with CPU-offloaded, TOUCHED-ROW-SPARSE state.

PyTorch's stock `torch.optim.SparseAdam` keeps the m, v moments at the
parameter's FULL shape, even though only some rows receive grad. For
our V_net at sqrt_n=5600/c_net=32, that's 16 GB × 2 = 32 GB of state
allocation on first .step() — OOMs a 15 GiB sandbox.

This module ships `CPUOffloadSparseAdam`, which keeps state on the host
(`device='cpu'`) AND only allocates state for rows that actually receive
gradient. Each `.step()`:

  1. Reads sparse grad (only touched rows).
  2. Coalesces; pulls (indices, values) to CPU.
  3. Maps each touched V-row to a position in m_buf/v_buf, allocating
     a new zero-row on first touch (m_buf and v_buf grow over time).
  4. Adam update on CPU using m_buf[buf_idx], v_buf[buf_idx].
  5. Writes new (m, v) back at the same buf positions.
  6. Sends the per-row delta back to the param device; applies in-place.

Memory scales with TOUCHED-row count × dim × 4 bytes × 2 (m + v), NOT
the bank's full shape. For a 100-step run with top_k=256, B=4, T=128
across 4 layers, that's ~5M touches × ~256 bytes ≈ 1.3 GB — vs the
dense-state version's 32 GB at V_net=16 GB.

V_local LR — router as low-level primitive:
  V_local rows are what each router-routed retrieval returns. The
  router itself (K_a/K_b/SwitchGate) lives in opt-dense at
  lr_d_mult=0.05; conceptually V_local is also part of the routing
  primitive — it should train SLOWLY (the routed-to values change
  little; the V_net it eventually distills into is what should
  consolidate). Defaults applied here:

    MMLLM_LR_LOCAL_MULT (default 0.05) — global V_local multiplier.
      Applied to every V_local update in the bank optimizer. Drops
      V_local's effective LR from bank_lr × 1.0 (~9e-2 at peak) to
      bank_lr × 0.05 (~4.5e-3 at peak) — comparable to dense group.
      Set =1.0 to recover the old high-LR behavior for A/B testing.

    MMLLM_LR_LAYER_MULTS="m0,m1,...,m7" — optional per-layer override.
      Stacked on top of LOCAL_MULT. E.g. LOCAL_MULT=0.05 + LAYER_MULTS
      "2.0,1.5,..." gives effective bank_lr × 0.05 × m_i for layer i.
      Tiled via modulo when shorter than the number of Local layers.

  Only applies to parameters whose row count is divisible by sqrt_local**2
  (the trunk-shaped layout of V_local). V_net's (sqrt_n**2, c_net) shape
  has a different aspect and is left unscaled.
"""

from __future__ import annotations

import os
import torch


def _get_local_default_mult():
    """V_local global default multiplier. Without this, V_local trains
    at the bank LR (lr_b_mult=3.0 × base = 9e-2 at peak), which is the
    wrong magnitude for the router primitive — routers should train
    SLOW (they're a low-level primitive; the V values they retrieve
    are what should change fast, not the routing decisions). Default
    0.05 puts V_local at ~4.5e-3 at peak — ~20× below bank, comparable
    to the dense (K_a/K_b/SwitchGate) group at 0.05.

    Override via MMLLM_LR_LOCAL_MULT (e.g. set =1.0 to recover the old
    high-LR behavior for A/B testing)."""
    cached = getattr(_get_local_default_mult, "_cache", _SENTINEL := object())
    if cached is _SENTINEL:
        raw = os.environ.get("MMLLM_LR_LOCAL_MULT", "").strip()
        try:
            cached = float(raw) if raw else 0.05
        except Exception:
            cached = 0.05
        _get_local_default_mult._cache = cached
    return cached


def _get_layer_mults():
    """Parse MMLLM_LR_LAYER_MULTS env var into a 1-D CPU tensor of
    per-layer multipliers, or None if unset/empty. Stacked ON TOP of
    the LOCAL_MULT global — so e.g. setting MMLLM_LR_LAYER_MULTS=2.0,...
    with default MMLLM_LR_LOCAL_MULT=0.05 yields V_local layer 0 at
    effective bank_lr × 0.05 × 2.0 = bank_lr × 0.1. Cached per-process."""
    cached = getattr(_get_layer_mults, "_cache", _SENTINEL := object())
    if cached is _SENTINEL:
        raw = os.environ.get("MMLLM_LR_LAYER_MULTS", "").strip()
        if not raw:
            cached = None
        else:
            try:
                vals = [float(x) for x in raw.split(",") if x.strip()]
                cached = torch.tensor(vals, dtype=torch.float32) if vals else None
            except Exception:
                cached = None
        _get_layer_mults._cache = cached
    return cached


def _is_v_local(p_shape_0, sqrt_local):
    """A param is V_local iff its row count divides cleanly into >1
    trunks of size sqrt_local**2. V_net's (sqrt_n**2, c_net) has
    sqrt_n^2 rows; for cpu-mini that's 4096 vs sqrt_local^2 = 51076 —
    not divisible, so V_net falls through."""
    rows_per_trunk = sqrt_local * sqrt_local
    if p_shape_0 % rows_per_trunk != 0:
        return False
    return p_shape_0 // rows_per_trunk >= 2


class CPUOffloadSparseAdam(torch.optim.Optimizer):
    """SparseAdam with state pinned to CPU. Designed for sparse-grad
    `nn.Embedding` parameters (our bank V).

    `lr`, `betas`, `eps` follow torch.optim.SparseAdam defaults so this
    is a drop-in replacement when invoked the same way.
    """

    def __init__(self, params, lr: float = 1e-3,
                 betas: tuple[float, float] = (0.9, 0.999),
                 eps: float = 1e-8):
        if lr <= 0:
            raise ValueError(f"lr must be positive: {lr}")
        defaults = dict(lr=lr, betas=betas, eps=eps)
        super().__init__(params, defaults)

    def load_state_dict(self, state_dict):
        """Restore optimizer state.

        Old ckpts saved with the dense-state version had keys "m" and "v"
        as full V-shape tensors. This sparse-state version uses "m_buf",
        "v_buf", and "row_to_buf" — incompatible layouts. We skip the
        load when we detect the old format and fall back to fresh state
        (training resumes with Adam moments at zero, which is what fresh
        init would have been anyway for any new run).
        """
        # Detect old-format state and skip.
        old_format = False
        for pid, st in (state_dict.get("state", {}) or {}).items():
            if isinstance(st, dict) and ("m" in st or "v" in st) and "m_buf" not in st:
                old_format = True
                break
        if old_format:
            # Don't load — state stays empty, next step() lazy-inits the
            # new sparse buffers.
            return
        super().load_state_dict(state_dict)
        # Force all CPU residence on loaded sparse state too AND
        # convert any old-format dict `row_to_buf` to the new dense
        # torch.long lookup tensor. The dense lookup is `p.shape[0]`
        # entries (V-rows), with -1 marking unallocated. Old ckpts had
        # `row_to_buf: dict[int, int]` of TOUCHED rows only — that
        # version was the source of GB-scale Python-dict overhead that
        # OOM'd the 15 GB tier mid-round. Converting on load means
        # existing harvested opt-sparse-net.pt files (saved with the
        # dict format) keep working; the next save writes the new
        # tensor format.
        for group in self.param_groups:
            for p in group["params"]:
                state = self.state.get(p, {})
                # Coerce m_buf / v_buf to CPU + float dtype matching the
                # parameter. Shape may drift across topology changes
                # (different sub_top_k, different bank rows touched) —
                # if it does, drop the buffer rather than load stale.
                for key in ("m_buf", "v_buf"):
                    t = state.get(key)
                    if t is None:
                        continue
                    if t.device.type != "cpu":
                        t = t.to("cpu")
                    if t.dtype != p.dtype:
                        t = t.to(dtype=p.dtype)
                    if t.ndim == 2 and t.shape[-1] != p.shape[-1]:
                        # Topology mismatch — discard, next step() will
                        # re-grow from scratch.
                        t = torch.zeros((0, p.shape[-1]),
                                        dtype=p.dtype, device="cpu")
                    state[key] = t
                rtb = state.get("row_to_buf")
                if isinstance(rtb, dict):
                    buf_lookup = torch.full((p.shape[0],), -1,
                                            dtype=torch.long, device="cpu")
                    if rtb:
                        rows  = torch.tensor(list(rtb.keys()),   dtype=torch.long)
                        bidxs = torch.tensor(list(rtb.values()), dtype=torch.long)
                        buf_lookup[rows] = bidxs
                    state["row_to_buf"] = buf_lookup
                elif isinstance(rtb, torch.Tensor):
                    # Force CPU + torch.long. row_to_buf is a row-index
                    # lookup; if a stale ckpt saved it as float (legacy
                    # bug), index_put on line ~270 will raise dtype
                    # mismatch on the first first-touched-row of the
                    # next step. Coerce here so the run survives the
                    # next save/load cycle as well.
                    state["row_to_buf"] = rtb.to(device="cpu",
                                                 dtype=torch.long)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        layer_mults = _get_layer_mults()
        local_default_mult = _get_local_default_mult()
        sqrt_local = int(os.environ.get("MMLLM_SQRT_N", "226"))
        v_local_counter = 0

        for group in self.param_groups:
            beta1, beta2 = group["betas"]
            lr = group["lr"]
            eps = group["eps"]

            for p in group["params"]:
                if p.grad is None:
                    continue
                grad = p.grad
                if not grad.is_sparse:
                    raise RuntimeError(
                        "CPUOffloadSparseAdam only handles sparse grads "
                        f"(got dense grad on a parameter of shape {tuple(p.shape)})"
                    )

                # V_local effective multiplier:
                #   local_default_mult (slows the router-routed values to a
                #   low-LR primitive) × per-layer_mult (if set; defaults 1.0).
                # V_net's shape doesn't match _is_v_local and passes through
                # at multiplier 1.0 (unchanged from bank's lr_b_mult).
                layer_mult = 1.0
                if _is_v_local(p.shape[0], sqrt_local):
                    per_layer = 1.0
                    if layer_mults is not None:
                        per_layer = float(layer_mults[v_local_counter % len(layer_mults)])
                    layer_mult = local_default_mult * per_layer
                    v_local_counter += 1

                state = self.state[p]
                if len(state) == 0:
                    # Sparse-state init: m_buf / v_buf are growing CPU
                    # tensors that hold moments for ONLY touched rows.
                    # row_to_buf is a row-indexed long tensor mapping
                    # V-row index → row position in m_buf/v_buf, with
                    # -1 marking "this row hasn't been touched yet."
                    #
                    # The tensor's full V-row-count size is a constant
                    # upfront cost (p.shape[0] × 8 B) — for V_net at
                    # sqrt_n²=1M, c_net=8, that's 8 MB / layer × 32 layers
                    # = 256 MB. Earlier versions used a Python dict
                    # `{int → int}`, which grew at ~240 bytes / touched
                    # row × 32 layers — a few GB at ~100-step training
                    # rounds, and unbounded across rounds in a chain.
                    # The dense tensor lookup pays the constant cost
                    # upfront but caps the memory and vectorizes the
                    # gradient-to-buf-idx mapping below (was a Python
                    # for-loop, now one tensor index).
                    # m_buf has a logical size (state["m_buf_used"]) and
                    # a physical capacity (state["m_buf"].shape[0]). When
                    # capacity is exhausted, grow geometrically (×2) so
                    # the cat amortizes to O(1) per row over a round.
                    # The previous design cat'd every step, which was
                    # O(touched_rows²) total over N steps and dominated
                    # opt-sparse-net wall (~26% of step time at the
                    # wave-2 recipe).
                    state["step"] = 0
                    state["m_buf"] = torch.zeros((0, p.shape[-1]),
                                                 dtype=p.dtype, device="cpu")
                    state["v_buf"] = torch.zeros((0, p.shape[-1]),
                                                 dtype=p.dtype, device="cpu")
                    state["m_buf_used"] = 0
                    state["row_to_buf"] = torch.full((p.shape[0],), -1,
                                                    dtype=torch.long,
                                                    device="cpu")

                state["step"] += 1
                step_count = state["step"]

                # Coalesce duplicate indices (sparse_grad can repeat rows
                # if the same row is touched multiple times in one step).
                grad = grad.coalesce()
                indices_gpu = grad._indices()[0]   # 1-D row indices (long), on grad.device
                values_gpu = grad._values()        # (nnz, dim)

                # One round-trip to CPU.
                indices_cpu = indices_gpu.to("cpu", non_blocking=False)
                values_cpu = values_gpu.to("cpu", non_blocking=False)

                row_to_buf = state["row_to_buf"]

                # Vectorized V-row → m_buf-position lookup. -1 entries
                # mark first-touched rows; we allocate new m_buf/v_buf
                # rows for them and update the lookup tensor.
                buf_idx = row_to_buf[indices_cpu]                  # (nnz,) long
                new_mask = buf_idx == -1
                if bool(new_mask.any().item()):
                    n_new = int(new_mask.sum().item())
                    new_v_rows = indices_cpu[new_mask]
                    cur_used = state.get("m_buf_used", state["m_buf"].shape[0])
                    cur_cap  = state["m_buf"].shape[0]
                    needed   = cur_used + n_new
                    if needed > cur_cap:
                        # Geometric growth (×2, or exactly what's needed —
                        # whichever is larger). One cat per growth event
                        # instead of one cat per step.
                        new_cap = max(needed, cur_cap * 2, 64)
                        grow = new_cap - cur_cap
                        zero_pad = torch.zeros((grow, p.shape[-1]),
                                               dtype=p.dtype, device="cpu")
                        state["m_buf"] = torch.cat([state["m_buf"], zero_pad], dim=0)
                        state["v_buf"] = torch.cat([state["v_buf"], zero_pad.clone()], dim=0)
                    new_buf_idx = torch.arange(cur_used,
                                               cur_used + n_new,
                                               dtype=torch.long, device="cpu")
                    row_to_buf[new_v_rows] = new_buf_idx
                    buf_idx[new_mask] = new_buf_idx
                    state["m_buf_used"] = cur_used + n_new
                m_buf = state["m_buf"]
                v_buf = state["v_buf"]

                # Pull old moments for the touched rows.
                m_old = m_buf[buf_idx]
                v_old = v_buf[buf_idx]

                # Adam update (on CPU).
                m_new = m_old.mul(beta1).add_(values_cpu, alpha=1 - beta1)
                v_new = v_old.mul(beta2).addcmul_(values_cpu, values_cpu,
                                                  value=1 - beta2)

                # Bias-corrected moments.
                bc1 = 1.0 - beta1 ** step_count
                bc2 = 1.0 - beta2 ** step_count
                m_hat = m_new.div(bc1)
                v_hat = v_new.div(bc2)

                # Per-row update delta (on CPU). Per-layer LR scaling
                # for V_local: scalar multiply on the whole delta (the
                # layer_mult is the same for every touched row of this
                # param). For V_net, layer_mult is 1.0.
                delta_cpu = (-lr * layer_mult) * m_hat / (v_hat.sqrt().add_(eps))

                # Write moments back to CPU state at their buf positions.
                m_buf[buf_idx] = m_new
                v_buf[buf_idx] = v_new

                # Apply the delta to the parameter on its native device.
                # index_add_ handles duplicate indices correctly (already
                # coalesced above so duplicates won't actually appear).
                p.data.index_add_(0, indices_gpu, delta_cpu.to(p.device))

        return loss


class CPUSparseSGD(torch.optim.Optimizer):
    """Plain SGD for sparse-grad parameters. No m, v moments — just
    `p[i] -= lr * grad[i]` for each touched row. Zero per-param state,
    the lightest possible sparse update.

    Designed as a drop-in for `CPUOffloadSparseAdam` when the bank's
    optimizer-state memory becomes the cliff. At N=16 trunks × bank
    sqrt_n=226 × q_dim=128 × 8 Local layers, SparseAdam state runs
    ~6.7 GB (m + v at full touch); CPUSparseSGD runs 0 GB. The
    training dynamics get noisier (no momentum), but for a Hogwild-
    style consolidation many trunks distill into a shared V_net the
    averaging may compensate.

    Same constructor surface as torch.optim.SparseAdam — lr only. Use
    by setting MMLLM_SPARSE_OPT=sgd; pick-sparse-optimizer routes to
    this class.
    """

    def __init__(self, params, lr: float = 1e-3):
        if lr <= 0:
            raise ValueError(f"lr must be positive: {lr}")
        defaults = dict(lr=lr)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        layer_mults = _get_layer_mults()
        local_default_mult = _get_local_default_mult()
        sqrt_local = int(os.environ.get("MMLLM_SQRT_N", "226"))
        v_local_counter = 0

        for group in self.param_groups:
            lr = group["lr"]

            for p in group["params"]:
                if p.grad is None:
                    continue
                grad = p.grad
                if not grad.is_sparse:
                    raise RuntimeError(
                        "CPUSparseSGD only handles sparse grads "
                        f"(got dense grad on a parameter of shape {tuple(p.shape)})"
                    )

                # V_local: local_default_mult × per-layer_mult; V_net: 1.0.
                layer_mult = 1.0
                if _is_v_local(p.shape[0], sqrt_local):
                    per_layer = 1.0
                    if layer_mults is not None:
                        per_layer = float(layer_mults[v_local_counter % len(layer_mults)])
                    layer_mult = local_default_mult * per_layer
                    v_local_counter += 1

                grad = grad.coalesce()
                indices = grad._indices()[0]              # 1-D row indices, grad.device
                values  = grad._values()                  # (nnz, dim), grad.device

                # Match parameter device + dtype before in-place scatter.
                # p may be mmap-backed fp32 on CPU while grad is fp32 on GPU.
                indices_p = indices.to(p.device)
                values_p  = values.to(device=p.device, dtype=p.dtype)

                # In-place: p[indices_p] += -lr * layer_mult * values_p
                # (with duplicate-index summation, already coalesced so unique).
                p.data.index_add_(0, indices_p, values_p, alpha=-lr * layer_mult)

        return loss
