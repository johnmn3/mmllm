# Fusing H-Net Dynamic Chunking with an eve-style log-32 Trie NetBank

**Status:** design / implementation plan. Default-OFF, compose-on-top.
**Author:** genesis architecture notes, 2026-06-28.
**Scope:** byte-level LM (`mmllm-src`), dual backend torch (`mmllm/`) + MLX (`mmllm/mlx/`); live run is MLX.

> Guiding principle (from `compose-dont-scrap`): every new piece lands behind an
> env gate that defaults to the current behaviour **byte-identically**. The
> working chain (round-9 distill baseline, sym24 canonical config) must keep
> running with the new code present and all gates unset.

---

## 0. The core realization

The H-Net dynamic-chunking router and the NetBank residual-VQ router are **the
same operation**: a continuous vector is mapped to a discrete address by
cosine/inner-product routing.

- H-Net chunker (arXiv:2507.07955): `q_t = W_q x̂_t`, `k_t = W_k x̂_t`,
  boundary prob `p_t = ½(1 − cos(q_t, k_{t−1}))`, cut where `p_t ≥ 0.5`.
- NetBank residual-VQ (`mmllm/mlx/banks.py:104-149`): `code0 = argmax(q·C0ᵀ)`,
  residual `r = q − C0[code0]`, `code1 = argmax(r·C2ᵀ)`, leaf
  `fine = argmax(r·Cfᵀ)`, global block `blk = path·fpc + fine`, output
  `= expander(Σ_k softmax(scores)·V[leaf]) + Σ_ℓ coarse_value_ℓ[path_ℓ]`.

Both descend a tree of learned centroids by repeated nearest-centroid routing on
a running residual, summing a shared per-level "ancestor" value plus a leaf
value. The residual-VQ is a **shallow (depth 2-3) learned analog of the eve
trie**. Deepening it to a recursive **32-way, depth-`log₃₂N` trie** and feeding
it the **H-Net chunk key as the descent key** unifies the two systems:

> **The chunk boundary key IS the memory address.** One cosine-routing op both
> decides the chunk and indexes the consolidated memory.

This lets us reuse the entire StreamV disk-paging machinery
(`mmllm/mlx/stream_v.py`) — bounded LRU, `pread`/`pwrite` + `F_NOCACHE`,
custom-function VJP that learns keys + scatters V-grad to disk — as the trie's
leaf store. The trie **shape** supplies eve's locality (shallow→hot upper nodes
resident, leaves LRU-paged) without re-introducing mmap page-cache thrash
(`ds4-cold-expert-streaming-pread`, `mmllm-invented-hot-cold-offload`).

---

## 1. Target architecture (full stack)

```
bytes (vocab 256)
  │  + n-gram hash features              ┌── Phase C (feature 4)
  ▼                                      │
[Mamba-2 byte encoder]  full byte rate   ┐
  │                                      │── Phase B (H-Net spine, feature 1)
[cosine chunker]  p_t, cut, STE          │   ~6-byte chunks, ratio loss α
  │  chunk keys  z̃_t  ──────────────────┘
  ▼
[eve-VQ trie NetBank]  descend 32-way trie with chunk key   ┐
  │  read = Σ_ℓ ancestor_ℓ + leaf_V   (StreamV deep LRU)     │── Phase A (memory)
  ▼  write = copy-path-on-write (Phase D, consolidation)     ┘
[main Transformer]  32 dense layers on chunk residual stream (d=256, d_ff=768)
  │  + dual-tier attention + two-level skill router (existing)
  ▼
[dechunk]  STE upsample chunk→byte (confidence c_t gate)
  ▼
[Mamba-2 byte decoder]  full byte rate
  │
[MTP heads]  n≈8 byte heads (t+1..t+8)   ── Phase C (feature 3)
  ▼
bytes
```

The existing model **is** the "main Transformer" box: 32 transformer layers
(`core.lpy:build-block` 1943-2065), dual-tier attention
(`mlx/blocks.py:145-220`), per-layer StreamV NetBanks, two-level skill router
(`netbank.py:543-603`, `mlx/banks.py:177-215`). Phases A-D wrap and deepen it;
none of them rewrite it.

### Current dims (the chain, do not change as defaults)
- vocab 256, d_model 256, d_ff 768, 32 layers, head_dim from `n-heads`.
- q_dim = `n_long_heads · head_dim` (`build-block:1951`); this is the bank query
  width and the trie key width.
- NetBank per module: `sqrt_n=256`, `c_net=8`, `n_blocks=160` → ≈10GB V on disk.
- StreamV cache: `MMLLM_NET_CACHE_ROWS` (default 65536) rows resident.

---

## 2. Phase A — deepen residual-VQ to a true 32-way multi-level trie

