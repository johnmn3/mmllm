# harvest-3way-r1188 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1188 ctrl_bpc |
|--------|--------|--------------:|
| kkWhJ | origin/claude/train-sym24-4e9c53c4-kkWhJ | 2.3127 |
| bYdRn | fork-joly-os-mmllm-claude-train-sym24-abbe8a4b-bYdRn | 2.3138 |
| Gctgz | fork-slaa-us-mmllm-claude-train-sym24-fc18efba-Gctgz | 2.6888 |
| **mean** | | **2.4384** |
| **best** | | **2.3127** |

## Chain progression R1187 → R1188

Previous harvest: `workers/dispatcher/harvest-5way-r1187_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3862         | 2.4384         | +0.0522 |
| ctrl_bpc best  | 2.3080         | 2.3127         | +0.0047 |

## Per-round trajectory (best bird: kkWhJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1188 | 6644 | 2.3127 | +0.2524 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1187_sym24`

## Output

`workers/dispatcher/harvest-3way-r1188_sym24/round-1188/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

