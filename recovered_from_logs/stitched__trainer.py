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
<<<MISSING line 58>>>
<<<MISSING line 59>>>
<<<MISSING line 60>>>
<<<MISSING line 61>>>
<<<MISSING line 62>>>
<<<MISSING line 63>>>
<<<MISSING line 64>>>
<<<MISSING line 65>>>
<<<MISSING line 66>>>
<<<MISSING line 67>>>
<<<MISSING line 68>>>
<<<MISSING line 69>>>
<<<MISSING line 70>>>
<<<MISSING line 71>>>
<<<MISSING line 72>>>
<<<MISSING line 73>>>
<<<MISSING line 74>>>
<<<MISSING line 75>>>
<<<MISSING line 76>>>
<<<MISSING line 77>>>
<<<MISSING line 78>>>
<<<MISSING line 79>>>
<<<MISSING line 80>>>
<<<MISSING line 81>>>
<<<MISSING line 82>>>
<<<MISSING line 83>>>
<<<MISSING line 84>>>
<<<MISSING line 85>>>
<<<MISSING line 86>>>
<<<MISSING line 87>>>
<<<MISSING line 88>>>
<<<MISSING line 89>>>
<<<MISSING line 90>>>
<<<MISSING line 91>>>
<<<MISSING line 92>>>
<<<MISSING line 93>>>
<<<MISSING line 94>>>
<<<MISSING line 95>>>
<<<MISSING line 96>>>
<<<MISSING line 97>>>
        # does not. W_ctx makes the bank query content-discriminative (bank_q += W_ctx·x)
        # — the missing ingredient that de-collapses retrieval. Trained as a dense param.
        bq = g("bank-query")
        if bq is not None and getattr(bq, "proj", None) is not None:
            tb["bank_query_w"] = _mxa(bq.proj.weight)        # [q_dim, d_model]

        mem = g("memory")
        if mem is not None:
            bmeta["memory"] = True
            tb["mem_q_norm_w"] = _mxa(mem.q_norm.weight)
            tb["mem_K_a"] = _mxa(mem.K_a); tb["mem_K_b"] = _mxa(mem.K_b)
            tb["V_local"] = _mxa(mem.V.weight)
            sb["mem"] = {"eps": _eps(mem.q_norm), "sub_dim": mem.sub_dim,
                         "sqrt_n": mem.sqrt_n, "sub_top_k": mem.sub_top_k,
                         "top_k": mem.top_k, "n_trunks": getattr(mem, "n_trunks", 1)}
        nb = g("netbank")
        if nb is not None:
            bmeta["netbank"] = True
            # MMLLM_NET_WIDEN=C: widen netbank code dim c_net -> C (8->16=q_dim),
            # removing the expander-rank bottleneck. V_net new cols=0; expander
            # new cols=small random (zero-on-both deadlocks the gradient).
            _widen = int(os.environ.get("MMLLM_NET_WIDEN", "0"))
            def _emit_net(bank):
                d = {"net_q_norm_w": _mxa(bank.q_norm.weight),
                     "net_K_a": _mxa(bank.K_a), "net_K_b": _mxa(bank.K_b),
                     "net_expander_w": _mxa(bank.expander.weight),
                     "V_net": _mxa(bank.V.weight)}
                if getattr(bank, "block_codebook", None) is not None:
                    d["net_block_codebook"] = _mxa(bank.block_codebook)   # learned VQ centroids (trainable)
                for _nm in ("coarse_codebook", "coarse_value", "coarse2_codebook", "coarse2_value", "fine_codebook"):   # Stage 2 path-sum
                    if getattr(bank, _nm, None) is not None:
                        d["net_" + _nm] = _mxa(getattr(bank, _nm))
                if _widen > d["V_net"].shape[1]:
                    _pad = _widen - d["V_net"].shape[1]; _N = d["V_net"].shape[0]
                    d["V_net"] = mx.concatenate(
                        [d["V_net"], mx.zeros((_N, _pad), dtype=d["V_net"].dtype)], axis=1)
                    _ew = d["net_expander_w"]
                    d["net_expander_w"] = mx.concatenate(
                        [_ew, (0.02 * mx.random.normal((_ew.shape[0], _pad))).astype(_ew.dtype)], axis=1)
                return d
            if hasattr(nb, "banks"):                 # ModularNetBank (skill-module partition)
                bmeta["net_modular"] = True
                bmeta["net_modules"] = list(nb.module_names)
                tb["netbanks"] = {name: _emit_net(nb.banks[name]) for name in nb.module_names}
                ref = nb.banks[nb.module_names[0]]
                sb["net"] = {"eps": _eps(ref.q_norm), "sub_dim": ref.sub_dim,
                             "sqrt_n": ref.sqrt_n, "sub_top_k": ref.sub_top_k, "top_k": ref.top_k,
                             "n_blocks": getattr(ref, "n_blocks", 1)}
                             "sqrt_n": ref.sqrt_n, "sub_top_k": ref.sub_top_k, "top_k": ref.top_k,
                             "n_blocks": getattr(ref, "n_blocks", 1)}
                if _vstream:                              # disk-stream: V on disk via StreamV handles (per module)
                    from mmllm.mlx.stream_v import StreamV
                    _slr = float(os.environ.get("MMLLM_NET_STREAM_LR", "0.003"))
                    sb["net"]["stream"] = {name: StreamV(nb.banks[name].mmap_path,
                                                         nb.banks[name].n, nb.banks[name].c_net, lr=_slr)
                                           for name in nb.module_names}
                if getattr(ref, "n_blocks", 1) > 1 and hasattr(ref, "block_proj"):
                    # fixed LSH [q_dim, n_blocks] — CONSTANT, lives in static (not
                    # trainable, so no spurious grad / optimizer corruption). Same R
                    # across modules (shared seed), so one copy suffices.
                    sb["net"]["block_proj"] = _mxa(ref.block_proj)
                if getattr(nb, "router", None) is not None:   # learned skill router
                tb["net_K_a"] = d["net_K_a"]; tb["net_K_b"] = d["net_K_b"]
def _reassemble(trainable, static, meta, student=False, drop_net=False):
    """trainable + static -> the param dict model.forward consumes. Gate params
    come from `trainable` (via closures) so gradients flow to them.

    student names the OUTPUT-KD student forward's freeze level (all LOCAL banks
    off in every case — the future state when locals reset):
      "off"   -> not a student forward (locals ON, nothing frozen): the teacher/CE path.
      "none"  -> locals off, nothing frozen (gate+net+trunk all adapt to locals-off).
      "trunk" -> locals off, freeze the DENSE TRUNK + embeddings; gate + netbank
                 adapt. Honours "the trunk freezes over time" while letting routing
                 and consolidation (where learning belongs) adapt. [default]
      "all"   -> locals off, freeze everything except V_net (over-froze: V_net through
                 frozen keys can't absorb the gap → distorts. kept for ablation)."""
    sg = mx.stop_gradient
    lvl = student if isinstance(student, str) else ("all" if student else "off")
    Ft = (lambda t: sg(t)) if lvl in ("trunk", "all") else (lambda t: t)   # dense trunk + emb
    Fa = (lambda t: sg(t)) if lvl == "all" else (lambda t: t)              # gate + net keys
    Fo = (lambda t: None if t is None else Fa(t))                          # optional gate tensor
    locals_off = (lvl != "off")