**Shippable alone. No chunker. This is the MVP (see §7).** Phase A turns the
depth-2/3 residual-VQ into a depth-`D` 32-way trie and routes the (existing)
`bank_q` through it. It strictly generalizes the current code: `branch=anything,
D=current-depth` reproduces today's path-sum.

### 2.1 Data structure — the trie

A `B`-way (`B=32`) trie of depth `D`. Node addressing is **implicit / heap-style**
(no pointers): a node at level ℓ on path `(c0,…,c_{ℓ-1})` has linear id

```
node_id(ℓ, path) = base[ℓ] + Σ_{j<ℓ} c_j · B^{ℓ-1-j}      # mixed-radix, base-B
base[ℓ] = (B^ℓ − 1)/(B − 1)·? ...   # see layout below
```

We store the trie as **three flat arrays**, all addressable by `node_id`:

| array        | shape                | dtype | resident? | role |
|--------------|----------------------|-------|-----------|------|
| `C` codebooks| `[Σ_ℓ B^ℓ, q_dim]`   | fp32  | upper levels resident, deep levels paged | per-node child centroids (32 rows/parent) |
| `A` ancestor | `[Σ_ℓ B^ℓ, q_dim]`   | fp32  | resident (small) | per-node shared "value" added on every descent through it |
| `V` leaves   | `[B^D, c_net]`       | fp32  | **StreamV (disk, LRU)** | leaf value rows (the consolidated memory) |

Codebook layout per node: the 32 child centroids of node `n` occupy
`C[child_base(n) : child_base(n)+32]`. We keep the upper `R` levels (e.g. `R=2`,
`32²=1024` nodes) of `C`/`A` **fully resident** (cheap: `1024·256·4·2 ≈ 2MB`),
and page deeper-level `C` nodes (and all leaves) through StreamV slabs.

**Descent (read path):**
```
q = rms_norm(bank_q)               # banks.py:_rms_norm, q already long-head query
acc = 0 ; node = ROOT ; r = q
for ℓ in 0..D-1:
    Cnode = C[child_base(node) : child_base(node)+32]    # [32, q_dim]
    c = argmax(r @ Cnode.T)                              # 32-way nearest centroid
    child = node·32 + c
    acc += A[child]                                      # shared ancestor value (the path-sum)
    r   = r − Cnode[c]                                   # residual VQ
    node = child
leaf = node − leaf_base                                  # [B,T] leaf id in 0..B^D
# leaf retrieval reuses the EXISTING PKM top-k pipeline as the within-leaf store:
top_scores, top_global = _pkm_select(q_a, q_b, K_a, K_b, sqrt_n, sub_top_k, top_k)
top_global += leaf · (sqrt_n²)                            # leaf selects the V slab (banks.py:148-149)
out = expander( Σ softmax(top_scores)·V_stream[top_global] ) + acc
```

This is exactly the current `banks.py:104-174` generalized from `D∈{2,3}` to
arbitrary `D`, from per-level `argmax` over distinct codebooks to a **uniform
32-way step over a single addressable `C`**, and with the leaf id offsetting the
StreamV slab (already how `n_blocks` works: `banks.py:148-149`). The leaf count
`B^D` replaces `n_blocks`; pick `D` so `B^D ≈ n_blocks` (e.g. `32^1=32`,
`32^2=1024`, `32^3=32768`). Memory grows at `log₃₂` depth: each extra level
multiplies leaf capacity ×32 but adds only `B^ℓ` resident centroid rows.

### 2.2 Math — VQ losses (straight-through)

Each level contributes a commitment+codebook VQ loss on the residual (extends
`banks.py:107-129` `_vq`):
```
z_vq = Σ_ℓ [ mean((sg(r_ℓ) − c_ℓ)²) + 0.25·mean((r_ℓ − sg(c_ℓ))²) ]
```
fed on the `net_z` channel (`MMLLM_NET_Z_COEF`, `trainer.py:965,1000-1001`). The
`argmax` routing is non-differentiable; the residual subtraction `r − Cnode[c]`
carries gradient to the chosen centroid (standard VQ-VAE STE). Dead-code revive
(`trainer.py:1118-1225`) extends unchanged: per-level histogram of chosen child
codes, split busy centroids onto dead ones every `MMLLM_NET_VQ_REVIVE_EVERY`.

### 2.3 Disk `.bin` layout

- `C` and `A`: small enough to live in the existing dense param pytree for the
  resident upper levels; deep `C` levels share the StreamV format (one `.bin`
  per array, `[Nrows, q_dim]` fp32, `+.adm/.adv` Adam state, `stream_v.py:67-72`).
