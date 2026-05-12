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
"""

from __future__ import annotations

import torch


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
        # Force all CPU residence on loaded sparse state too.
        for group in self.param_groups:
            for p in group["params"]:
                state = self.state.get(p, {})
                for key in ("m_buf", "v_buf"):
                    t = state.get(key)
                    if t is not None and t.device.type != "cpu":
                        state[key] = t.to("cpu")

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

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

                state = self.state[p]
                if len(state) == 0:
                    # Sparse-state init: store m and v as growing CPU
                    # tensors of touched rows only. row_to_buf is a Python
                    # dict mapping V-row index → row position in m_buf/v_buf.
                    # First touch of a row appends a zero-row to the buffers.
                    #
                    # Memory scales with TOUCHED rows × dim × 4 bytes × 2
                    # (m + v), not bank size. For a 100-step training run
                    # touching ~5M unique rows at c_net=32, that's ~1.3 GB —
                    # vs the dense-state version's V_net-size × 2 (32 GB
                    # at sqrt_n=5600).
                    state["step"] = 0
                    state["m_buf"] = torch.zeros((0, p.shape[-1]),
                                                 dtype=p.dtype, device="cpu")
                    state["v_buf"] = torch.zeros((0, p.shape[-1]),
                                                 dtype=p.dtype, device="cpu")
                    state["row_to_buf"] = {}  # int → int

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
                m_buf = state["m_buf"]
                v_buf = state["v_buf"]

                # Map V-row indices → m_buf positions, allocating new
                # rows for first-touched indices.
                indices_list = indices_cpu.tolist()
                buf_idx_list = []
                new_rows_count = 0
                for vrow in indices_list:
                    bidx = row_to_buf.get(vrow)
                    if bidx is None:
                        bidx = m_buf.shape[0] + new_rows_count
                        row_to_buf[vrow] = bidx
                        new_rows_count += 1
                    buf_idx_list.append(bidx)
                if new_rows_count > 0:
                    # Grow m_buf and v_buf by new_rows_count zero rows.
                    zero_pad = torch.zeros((new_rows_count, p.shape[-1]),
                                           dtype=p.dtype, device="cpu")
                    m_buf = torch.cat([m_buf, zero_pad], dim=0)
                    v_buf = torch.cat([v_buf, zero_pad.clone()], dim=0)
                    state["m_buf"] = m_buf
                    state["v_buf"] = v_buf
                buf_idx = torch.tensor(buf_idx_list, dtype=torch.long, device="cpu")

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

                # Per-row update delta (on CPU).
                delta_cpu = -lr * m_hat / (v_hat.sqrt().add_(eps))

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

                grad = grad.coalesce()
                indices = grad._indices()[0]              # 1-D row indices, grad.device
                values  = grad._values()                  # (nnz, dim), grad.device

                # Match parameter device + dtype before in-place scatter.
                # p may be mmap-backed fp32 on CPU while grad is fp32 on GPU.
                indices_p = indices.to(p.device)
                values_p  = values.to(device=p.device, dtype=p.dtype)
                # In-place: p[indices_p] += -lr * values_p  (with duplicate-
                # index summation, already coalesced so unique).
                p.data.index_add_(0, indices_p, values_p, alpha=-lr)

        return loss
