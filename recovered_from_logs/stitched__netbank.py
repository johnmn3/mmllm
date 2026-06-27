<<<MISSING line 1>>>
<<<MISSING line 2>>>
<<<MISSING line 3>>>
<<<MISSING line 4>>>
<<<MISSING line 5>>>
<<<MISSING line 6>>>
<<<MISSING line 7>>>
<<<MISSING line 8>>>
<<<MISSING line 9>>>
<<<MISSING line 10>>>
<<<MISSING line 11>>>
<<<MISSING line 12>>>
<<<MISSING line 13>>>
<<<MISSING line 14>>>
<<<MISSING line 15>>>
<<<MISSING line 16>>>
<<<MISSING line 17>>>
<<<MISSING line 18>>>
<<<MISSING line 19>>>
<<<MISSING line 20>>>
<<<MISSING line 21>>>
<<<MISSING line 22>>>
<<<MISSING line 23>>>
<<<MISSING line 24>>>
<<<MISSING line 25>>>
<<<MISSING line 26>>>
<<<MISSING line 27>>>
<<<MISSING line 28>>>
<<<MISSING line 29>>>
<<<MISSING line 30>>>
<<<MISSING line 31>>>
<<<MISSING line 32>>>
<<<MISSING line 33>>>
<<<MISSING line 34>>>
<<<MISSING line 35>>>
<<<MISSING line 36>>>
<<<MISSING line 37>>>
<<<MISSING line 38>>>
<<<MISSING line 39>>>
<<<MISSING line 40>>>
<<<MISSING line 41>>>
<<<MISSING line 42>>>
<<<MISSING line 43>>>
<<<MISSING line 44>>>
<<<MISSING line 45>>>
<<<MISSING line 46>>>
<<<MISSING line 47>>>
<<<MISSING line 48>>>
<<<MISSING line 49>>>
<<<MISSING line 50>>>
<<<MISSING line 51>>>
<<<MISSING line 52>>>
<<<MISSING line 53>>>
<<<MISSING line 54>>>
<<<MISSING line 55>>>
<<<MISSING line 56>>>
<<<MISSING line 57>>>
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
                 bank_on_gpu: bool = False,
                 n_blocks: int = 1):
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
        self.n_coarse = int(n_coarse)
        if self.n_blocks > 1:
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
        `local.sqrt_n` rows of NetBank. Bootstraps the retrieval geometry
        so queries that score highly against a Local row also score highly
        against the corresponding NetBank row from step 0.

        K_a/K_b share dtype/shape between Local and NetBank, so they
        copy directly.

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
<<<MISSING line 345>>>
<<<MISSING line 346>>>
<<<MISSING line 347>>>
<<<MISSING line 348>>>
<<<MISSING line 349>>>
<<<MISSING line 350>>>
<<<MISSING line 351>>>
<<<MISSING line 352>>>
<<<MISSING line 353>>>
<<<MISSING line 354>>>
<<<MISSING line 355>>>
<<<MISSING line 356>>>
<<<MISSING line 357>>>
<<<MISSING line 358>>>
<<<MISSING line 359>>>
<<<MISSING line 360>>>
<<<MISSING line 361>>>
<<<MISSING line 362>>>
<<<MISSING line 363>>>
<<<MISSING line 364>>>
<<<MISSING line 365>>>
<<<MISSING line 366>>>
<<<MISSING line 367>>>
<<<MISSING line 368>>>
<<<MISSING line 369>>>
<<<MISSING line 370>>>
<<<MISSING line 371>>>
<<<MISSING line 372>>>
<<<MISSING line 373>>>
<<<MISSING line 374>>>
<<<MISSING line 375>>>
<<<MISSING line 376>>>
<<<MISSING line 377>>>
<<<MISSING line 378>>>
<<<MISSING line 379>>>
<<<MISSING line 380>>>
<<<MISSING line 381>>>
<<<MISSING line 382>>>
<<<MISSING line 383>>>
<<<MISSING line 384>>>
<<<MISSING line 385>>>
<<<MISSING line 386>>>
<<<MISSING line 387>>>
<<<MISSING line 388>>>
<<<MISSING line 389>>>
<<<MISSING line 390>>>
<<<MISSING line 391>>>
<<<MISSING line 392>>>
<<<MISSING line 393>>>
<<<MISSING line 394>>>
<<<MISSING line 395>>>
<<<MISSING line 396>>>
<<<MISSING line 397>>>
<<<MISSING line 398>>>
<<<MISSING line 399>>>
<<<MISSING line 400>>>
<<<MISSING line 401>>>
<<<MISSING line 402>>>
<<<MISSING line 403>>>
<<<MISSING line 404>>>
<<<MISSING line 405>>>
<<<MISSING line 406>>>
<<<MISSING line 407>>>
<<<MISSING line 408>>>
<<<MISSING line 409>>>
<<<MISSING line 410>>>
<<<MISSING line 411>>>
<<<MISSING line 412>>>
<<<MISSING line 413>>>
<<<MISSING line 414>>>
<<<MISSING line 415>>>
<<<MISSING line 416>>>
<<<MISSING line 417>>>
<<<MISSING line 418>>>
<<<MISSING line 419>>>
<<<MISSING line 420>>>
<<<MISSING line 421>>>
<<<MISSING line 422>>>
<<<MISSING line 423>>>
<<<MISSING line 424>>>
<<<MISSING line 425>>>
<<<MISSING line 426>>>
<<<MISSING line 427>>>
<<<MISSING line 428>>>
<<<MISSING line 429>>>
<<<MISSING line 430>>>
<<<MISSING line 431>>>
<<<MISSING line 432>>>
<<<MISSING line 433>>>
<<<MISSING line 434>>>
<<<MISSING line 435>>>
<<<MISSING line 436>>>
<<<MISSING line 437>>>
<<<MISSING line 438>>>
<<<MISSING line 439>>>
<<<MISSING line 440>>>
<<<MISSING line 441>>>
<<<MISSING line 442>>>
<<<MISSING line 443>>>
<<<MISSING line 444>>>
<<<MISSING line 445>>>
<<<MISSING line 446>>>
<<<MISSING line 447>>>
<<<MISSING line 448>>>
<<<MISSING line 449>>>
<<<MISSING line 450>>>
<<<MISSING line 451>>>
<<<MISSING line 452>>>
<<<MISSING line 453>>>
<<<MISSING line 454>>>
<<<MISSING line 455>>>
<<<MISSING line 456>>>
<<<MISSING line 457>>>
<<<MISSING line 458>>>
<<<MISSING line 459>>>
<<<MISSING line 460>>>
<<<MISSING line 461>>>
<<<MISSING line 462>>>
<<<MISSING line 463>>>
<<<MISSING line 464>>>
<<<MISSING line 465>>>
<<<MISSING line 466>>>
<<<MISSING line 467>>>
<<<MISSING line 468>>>
<<<MISSING line 469>>>
<<<MISSING line 470>>>
<<<MISSING line 471>>>
<<<MISSING line 472>>>
<<<MISSING line 473>>>
<<<MISSING line 474>>>
<<<MISSING line 475>>>
<<<MISSING line 476>>>
<<<MISSING line 477>>>
<<<MISSING line 478>>>
<<<MISSING line 479>>>
<<<MISSING line 480>>>
<<<MISSING line 481>>>
<<<MISSING line 482>>>
<<<MISSING line 483>>>
<<<MISSING line 484>>>
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