- `V` leaves: **unchanged** StreamV `.bin` (`[B^D·sqrt_n², c_net]` fp32 +
  `.adm`/`.adv`). The path naming reuses `skill_modules.netbank_v_path`
  (`skill_modules.py:63`) so harvester/torch/MLX agree.

### 2.4 New / changed files

| file | change |
|------|--------|
| `mmllm/mlx/banks.py:104-174` | replace the `if "coarse_codebook"` block with a `_trie_descend(p, q, r)` helper: loop `D` levels over a single `C`/`A` addressable array; return `(leaf_blk, acc)`. Keep depth-2/3 codepath when `net_trie_depth` absent (byte-identical). |
| `mmllm/netbank.py:180-218` | build `C`/`A` as `[Σ_ℓ 32^ℓ, q_dim]` / leaves `32^D·sqrt_n²` when `trie_depth>0`; else current `block_codebook`/`coarse_*`. New ctor args `trie_branch=32`, `trie_depth=0`, `trie_resident_levels=2`. |
| `mmllm/mlx/trainer.py:121-166,280-298` | `_emit_net`/`_reassemble`: emit `net_trie_C`,`net_trie_A` (resident) + StreamV handles for deep `C`; thread `trie_depth`/`trie_branch` through `sb["net"]`. |
| `mmllm/core.lpy:286-318,2038-2057` | `pick-netbank-trie-depth` (`MMLLM_NET_TRIE_DEPTH`, default 0), `pick-netbank-trie-branch` (default 32); pass to `ModularNetBank`. |

### 2.5 Dual-backend split + parity

- **MLX** is the live training/eval path (`banks.py`); implement `_trie_descend`
  there first.
- **torch** (`netbank.py:forward` 339-458) currently *ignores* the coarse path
  ("torch uses block 0", `netbank.py:202-203,212`). Keep that: torch builds the
  params (so ckpts/harvest carry them) but its forward uses leaf 0 unless we add
  the descent. Add a torch `_trie_descend` mirror **only** for the parity gate
  and CPU birds; production birds are MLX.
- **Parity** (`mlx/parity.py`): extend `extract_params` to copy `C`/`A`; assert
  MLX-vs-torch top-1 leaf agreement > 99.5% (ties at centroid boundaries are the
  only divergence, same tolerance as `banks.py:13-16`). Add a unit test that a
  depth-1 branch-`n_blocks` trie == the current `block_codebook` argmax output
  bit-for-bit.

### 2.6 Env gates (default-off)
```
MMLLM_NET_TRIE_DEPTH=0        # 0 → current residual-VQ (byte-identical). 2,3 enable trie.
MMLLM_NET_TRIE_BRANCH=32
MMLLM_NET_TRIE_RESIDENT_LEVELS=2
MMLLM_NET_Z_COEF (existing)   # now sums per-level VQ losses
```

### 2.7 Memory / lean budget (32GB)
- Resident `C`+`A` upper 2 levels: `(32+1024)·256·4·2 ≈ 2.2 MB` ×32 layers ≈ 70 MB.
- Deep `C` paged via StreamV (same cap as V).
- Leaves: `32^D·sqrt_n²·c_net·4`. At `D=2`, `sqrt_n=256`, `c_net=8`:
  `1024·65536·8·4 ≈ 2.1 GB`/module on disk; resident = `MMLLM_NET_CACHE_ROWS`
  only. At `D=3` it's 67 GB on disk but **resident footprint is unchanged**
  (StreamV bound, `stream_v.py:28-32`). Guard with `iogpu.wired_limit_mb`
  (`ds4-reap-fork-and-crash-safety`).

### 2.8 Tests + metrics
- bpc unchanged at depth 0 (regression gate).
- Δ_net (consolidation, `trainer.py:1469-1474`) ≥ depth-3 path-sum baseline.
- NB fill: % of leaves touched (extend the PKM-diag `trainer.py:467-515`); deeper
  trie should **raise** distinct-row %, **lower** pairwise Jaccard (less
  cross-corpus overwrite — the collapse blocker, `banks.py:95-103`).
- Retrieval accuracy: synthetic key→value recall probe (new test): write `K`
  distinct (key,val) pairs into leaves, measure exact-recall after `N` writes.

### 2.9 Risks + mitigations
| risk | mitigation |
|------|-----------|
| deep `C` paging thrash | resident upper `R` levels; only deepest level(s) paged; reuse StreamV LRU |
| argmax routing collapse (few leaves used) | per-level dead-code revive (`trainer.py:1118`); per-level VQ load-balance via `net_z` |
| ckpt/harvest format drift | `C`/`A`/leaves all via existing `.bin` + `netbank_v_path`; positional dense.pt unaffected (trie params at END, like router keys `trainer.py:1377-1386`) |
| torch parity divergence | gate parity to MLX-as-truth; torch forward optional |

