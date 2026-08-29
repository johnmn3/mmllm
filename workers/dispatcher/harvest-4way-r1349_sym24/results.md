# harvest-4way-r1349 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1349 ctrl_bpc |
|--------|--------|--------------:|
| r2xwC | fork-slaa-us-mmllm-claude-train-sym24-92e75e7e-r2xwC | 3.1625 |
| Ju2J2 | fork-joly-os-mmllm-claude-train-sym24-dde49b51-Ju2J2 | 3.3507 |
| yrbhk | origin/claude/train-sym24-e3bc2ad8-yrbhk | 3.6931 |
| urnFx | origin/claude/train-sym24-d4aa5e4e-urnFx | 3.6955 |
| **mean** | | **3.4754** |
| **best** | | **3.1625** |

## Chain progression R1348 → R1349

Previous harvest: `workers/dispatcher/harvest-5way-r1348_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3626         | 3.4754         | +0.1128 |
| ctrl_bpc best  | 3.2271         | 3.1625         | -0.0646 |

## Per-round trajectory (best bird: r2xwC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1349 | 6270 | 3.1625 | +0.1084 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1348_sym24`
  - `workers/dispatcher/harvest-5way-r1348_sym24`

## Output

`workers/dispatcher/harvest-4way-r1349_sym24/round-1349/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

