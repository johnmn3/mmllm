# harvest-3way-r22 — sparse-delta merge of 3 birds

FedAvg merge of 3 workers' round-22 endpoints from the smoke-r22 wave
(rounds 20-22, 7 steps each, frac=0.5 CORRECT recipe).

## Worker endpoints

| handle | branch                       | R22 ctrl_bpc |
|--------|------------------------------|-------------:|
| Qblru  | claude/smoke-r22-Qblru       | 1.2928       |
| tklXe  | claude/smoke-r22-tklXe       | 1.3138       |
| pGOfE  | claude/smoke-r22-pGOfE       | 1.3421       |
| **mean** |                            | **1.3162**   |

## Chain progression R19 → R22 (3 rounds × 7 steps = 21 training steps)

| metric          | R19 (frac=1.0 TAINTED) | R22 (frac=0.5) | Δ      |
|-----------------|-----------------------:|---------------:|-------:|
| ctrl_bpc mean   |                 1.9561 |         1.3162 | -0.6399 |
| ctrl_bpc best   |                 1.9374 |         1.2928 | -0.6446 |

## Per-round trajectory (Qblru, representative)

| round | wall_s | ctrl_bpc | ppl  | Δ_net  |
|-------|-------:|---------:|-----:|-------:|
| 20    |   1003 |   1.5154 | 2.86 | +0.0115 |
| 21    |    894 |   1.3493 | 2.55 | +0.0085 |
| 22    |    801 |   1.2928 | 2.45 | +0.0100 |

## Output

`workers/dispatcher/harvest-3way-r22/round-22/`:
- `delta-sparse-net.{0..31}.pt` (32 row-aware-merged delta files, ~131 MB total)
- `delta-sparse-net.meta.pt`
- `dense.pt` (averaged across 3 birds, 4.3 MB)
- `opt-sparse-net.{0..31}.pt` (averaged across tklXe + pGOfE — Qblru missing opt-state)
- `opt-sparse-net.meta.pt`

Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`.

## Caveats

- 3 birds instead of the 4-5 we usually quorum at. Qblru pushed without
  opt-sparse-net.*.pt for unclear reasons; opt-state averaged from the
  2 birds that did publish it.
- XvNVp crashed mid-training (pushed an old r10 snapshot, no r22).
  A 5th bird was reported crashed before push.
- Wall time per round is 800-1000s/round — much slower than r19's
  30-60s/round, because the r19 recipe was TAINTED (frac=1.0 froze
  24/32 layers, making each step cheap). The r22 numbers reflect actual
  full-model training cost.

## Battery eval: not run