---

## 3. Phase B — add 1-stage H-Net spine

Wrap the existing model in a single H-Net stage: a cheap **Mamba-2 byte
encoder/decoder** at full byte rate around the expensive transformer, which now
runs on **chunks** (~6 bytes). Wire the chunk key into the Phase-A trie address.

### 3.1 Components

**Mamba-2 encoder/decoder.** Small (1-2 layers, d_model 256) SSM blocks. MLX has
no stock Mamba; implement a minimal selective-SSM scan (`mlx.core` cumulative
scan via `mx.fast` or an associative-scan fallback). New module
`mmllm/mlx/mamba.py` (forward only, like `blocks.py`) + torch ref
`mmllm/mamba.py`. Default-off: when `MMLLM_HNET_STAGES=0`, encoder/decoder are
identity and the byte stream goes straight to the transformer (byte-identical).

**Cosine chunker (`mmllm/mlx/chunker.py`).**
```
x̂ = encoder(embed(bytes))                # [B, L, d]
q = x̂ @ W_q ; k = x̂ @ W_k                 # [B, L, d]
cos = Σ(q_t · k_{t-1}) / (|q_t||k_{t-1}|)
p_t = 0.5·(1 − cos)                        # boundary prob, p_0 := 1.0
cut = p_t ≥ 0.5                            # hard boundaries
```
Chunk representation `z̃_j` = the encoder state at each cut position (downsample).
Chunk count `M ≈ L/N`, target `N ≈ 6`.

**STE dechunk + confidence gate.** Upsample chunk outputs back to byte positions;
the confidence `c_t = p_t if cut else 1−p_t` is the straight-through value:
forward uses `z̃` (the routed chunk), gradient flows to `p_t` (H-Net's smoothing
EMA on the chunk side). `c_t` doubles as the **soft read/write gate** on the
NetBank: low confidence → down-weight the trie contribution (`out = c_t·out`).

**Ratio loss.** Pin avg chunk size to `N`:
```
L_ratio = α · ( N/(N-1) · F·G + (1−F)·(1−G)·N/(N-1) )      # H-Net eq.
F = mean(p_t) , G = mean(cut)                              # actual boundary mass/freq
```
added to `loss` in `trainer.py:loss_fn` (`MMLLM_HNET_RATIO_COEF`, default 0).

### 3.2 Chunk key → bank address

The chunk key `z̃_j` (or `W_addr·z̃_j`) **is** the descent key fed to the Phase-A
trie. Concretely: the transformer's `bank_q` (`blocks.py:189`) at chunk
resolution is routed through `_trie_descend`. Because the chunker already
computed a cosine-routing decision, we can **reuse `cut`/`p_t`** as the level-0
trie split for the top of the trie (the boundary decision and the coarsest
memory bucket coincide) — this is the "same op" unification made literal.

### 3.3 Integration points

- `mlx/model.py:forward` (17-57): insert `encoder → chunker → (existing block
  loop on chunks) → dechunk → decoder`. The block loop body is **unchanged**;
  only `x`'s sequence length changes from `L` to `M`. RoPE cache indexed by chunk
  position. Gated: stages=0 → unchanged loop.
- `mlx/trainer.py:loss_fn` (982-1032): add `L_ratio`; CE/MTP computed at byte
  rate after dechunk+decoder (so labels stay per-byte — no retokenization).
- `core.lpy:build-model` (2210): build encoder/decoder/chunker modules behind
  `pick-hnet-stages`; add their params at END of `(parameters)` (2315-2423) for
  positional ckpt compat (same discipline as mtp-head 2225).

### 3.4 Dual-backend + parity
- MLX first (live path). torch Mamba ref for parity + CPU birds.
- Parity gate: byte-rate logits match within tol with `stages=0` (identity
  encoder ⇒ exact). With `stages=1`, gate on **chunk boundary agreement** (cut
  masks identical) + bpc within 1e-3, not bitwise (SSM scan order differs).

### 3.5 Env gates
```
MMLLM_HNET_STAGES=0           # 0 → no chunking (byte-identical). 1 → one stage.
MMLLM_HNET_TARGET_N=6         # target avg chunk size
MMLLM_HNET_RATIO_COEF=0.0     # α on the ratio loss (enable with stages)
MMLLM_HNET_ENC_LAYERS=2 / MMLLM_HNET_DEC_LAYERS=2
MMLLM_HNET_CONF_GATE=0        # 1 → c_t gates the netbank read/write
```

### 3.6 Memory / risks
- Mamba encoder/decoder at d=256, 2 layers: negligible (<50 MB).
- Transformer FLOPs **drop** ~6× (runs on M≈L/6 chunks) — frees budget for deeper
  trie. B=2 stays near-optimal (`training-efficiency-shortlist`).
