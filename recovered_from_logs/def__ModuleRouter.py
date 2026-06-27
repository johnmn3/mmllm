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

    def __init__(self, q_dim: int, module_names, *, k_load=None, k_tok: int = 2):
        super().__init__()
        self.module_names = list(module_names)
        n = len(self.module_names)
        self._idx = {name: i for i, name in enumerate(self.module_names)}
        self.module_keys = nn.Parameter(torch.zeros(n, q_dim))
        self.k_load = n if k_load is None else max(1, min(int(k_load), n))
        self.k_tok = max(1, min(int(k_tok), n))

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
        """Level 2 → per-token convex weights over `names` (B,T,len(names))."""
        idx = torch.tensor([self._idx[n] for n in names], device=q.device)
        logits = q @ self.module_keys[idx].t()        # (B,T,m)
        m = len(names)
        k = min(self.k_tok, m)
        if k < m:                                     # keep top-k per token, mask rest
            topv, topi = logits.topk(k, dim=-1)
            masked = torch.full_like(logits, float("-inf"))
            logits = masked.scatter(-1, topi, topv)
        return torch.softmax(logits, dim=-1)