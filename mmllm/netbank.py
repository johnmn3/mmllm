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
                             chunk_rows: int = 4096,
                             readonly: bool = False) -> torch.Tensor:
    """Open or create an (n, dim) memmap of the given dtype, return a
    torch tensor sharing the mmap storage. fp32 default for SparseAdam
    numerical stability (fp16 SparseAdam state can underflow / overflow);
    fp16 available behind MMLLM_NET_DTYPE=fp16 once we add a mixed-
    precision optimizer.

    readonly=True (COLD-SHARE): the file is a FROZEN cold module read from the
    SHARED round-bank inode by every PAR birth. Open MAP_SHARED PROT_READ
    (np.memmap mode='r') so a stray torch write cannot corrupt the shared file —
    torch.from_numpy on the non-writable mmap yields a non-writable tensor that
    raises on any in-place write. Pairs with StreamV(readonly=True) on the MLX
    side; both backends now open the shared inode read-only."""
    np_dt, _torch_dt, bytes_per = _DTYPE_MAP[dtype_str]
    expected_bytes = n * dim * bytes_per
    if readonly:
        # COLD-SHARE: NEVER write/recreate the shared inode. Open mode='r' over the
        # first n rows. The shared file may be LARGER than expected_bytes (e.g. a
        # 160-block seed bin viewed as a 144-block trie) — that's fine, we map the
        # leading n rows (every in-trie leaf is in-bounds). Smaller → hard error
        # (a real cold module must exist; we must not fall through to a w+ that
        # would de-sparsify + randomize the file every PAR birth shares).
        if not (os.path.exists(path) and os.path.getsize(path) >= expected_bytes):
            raise FileNotFoundError(
                f"cold-share readonly bank missing or too small: {path} "
                f"(have {os.path.getsize(path) if os.path.exists(path) else 0}, "
                f"need >= {expected_bytes})")
        arr = np.memmap(path, dtype=np_dt, mode="r", shape=(n, dim))
        return torch.from_numpy(arr)
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
                          chunk_rows: int = 4096,
                          n_blocks: int = 1) -> dict:
    """Pre-allocate NetBank V mmap files, one per layer. Idempotent."""
    n = n_blocks * sqrt_n * sqrt_n
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
                 bank_on_gpu: bool = False,
                 n_blocks: int = 1,
                 vq_route: bool = False,
                 n_coarse: int = 1,
                 n_coarse2: int = 1,
                 trie_depth: int = 0,
                 trie_branch: int = 32,
                 trie_resident_levels: int = 2,
                 readonly: bool = False):
        super().__init__()
        assert q_dim % 2 == 0, "q_dim must be even"
        assert c_net <= q_dim, "c_net (bottleneck dim) must be <= q_dim"
        assert dtype in _DTYPE_MAP, f"dtype must be one of {list(_DTYPE_MAP)}"

        self.q_dim = q_dim
        self.sub_dim = q_dim // 2
        self.sqrt_n = sqrt_n
        # Phase A trie (MMLLM_NET_TRIE_DEPTH): when on, the leaf count B^D drives
        # n_blocks (each leaf is a contiguous sqrt_n² V slab, exactly like the
        # legacy block partition); a depth-D 32-way descent replaces the LSH/VQ
        # block router. Default depth 0 → unchanged (byte-identical).
        self.trie_depth = int(trie_depth)
        self.trie_branch = int(trie_branch)
        self.trie_resident_levels = int(trie_resident_levels)
        # DYNAMIC DEPTH: a token stops descending once its residual norm < trie_stop_tau.
        # 0 → never stops early (fixed full depth). Higher → shallower average depth. Tune
        # toward the target avg (e.g. ~3.0 → ~6 levels at D_max=8 in the validated heap).
        self.trie_stop_tau = float(os.environ.get("MMLLM_NET_TRIE_STOP_TAU", "0.0"))
        if self.trie_depth > 0:
            # DYNAMIC DEPTH: a token can terminate at ANY node (not only the bottom
            # leaves), so EVERY heap node owns a V slab — n_blocks = the full node count
            # (B^{D+1}−1)/(B−1), not just B^D bottom leaves. The descent returns the stop
            # node's heap id, which offsets V exactly like the old leaf id did. (Stop is
            # data-driven by residual norm — MMLLM_NET_TRIE_STOP_TAU; 0 ⇒ full depth.)
            B, D = self.trie_branch, self.trie_depth
            n_blocks = (B ** (D + 1) - 1) // (B - 1)
        self.n_blocks = int(n_blocks)
        self.n = self.n_blocks * sqrt_n * sqrt_n
        self.c_net = c_net
        self.top_k = top_k
        self.sub_top_k = min(sub_top_k, sqrt_n)
        self.mmap_path = mmap_path
        self.readonly = bool(readonly)   # COLD-SHARE: shared inode opened read-only
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

        self.vq_route = bool(vq_route)
        self.n_coarse = int(n_coarse)
        if self.trie_depth > 0:
            # PHASE A: depth-D, B-way residual-VQ trie. Flat heap-indexed C/A over
            # all nodes (levels 0..D): (B^{D+1}−1)/(B−1) rows. C = per-node child
            # centroids, A = per-node shared "ancestor" value. Both zero-init →
            # acc=0 and argmax ties→leaf 0 until the per-level VQ loss + dead-code
            # revive train them (like coarse_value). Leaves live in V (n_blocks=B^D
            # slabs). No block_proj/block_codebook in trie mode. (MLX forward path;
            # torch forward uses leaf 0, same convention as the coarse path.)
            B, D = self.trie_branch, self.trie_depth
            n_nodes = (B ** (D + 1) - 1) // (B - 1)
            self.trie_C = nn.Parameter(torch.zeros(n_nodes, q_dim))
            self.trie_A = nn.Parameter(torch.zeros(n_nodes, q_dim))
        elif self.n_blocks > 1:
            _g = torch.Generator().manual_seed(0x5EED)
            self.register_buffer(
                "block_proj",
                (torch.randn(q_dim, self.n_blocks, generator=_g) / (q_dim ** 0.5)),
                persistent=True,
            )
            if self.vq_route:
                # Stage 1: LEARNED VQ codebook (centroids in q-space). Routing
                # blk = argmax(q@C.T) (cosine; q rms-normed), trained by the VQ
                # commitment+codebook loss so blocks become real semantic clusters
                # instead of random LSH cones. Init at block_proj scale.
                self.block_codebook = nn.Parameter(
                    torch.randn(self.n_blocks, q_dim, generator=_g) / (q_dim ** 0.5))
                if self.n_coarse > 1:
                    # Stage 2/3: RESIDUAL-VQ PATH-SUM. n_coarse coarse clusters (+ optional
                    # n_coarse2 second coarse level → depth-3). codeN from the running
                    # residual; each level's coarse_value[path] is a SHARED contribution
                    # added to every retrieval under that path (the "ancestor"). leaf block
                    # = path*fpc + fine. Similar q share coarse codes → share upper-level
                    # contributions, diverge only at the leaf. value tables zero-init = no-op
                    # until learned. (Applied in the MLX forward; torch uses block 0.)
                    self.n_coarse2 = int(n_coarse2)
                    n_levels = self.n_coarse * (self.n_coarse2 if self.n_coarse2 > 1 else 1)
                    assert self.n_blocks % n_levels == 0, "n_blocks must be divisible by n_coarse*n_coarse2"
                    # RECOVERY NOTE (best-inference): the depth-3 coarse-value table
                    # allocations past this point were NOT captured verbatim in the
                    # transcript (read #11 / blob 13503 cut off at the assert above;
                    # blob 13246 cut off at `fpc = self.n_blocks`). The lines below
                    # follow the captured depth-2 pattern (blob 13121). torch ignores
                    # these (uses block 0); they matter only for the MLX forward.
                    fpc = self.n_blocks // n_levels
                    self.coarse_codebook = nn.Parameter(
                        torch.randn(self.n_coarse, q_dim, generator=_g) / (q_dim ** 0.5))
                    self.coarse_value = nn.Parameter(torch.zeros(self.n_coarse, q_dim))
                    self.fine_codebook = nn.Parameter(
                        torch.randn(fpc, q_dim, generator=_g) / (q_dim ** 0.5))
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
            v_tensor = _mmap_value_tensor_typed(mmap_path, self.n, c_net, dtype,
                                                readonly=self.readonly)
            # COLD-SHARE: freeze a read-only (shared-inode) cold module so no
            # optimizer/grad ever targets the shared file. Hot module unchanged.
            self.V = CPUPinnedEmbedding.from_pretrained(
                v_tensor, freeze=self.readonly, sparse=True,
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


# ════════════════════════ ModularNetBank ════════════════════════
#
# Skill-module partition of the NetBank. Instead of one monolithic bank
# shared by every skill (which causes cross-skill interference — training
# one skill drifts another skill's rows, the ctrl_bpc-regression failure
# mode), hold ONE independent NetBank per skill module. Each module owns its
# K_a/K_b/V_net/expander and its own per-layer mmap file, so a cooled
# (frozen) module's rows literally cannot move — cross-skill forgetting
# becomes structurally impossible rather than merely discouraged.
#
# Drop-in for NetBank: forward(q) -> (B, T, q_dim); attention_kernel's
# `netbank(bank_q)` call is unchanged. Routing (which module(s) a forward
# consults) is set out-of-band via set_active() BEFORE the forward — by the
# corpus tag during genesis, by the learned skill-router later — so the
# attention-kernel signature stays untouched.
#
# Staged-cooling support:
#   * per-module optimizer groups via module_{dense,sparse}_parameters(name)
#     → each bank gets its own LR multiplier / cosine schedule, so mastered
#     banks sit at ~0 while the newest bank is hot.
#   * freeze_module(name) hard-stops a mastered module (requires_grad=False)
#     → optimizer steps are no-ops and its V_net moved% -> 0 by construction.


class ModuleRouter(nn.Module):
    """Learned two-level skill router over a ModularNetBank's per-module banks.

    Scores the bank query q against one learned key vector per module:
      Level 1 — preselect(q): mean-pool q over T, score ALL N modules, take
        top-`k_load`. These are the modules RUN (and mmap-paged-in) this forward
        = the LRU hot-set admission policy. Cheap (a [B,N] matmul; no bank fwd
        for the unselected).
      Level 2 — weights(q, names): per-token score over the loaded set, keep
        top-`k_tok`, softmax → per-token convex weights for the weighted sum.
        Off-domain modules get ≈0 weight per token → no interference; the summed
        magnitude is bounded (weights sum to 1) regardless of how many are loaded.
      logits(q): per-token scores over ALL modules — used for the genesis
        aux cross-entropy loss (supervised by the corpus→module tag).

    `module_keys` is ZERO-init: an untrained router gives uniform weights (a
    convex combination = mean of the active modules), which is well-behaved and
    bounded; it trains toward sharp per-skill routing. (Router OFF — not built —
    leaves the plain-sum forward byte-identical; see ModularNetBank.)"""

    def __init__(self, q_dim: int, module_names, *, k_load=None, k_tok: int = 2,
                 gate: str = "softmax"):
        super().__init__()
        self.module_names = list(module_names)
        n = len(self.module_names)
        self._idx = {name: i for i, name in enumerate(self.module_names)}
        self.module_keys = nn.Parameter(torch.zeros(n, q_dim))
        self.k_load = n if k_load is None else max(1, min(int(k_load), n))
        self.k_tok = max(1, min(int(k_tok), n))
        self.gate = gate                  # "softmax" (convex top-k) | "sigmoid" (per-module)

    def logits(self, q: torch.Tensor) -> torch.Tensor:
        """q (B,T,q_dim) → per-token module logits (B,T,N)."""
        return q @ self.module_keys.t()

    def preselect(self, q: torch.Tensor):
        """Level 1 → list of module names to run (union of per-sequence top-k_load)."""
        if self.k_load >= len(self.module_names):
            return list(self.module_names)
        qbar = q.mean(dim=1)                          # (B, q_dim)
        sel = (qbar @ self.module_keys.t()).topk(self.k_load, dim=-1).indices  # (B, k_load)
        keep = sorted(set(int(i) for i in sel.flatten().tolist()))            # union across batch
        return [self.module_names[i] for i in keep]

    def weights(self, q: torch.Tensor, names) -> torch.Tensor:
        """Level 2 → per-token module weights over `names` (B,T,len(names)).
        softmax: convex top-k_tok (sums to 1, forces a fixed-k choice).
        sigmoid: independent per-module gate in [0,1] — variable effective-k, so
        OVERLAPPING skills can co-fire (both ≈1) or self-suppress (≈0) instead of
        competing in a softmax (fixes the overlapping-skill routing tax)."""
        idx = torch.tensor([self._idx[n] for n in names], device=q.device)
        logits = q @ self.module_keys[idx].t()        # (B,T,m)
        if self.gate == "sigmoid":
            return torch.sigmoid(logits)
        m = len(names)
        k = min(self.k_tok, m)
        if k < m:                                     # keep top-k per token, mask rest
            topv, topi = logits.topk(k, dim=-1)
            masked = torch.full_like(logits, float("-inf"))
            logits = masked.scatter(-1, topi, topv)
        return torch.softmax(logits, dim=-1)


class ModularNetBank(nn.Module):
    """A dict of independent per-skill NetBank modules sharing the NetBank
    forward interface. See module comment above."""

    def __init__(self, q_dim: int, module_names, *,
                 sqrt_n: int = 8192, c_net: int = 64,
                 top_k: int = 64, sub_top_k: int = 64,
                 mmap_prefix: "str | None" = None, mmap_layer: "int | None" = None,
                 delay_ms_min: float = 1.0, delay_ms_max: float = 10.0,
                 dtype: str = "fp32", bank_on_gpu: bool = False,
                 router: bool = False, router_k_load=None, router_k_tok: int = 2,
                 router_drive: bool = False, router_gate: str = "softmax",
                 n_blocks: int = 1, vq_route: bool = False, n_coarse: int = 1,
                 n_coarse2: int = 1, trie_depth: int = 0, trie_branch: int = 32,
                 trie_resident_levels: int = 2):
        super().__init__()
        module_names = list(module_names)
        if not module_names:
            raise ValueError("ModularNetBank needs at least one module name")
        self.module_names = module_names
        self.q_dim = q_dim
        self.banks = nn.ModuleDict()
        # COLD-SHARE (default off): a "bird" trains its HOT module and freezes the
        # rest. When on, the cold (frozen) modules are NOT CoW-cloned per bird;
        # they point at the SHARED round-bank prefix instead, so torch's V mmap and
        # the MLX StreamV both open the SAME inode across all PAR births → one copy
        # via the OS page cache. Off → mmap_prefix for every module (unchanged).
        _cold_share = os.environ.get("MMLLM_NET_COLD_SHARE", "").lower() in ("1", "true", "yes")
        _hot = os.environ.get("MMLLM_NET_HOT_MODULE", "")
        _rb_prefix = os.environ.get("MMLLM_NET_COLD_SHARE_RB_PREFIX", "")
        for name in module_names:
            mp = None
            _ro = False
            if mmap_prefix is not None:
                # shared cross-backend naming (torch + MLX + harvester agree)
                from mmllm.skill_modules import netbank_v_path
                _prefix = mmap_prefix
                if _cold_share and _rb_prefix and _hot and name != _hot:
                    _prefix = _rb_prefix                    # cold module → shared round-bank inode
                    _ro = True                              # ...opened read-only (no stray write → no shared-file corruption)
                mp = netbank_v_path(_prefix, name, 0 if mmap_layer is None else mmap_layer)
            self.banks[name] = NetBank(
                q_dim, sqrt_n=sqrt_n, c_net=c_net, top_k=top_k,
                sub_top_k=sub_top_k, mmap_path=mp,
                delay_ms_min=delay_ms_min, delay_ms_max=delay_ms_max,
                dtype=dtype, bank_on_gpu=bank_on_gpu, n_blocks=n_blocks,
                vq_route=vq_route, n_coarse=n_coarse, n_coarse2=n_coarse2,
                trie_depth=trie_depth, trie_branch=trie_branch,
                trie_resident_levels=trie_resident_levels, readonly=_ro,
            )
        # Routing: which module(s) the next forward consults. None = all.
        self._active = None
        # Learned two-level skill router (default OFF → plain-sum behavior intact).
        # router_drive lets it pick the active set when _active is None (inference);
        # during genesis _active is the corpus tag, so the router only LEARNS.
        self.router = (ModuleRouter(q_dim, module_names, k_load=router_k_load,
                                    k_tok=router_k_tok, gate=router_gate)
                       if router else None)
        self.router_drive = bool(router_drive)
        self.router_logits = None          # stashed per forward for the aux loss
        # Telemetry parity with NetBank (the block forward reads last_z_loss).
        self.last_z_loss = None

    # ─────────────────── routing ───────────────────

    def set_active(self, names) -> None:
        """Restrict the next forward(s) to module name(s). Set by the corpus
        tag during genesis, by the learned router later. None = all modules
        (composition)."""
        if names is None:
            self._active = None
            return
        if isinstance(names, str):
            names = [names]
        names = list(names)
        for n in names:
            if n not in self.banks:
                raise KeyError(f"unknown netbank module {n!r}; have {self.module_names}")
        self._active = names

    def active_names(self):
        return list(self._active) if self._active is not None else list(self.module_names)

    # ─────────────────── forward (drop-in for NetBank) ───────────────────

    def forward(self, q: torch.Tensor) -> torch.Tensor:
        # Stash per-token logits over ALL modules for the genesis aux loss
        # (computed even when the corpus tag drives, so the router learns).
        self.router_logits = self.router.logits(q) if self.router is not None else None
        # Level 1: router picks the active set only at inference (router_drive
        # AND no corpus tag set); during genesis _active is the tag → unchanged.
        if self.router is not None and self.router_drive and self._active is None:
            names = self.router.preselect(q)
        else:
            names = self.active_names()
        if len(names) == 1:
            out = self.banks[names[0]](q)
            self.last_z_loss = self.banks[names[0]].last_z_loss
            return out
        # Composition. With a DRIVING router: per-token convex weights (Level 2)
        # bound the magnitude and zero off-domain modules. Otherwise the plain sum
        # (so drive=False is byte-comparable to the no-router baseline).
        w = self.router.weights(q, names) if (self.router is not None and self.router_drive) else None
        out = None
        z = None
        for i, n in enumerate(names):
            o = self.banks[n](q)
            if w is not None:
                o = o * w[..., i:i + 1]
            out = o if out is None else out + o
            lz = self.banks[n].last_z_loss
            if lz is not None:
                z = lz if z is None else z + lz
        self.last_z_loss = z
        return out

    # ───────────── per-module parameter access (per-module LR) ─────────────

    def module_dense_parameters(self, name):
        return self.banks[name].dense_parameters()

    def module_sparse_parameters(self, name):
        return self.banks[name].sparse_parameters()

    # aggregate access — back-compat with the single-bank optimizer setup
    def dense_parameters(self):
        return [p for n in self.module_names for p in self.banks[n].dense_parameters()]

    def sparse_parameters(self):
        return [p for n in self.module_names for p in self.banks[n].sparse_parameters()]

    # ─────────────────── cooling ───────────────────

    def freeze_module(self, name: str, frozen: bool = True) -> None:
        """Cooling: stop a mastered module's params updating (requires_grad
        off) so optimizer steps are no-ops and its V_net moved% -> 0. The
        structural isolation guarantee — a cooled skill cannot drift."""
        b = self.banks[name]
        for p in list(b.dense_parameters()) + list(b.sparse_parameters()):
            p.requires_grad_(not frozen)

    def is_frozen(self, name: str) -> bool:
        return not any(p.requires_grad for p in self.banks[name].dense_parameters())

    def warm_start_module(self, name, local_K_a, local_K_b, local_V=None):
        self.banks[name].warm_start_from(local_K_a, local_K_b, local_V)
