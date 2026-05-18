"""Off-machine "long-term memory" tier — the third part of the triune-brain
architecture (forebrain = local PKM bank, midbrain = dense router, long-term =
NetBank).

Same query API as `mmllm.memory.ProductKeyMemory` so it slots into the same
attention block as a parallel retrieval source. Differences from the Local
Bank, all motivated by "what would actually live on a remote shared cluster":

  1. Larger scale            sqrt_n=8192 (67M entries) vs Local 2048 (4.2M)
  2. Learned-bottleneck V    V_net is (n, c_net) with c_net << q_dim;
                             a learned `expander` Linear projects retrieved
                             rows back up to q_dim. Compresses both the
                             on-disk footprint AND the production network
                             payload by q_dim/c_net (default ~3.5×).
  3. Compressed dtype        fp16 V (vs Local fp32) — another 2×.
  4. Larger top-k payload    64 rows per query vs Local 16 — amortizes the
                             round-trip latency over more retrieved values.
  5. Simulated WAN delay     uniform 1-10ms blocking sleep per forward
                             pass, applied in BOTH training and eval so the
                             model is calibrated to the latency tier it'll
                             see in production deployment.

Storage: always CPU-mmap (this IS the off-machine tier; in production it
lives on a remote cluster's RAM/NVMe). One file per transformer layer
analogous to the Local Bank's `<bank>.<i>.bin` layout.

Warm-start: in v1, `warm_start_from()` copies a Local Bank's K_a/K_b into
NetBank's first `local.sqrt_n` rows. The remaining rows + V stay at random
init. This bootstraps NetBank's retrieval geometry from Local's so the
larger space starts useful from step 0 instead of cold.

Future iterations (deferred from v1):
  - PQ (product quantization) on V_net for 8-16× extra compression
  - Adaptive routing classifier ("skip NetBank?" per token) to reduce
    production network traffic
  - Async overlap with SDPA + Local Bank
  - Multi-tier hierarchy (regional + global NetBanks)
"""
import os
import time
import random

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from mmllm.memory import CPUPinnedEmbedding
from mmllm._pkm_autograd import HAS_CPP_KERNELS, PKMFusedTopK, netbank_inference_forward


_DTYPE_MAP = {
    "fp32": (np.float32, torch.float32, 4),
    "fp16": (np.float16, torch.float16, 2),
}


def _mmap_value_tensor_typed(path: str, n: int, dim: int,
                             dtype_str: str = "fp32",
                             init_scale: float = 0.02,
                             chunk_rows: int = 4096) -> torch.Tensor:
    """Open or create an (n, dim) memmap of the given dtype, return a
    torch tensor sharing the mmap storage. fp32 default for SparseAdam
    numerical stability (fp16 SparseAdam state can underflow / overflow);
    fp16 available behind MMLLM_NET_DTYPE=fp16 once we add a mixed-
    precision optimizer."""
    np_dt, _torch_dt, bytes_per = _DTYPE_MAP[dtype_str]
    expected_bytes = n * dim * bytes_per
    if os.path.exists(path) and os.path.getsize(path) == expected_bytes:
        arr = np.memmap(path, dtype=np_dt, mode="r+", shape=(n, dim))
    else:
        arr = np.memmap(path, dtype=np_dt, mode="w+", shape=(n, dim))
        for i in range(0, n, chunk_rows):
            end = min(i + chunk_rows, n)
            arr[i:end] = (np.random.standard_normal((end - i, dim))
                          * init_scale).astype(np_dt)
        arr.flush()
    return torch.from_numpy(arr)


def prepare_netbank_files(bank_path_prefix: str, n_layers: int,
                          sqrt_n: int, c_net: int,
                          dtype_str: str = "fp32",
                          init_scale: float = 0.02,
                          chunk_rows: int = 4096) -> dict:
    """Pre-allocate NetBank V mmap files, one per layer. Idempotent."""
    n = sqrt_n * sqrt_n
    bytes_per = _DTYPE_MAP[dtype_str][2]
    expected_bytes = n * c_net * bytes_per
    out = []
    for i in range(n_layers):
        path = f"{bank_path_prefix}.{i}.bin"
        if os.path.exists(path) and os.path.getsize(path) == expected_bytes:
            out.append({"path": path, "bytes": expected_bytes, "cached": True})
            continue
        _mmap_value_tensor_typed(path, n, c_net, dtype_str, init_scale, chunk_rows)
        out.append({"path": path, "bytes": expected_bytes, "cached": False})
    return {
        "paths": out,
        "n_layers": n_layers,
        "total_bytes": expected_bytes * n_layers,
        "sqrt_n": sqrt_n,
        "c_net": c_net,
        "dtype": dtype_str,
    }


