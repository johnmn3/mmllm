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