def _mlx_eval_bpc(trainable, static, meta, vdata, T, B, cap, net_active, vocab, drop_net=False):
    """MLX bits-per-char over vdata, full-model forward — used in the disk-stream
    path (MMLLM_NET_VSTREAM) instead of eval_bpc's torch forward, which would index
    the 1-row dummy torch V. Routes V through StreamV (bounded LRU, hard eviction
    authority), exactly like training. net_active: None=all modules, or [names].
    drop_net=True → netbank OFF (for the Δ_net consolidation ablation)."""
    import numpy as _np, mlx.core as _mx, mmllm.mlx.model as _MD
    data = _np.asarray(vdata).reshape(-1).astype(_np.int64)
    n_win = max(1, min((len(data) - 1) // T, cap // T))
    static = dict(static); static["_net_active"] = net_active     # control eval composition
    P = _reassemble(trainable, static, meta, drop_net=drop_net)   # full model (or net OFF), V via StreamV
    tot_nats = 0.0; tot_tok = 0
    for s in range(0, n_win, B):
        nb = min(B, n_win - s)
        xb = _np.empty((nb, T), _np.int64); yb = _np.empty((nb, T), _np.int64)
        for j in range(nb):
            o = (s + j) * T
            xb[j] = data[o:o + T]; yb[j] = data[o + 1:o + 1 + T]
        lg = _MD.forward(P, _mx.array(xb))
        lg = (lg[0] if isinstance(lg, tuple) else lg).reshape(-1, vocab)
        logp = lg - _mx.logsumexp(lg, axis=-1, keepdims=True)
        ce = -_mx.take_along_axis(logp, _mx.array(yb).reshape(-1)[:, None], axis=-1)
        _mx.eval(ce)
        tot_nats += float(_mx.sum(ce)); tot_tok += ce.size
    return (tot_nats / max(1, tot_tok)) / 0.6931471805599453   # nats→bits


def _reassemble(trainable, static, meta, student=False, drop_net=False):
    """trainable + static -> the param dict model.forward consumes. Gate params
    come from `trainable` (via closures) so gradients flow to them.

    student names the OUTPUT-KD student forward's freeze level (all LOCAL banks
    off in every case — the future state when locals reset):
      "off"   -> not a student forward (locals ON, nothing frozen): the teacher/CE path.
      "none"  -> locals off, nothing frozen (gate+net+trunk all adapt to locals-off).
      "trunk" -> locals off, freeze the DENSE TRUNK + embeddings; gate + netbank
                 adapt. Honours "the trunk freezes over time" while letting routing
                 and consolidation (where learning belongs) adapt. [default]
      "all"   -> locals off, freeze everything except V_net (over-froze: V_net through
                 frozen keys can't absorb the gap → distorts. kept for ablation)."""
    sg = mx.stop_gradient
    lvl = student if isinstance(student, str) else ("all" if student else "off")
    Ft = (lambda t: sg(t)) if lvl in ("trunk", "all") else (lambda t: t)   # dense trunk + emb
    Fa = (lambda t: sg(t)) if lvl == "all" else (lambda t: t)              # gate + net keys
    Fo = (lambda t: None if t is None else Fa(t))                          # optional gate tensor
    locals_off = (lvl != "off")
    P = {
        "tok_emb": Ft(trainable["tok_emb"]),
        "norm_final_w": Ft(trainable["norm_final_w"]),
        "norm_final_eps": static["norm_final_eps"],
        "rope_cos": static["rope_cos"], "rope_sin": static["rope_sin"],
        "blocks": [],
    }
    for tb, sb, bm in zip(trainable["blocks"], static["blocks"], meta["blocks"]):
        b = {k: Ft(tb[k]) for k in ("norm1_w", "norm2_w", "q_proj", "k_proj_s",
                                    "v_proj_s", "k_proj_l", "v_proj_l", "o_proj",
                                    "gate_proj", "up_proj", "down_proj")}
        b.update(n_heads=sb["n_heads"], n_short_heads=sb["n_short_heads"],
                 n_long_heads=sb["n_long_heads"], n_short_kv=sb["n_short_kv"],
                 n_long_kv=sb["n_long_kv"], head_dim=sb["head_dim"],
        elif bm["netbank"] and not drop_net:            # drop_net=True -> LOCAL-only teacher
            nn_ = sb["net"]
            b["netbank"] = {"q_norm_w": Fa(tb["net_q_norm_w"]), "eps": nn_["eps"],
                            "K_a": Fa(tb["net_K_a"]), "K_b": Fa(tb["net_K_b"]),
                            "V": tb["V_net"],                    # V_net stays LIVE
                            "expander_w": Fa(tb["net_expander_w"]), "sub_dim": nn_["sub_dim"],
                            "sqrt_n": nn_["sqrt_n"], "sub_top_k": nn_["sub_top_k"],
                            "top_k": nn_["top_k"]}
        P["blocks"].append(b)
    return P


def _write_back(trainable, m, K):
    """Copy trained MLX arrays back into the torch model params, by role."""
    import torch
    def cp(param, arr):
        param.data.copy_(torch.from_numpy(np.array(arr)).to(param.dtype))
    cp(m.get(K("tok-emb")).weight, trainable["tok_emb"])
    cp(m.get(K("norm-final")).weight, trainable["norm_final_w"])
    for tb, blk in zip(trainable["blocks"], m.get(K("blocks"))):
        g = lambda n: blk.get(K(n))
        for role, key in (("norm1_w", "norm1"), ("norm2_w", "norm2"), ("q_proj", "q-proj"),
                          ("k_proj_s", "k-proj-s"), ("v_proj_s", "v-proj-s"),
                          ("k_proj_l", "k-proj-l"), ("v_proj_l", "v-proj-l"),
                          ("o_proj", "o-proj"), ("gate_proj", "gate-proj"),
            else:
    """Copy trained MLX arrays back into the torch model params, by role."""
    import torch
    def cp(param, arr):
        param.data.copy_(torch.from_numpy(np.array(arr)).to(param.dtype))
    cp(m.get(K("tok-emb")).weight, trainable["tok_emb"])
    cp(m.get(K("norm-final")).weight, trainable["norm_final_w"])
    for tb, blk in zip(trainable["blocks"], m.get(K("blocks"))):
        g = lambda n: blk.get(K(n))
        for role, key in (("norm1_w", "norm1"), ("norm2_w", "norm2"), ("q_proj", "q-proj"),
                          ("k_proj_s", "k-proj-s"), ("v_proj_s", "v-proj-s"),
                          ("k_proj_l", "k-proj-l"), ("v_proj_l", "v-proj-l"),
                          ("o_proj", "o-proj"), ("gate_proj", "gate-proj"),
                          ("up_proj", "up-proj"), ("down_proj", "down-proj")):
            cp(g(key).weight, tb[role])
        gate = g("long-gate")
        if type(gate).__name__ == "SwitchGate":
            cp(gate.gate_proj, tb["sw_gate_proj"]); cp(gate.gate_proj_3, tb["sw_gate_proj_3"])
            if "sw_alpha_net" in tb: cp(gate.alpha_net, tb["sw_alpha_net"])
            if "sw_local_active_proj" in tb:
                cp(gate.local_active_proj, tb["sw_local_active_proj"])
                cp(gate.local_active_bias, tb["sw_local_active_bias"])
        mem = g("memory")
        if mem is not None:
            cp(mem.q_norm.weight, tb["mem_q_norm_w"]); cp(mem.K_a, tb["mem_K_a"])
            cp(mem.K_b, tb["mem_K_b"]); cp(mem.V.weight, tb["V_local"])
        nb = g("netbank")
        if nb is not None:
            if hasattr(nb, "banks"):                  # ModularNetBank: per-module write-back
                for name, d in tb["netbanks"].items():
                    bank = nb.banks[name]
                    cp(bank.q_norm.weight, d["net_q_norm_w"]); cp(bank.K_a, d["net_K_a"])
                    cp(bank.K_b, d["net_K_b"]); cp(bank.expander.weight, d["net_expander_w"])
                    cp(bank.V.weight, d["V_net"])
                if getattr(nb, "router", None) is not None and "router_keys" in tb:
                    cp(nb.router.module_keys, tb["router_keys"])   # learned router keys
            else:
                cp(nb.q_norm.weight, tb["net_q_norm_w"]); cp(nb.K_a, tb["net_K_a"])
                cp(nb.K_b, tb["net_K_b"]); cp(nb.expander.weight, tb["net_expander_w"])
                cp(nb.V.weight, tb["V_net"])


# ───────────────────────── optimizers ─────────────────────────
def _blk_get(block, path):
    """Navigate a per-block trainable subtree by a path tuple. Sparse-V keys are
    ('V_local',)/('V_net',) (legacy) or ('netbanks', <module>, 'V_net') (modular)."""
    node = block
    for p in path:
        node = node[p]
    return node


def _blk_set(block, path, val):
    node = block
    for p in path[:-1]:
        node = node[p]
        return _map_with_path(params, grads, upd)


def _map_with_path(params, grads, fn, prefix=""):
    """Walk two matching pytrees (dict/list of arrays), applying fn(path,p,g)."""
    if isinstance(params, dict):
        return {k: _map_with_path(params[k], grads.get(k), fn, f"{prefix}.{k}")
                for k in params}
    if isinstance(params, list):
        return [_map_with_path(params[i], grads[i], fn, f"{prefix}.{i}")
                for i in range(len(params))]
    return fn(prefix, params, grads)

def _map_with_path(params, grads, fn, prefix=""):
    """Walk two matching pytrees (dict/list of arrays), applying fn(path,p,g)."""
    if isinstance(params, dict):
        return {k: _map_with_path(params[k], grads.get(k), fn, f"{prefix}.{k}")
                for k in params}
    if isinstance(params, list):
        return [_map_with_path(params[i], grads[i], fn, f"{prefix}.{i}")
                for i in range(len(params))]
    return fn(prefix, params, grads)


            continue
        if hasattr(c, "named_parameters"):
            for pn, p in c.named_parameters():
                out[f"{tk}.{pn}"] = p
        elif hasattr(c, "weight"):
            out[f"{tk}.weight"] = c.weight
    _bkeys = ("norm1", "norm2", "q-proj", "k-proj-s", "v-proj-s", "k-proj-l", "v-proj-l",
              "o-proj", "gate-proj", "up-proj", "down-proj", "bank-query", "bank-feedback",
              "memory", "netbank", "long-gate", "carry")
    for i, blk in enumerate(m.get(K("blocks")) or []):
        for sk in _bkeys:
            comp = blk.get(K(sk))
            if comp is not None and hasattr(comp, "named_parameters"):
                for pn, p in comp.named_parameters():
                    out[f"b{i}.{sk}.{pn}"] = p
    return out


def _map_with_path(params, grads, fn, prefix=""):
    """Walk two matching pytrees (dict/list of arrays), applying fn(path,p,g)."""

def _blk_set(block, path, val):
    node = block
    for p in path[:-1]:
        node = node[p]
    node[path[-1]] = val


class _DenseAdam:
    """Adam over the dense subtree (everything except the V tables). Operates on
    a flat name->array view so SparseAdam can own V_local/V_net separately."""
    def __init__(self, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, wd=0.0):
        self.lr, (self.b1, self.b2), self.eps, self.wd = lr, betas, eps, wd
        # Router keys are dense but must keep learning when the trunk is FROZEN
        # (extension regime). router_lr (when set) overrides self.lr for any
        # *.router_keys leaf so MMLLM_LR_DENSE_MULT=0 doesn't freeze routing.
        self.router_lr = None
        self.m, self.v, self.t = {}, {}, 0

    def step(self, params, grads, skip_keys):
        self.t += 1
        bc1 = 1.0 - self.b1 ** self.t
        bc2 = 1.0 - self.b2 ** self.t
        def upd(path, p, g):
            if path in skip_keys or g is None:
                return p
            lr = (self.router_lr if (self.router_lr is not None and path.endswith("router_keys"))
                  else self.lr)
            self.m[path] = self.b1 * self.m.get(path, mx.zeros(p.shape)) + (1 - self.b1) * g
            self.v[path] = self.b2 * self.v.get(path, mx.zeros(p.shape)) + (1 - self.b2) * g * g
            step = lr * (self.m[path] / bc1) / (mx.sqrt(self.v[path] / bc2) + self.eps)
            if self.wd:
                step = step + lr * self.wd * p
            return p - step
        return _map_with_path(params, grads, upd)


def _named_params(m, K):
    """Stable {name: torch.Parameter} over the basilisp model map (which has NO
    .named_parameters — only its leaf components are torch Modules). Names are
    structural (b<i>.<component>.<param>) so they're invariant to module-count
    changes: a cold-added module's params get NEW names → resume leaves them at
    init while existing params load by name. Used by the module-growth-safe
    name-keyed dense_named.pt save/resume."""
    out = {}
    for tk in ("tok-emb", "norm-final", "mtp-head", "importance-head", "delim-head"):
        c = m.get(K(tk))
        if c is None:
            continue
        if hasattr(c, "named_parameters"):
            for pn, p in c.named_parameters():
                out[f"{tk}.{pn}"] = p
        elif hasattr(c, "weight"):
            out[f"{tk}.weight"] = c.weight
    _bkeys = ("norm1", "norm2", "q-proj", "k-proj-s", "v-proj-s", "k-proj-l", "v-proj-l",
              "o-proj", "gate-proj", "up-proj", "down-proj", "bank-query", "bank-feedback",
              "memory", "netbank", "long-gate", "carry")
    for i, blk in enumerate(m.get(K("blocks")) or []):
        for sk in _bkeys:
            comp = blk.get(K(sk))
            if comp is not None and hasattr(comp, "named_parameters"):
                for pn, p in comp.named_parameters():
                    if pn.endswith("V.weight"):
                        continue          # the bank VALUE tables (V_local / V_net) are
                                          # huge + persist via their mmap .bin files —
                                          # NEVER put them in dense_named.pt (else each
                                          # ckpt balloons by the full bank size).
                    out[f"b{i}.{sk}.{pn}"] = p
    return out


def _map_with_path(params, grads, fn, prefix=""):
    """Walk two matching pytrees (dict/list of arrays), applying fn(path,p,g)."""
    if isinstance(params, dict):
        return {k: _map_with_path(params[k], grads.get(k), fn, f"{prefix}.{k}")
                for k in params}
    if isinstance(params, list):
        return [_map_with_path(params[i], grads[i], fn, f"{prefix}.{i}")
                for i in range(len(params))]
    return fn(prefix, params, grads)


<<<MISSING line 447>>>
    _cands.sort()
    if (os.environ.get("MMLLM_MLX_RESUME", "true").lower() in ("1", "true")
            and _cands):
        resume_step, resume_dir = _cands[-1]
        resume = os.path.join(resume_dir, "dense.pt")
        saved = list(torch.load(resume, map_location="cpu", weights_only=False))
        ps = list(params_fn(m))
        nload = 0
        for p, s in zip(ps, saved):
            if tuple(p.shape) == tuple(s.shape):
                p.data.copy_(s.to(p.dtype)); nload += 1
        print(f"  [mlx] resumed {nload}/{len(ps)} dense params from {resume} (step {resume_step})")
        # chain semantics: V_local zero-inits each round (V_net carries via mmap).
        if os.environ.get("MMLLM_MLX_RESET_LOCAL", "true").lower() in ("1", "true"):
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    mem.V.weight.data.zero_()

    # steps this round = train from the resumed step toward `total` (extend_chain
    # passes total=STEPS+1 and seeds step-1, i.e. STEPS training steps).
    n_steps = min(max(1, total - resume_step), cap)
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
<<<MISSING line 485>>>
            ents.append((e[:c].strip(), float(e[c + 1:].strip())))
        corpora = [np.asarray(load_corpus(p, use_mmap=True)).reshape(-1) for p, _ in ents]
        ws = np.array([w for _, w in ents], dtype=float); ws = ws / ws.sum()
        corpus_path = ents[0][0]                          # for the "round" eval-mode fallback
        print(f"  [mlx] per-step mix: {len(corpora)} corpora (weighted), windows drawn per-sample")
    else:
        corpora = [np.asarray(load_corpus(train_path, use_mmap=True)).reshape(-1)]
        ws = np.array([1.0]); corpus_path = train_path

    def batch():
        # each of B samples: draw a corpus (weighted) + a random window → diverse batch
        cis = _rng.choice(len(corpora), size=B, p=ws)
        xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
def train_round(cfg, train_path, val_path, ckpt_dir, log_path,
                total, eval_every, ckpt_every):
    """Run one bird round in MLX. Builds via basilisp, trains in MLX, writes
    back to the torch model, saves dense.pt + bank bins (harvest-compatible)."""
    import basilisp.lang.runtime as rt
    from basilisp.lang import keyword as kw, symbol as sym
    import torch
    K = kw.keyword
    def bvar(n):
        return rt.Var.find(sym.symbol(n, ns="mmllm.core")).value

    build_model = bvar("build-model")
    from mmllm.corpus import load_as_tensor as load_corpus  # plain Python module

    B = int(os.environ.get("MMLLM_BATCH", str(bvar("pick-batch")())))  # match torch's pick-batch
    T = int(cfg.get(K("seq-len")) or 256)
    cap = int(os.environ.get("MMLLM_MLX_MAX_STEPS", str(total)))
    n_steps = min(total, cap)
    # LRs are NOT fixed here — they're computed per step by the recipe schedule
    # (lr-at-step × pick-lr-{bank,net,dense}-mult; see `schedule` below). The bank
    # SparseAdam / dense AdamW are seeded with the recipe base and overwritten each
    # step, so there are no standalone lr_dense/lr_bank/lr_net knobs to drift.
    lr_base = float(bvar("pick-lr")())
    # Batch-LR scaling: a B× larger batch averages the gradient over B× samples, so
    # the step must grow to convert the bigger batch into faster convergence — else
    # B>1 just burns tokens at the B=1 step size. √B (default) is the safe rule;
    # linear is aggressive. B=1 → ×1 (no-op). MMLLM_LR_BATCH_SCALE=sqrt|linear|none.
    _lr_bscale_mode = os.environ.get("MMLLM_LR_BATCH_SCALE", "sqrt")
    _lr_bscale = (B ** 0.5) if _lr_bscale_mode == "sqrt" else (float(B) if _lr_bscale_mode == "linear" else 1.0)
    if _lr_bscale != 1.0:
        print(f"  [mlx] LR batch-scale ({_lr_bscale_mode}): B={B} → lr ×{_lr_bscale:.2f}", flush=True)

    print(f"  [mlx] train_round: B={B} T={T} steps={n_steps} "
          f"lr_base={lr_base} (per-step schedule: pick-lr × {{bank,net,dense}}-mult)")

    m = build_model(cfg)
    # REWARM: one-shot realign the NetBank K_a/K_b from the (healthy, content-aligned)
    # Local Bank keys — the purpose-built lever (core.lpy rewarm-netbank-keys-only!)
    # for breaking the collapsed-keys / gate-suppresses-Net feedback loop. train-long
    # calls this on the torch path; the MLX path bypasses train-long, so do it here.
    if os.environ.get("MMLLM_REWARM_NETBANK_KEYS", "").lower() == "true":
        bvar("rewarm-netbank-keys-only!")(m)
        print("  [mlx] REWARM_NETBANK_KEYS: realigned net K_a/K_b from Local (V untouched)")
    params_fn = bvar("parameters")
    vocab = m.get(K("tok-emb")).weight.shape[0]

    # Chain resume: load the LATEST ckpt_dir/step-<N>/dense.pt — the layout
    # extend_chain.sh uses (it seeds the chain head at step-1/dense.pt and reads
    # the bird's output from the highest step-N dir). Loading from ckpt_dir
    # directly would MISS the head and train from scratch, regressing the chain.
    # V_net carries across rounds via its stable mmap path (bank_on_gpu=false);
    # V_local resets to build-time init — standard chain semantics.
    import glob as _glob, re as _re
    resume_step = 0
    _cands = []
    for _p in _glob.glob(os.path.join(ckpt_dir, "step-*")):
        _mo = _re.match(r".*step-(\d+)$", _p)
        if _mo and os.path.exists(os.path.join(_p, "dense.pt")):
            _cands.append((int(_mo.group(1)), _p))
    _cands.sort()
    if (os.environ.get("MMLLM_MLX_RESUME", "true").lower() in ("1", "true")
            and _cands):
        resume_step, resume_dir = _cands[-1]
        resume = os.path.join(resume_dir, "dense.pt")
        ps = list(params_fn(m))
        nload = 0
        # Module-growth-safe resume: a name-keyed sidecar (dense_named.pt) matches
        # params BY NAME, so a cold-add (a block's netbank gains a module → the
        # positional list shifts + same-shape params misalign across blocks) loads
        # cleanly and the new module's params stay at init. Falls back to the
        # legacy positional zip for pre-sidecar ckpts. (dense.pt stays for harvest.)
        _named_path = os.path.join(resume_dir, "dense_named.pt")
        if os.path.exists(_named_path):
            _named = torch.load(_named_path, map_location="cpu", weights_only=False)
            _new = 0
            for n, p in _named_params(m, K).items():
                s = _named.get(n)
                if s is not None and tuple(p.shape) == tuple(s.shape):
                    p.data.copy_(s.to(p.dtype)); nload += 1
                elif s is None:
                    _new += 1                       # new param (e.g. a cold-added module) → init
            print(f"  [mlx] resumed {nload} dense params BY NAME from {_named_path} "
                  f"(module-growth safe; {_new} new params at init)")
        else:
            saved = list(torch.load(resume, map_location="cpu", weights_only=False))
            for p, s in zip(ps, saved):
                if tuple(p.shape) == tuple(s.shape):
                    p.data.copy_(s.to(p.dtype)); nload += 1
            print(f"  [mlx] resumed {nload}/{len(ps)} dense params from {resume} (step {resume_step})")
        # WAKE. Lighter than the old zero-wipe: the LB carries across rounds via its
        # r+ mmap (write-through); at wake we blend in noise so it partially forgets
        # + stays plastic (no hard reset, no blank-LB poison). MMLLM_LOCAL_NOISE_FRAC
        # (e.g. 0.5 = half/half: V ← (1-p)·V + p·𝒩(0,std)). Falls back to the legacy
        # zero-wipe when NOISE_FRAC=0 (+ RESET_LOCAL) for backward-compat.
        _noise_frac = float(os.environ.get("MMLLM_LOCAL_NOISE_FRAC", "0"))
        if _noise_frac > 0:
            import torch as _t
            _nb = 0
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    V = mem.V.weight.data
                    std = float(V.std())
                    if std == 0.0:
                        std = 1.0                      # round-1 fresh LB → seed with unit noise
                    V.mul_(1.0 - _noise_frac).add_(_t.randn_like(V) * (std * _noise_frac))
                    _nb += 1
            print(f"  [mlx] LB wake: blended {int(_noise_frac*100)}% noise into {_nb} Local Banks "
                  f"(no wipe; LB carries via mmap)")
        elif os.environ.get("MMLLM_MLX_RESET_LOCAL", "true").lower() in ("1", "true"):
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    mem.V.weight.data.zero_()

    # steps this round = train from the resumed step toward `total` (extend_chain
    # passes total=STEPS+1 and seeds step-1, i.e. STEPS training steps).
    n_steps = min(max(1, total - resume_step), cap)

    # PER-STEP MIX: each batch draws its windows from corpora sampled per-window
    # (weighted), so EVERY step trains on the diverse mix and the NetBank
    _rng = np.random.default_rng()
    # RETENTION test phase switch: train MMLLM_MIX_P1 (the probe corpus) for the
    # first MMLLM_PHASE1_STEPS cumulative steps, then MMLLM_MIX_P2 (other corpora)
    # — locals reset each round, V_net carries. With MMLLM_PROBE fixed on the probe
    # corpus, Δ_net over the P2 rounds measures how much of P1 the net RETAINS.
    _p1_rounds = int(os.environ.get("MMLLM_PHASE1_ROUNDS", "0"))
    if _p1_rounds:
        # Phase by a per-arm FILE COUNTER (neither resume_step nor log_path carry a
        # usable round index — resume_step is pinned at 1, log_path is a generic
        # name). train_round runs once per round, so increment-per-call IS the round
        # count: train MMLLM_MIX_P1 (the probe) for the first _p1_rounds rounds, then
        # MMLLM_MIX_P2 (others). The driver clears the marker before each run.
        _marker = os.environ.get("MMLLM_PHASE_MARKER", "/tmp/ret-phase-start")
        _n = int(open(_marker).read().strip()) if os.path.exists(_marker) else 0
        with open(_marker, "w") as _f:
            _f.write(str(_n + 1))
        _mix = os.environ.get("MMLLM_MIX_P1" if _n < _p1_rounds else "MMLLM_MIX_P2", "").strip()
        print(f"  [mlx] retention phase: {'P1(probe)' if _n < _p1_rounds else 'P2(other)'} "
              f"round_count={_n} (P1 rounds={_p1_rounds})")
    else:
        _mix = os.environ.get("MMLLM_MIX", "").strip()
    if _mix:
        ents = []
        for e in _mix.split(","):
            e = e.strip()
            if not e:
                continue
            c = e.rfind(":")
            ents.append((e[:c].strip(), float(e[c + 1:].strip())))
        corpora = [np.asarray(load_corpus(p, use_mmap=True)).reshape(-1) for p, _ in ents]
        ws = np.array([w for _, w in ents], dtype=float); ws = ws / ws.sum()
        corpus_path = ents[0][0]                          # for the "round" eval-mode fallback
        _mix_paths = [p for p, _ in ents]
        print(f"  [mlx] per-step mix: {len(corpora)} corpora (weighted), windows drawn per-sample")
    else:
        corpora = [np.asarray(load_corpus(train_path, use_mmap=True)).reshape(-1)]
        ws = np.array([1.0]); corpus_path = train_path; _mix_paths = [train_path]

    # Skill-module routing: per-corpus module name (None unless MMLLM_NET_MODULES).
    # When modular, sample ONE corpus per batch (not per-window) so the batch maps
                else:
                    _qd = sb["n_long_heads"] * sb["head_dim"]
                    tb["bank_query_w"] = mx.zeros((_qd, _dm))
                _n += 1
        print(f"  [mlx] CTXADD_INJECT: W_ctx on {_n} blocks ({_loaded} loaded from persisted, rest zero)")

    # Router keys persist OUTSIDE the (fixed positional) dense.pt — like W_ctx —
    # in router-keys.<bi>.npy. The fresh torch model re-zero-inits them, so resume
    # the trained keys here (over the zeros) for cross-round learning + offline eval.
    _rdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
    _rload = 0
    for _bi, tb in enumerate(trainable["blocks"]):
        if "router_keys" in tb:
            _rp = os.path.join(_rdir, f"router-keys.{_bi}.npy")
            if os.path.exists(_rp):
                tb["router_keys"] = mx.array(np.load(_rp)); _rload += 1
    if _rload:
        print(f"  [mlx] resumed router keys for {_rload} blocks from {_rdir}")

    if os.environ.get("MMLLM_PKM_DIAG") and not os.environ.get("MMLLM_POST_DIAG"):
        _run_pkm_diag(_reassemble(trainable, static, meta), load_corpus, T)
<<<MISSING line 681>>>
<<<MISSING line 682>>>
<<<MISSING line 683>>>
<<<MISSING line 684>>>
<<<MISSING line 685>>>
<<<MISSING line 686>>>
<<<MISSING line 687>>>
<<<MISSING line 688>>>
<<<MISSING line 689>>>
<<<MISSING line 690>>>
<<<MISSING line 691>>>
<<<MISSING line 692>>>
    # at composition time. Cool these via MMLLM_NET_COOL_MODULES so they stay
    # frozen. Empty by default (each batch routes to its own module only).
    _core_active = [m for m in os.environ.get("MMLLM_NET_CORE_MODULES", "").split(",")
    # Co-train phase: with the router DRIVING, let it pick the active set during
    # training too (active=None → Level-1) so the train path == the inference path
    # (modules adapt to the routed, convex-weighted regime). Phase 1 (drive off)
    # aux-warms the router under corpus-tag isolation first.
    _drive_train = os.environ.get("MMLLM_NET_ROUTER_DRIVE", "false").lower() in ("1", "true", "yes")
    if _drive_train and corpus_modules is not None:
        print("  [mlx] router DRIVE on → router picks the active set during training (co-train)")

    def batch():
    def batch():
        if corpus_modules is not None:
            # MODULAR: one corpus for the whole batch → route all windows to its module.
            ci = int(_rng.choice(len(corpora), p=ws))
            _routed = corpus_modules[ci]
            # router aux-loss target: the routed module's index in the full list
            static["_router_target"] = (_net_modules.index(_routed)
                                        if (_routed in _net_modules) else None)
            if _drive_train:                    # co-train: router picks (Level-1) + weights (Level-2)
                static["_net_active"] = None
            elif _core_active is not None:      # active = core ∪ {routed specialist}
                _r = [_routed] if isinstance(_routed, str) else (list(_routed) if _routed else [])
                static["_net_active"] = list(dict.fromkeys(_core_active + _r))
            else:
                static["_net_active"] = _routed
            c = corpora[ci]
            xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
            for j in range(B):
                o = int(_rng.integers(0, c.size - T - 1))
                xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
            return mx.array(xb), mx.array(yb)
        # per-window mix (monolithic net): each of B samples its own corpus + window
        cis = _rng.choice(len(corpora), size=B, p=ws)
        xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
        for j in range(B):
            c = corpora[int(cis[j])]; o = int(_rng.integers(0, c.size - T - 1))
            xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
        return mx.array(xb), mx.array(yb)

    n_trunks = 1
    for blk in m.get(K("blocks")):
        mem = blk.get(K("memory"))
        if mem is not None:
            n_trunks = max(n_trunks, getattr(mem, "n_trunks", 1))
    trunk_ids = mx.array((np.arange(B) % n_trunks).astype(np.int64))
    # MMLLM_NET_WIDEN=C: widen the torch NetBank code dim c_net -> C (8->16=q_dim),
    # AFTER the head is loaded, so the FULL pipeline (extract/train/eval/write-back)
    # runs at C — the expander rank (c_net) is the netbank's functional bottleneck.
    # V new cols=0 (empty memory); expander new cols=small random (zero-on-both
    # deadlocks the gradient). Output unchanged at start; distill can then populate
    # the new capacity. Smoke-only (the chain V_net.bin stays c_net=8).
    _wide = int(os.environ.get("MMLLM_NET_WIDEN", "0"))
    if _wide:
        import torch
        import torch.nn as nn
        _did = 0
        for blk in m.get(K("blocks")):
            nb = blk.get(K("netbank"))
            if nb is None or not hasattr(getattr(nb, "V", None), "weight"):
                continue
            if getattr(nb, "c_net", _wide) >= _wide:
                continue
            with torch.no_grad():
                Vw = nb.V.weight; dev, dt = Vw.device, Vw.dtype; pad = _wide - Vw.shape[1]
                newV = torch.cat([Vw, torch.zeros(Vw.shape[0], pad, device=dev, dtype=dt)], dim=1)
                nb.V = nn.Embedding(newV.shape[0], _wide, _weight=newV).to(dev)
                Ew = nb.expander.weight
                newE = torch.cat([Ew, 0.02 * torch.randn(Ew.shape[0], pad, device=dev, dtype=dt)], dim=1)
                exp = nn.Linear(_wide, Ew.shape[0], bias=False).to(dev); exp.weight = nn.Parameter(newE)
                nb.expander = exp; nb.c_net = _wide
                _did += 1
        print(f"  [mlx] NET_WIDEN: widened {_did} netbanks to c_net={_wide} (torch model)")

    trainable, static, meta = _extract(m, K, trunk_ids)

    # CTXADD inject: add a zero W_ctx (ctx-add bank query) at the MLX-trainable level
    # AFTER the (positional) resume, so resume stays clean. W_ctx trains as a dense
    # param toward content-discriminative queries → de-collapses retrieval. Single-run
    # test (not persisted — for genesis/chain it must live in the torch model).
    if os.environ.get("MMLLM_CTXADD_INJECT") == "true":
    sparse = {}   # (bi, path_tuple) -> SparseAdam; path navigates trainable["blocks"][bi]
    for bi, tb in enumerate(trainable["blocks"]):
        if "V_local" in tb:
            sparse[(bi, ("V_local",))] = SparseAdam(tb["V_local"].shape[0],
                                                    tb["V_local"].shape[1], lr=lr_base)
        if "netbanks" in tb:                          # ModularNetBank: one SparseAdam per module
            for name, d in tb["netbanks"].items():
                sparse[(bi, ("netbanks", name, "V_net"))] = SparseAdam(
                    d["V_net"].shape[0], d["V_net"].shape[1], lr=lr_base)
        elif "V_net" in tb:
            sparse[(bi, ("V_net",))] = SparseAdam(tb["V_net"].shape[0],
                    tb["bank_query_w"] = mx.zeros((_qd, _dm))
                _n += 1
        print(f"  [mlx] CTXADD_INJECT: W_ctx on {_n} blocks ({_loaded} loaded from persisted, rest zero)")

    # Router keys persist OUTSIDE the (fixed positional) dense.pt — like W_ctx —
    # in router-keys.<bi>.npy. The fresh torch model re-zero-inits them, so resume
    # the trained keys here (over the zeros) for cross-round learning + offline eval.
    _rdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
    _rload = 0
    for _bi, tb in enumerate(trainable["blocks"]):
        if "router_keys" in tb:
            _rp = os.path.join(_rdir, f"router-keys.{_bi}.npy")
            if os.path.exists(_rp):
                _saved = mx.array(np.load(_rp)); _cur = tb["router_keys"]
                if tuple(_saved.shape) == tuple(_cur.shape):
                    tb["router_keys"] = _saved
                elif _saved.shape[0] < _cur.shape[0] and _saved.shape[1] == _cur.shape[1]:
                    # cold-add: module count grew → keep trained rows for the existing
                    # modules, new (appended) modules' rows stay at init.
                    tb["router_keys"] = mx.concatenate([_saved, _cur[_saved.shape[0]:]], axis=0)
                _rload += 1
    if _rload:
        print(f"  [mlx] resumed router keys for {_rload} blocks from {_rdir} "
              f"(grow-safe: existing modules' rows kept, new modules at init)")

            t_logp = mx.stop_gradient(t_lg - mx.logsumexp(t_lg, axis=-1, keepdims=True))
            t_p = mx.exp(t_logp)
            Pnet = _reassemble(tr, static, meta, student=_kd_freeze)   # net-only student (locals off)
            s_lg = _model.forward(Pnet, xb).reshape(-1, vocab) / _kd_temp
            s_logp = s_lg - mx.logsumexp(s_lg, axis=-1, keepdims=True)
            kd = (t_p * (t_logp - s_logp)).sum(-1).mean() * (_kd_temp * _kd_temp)
            loss = loss + _kd_coef * kd
        else:
    # consolidation check: how far did each V table move from init?
    def schedule(local_step):
        g = resume_step + local_step                       # global step in schedule
        cur = float(_lr_at_step(g, total, _pick_lr(), _warmup, _pick_lr_min()))
        return (cur * float(_bank_mult(g, total)),         # lr_bank (V_local)
        elif "V_net" in tb:
            sparse[(bi, ("V_net",))] = SparseAdam(tb["V_net"].shape[0],
                                                  tb["V_net"].shape[1], lr=lr_base)
    dense_opt = _DenseAdam(lr=lr_base)  # overwritten per-step by the schedule
                                                  tb["V_net"].shape[1], lr=lr_base)
    losses = []
    for step in range(1, n_steps + 1):
        lb, ln, ld, dc, cur = schedule(step)
        static["_distill_coef"] = dc
        dense_opt.lr = ld
        dense_opt.router_lr = cur * _router_lr_mult     # router LR ≠ trunk (dense) LR
        for (bi, path), opt in sparse.items():
            opt.lr = lb if path[-1] == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        # sparse banks first (read grads before dense update rewrites the tree)
        for (bi, path), opt in sparse.items():
            gV = np.array(_blk_get(grads["blocks"][bi], path))
                cur * float(_dense_mult(g, total)),        # lr_dense
                float(_distill(g, total)),                 # distill coef
                cur)                                       # base lr (for router)

    # ── Local-Bank LR controls (ported from torch optim.py) ──
    # LOCAL_MULT: global V_local LR reduction (default 0.05) — the LB is a routing
    #   PRIMITIVE that should learn SLOW (~20× below bank_lr); the V values it
    # corpus→module label so its keys become discriminative during genesis (the
    # router then drives Level-1/2 at inference). 0 disables.
    _router_aux_coef = float(os.environ.get("MMLLM_NET_ROUTER_AUX_COEF", "0.1"))

    def loss_fn(tr):
        xb, yb = static["_xb"], static["_yb"]
        P = _reassemble(tr, static, meta)
        logits, distill_total, z_total, net_z_total, router_logits, n_distill = _model.forward(
            P, xb, collect_aux=True)
        lg = logits.reshape(-1, vocab)
        logp = lg - mx.logsumexp(lg, axis=-1, keepdims=True)
        ce = -mx.take_along_axis(logp, yb.reshape(-1)[:, None], axis=-1).mean()
        loss = ce
        if z_coef:
            loss = loss + z_coef * z_total
        if _net_z_coef:
            loss = loss + _net_z_coef * net_z_total
        if _router_aux_coef and router_logits is not None and static.get("_router_target") is not None:
            rl = router_logits.reshape(-1, router_logits.shape[-1])   # (B*T, N) summed over blocks
            rlogp = rl - mx.logsumexp(rl, axis=-1, keepdims=True)
            loss = loss + _router_aux_coef * (-rlogp[:, static["_router_target"]].mean())
        if _kd_obj:
            # REAL LB->NB output distillation (Hinton soft-target KD):
            #   TEACHER = Local-only forward (sdpa+local, net OFF), the good/stable
            #     teacher (local just trained this round's data). Detached (stop_grad).
            #   STUDENT = net-only forward (sdpa+net, local OFF) — the future state.
            #   loss = KL(teacher_softT || student_softT) * T^2  (dark knowledge).
            # The net LEARNS to reproduce the local's OUTPUT DISTRIBUTION. Success is
            # this KL FALLING (net matches local) — not Δ_net.
            Ploc = _reassemble(tr, static, meta, drop_net=True)        # local-only teacher
            t_lg = _model.forward(Ploc, xb).reshape(-1, vocab) / _kd_temp
            t_logp = mx.stop_gradient(t_lg - mx.logsumexp(t_lg, axis=-1, keepdims=True))
            t_p = mx.exp(t_logp)
            Pnet = _reassemble(tr, static, meta, student=_kd_freeze)   # net-only student (locals off)
            s_lg = _model.forward(Pnet, xb).reshape(-1, vocab) / _kd_temp
            s_logp = s_lg - mx.logsumexp(s_lg, axis=-1, keepdims=True)
            kd = (t_p * (t_logp - s_logp)).sum(-1).mean() * (_kd_temp * _kd_temp)
            loss = loss + _kd_coef * kd
        else:
            dc = static["_distill_coef"]
            if dc and n_distill:
                loss = loss + dc * (distill_total / max(1, n_distill))
        return loss

    # Per-step LR + distill schedule — call the SAME basilisp functions train-long
    # uses (core.lpy:4783-4789) so the recipe is byte-identical: cur_lr =
    # lr-at-step(cosine from pick-lr to LR_MIN); lr_bank/lr_net/lr_dense = cur_lr ×
    # the per-tier mult ramps (lr_net ramps to pick-lr × LR_NET_MULT_END — the
    # wake/sleep consolidation the prod recipe needs; my old hardcoded lr_net=1e-4
    # was the bug that left V_net frozen). The round trains the [resume_step+1,
    # total] slice of the global schedule.
    _lr_at_step = bvar("lr-at-step"); _pick_lr = bvar("pick-lr")
    _pick_lr_min = bvar("pick-lr-min"); _warmup = bvar("pick-lr-warmup")()
    _bank_mult = bvar("pick-lr-bank-mult"); _net_mult = bvar("pick-lr-net-mult")
    _dense_mult = bvar("pick-lr-dense-mult"); _distill = bvar("pick-distill-coef")
    # Router-key LR multiplier — applied independent of the trunk (dense) mult so
    # the router keeps learning when the trunk is frozen (extension). Default 1.0.
    _router_lr_mult = float(os.environ.get("MMLLM_NET_ROUTER_LR_MULT", "1.0"))

        cur = float(_lr_at_step(g, total, _pick_lr(), _warmup, _pick_lr_min()))
        return (cur * float(_bank_mult(g, total)),         # lr_bank (V_local)
                cur * float(_net_mult(g, total)),          # lr_net  (V_net)
                cur * float(_dense_mult(g, total)),        # lr_dense
                float(_distill(g, total)),                 # distill coef
                cur)                                       # base lr (for router)

    # ── Local-Bank LR controls (ported from torch optim.py) ──
    # LOCAL_MULT: global V_local LR reduction (default 0.05) — the LB is a routing
    #   PRIMITIVE that should learn SLOW (~20× below bank_lr); the V values it
    #   retrieves change fast, the routing decisions shouldn't.
    # LAYER_MULTS: per-LB-layer multipliers (stacked on LOCAL_MULT), tiled by the
    #   LB's ordinal position → the staggered U-shape so the 8 LBs SPECIALIZE
    #   instead of being redundant. (MLX previously ran all V_local at full bank_lr,
    #   uniform — this restores the torch behaviour.)
    _local_mult = float(os.environ.get("MMLLM_LR_LOCAL_MULT", "0.05"))
    _layer_mults = [float(x) for x in os.environ.get("MMLLM_LR_LAYER_MULTS", "").split(",") if x.strip()] or None
    _lb_bis = sorted(bi for (bi, path) in sparse if path[-1] == "V_local")
    _lb_ord = {bi: i for i, bi in enumerate(_lb_bis)}
    # WAKE→SLEEP LB-LR decay (within each round, no reset): the LB rides a high LR
    # at wake (learn the round's new data fast) decaying to a low LR at sleep (settle
    # while distilling into the NB). Whole-round linear decay LR_WAKE→LR_SLEEP.
    # Defaults 1.0/1.0 = flat (off, backward-compatible).
    _lr_wake = float(os.environ.get("MMLLM_LOCAL_LR_WAKE", "1.0"))
    _lr_sleep = float(os.environ.get("MMLLM_LOCAL_LR_SLEEP", "1.0"))
    def _wake_sleep(local_step):
        if n_steps <= 1:
            return _lr_wake
        return _lr_wake + (_lr_sleep - _lr_wake) * ((local_step - 1) / (n_steps - 1))
    def _vlocal_lr(bi, lb, local_step):
        m = _local_mult * _wake_sleep(local_step)
        if _layer_mults:
            m *= _layer_mults[_lb_ord[bi] % len(_layer_mults)]
        return lb * m
    # Post-reset POISON GUARD: V_local is zeroed each round (reset) → contributes 0.
    # Freeze its update for the first LOCAL_WARMUP steps so the blanked LB stays at
    # zero (no poison) while the trunk+NBs stabilize; then it unfreezes and learns
    # (with its per-layer LR). Default 0 = off (backward-compatible).
    # zero (no poison) while the trunk+NBs stabilize; then it unfreezes and learns
    # (with its per-layer LR). Default 0 = off (backward-compatible).
    _local_warmup = int(os.environ.get("MMLLM_LOCAL_WARMUP_STEPS", "0"))

    losses = []
    for step in range(1, n_steps + 1):
        lb, ln, ld, dc, cur = schedule(step)
        static["_distill_coef"] = dc
        dense_opt.lr = ld
        dense_opt.router_lr = cur * _router_lr_mult     # router LR ≠ trunk (dense) LR
        for (bi, path), opt in sparse.items():
            opt.lr = _vlocal_lr(bi, lb, step) if path[-1] == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        # sparse banks first (read grads before dense update rewrites the tree)
        for (bi, path), opt in sparse.items():
            if path[-1] == "V_local" and step <= _local_warmup:
                continue                       # poison guard: keep blanked LB frozen (zero) until warm
            gV = np.array(_blk_get(grads["blocks"][bi], path))
            rows = np.nonzero(np.abs(gV).sum(1) > 0)[0]
            if len(rows):
                _blk_set(trainable["blocks"][bi], path,
    losses = []
    for step in range(1, n_steps + 1):
        lb, ln, ld, dc, cur = schedule(step)
        static["_distill_coef"] = dc
        dense_opt.lr = ld
        dense_opt.router_lr = cur * _router_lr_mult     # router LR ≠ trunk (dense) LR
        for (bi, path), opt in sparse.items():
            opt.lr = _vlocal_lr(bi, lb, step) if path[-1] == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        if step == 1: _memprof("post-fwd+bwd (graph peak)")
        if step == 1 and os.environ.get("MMLLM_MEM_PROFILE"):
            _szs = []
            def _walk(o, path=""):
    _router_lr_mult = float(os.environ.get("MMLLM_NET_ROUTER_LR_MULT", "1.0"))

    def schedule(local_step):
        g = resume_step + local_step                       # global step in schedule
        cur = float(_lr_at_step(g, total, _pick_lr(), _warmup, _pick_lr_min()))
        return (cur * float(_bank_mult(g, total)),         # lr_bank (V_local)
                cur * float(_net_mult(g, total)),          # lr_net  (V_net)
                cur * float(_dense_mult(g, total)),        # lr_dense
                float(_distill(g, total)),                 # distill coef
                cur)                                       # base lr (for router)
                        f" | net_z={float(_nzt):.3f} (collapse proxy: falling=spreading)")
                if _kd_obj:
                    _sbpc = float(-mx.take_along_axis(_sl * _kd_temp - mx.logsumexp(_sl * _kd_temp, axis=-1, keepdims=True),
                                  yb.reshape(-1)[:, None], axis=-1).mean()) / math.log(2)
                    _dbg += (f" | KD(local→net)={_kdv:.4f} (FALLING=net learning local) "
                             f"teacher_bpc={_tbpc:.3f} student_bpc={_sbpc:.3f}")
            except Exception as _e:
                _dbg = f"  [DISTILL] diag-failed: {_e}"
            print(f"  [mlx] step {step}/{n_steps}  loss={losses[-1]:.4f}  "
                  f"lr_b={lb:.2e} lr_n={ln:.2e} lr_d={ld:.2e} distill_c={dc:.2f}{_dbg}")

    # POST-TRAINING diag: run the key-collapse diagnostic on the TRAINED trainable
    # (with the now-trained W_ctx if ctx-add was injected). Tests whether learned
    # content-discriminative queries de-collapsed retrieval, in-process (no resume).
    if os.environ.get("MMLLM_POST_DIAG"):
        _run_pkm_diag(_reassemble(trainable, static, meta), load_corpus, T)


    # write trained weights back into the torch model + save (harvest-compatible)
    _write_back(trainable, m, K)
    # Save dense.pt into a step-<total> dir (the layout extend_chain.sh reads:
    # it copies the highest step-N/dense.pt out for delta-encode + push). Bank
    # bins stay at ckpt_dir level (matches save-checkpoint!).
    target_step = total
    step_dir = os.path.join(ckpt_dir, f"step-{target_step}")
    dense_path = os.path.join(step_dir, "dense.pt")
    torch.save([p.detach().clone() for p in params_fn(m)], dense_path)
    # name-keyed sidecar for module-growth-safe resume (cold-add); dense.pt stays
    # positional for the backend-agnostic harvest.
    torch.save({n: p.detach().clone() for n, p in _named_params(m, K).items()},
               os.path.join(step_dir, "dense_named.pt"))
    with open(os.path.join(step_dir, "step.txt"), "w") as _sf:
        _sf.write(str(target_step))
    # Self-cleaning: prune old step-N ckpt dirs, keep only the latest MMLLM_CKPT_KEEP
    # (default 2 — resume needs the max; 2 leaves one safety margin). Without this a
    # long run accumulates one ~dense.pt-sized dir PER ROUND and fills the disk.
    try:
        import glob as _g, re as _re, shutil as _sh
        _keep = max(1, int(os.environ.get("MMLLM_CKPT_KEEP", "2")))
        _dirs = sorted(((int(_re.search(r"step-(\d+)$", p).group(1)), p)
                        for p in _g.glob(os.path.join(ckpt_dir, "step-*"))
                        if _re.search(r"step-(\d+)$", p)), reverse=True)
        for _, _old in _dirs[_keep:]:
            _sh.rmtree(_old, ignore_errors=True)
        if len(_dirs) > _keep:
            print(f"  [mlx] ckpt prune: kept latest {_keep} step dirs, removed {len(_dirs)-_keep}")
    except Exception as _e:
<<<MISSING line 1045>>>
<<<MISSING line 1046>>>
<<<MISSING line 1047>>>
<<<MISSING line 1048>>>
<<<MISSING line 1049>>>
<<<MISSING line 1050>>>
<<<MISSING line 1051>>>
<<<MISSING line 1052>>>
<<<MISSING line 1053>>>
<<<MISSING line 1054>>>
<<<MISSING line 1055>>>
<<<MISSING line 1056>>>
<<<MISSING line 1057>>>
<<<MISSING line 1058>>>
<<<MISSING line 1059>>>
<<<MISSING line 1060>>>
<<<MISSING line 1061>>>
<<<MISSING line 1062>>>
<<<MISSING line 1063>>>
<<<MISSING line 1064>>>
<<<MISSING line 1065>>>
<<<MISSING line 1066>>>
<<<MISSING line 1067>>>
<<<MISSING line 1068>>>
<<<MISSING line 1069>>>
<<<MISSING line 1070>>>
<<<MISSING line 1071>>>
<<<MISSING line 1072>>>
<<<MISSING line 1073>>>
<<<MISSING line 1074>>>
<<<MISSING line 1075>>>
<<<MISSING line 1076>>>
<<<MISSING line 1077>>>
<<<MISSING line 1078>>>
<<<MISSING line 1079>>>
<<<MISSING line 1080>>>
<<<MISSING line 1081>>>
    # eval ctrl_bpc (torch forward of the MLX-trained, written-back model — also
    # cross-validates the write-back). Best-effort.
    #
    # Eval corpus must REFLECT the training distribution, not a fixed single corpus
    # — otherwise ctrl_bpc measures drift away from that corpus rather than quality
    # (the chain-wide default evals val_path=fim-json even while training the diverse
    # MMLLM_MIX). MMLLM_MLX_EVAL_MODE:
    #   mix   (default when MMLLM_MIX set) — held-out tail of EACH mix corpus,
    #          concatenated: mix-representative AND identical across birds (so the
    #          harvest's cross-bird ctrl_bpc comparison stays valid).
    #   round — this round's trained corpus (reflects the round; not cross-comparable)
    #   val   — legacy fixed val_path (fim-json)
    # Eval cap + B mirror the torch path (pick-ablation-eval-cap, B=16).
    try:
        eval_bpc = bvar("eval-bpc")
        ev = int(bvar("pick-ablation-eval-cap")(25000))          # = torch's cap (recipe-driven)
        eval_b = int(os.environ.get("MMLLM_EVAL_BATCH", "16"))   # torch evals at 16
        eval_mode = os.environ.get("MMLLM_MLX_EVAL_MODE", "mix" if _mix else "val")
        _probe = os.environ.get("MMLLM_PROBE", "").strip()
        if _probe:
            # RETENTION test: eval on a FIXED probe corpus, DECOUPLED from the train
            # mix. Train the net on the probe early, then train on OTHER corpora
            # (locals reset, net carries); Δ_net on the probe each round = how much
            # of the probe the net still retains (true cross-round consolidation).
            vdata = load_corpus(_probe)
            print(f"  [mlx] eval corpus: PROBE {os.path.basename(_probe)} (retention test)")
        elif eval_mode == "mix" and _mix:
            # Same builder the torch train-long calls (core.lpy:pick-mix-val):
            # held-out tail of EACH MMLLM_MIX corpus, in MMLLM_MIX order, sized by
            # MMLLM_MIX_VAL_PER_CORPUS. Calling it (rather than rebuilding inline)
            # is what guarantees MLX and fork birds eval byte-identical tokens, so
            # the harvest's cross-bird ctrl_bpc comparison stays valid.
            vdata = bvar("pick-mix-val")()
            per = int(os.environ.get("MMLLM_MIX_VAL_PER_CORPUS", "4096"))
            print(f"  [mlx] eval corpus: mix held-out ({len(ents)} corpora × {per} tok)")
        elif eval_mode == "round":
            vdata = load_corpus(corpus_path)
            print(f"  [mlx] eval corpus: {os.path.basename(corpus_path)} (this round's)")
        else:
            vdata = load_corpus(val_path)
            print(f"  [mlx] eval corpus: {os.path.basename(val_path)} (fixed val)")
        # Composition control: MMLLM_NET_EVAL_ACTIVE restricts the eval to a
        # chosen module set (comma list); "" / "all" → all modules (default
        # composition). Lets us measure a single module's standalone skill, or
        # whether composing an independently-trained module with an extended set
        # interferes (train-active-set ≠ eval-active-set). No-op on non-modular.
        _eval_active = os.environ.get("MMLLM_NET_EVAL_ACTIVE", "").strip()
        if _eval_active:
            _names = (None if _eval_active.lower() == "all"
                      else [s.strip() for s in _eval_active.split(",") if s.strip()])
            _set = 0
            for _blk in (m.get(kw.keyword("blocks")) or []):
                _nb = _blk.get(kw.keyword("netbank"))
                if _nb is not None and hasattr(_nb, "set_active"):
                    _nb.set_active(_names); _set += 1
            print(f"  [mlx] eval net-active = {_names if _names else 'ALL'} "
                  f"({_set} modular blocks)")
        r = eval_bpc(m, vdata, T, eval_b, ev)
        bpc = float(r.get(kw.keyword("bpc")))
        result["ctrl_bpc"] = bpc
        print(f"  [mlx] eval ctrl_bpc={bpc:.4f}")
        # ablations: Δ_local, Δ_net, Δ_both (zero the bank V -> re-eval -> restore).