- Risk: chunk ratio drift (all-boundaries or no-boundaries collapse) →
  monitor `G=mean(cut)`, ratio loss + warmup `α`. Risk: dechunk grad
  instability → STE smoothing EMA (H-Net), clip via existing ZClip path.
- Risk: B=2 + chunking changes effective batch of memory writes → keep
  `MMLLM_NET_CACHE_ROWS` sized for a full chunk-step touched set.

---

## 4. Phase C — MTP byte heads + n-gram hash input features

### 4.1 MTP heads (feature 3)

The model **already has a single t+2 MTP head** (`core.lpy:2225`,
`pick-mtp-coef` 2200-2208, `collect-mtp-loss` 2729-2762). Generalize to `n≈8`
heads predicting t+1..t+8 from the **decoder** output (byte rate).

- `core.lpy:build-model:2225`: build `mtp-head` as `n` Linears (or one
  `Linear(d, n·vocab)` reshaped). Default `MMLLM_MTP_HEADS=1` → current behaviour.
- `collect-mtp-loss:2729`: sum CE over the `n` offsets, each shifted label;
  coef per-head decay (`MMLLM_MTP_COEF` × `γ^k`).
- MLX: `mlx/model.py:forward` already returns aux; add MTP logits computed on the
  post-decoder hidden state; `trainer.py:loss_fn` adds the MTP CE term (mirror
  the existing `_kd_obj`/distill add at 1006-1031).
- Heads live at END of `(parameters)` (2400) — positional ckpt compat preserved.

### 4.2 n-gram hash input features (feature 4)

Augment the byte embedding with hashed n-gram features (byte-level analog of
hash embeddings / fastText). For each position, hash the preceding `g`-gram
(g∈{2,3,4}) into a `H`-bucket table, sum the looked-up vectors into the input:
```
e_t = tok_emb[b_t] + Σ_{g∈G} HashEmb_g[ hash_g(b_{t-g+1..t}) mod H_g ]
```
- New module `mmllm/ngram.py` (+ MLX mirror): `HashEmb_g` = `nn.Embedding(H_g,
  d_model)`, rolling polynomial hash computed in the data loader (cheap, on the
  uint8 windows) so the forward just does an embedding add.
- `core.lpy:build-model`: build hash tables behind `pick-ngram-hash` (default
  off); add to `(parameters)` at END.
- `mlx/model.py:forward:22` (`x = tok_emb[tokens]`): add the precomputed hash
  embeddings (passed alongside tokens in the batch dict). Gated: no tables →
  unchanged.
- Hashes feed the encoder (Phase B) when present, else the transformer directly.

### 4.3 Env gates
```
MMLLM_MTP_HEADS=1             # n MTP byte heads (1 → current single t+2 head)
MMLLM_MTP_COEF (existing) / MMLLM_MTP_DECAY=0.7
MMLLM_NGRAM_HASH=             # "2:65536,3:262144" → enable g-gram hash tables
```

### 4.4 Tests / risks
- MTP: bpc(t+1 head) must equal baseline at HEADS=1; multi-head should lower bpc
  (denser gradient, `training-efficiency-shortlist` MTP-byte).
- n-gram: collision rate monitor; risk = hash collisions inject noise → start
  with large `H`, zero-init add path so it's inert at step 0.
- Memory: hash tables `H·d·4`; `2:65536`→64 MB, `3:262144`→256 MB. Bound via `H`.

---

## 5. Phase D — copy-path-on-write versioning → consolidation snapshots

eve's structural sharing + atomic root-CAS becomes the wake/sleep consolidation
mechanism. On a write (a learning step that updates leaf rows), instead of
mutating in place, **copy the root→leaf path** (the `O(D)` touched `C`/`A`/leaf
nodes) into fresh slots and atomically swap a new **root version**. Unwritten
subtrees are shared between versions (no copy). A version = a consolidation
snapshot; harvest publishes a version; readers pin a root.

### 5.1 Mechanism over StreamV
- Add a `version` epoch to `StreamV` (`stream_v.py`): writes (`adam_step`,
  `:113`) go to **new rows** appended at a version-local offset for the touched
  path nodes; a `roots[]` table maps `version → root node base`.
- `flush()` (`:130`) seals a version (fsync + write the root pointer). The
  wave/harvest orchestration (`staged-wave-consolidation`, `harvester.py`)
  publishes version `v` as the new round-bank inode; cold-share readers
  (`stream_v.py:40-49`, `MMLLM_NET_COLD_SHARE`) open it read-only.
