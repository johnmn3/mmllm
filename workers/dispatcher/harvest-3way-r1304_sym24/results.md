# harvest-3way-r1304 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1304 ctrl_bpc |
|--------|--------|--------------:|
| lffLu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b7ebc66b-lffLu | 3.5563 |
| z7ilS | fork-joly-os-mmllm-claude-train-sym24-6e97a0a9-z7ilS | 3.5564 |
| i7HVa | origin/claude/train-sym24-6177d488-i7HVa | 3.8958 |
| **mean** | | **3.6695** |
| **best** | | **3.5563** |

## Chain progression R1303 → R1304

Previous harvest: `workers/dispatcher/harvest-4way-r1303_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6021         | 3.6695         | +0.0674 |
| ctrl_bpc best  | 3.5844         | 3.5563         | -0.0281 |

## Per-round trajectory (best bird: lffLu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1304 | 3732 | 3.5563 | +0.0659 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1303_sym24`

## Output

`workers/dispatcher/harvest-3way-r1304_sym24/round-1304/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

