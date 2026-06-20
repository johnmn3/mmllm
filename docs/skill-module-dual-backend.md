# Skill-module netbank — dual-backend implementation story

Partition the monolithic NetBank into per-skill modules (one independent
`NetBank` per skill), cooled on a staged schedule. **Both backends must
implement it identically** or torch GH-birds and MLX Apple-birds produce
incompatible artifacts and the harvest can't merge them.

## Shared contract — `mmllm/skill_modules.py` (torch-free, both import it)
- `parse_modules()` ← `MMLLM_NET_MODULES="gutenberg-prose,amps-math,stackexchange-dialogue"`. Empty/unset → `[]` = legacy single bank (**zero behavior change when unset**).
- `module_for_corpus(corpus_key, modules)` — genesis tag-routing (the mix sampler already knows each batch's corpus). Learned skill-router supersedes later.
- `netbank_v_path(dir, module, layer)` → **`V_net.<module>.<layer>.bin`** — the ONE on-disk convention torch, MLX, and the harvester all use. Extends the legacy `V_net.<layer>.bin`.

## torch backend — GH CI birds  (`netbank.py` + `core.lpy`)
- **DONE:** `ModularNetBank` (drop-in `forward(q)`, `set_active()`, `freeze_module()`, `module_{dense,sparse}_parameters(name)`), now using `netbank_v_path`. Unit tests in `tests/test_modular_netbank.py`.
- **NEXT (`core.lpy`):**
  1. **Build** (~`build_bank_query`/netbank build, ~1919): if `parse_modules()` non-empty → `ModularNetBank(q_dim, modules, mmap_dir=…, mmap_layer=block_idx, sqrt_n/c_net/top_k from env)`; else current single `NetBank` (unchanged path).
  2. **Route** (train-step, where the batch's corpus is known): `netbank.set_active(module_for_corpus(corpus_key, modules))` before the block forward. `attention_kernel` is untouched (still calls `netbank(bank_q)`).
  3. **Per-module LR** (optimizer setup, the `MMLLM_LR_NET_MULT` group): one SparseAdam group per `module_sparse_parameters(name)` + AdamW group per `module_dense_parameters(name)`, each with its own multiplier/cosine. Cooling = drive a mastered module's mult → 0 (or `freeze_module`).

## MLX backend — Apple-Silicon local birds  (`mlx/banks.py` + `mlx/trainer.py` + `mlx/bridge.py`)
- **DONE:** `netbank_forward_modular(banks, active, q)` — `banks={module: params_dict}`, routes/sums exactly like `ModularNetBank.forward`.
- **NEXT (`mlx/trainer.py`):**
  1. **Build** (~113-199, where `b["netbank"]={…}` is assembled): build `b["netbanks"]={module: params_dict}`, each module's `V`/`V_mmap` from `netbank_v_path(dir, module, layer)` via `bridge.py`. (Note: `MMLLM_NET_WIDEN` already widens `c_net` — applies per module.)
  2. **Route** (block forward / `switch_gate_eval` call site): `net_out = netbank_forward_modular(b["netbanks"], active, q)` where `active = module_for_corpus(corpus_key, modules)`.
  3. **Per-module SparseAdam + freeze** (`mlx/sparse_adam.py`, the `Fa`/`Ft` freeze split ~151): tag each module's `V` as its own SparseAdam target with its own LR; a frozen module's `V` goes through `Ft` (excluded from trainables) → rows can't move = same isolation as torch `freeze_module`.

## Harvest — both (`harvester.py`, backend-agnostic)
Already filename/format based and refuses to merge Local banks. Extend to **per-module FedAvg**: glob `V_net.<module>.<layer>.bin`, merge each module only across birds that trained it (no cross-skill averaging-away = fixes dense-delta degeneracy). torch and MLX birds drop identical files → merge transparently.

## Cooling curriculum (both backends, via the above hooks)
Genesis: 3 modules hot (high per-module net-LR). Master (held-out val-bpc plateau) → freeze them (LR→0 / `freeze_module` / `Ft`) → add module 4 hot → repeat. A frozen module's `moved% → 0` by construction → cross-skill interference structurally impossible.

## Status
| piece | torch | MLX |
|---|---|---|
| shared contract (`skill_modules.py`) | ✅ (shared) | ✅ (shared) |
| modular netbank forward | ✅ `ModularNetBank` | ✅ `netbank_forward_modular` |
| build wiring | ▶ `core.lpy` | ▶ `mlx/trainer.py` |
| routing (corpus→active) | ▶ train-step | ▶ block forward |
| per-module LR + cooling | ▶ optimizer groups | ▶ SparseAdam `Fa/Ft` |
| harvest per-module merge | ▶ `harvester.py` (shared) | ▶ `harvester.py` (shared) |
| runtime validation | torch env (CI/Modal) | Apple-Silicon MLX |