class ModularNetBank(nn.Module):
    """A dict of independent per-skill NetBank modules sharing the NetBank
    forward interface. See module comment above."""

    def __init__(self, q_dim: int, module_names, *,
                 sqrt_n: int = 8192, c_net: int = 64,
                 top_k: int = 64, sub_top_k: int = 64,
                 mmap_prefix: "str | None" = None, mmap_layer: "int | None" = None,
                 delay_ms_min: float = 1.0, delay_ms_max: float = 10.0,
                 dtype: str = "fp32", bank_on_gpu: bool = False):
        super().__init__()
        module_names = list(module_names)
        if not module_names:
            raise ValueError("ModularNetBank needs at least one module name")
        self.module_names = module_names
        self.q_dim = q_dim
        self.banks = nn.ModuleDict()
        for name in module_names:
            mp = None
            if mmap_prefix is not None:
                # shared cross-backend naming (torch + MLX + harvester agree)
                from mmllm.skill_modules import netbank_v_path
                mp = netbank_v_path(mmap_prefix, name, 0 if mmap_layer is None else mmap_layer)
            self.banks[name] = NetBank(
                q_dim, sqrt_n=sqrt_n, c_net=c_net, top_k=top_k,
                sub_top_k=sub_top_k, mmap_path=mp,
                delay_ms_min=delay_ms_min, delay_ms_max=delay_ms_max,
                dtype=dtype, bank_on_gpu=bank_on_gpu,
            )
        # Routing: which module(s) the next forward consults. None = all.
        self._active = None
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
        names = self.active_names()
        if len(names) == 1:
            out = self.banks[names[0]](q)
            self.last_z_loss = self.banks[names[0]].last_z_loss
            return out
        # composition: sum active module outputs (a learned gate can replace
        # the plain sum once we move past genesis tag-routing).
        out = None
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
                 router_drive: bool = False, router_gate: str = "softmax"):
        super().__init__()
        module_names = list(module_names)
        if not module_names:
            raise ValueError("ModularNetBank needs at least one module name")
        self.module_names = module_names
        self.q_dim = q_dim
        self.banks = nn.ModuleDict()
        for name in module_names:
            mp = None
            if mmap_prefix is not None:
                # shared cross-backend naming (torch + MLX + harvester agree)
                from mmllm.skill_modules import netbank_v_path
                mp = netbank_v_path(mmap_prefix, name, 0 if mmap_layer is None else mmap_layer)
            self.banks[name] = NetBank(
                q_dim, sqrt_n=sqrt_n, c_net=c_net, top_k=top_k,
                sub_top_k=sub_top_k, mmap_path=mp,
                delay_ms_min=delay_ms_min, delay_ms_max=delay_ms_max,
                dtype=dtype, bank_on_gpu=bank_on_gpu,
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
                 delay_ms_min: float = 1.0, delay_ms_max: float = 10.0,
                 dtype: str = "fp32", bank_on_gpu: bool = False,
                 router: bool = False, router_k_load=None, router_k_tok: int = 2,
                 router_drive: bool = False, router_gate: str = "softmax",
                 n_blocks: int = 1, vq_route: bool = False, n_coarse: int = 1,
                 n_coarse2: int = 1):
        super().__init__()
        module_names = list(module_names)
        if not module_names:
            raise ValueError("ModularNetBank needs at least one module name")
        self.module_names = module_names
        self.q_dim = q_dim
        self.banks = nn.ModuleDict()
        for name in module_names:
            mp = None
            if mmap_prefix is not None:
                # shared cross-backend naming (torch + MLX + harvester agree)
                from mmllm.skill_modules import netbank_v_path
                mp = netbank_v_path(mmap_prefix, name, 0 if mmap_layer is None else mmap_layer)
            self.banks[name] = NetBank(
                q_dim, sqrt_n=sqrt_n, c_net=c_net, top_k=top_k,
                sub_top_k=sub_top_k, mmap_path=mp,
                delay_ms_min=delay_ms_min, delay_ms_max=delay_ms_max,
                dtype=dtype, bank_on_gpu=bank_on_gpu, n_blocks=n_blocks,
                vq_route=vq_route, n_coarse=n_coarse, n_coarse2=n_coarse2,
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