- Copy-on-write touches only `O(D·sqrt_n²)` rows per step → cheap; shared
  subtrees mean a snapshot is a delta, fixing the **dense-delta degeneracy**
  (`mmllm-dense-delta-degeneracy`: today a mature chain's V_net is dense vs r0).

### 5.2 Integration
- `trainer.py:1302-1315` (StreamV flush / persist) → seal version, write
  `roots.bin`.
- `harvester.py` (FedAvg harvest) → merge per-version path deltas instead of full
  V (a structurally-shared merge: only diverged paths are averaged).
- Gated `MMLLM_NET_TRIE_COW=0` (default off → in-place, current behaviour).

### 5.3 Risks
- Version-store growth → GC unreferenced old versions (keep latest `K`, mirror
  `MMLLM_CKPT_KEEP` `trainer.py:1330-1344`).
- Concurrency (PAR births writing) → root-CAS is per-bird-local; harvest
  serializes the merge (already the wave model).
- This is the most speculative phase; ship A-C first, D last.

---

## 6. Cross-cutting: dual-backend parity discipline

1. Implement each phase in **MLX first** (live path), torch as parity ref / CPU
   bird fallback.
2. Every phase keeps `_extract`/`_reassemble`/`_write_back`
   (`trainer.py:50-373`) symmetric: new params emitted by `_emit_net` / built in
   `build-block`, frozen-able via the `Fa`/`Ft` closures (`:228-231`) so the KD
   student/trunk-freeze regimes still hold.
3. New params go at the **END** of `(parameters)` and in name-keyed sidecars
   (`router-keys.<bi>.npy` pattern, `trainer.py:1377-1386`;
   `_named_params` 421-452) so positional dense.pt + harvest stay compatible and
   resume is module-growth-safe.
4. Parity gate (`mlx/parity.py`) extended per phase; gate is **MLX-as-truth**,
   torch tolerant (ties/scan-order). Top-1 routing agreement > 99.5%.

---

## 7. MVP — Phase A PR spec ("MVP-A")

**Title:** `feat(netbank): 32-way multi-level VQ trie behind MMLLM_NET_TRIE_DEPTH (default-off)`

**Goal:** deepen the residual-VQ (`banks.py:104-149`) into a depth-`D`, 32-way
trie, leaf→StreamV slab. No chunker, no Mamba, no MTP. Ships on the working
chain with all gates unset = byte-identical.

**Changes (minimal, ~1 file of real logic):**
1. `mmllm/mlx/banks.py`: add `_trie_descend(p, q)` (≈30 lines) returning
   `(leaf_blk, acc)`; in `netbank_forward` (104-149) branch to it when
   `p.get("net_trie_depth")`. Existing depth-2/3 path untouched.
2. `mmllm/netbank.py:180-218`: when `trie_depth>0`, allocate `C=[Σ_ℓ32^ℓ,q_dim]`,
   `A=[same,q_dim]` (zero-init → no-op until learned, like `coarse_value`
   `netbank.py:216`); set `n_blocks=32^D`. New ctor kwargs.
3. `mmllm/mlx/trainer.py`: `_emit_net` (121-139) emits `net_trie_C/_A`;
   `_reassemble` (280-298) passes them + `trie_depth` into the bank dict; add
   `C`/`A` to the dense-Adam tree (they learn).
4. `mmllm/core.lpy`: `pick-netbank-trie-depth`/`-branch` (near 286-318); pass to
   `ModularNetBank` (2038). `ModularNetBank.__init__` (`netbank.py:610`) +
   `NetBank.__init__` thread the kwargs.
5. `mmllm/mlx/parity.py`: copy `C`/`A`; depth-1 == `block_codebook` unit test.

**Validation (launch-time health check + logging, per `always-log-runs`):**
- `MMLLM_NET_TRIE_DEPTH=0` smoke: bpc + Δ_net identical to HEAD (regression gate,
  must be exact).
- `MMLLM_NET_TRIE_DEPTH=2` smoke (sqrt_n=256, c_net=8, B=2, short run): logs
  per-step loss, minieval_bpc, Δ_net, net_z, **per-level leaf-fill %** and
  **pairwise Jaccard** (extend `_run_pkm_diag` 467-515).
- Acceptance: depth-2 Δ_net ≥ depth-3 path-sum baseline AND leaf Jaccard <
  baseline (less collapse). 32GB resident bounded (StreamV cap unchanged).
- Health check at launch: assert `C`/`A` shapes, assert depth-0 byte-identity on
  the first batch before committing to the full run.

**Risk for MVP:** lowest of the four phases — it's a generalization of code that
already exists and ships. The one real risk is leaf under-fill at high `D`;
mitigated by starting at `D=2` and the existing dead-code revive.

---

## 8. Effort / sequencing estimate

| phase | scope | depends on | est. effort | ship risk |
|-------|-------|-----------|-------------|-----------|
| **A** trie NetBank (MVP) | deepen residual-VQ → 32-way trie + StreamV leaves | — | **2-3 days** | low |
| **B** H-Net 1-stage spine | Mamba enc/dec + cosine chunker + ratio loss + STE dechunk + key→addr | A (key feeds trie) | 5-8 days | med-high (MLX Mamba, chunk stability) |
| **C** MTP heads + n-gram hash | extend existing mtp-head to n; hash input | — (parallel to A/B) | 2-3 days | low |
| **D** copy-path-on-write versioning | StreamV version epochs + harvest delta merge | A | 4-6 days | high (speculative) |

**Recommended order:** A (MVP, immediate value, de-risks the trie) → C (cheap,
parallelizable, denser gradient) → B (the big architectural win; needs A's
address path) → D (consolidation snapshots; last, highest risk). Each lands
default-off; the chain keeps running throughout.

**Total:** ~3-4 weeks of focused work to all four phases, with A+C deliverable
in the first week and independently valuable.

---

## 9. Appendix — grounding file:line index

- residual-VQ routing (the trie seed): `mmllm/mlx/banks.py:104-174`
- StreamV disk LRU + VJP: `mmllm/mlx/stream_v.py:23-155`, `157-190`
- NetBank / ModularNetBank / ModuleRouter: `mmllm/netbank.py:109-330`, `543-603`, `606-715`
- VQ codebook build (extend for trie): `mmllm/netbank.py:180-218`
- block forward + bank wiring: `mmllm/mlx/blocks.py:145-220`, `223-233`
- model forward (chunker insertion point): `mmllm/mlx/model.py:17-57`
- extract/reassemble/loss/step: `mmllm/mlx/trainer.py:50-185`, `215-324`, `982-1032`, `1134-1294`
- build-block / build-model / pickers / mtp-head: `mmllm/core.lpy:1943-2065`, `2210-2289`, `286-318`, `2225`, `2729-2762`
- skill-module path naming: `mmllm/skill_modules.py:63`
- parity harness: `mmllm/mlx/parity.py`

---

## Roadmap beyond MVP (banked 2026-06-28)

**Key reframe (logical vs structural nesting):** "deep nesting" is what we want *logically* (token⊂line⊂fn⊂module), and that depth comes from the **H-Net stage stack**, NOT the trie. A shallow trie (depth-1/2) is fine as the per-stage *addresser*; deepening the structural trie only buys capacity, not richer recall. So: stack H-Net, keep the trie shallow.

### Phase E — multi-stage H-Net (LOGICAL nesting) — the real "deep nesting"
- Phase B shipped 1-stage. Stack to 2–3 stages: byte → chunk → super-chunk(→…). Each stage = one logical abstraction level; the super-chunk key *is* a higher-order concept. Avg logical depth 6+ = a few stacked stages, not a 6-deep tree.
- Each stage's chunk key hits its own shallow trie NetBank (the addresser at that abstraction level) → hierarchical content-addressed memory.
- Reuses everything: the cosine chunker (Phase B), the trie addresser (Phase A), versioning (Phase D). Mainly: generalize the spine to recurse stages + per-stage netbanks; the ratio loss per stage pins each stage's compression.
- This is the lever for the user's "6+ deep on average" recall. SPIKE: 2-stage on tiny config, measure whether stage-2 super-chunk keys carry coarser/more-abstract retrieval than stage-1.

### Phase F — lazy-grow sparse StreamV (STRUCTURAL capacity) — DEFERRED
- The MVP trie is capped at ≤160 leaves because StreamV is a fixed clone of the seed's 160-block bin (`_read_row` preads by raw offset, no EOF guard → crash past 160). This is a *capacity* ceiling, not a depth one.
- eve-proper: V file sparse + grows KB→TB on demand; only touched leaves materialize; upper nodes resident, leaves LRU-paged (the eve trick). Removes the leaf ceiling → branch-32 structural tries, ~10^9 slots, mostly cold on disk.
- NOT a prerequisite for logical depth (Phase E delivers that). Do this when capacity (not abstraction depth) is the bottleneck. Pairs with smaller per-leaf V.

### Phase G — threaded births (spiked 2026-06-28): REFRAME to memory-density, NOT compute-throughput
**Verdict: viable as a memory play, BLOCKED as a throughput play by the single GPU.**

- **Probe 1 (does MLX thread-parallelize compute?): NO.** MLX *does* release the GIL during `eval` (dispatch-bound threaded/sequential ratio 0.79–0.80 — Python dispatch overlaps), but there is ONE GPU so compute-bound kernels SERIALIZE (D=512 ratio 1.03, D=1024 ratio 1.10 — a slight scheduler-contention penalty). **Threaded births give zero compute speedup.** "Super-parallel = more throughput" is a hardware (1-GPU) wall, not a software one.
- **Probe 2 (shared versioned banks across threads): HOLDS.** N threads on one MAP_SHARED readonly base (50× concurrent reads, base bytes untouched); each thread its own `.ver` overlay with overlapping rows → no bleed, base immutable; `merge_version_deltas` harvest correct. The versioned-CoW infra is genuinely thread-safe — the data side is ready.
- **Probe 3 (memory): the actual win, size unknown.** Threading collapses to 1× the read-only shared portion (MLX runtime + frozen trunk/dense params + MLX pool). Cold banks are ALREADY process-shared via cold-share page-cache (no extra gain). Still scales with N: per-worker hot module + Adam + activations + autograd graph. **If the ~24 GB/process is mostly frozen-trunk/dense → big win (fit more births per RAM); if mostly activations → modest.** Unknown which dominates.

**So the real prize:** threaded births let you fit MORE concurrent births in 32 GB (push past the PAR=2 memory wall), NOT run them faster. Memory-density, not speed.

**Design:** `genesis_composed_bird` per-process `main()` → `worker(tid)` thread pool sharing one loaded model (frozen trunk/dense + cold `StreamV(readonly)` 1×); per-thread owns hot module + `StreamV(versioning)` (own `.ver/.vidx/.adm/.adv` — per-thread paths MANDATORY) + optimizer + `value_and_grad` closure + its own `mx.Stream` (cuts scheduler contention). Barrier at round end → collect each thread's `version_delta()` → merge → one `materialize` writer.
**Gotchas:** single-GPU serialization; give each thread its own `mx.Stream`; MLX autograd thread-safety UNPROVEN at real scale; per-thread paths mandatory (shared path = corruption).
**Next experiment (decisive):** a real 2-thread births run (actual model, not toy) measuring **peak RSS vs 2 separate processes** + round wall-time → quantifies the true memory saving (does frozen-trunk sharing dominate the 24 GB?) and confirms MLX autograd survives concurrent real graphs.

**Phase G — PROVEN at toy scale (2026-06-28), real autograd:**
- **Q1 trunk shares by reference (the prize gate):** 2nd worker's trunk view = **+0 MB** (`_reassemble` wraps the same `trainable` buffers via `Ft`=identity/`stop_gradient`, no data copy). Saving = **(N−1)×trunk**, structural at any scale.
- **Q2 concurrent autograd is corruption-free at model scale:** two threads each running `mx.value_and_grad` through the shared frozen trunk → losses **bit-identical** to solo. MLX functional autograd over immutable shared arrays is concurrency-safe (grads return as new arrays; nothing mutated in place). Combined with Probe-2 versioned-bank write isolation → both halves (shared-read trunk + private-write bank) proven.
- **REMAINING (the only unknown):** the production **trunk : per-worker(activations+hot-bank) ratio** — sets the actual PAR multiplier. Needs ONE full-scale measurement: peak RSS of 2 real births threaded vs 2 processes, on an idle box. Everything it depends on is proven.

**Phase G — PRODUCTION-SCALE MEASURED (2026-06-28, d=256, real H-Net births):**
- **Shareable bucket ≈ 10.5 G = ~95% of an 11.1 G birth** (framework runtime + torch/MLX + 0.4 G MLX trunk + 0.5 G pool + cold-bank page cache; dense.pt only 130 MB). Per-worker increment = **0.43 G** (2-birth RSS 11.57 G vs 11.14 G; trunk same `id()` across threads, trunk grads None, no NaN, losses fell).
- **Concurrent forward sweep:** 2→11.5 G, 4→12.9 G, 8→14.7 G, **16 births → 18.1 G**. Ratio shareable:per-worker ≈ **20–25 : 1** → runtime/model-dominated → BIG win, NOT activation-bound.
- **VERDICT: PAR 2 → realistically 6–8** (16 forward-births proven in 18 G; training-peak ~6–8 simultaneous, more staggered). Transformative — kills the swap-thrash.
- **BLOCKER (MLX 0.31.2):** true concurrent *training* threads throw `no Stream(gpu,0) in current thread` — the H-Net chunker's `mx.max(...).item()` host-sync inside `value_and_grad` fails off the main thread (clean repro). Fork-after-MLX hits Metal kernel-load races.
- **FIX options:** (a) **static/bounded chunk-length — kill the in-trace `.item()`** [BEST: unblocks threads AND keeps the runtime-share win]; (b) upstream per-thread MLX streams; (c) spawn-multiprocess + mmap [loses the win — the 10.5 G is per-process runtime, not mmap-shareable]. To ship: worker-pool restructure + the (a) chunker fix.
