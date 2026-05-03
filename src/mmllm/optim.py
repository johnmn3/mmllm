"""Custom optimizer with CPU-offloaded sparse state for mmllm.

PyTorch's stock `torch.optim.SparseAdam` keeps the m, v moments on the
same device as the parameter. For our 18.8 GB bank V on GPU, that's
~38 GB of GPU VRAM consumed by Adam moments — half the A100-80GB.

This module ships `CPUOffloadSparseAdam`, a drop-in replacement that
keeps state on the host (`device='cpu'`) while V.weight stays on GPU.
Each `.step()`:

  1. Reads sparse grad off GPU (only touched rows).
  2. Coalesces; pulls (indices, values) to CPU via single .to('cpu').
  3. Looks up state[indices] on CPU, computes Adam update on CPU.
  4. Writes new (m, v) back to CPU state at the same indices.
  5. Sends the per-row delta back to GPU; applies in-place to V.

Per-step cross-device transfer is bounded by touched-row count × dim,
which is the same as the sparse grad we'd send anyway — no asymptotic
overhead vs on-GPU SparseAdam, just one extra CPU round-trip in
exchange for ~38 GB of GPU memory back.

Memory math at sqrt_n=2048:
  - V on GPU: 4.2M × 224 × 4 = 3.76 GB / layer × 5 = 18.8 GB
  - state on CPU: same shape × 2 (m, v) = 37.6 GB / 5 layers
  - Need ~64 GB host RAM to hold state across all 5 layers.
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
                    # Lazy init state on CPU. Same dtype/shape as p but on host.
                    state["step"] = 0
                    state["m"] = torch.zeros(p.shape, dtype=p.dtype, device="cpu")
                    state["v"] = torch.zeros(p.shape, dtype=p.dtype, device="cpu")

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

                m = state["m"]  # (n, dim) CPU
                v = state["v"]

                # Pull old moments for the touched rows.
                m_old = m[indices_cpu]
                v_old = v[indices_cpu]

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

                # Write moments back to CPU state.
                m[indices_cpu] = m_new
                v[indices_cpu] = v_new

                # Apply the delta to the parameter on its native device.
                # index_add_ handles duplicate indices correctly (already
                # coalesced above so duplicates won't actually appear).
                p.data.index_add_(0, indices_gpu, delta_cpu.to(p.device))

        return loss