class NetBank(nn.Module):
    """Off-machine long-term memory bank. See module docstring for the
    triune-brain framing.

    Args:
        q_dim:        same as the rest of the model — query dimension and
                      output dimension (post-bottleneck-expansion).
        sqrt_n:       side length of the bank; total entries = sqrt_n².
                      Default 8192 → 67M entries.
        c_net:        bottleneck dim of V_net; rows are stored as c_net
                      latents and expanded to q_dim by `expander`.
        top_k:        rows retrieved per query (larger payload amortizes
                      simulated network round-trip).
        sub_top_k:    sub-keys retained per K_a/K_b half before the
                      outer-sum re-rank. >= top_k.
        mmap_path:    per-layer file path; if set, V_net is mmap-backed.
                      Always set in production (NetBank IS off-machine);
                      None for unit-test only.
        delay_ms_min: minimum simulated network delay per forward (ms).
        delay_ms_max: maximum simulated network delay per forward (ms).
                      Set both to 0.0 to disable for non-prod use.
    """

    def __init__(self, q_dim: int, sqrt_n: int = 8192,
                 c_net: int = 64,
                 top_k: int = 64, sub_top_k: int = 64,
                 mmap_path: str | None = None,
                 delay_ms_min: float = 1.0,
                 delay_ms_max: float = 10.0,
                 dtype: str = "fp32",
                 bank_on_gpu: bool = False):
        super().__init__()
        assert q_dim % 2 == 0, "q_dim must be even"
        assert c_net <= q_dim, "c_net (bottleneck dim) must be <= q_dim"
        assert dtype in _DTYPE_MAP, f"dtype must be one of {list(_DTYPE_MAP)}"

        self.q_dim = q_dim
        self.sub_dim = q_dim // 2
        self.sqrt_n = sqrt_n
        self.n = sqrt_n * sqrt_n
        self.c_net = c_net
        self.top_k = top_k
        self.sub_top_k = min(sub_top_k, sqrt_n)
        self.mmap_path = mmap_path
        self.delay_ms_min = float(delay_ms_min)
        self.delay_ms_max = float(delay_ms_max)
        self.dtype_str = dtype
        self.bank_on_gpu = bool(bank_on_gpu)

        # Query normalization (PEER 2024) — separate from Local's q_norm
        # since each tier learns its own scale.
        self.q_norm = nn.RMSNorm(q_dim)

        # Sub-key matrices (always GPU-resident; small + dense-grad).
        # Shape matches Local's K_a/K_b at our sqrt_n so warm_start_from()
        # can copy into the first `local.sqrt_n` rows.
        self.K_a = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)
        self.K_b = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)

        # Learned expander: latent (c_net) → output (q_dim). Zero-init
        # would make NetBank contribute nothing at step 0 — for warm-start
        # this would waste the K_a/K_b copy. So scaled-Gaussian init at
        # 1/sqrt(c_net) so the expanded values have unit-ish variance.
        self.expander = nn.Linear(c_net, q_dim, bias=False)
        nn.init.normal_(self.expander.weight, mean=0.0, std=1.0 / (c_net ** 0.5))

        # V_net storage. Three modes:
        #
        #   bank_on_gpu=True (training-fast path): plain nn.Embedding,
        #   parent .to(cuda) moves V to VRAM. No mmap, no FUSE. Sized to
        #   fit alongside Local Bank in 80GB VRAM (sqrt_n=4096+c_net=64
        #   fp32 → 21.5GB total for NetBank). The 1-10ms simulated
        #   delay still fires per forward to keep the model calibrated
        #   to the production WAN-latency tier; the storage just isn't
        #   actually off-machine during training.
        #
        #   bank_on_gpu=False, mmap_path set: CPUPinnedEmbedding wrapping
        #   the mmap. parent .to(cuda) skips V (stays at host RAM /
        #   FUSE). Truer to the "off-machine" simulation but adds real
        #   FUSE latency on top of the simulated WAN delay.
        #
        #   bank_on_gpu=False, mmap_path=None: unit-test only — plain
        #   nn.Embedding allocated wherever the parent ends up.
        torch_dt = _DTYPE_MAP[dtype][1]
        if self.bank_on_gpu:
            self.V = nn.Embedding(self.n, c_net, sparse=True, dtype=torch_dt)
            with torch.no_grad():
                self.V.weight.normal_(0, 0.02)
        elif mmap_path is not None:
            v_tensor = _mmap_value_tensor_typed(mmap_path, self.n, c_net, dtype)
            self.V = CPUPinnedEmbedding.from_pretrained(
                v_tensor, freeze=False, sparse=True,
            )
        else:
            # Unit-test path: no mmap, no CPU-pinning, plain nn.Embedding.
            self.V = nn.Embedding(self.n, c_net, sparse=True, dtype=torch_dt)
            with torch.no_grad():
                self.V.weight.normal_(0, 0.02)

        # Slot-usage tracking — same shape/API as ProductKeyMemory so the
        # train-loop's per-layer slot logging works for both tiers.
        self.register_buffer(
            "ka_hits", torch.zeros(sqrt_n, dtype=torch.long), persistent=False,
        )
        self.register_buffer(
            "kb_hits", torch.zeros(sqrt_n, dtype=torch.long), persistent=False,
        )
        # z-loss accumulator, picked up by train-step
        self.last_z_loss: torch.Tensor | None = None
        # Instrumentation: written at the end of forward(). Mean L2 norm of
        # NetBank's residual contribution per (B,T) position. The headline
        # diagnostic for "is NetBank actually being adopted as a function
        # tier?" — if last_output_norm stays tiny while Local Bank's
        # equivalent grows, the gate / V / routing is collapsing the
        # NetBank path regardless of how V was initialized.
        self.last_output_norm: float = 0.0

    # ─────────────────────── parameter routing ───────────────────────

    def dense_parameters(self):
        """Dense-grad params route to AdamW. q_norm.weight + expander.weight
        appended after K_a/K_b for positional ckpt-load compat with any
        future v0 ckpts (none exist yet, but keeping the convention)."""
        return [
            self.K_a, self.K_b,
            self.q_norm.weight,
            self.expander.weight,
        ]

    def sparse_parameters(self):
        """V_net.weight routes to a separate SparseAdam (opt-sparse-net) so
        its lr can be cooled independently from the Local Bank's V."""
        return [self.V.weight]

    # ─────────────────────── warm-start ───────────────────────

    def warm_start_from(self, local_K_a: torch.Tensor,
                        local_K_b: torch.Tensor,
                        local_V: "torch.Tensor | None" = None) -> None:
        """Copy a Local Bank's K_a/K_b (and optionally V) into the first
        `local.sqrt_n` rows of NetBank. Bootstraps the retrieval geometry
        so queries that score highly against a Local row also score highly
        against the corresponding NetBank row from step 0.

        K_a/K_b share dtype/shape between Local and NetBank, so they
        copy directly.

        V_net has the learned-bottleneck shape (n, c_net) while Local's
        V is (n, q_dim) with q_dim >> c_net. When `local_V` is provided,
        we project it down to c_net via the expander's left-pseudoinverse:
        the V_net values we pick are the least-squares solution to
        `expander(V_net) ≈ local_V`, so at step 0 the retrieved+expanded
        NetBank output approximates Local's V on the warm-started rows.

        Pass local_V=None to keep the v1 behavior (V stays random)."""
        with torch.no_grad():
            local_n = local_K_a.shape[0]
            n_copy = min(local_n, self.sqrt_n)
            self.K_a.data[:n_copy].copy_(
                local_K_a.data[:n_copy].to(self.K_a.dtype).to(self.K_a.device)
            )
            self.K_b.data[:n_copy].copy_(
                local_K_b.data[:n_copy].to(self.K_b.dtype).to(self.K_b.device)
            )
            if local_V is not None:
                # Local V is (n_local, q_dim). Project to (n_local, c_net)
                # via the expander pseudo-inverse so expander(V_net) ≈ V_local
                # on warm-started rows at step 0.
                v_local = local_V[:n_copy].to(self.expander.weight.dtype).to(
                    self.expander.weight.device)
                # expander.weight is (q_dim, c_net); pinv is (c_net, q_dim)
                W_pinv = torch.linalg.pinv(self.expander.weight)
                # (n_copy, q_dim) @ (q_dim, c_net) = (n_copy, c_net)
                v_warm = v_local @ W_pinv.T
                # Write into the V embedding's weight tensor
                v_dst = self.V.weight if hasattr(self.V, "weight") else self.V
                v_dst.data[:n_copy].copy_(v_warm.to(v_dst.dtype).to(v_dst.device))

    # ─────────────────────── forward ───────────────────────

    def _simulate_delay(self):
        """uniform random blocking sleep. Could move to a worker thread to
        avoid stalling GPU compute, but the sleep emits a real async-ready
        signal in production; for v1 we just block."""
        ms = random.uniform(self.delay_ms_min, self.delay_ms_max)
        time.sleep(ms / 1000.0)

    def forward(self, q: torch.Tensor) -> torch.Tensor:
        """q: (B, T, q_dim) → (B, T, q_dim) softmax-weighted retrieval.

        Math is the same as ProductKeyMemory.forward except for:
          - q_norm is applied
          - z-loss accumulator + slot-usage hits tracked (training only)
          - V_net rows are c_net-dim fp16; we expand to q_dim via the
            learned expander after the gather
          - blocking simulated network delay (training only — production
            inference shouldn't pay a synthetic latency tax)
        """
        if self.training and self.delay_ms_max > 0:
            self._simulate_delay()

        # Inference fast path: one C++ call fuses score → sub-topk →
        # outer-sum-topk → gather → softmax → weighted-sum into a single
        # entry point, then Python applies the (small) expander linear.
        # Drops ~30 ATen-op dispatches + Python orchestration per layer.
        # Only safe when not training (no autograd recording in C++) and
        # V is on CPU fp32 (only path the fused kernel supports).
        #
        # Skips: training z-loss, sub-key hit counters, last_output_norm
        # .item() telemetry — all training-only side effects.
        if (not self.training
                and HAS_CPP_KERNELS
                and self.V.weight.is_cpu
                and self.V.weight.dtype == torch.float32):
            return netbank_inference_forward(self, q)

        B, T, D = q.shape
        q = self.q_norm(q)
        q_a = q[..., :self.sub_dim]
        q_b = q[..., self.sub_dim:]

        scores_a = q_a @ self.K_a.T
        scores_b = q_b @ self.K_b.T

        if self.training:
            # z_loss is not collected for NetBank — collect-z-loss reads
            # only from Local PKM (:memory). Computing it with autograd
            # alive holds scores_a/b past the block forward, defeating
            # gradient checkpointing. Detach so this is telemetry-only.
            with torch.no_grad():
                lse_a = torch.logsumexp(scores_a, dim=-1)
                lse_b = torch.logsumexp(scores_b, dim=-1)
                self.last_z_loss = lse_a.square().mean() + lse_b.square().mean()
        else:
            self.last_z_loss = None

        top_a_s, top_a_i = scores_a.topk(self.sub_top_k, dim=-1)
        top_b_s, top_b_i = scores_b.topk(self.sub_top_k, dim=-1)

        if self.training:
            with torch.no_grad():
                self.ka_hits.add_(
                    torch.bincount(top_a_i.view(-1), minlength=self.sqrt_n)
                )
                self.kb_hits.add_(
                    torch.bincount(top_b_i.view(-1), minlength=self.sqrt_n)
                )

        # Outer-sum re-rank. The Python path materializes a
        # (B, T, sub_top_k²) `combined_scores` tensor which is the
        # dominant per-call activation at training time (4-256 MB per
        # call depending on B, T, sub_top_k). PKMFusedTopK is a C++
        # kernel that scans the S² outer-sum with a per-row min-heap,
        # skipping the temp entirely; identical autograd to the Python
        # path. Same kernel as Local PKM (memory.py:982) — the math
        # is generic across NetBank and Local PKM.
        if HAS_CPP_KERNELS and top_a_s.is_cpu:
            top_scores, top_global = PKMFusedTopK.apply(
                top_a_s, top_a_i, top_b_s, top_b_i, self.sqrt_n, self.top_k,
            )
        else:
            combined_scores = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
            top_scores, top_local = combined_scores.topk(self.top_k, dim=-1)
            # `top_local` indexes into the flat sub_top_k² combined grid.
            # Decompose back into (a_within, b_within) and gather the *global*
            # key indices from top_a_i / top_b_i — small (B,T,top_k) gathers.
            a_within = torch.div(top_local, self.sub_top_k, rounding_mode="floor")
            b_within = top_local - a_within * self.sub_top_k
            top_a_global = top_a_i.gather(-1, a_within)                # (B, T, top_k)
            top_b_global = top_b_i.gather(-1, b_within)
            top_global   = top_a_global * self.sqrt_n + top_b_global

        # Cross-device gather: V_net is fp16 CPU-mmap. Move indices to V's
        # device, gather rows there, ship results back up to q's device,
        # promote to fp32 for the expander matmul. Autograd flows back
        # through both .to() hops as sparse-grads on V_net.
        v_device = self.V.weight.device
        if v_device != q.device:
            top_global_v = top_global.to(v_device)
            latent_v = self.V(top_global_v)                        # (B, T, top_k, c_net) fp16
            latent = latent_v.to(q.device).float()
        else:
            latent = self.V(top_global).float()

        # Bottleneck → q_dim expansion. Fold the softmax weighting INTO the
        # weighted-sum via einsum instead of materializing the (B,T,top_k,q_dim)
        # `values` tensor and multiplying it elementwise by broadcasted softmax
        # weights. The naive version costs ~4 ms / call from the extra
        # allocation + broadcast; einsum does the contraction in one pass.
        weights = F.softmax(top_scores, dim=-1)                    # (B, T, top_k)
        # latent: (B,T,top_k,c_net); expander.weight: (q_dim,c_net)
        # out = sum_k weights[b,t,k] * (latent[b,t,k,:] @ expander.weight.T) + bias_scaled
        # Equivalent and avoids the intermediate (B,T,top_k,q_dim) allocation:
        weighted_latent = torch.einsum("btkc,btk->btc", latent, weights)
        out = self.expander(weighted_latent)

        # ── instrumentation: "is NetBank actually producing signal?" ──
        # Mean L2 norm of NetBank output per (B,T) position. ONLY in
        # training mode — at inference this is a per-layer CPU sync
        # (~30µs × 32 layers × tok = real fraction of decode wall) with
        # no functional value (telemetry consumer is the training loop).
        if self.training:
            with torch.no_grad():
                self.last_output_norm = float(
                    out.detach().pow(2).sum(-1).sqrt().mean().item()
                )
        return out

    # ─────────────────────── slot-usage helpers ───────────────────────

    def slot_usage_stats(self) -> dict:
        with torch.no_grad():
            ka_total = self.ka_hits.sum().item()
            kb_total = self.kb_hits.sum().item()
            stats = {
                "dead_a":   int((self.ka_hits == 0).sum().item()),
                "dead_b":   int((self.kb_hits == 0).sum().item()),
                "ka_total": ka_total,
                "kb_total": kb_total,
            }
            if ka_total > 0:
                pa = self.ka_hits.float() / ka_total
                pa_pos = pa[pa > 0]
                stats["entropy_a"] = -(pa_pos * pa_pos.log2()).sum().item()
                stats["entropy_a_max"] = float(torch.tensor(self.sqrt_n).log2())
            if kb_total > 0:
                pb = self.kb_hits.float() / kb_total
                pb_pos = pb[pb > 0]
                stats["entropy_b"] = -(pb_pos * pb_pos.log2()).sum().item()
            return stats

    def reset_slot_usage(self) -> None:
        with torch.no_grad():
            self.ka_hits.zero_()
            self.kb_hits.zero_()

    def reinit_dead_slots(self, hit_threshold: int = 0,
                          k_init_scale: float = 0.02) -> dict:
        """Re-init dead K_a/K_b rows. NetBank doesn't reset corresponding
        V rows (the Local Bank's V-reset path requires GPU-resident V; ours
        is mmap fp16). SparseAdam will learn what to put there once K
        attention pulls it in."""
        with torch.no_grad():
            ka_dead = self.ka_hits <= hit_threshold
            kb_dead = self.kb_hits <= hit_threshold
            n_a = int(ka_dead.sum().item())
            n_b = int(kb_dead.sum().item())
            if n_a > 0:
                noise = torch.randn(
                    n_a, self.sub_dim,
                    device=self.K_a.device, dtype=self.K_a.dtype,
                ) * k_init_scale
                self.K_a.data[ka_dead] = noise
            if n_b > 0:
                noise = torch.randn(
                    n_b, self.sub_dim,
                    device=self.K_b.device, dtype=self.K_b.dtype,
                ) * k_init_scale
                self.K_b.data[kb_dead] = noise
            return {"n_ka_reinit": n_a, "n_kb_reinit": n_b}

    def zero_bank(self) -> None:
        """Zero V_net (ablation utility, mirrors ProductKeyMemory)."""
        with torch.no_grad():
            self.V.weight.zero_()
