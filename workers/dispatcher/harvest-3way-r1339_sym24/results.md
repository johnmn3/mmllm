# harvest-3way-r1339 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1339 ctrl_bpc |
|--------|--------|--------------:|
| Po6Lo | fork-slaa-us-mmllm-claude-train-sym24-f189b555-Po6Lo | 3.2521 |
| 1DH2Q | origin/claude/train-sym24-c5bbbe32-1DH2Q | 3.2642 |
| n5heL | fork-joly-os-mmllm-claude-train-sym24-6a77ab4b-n5heL | 3.3602 |
| **mean** | | **3.2922** |
| **best** | | **3.2521** |

## Chain progression R1338 → R1339

Previous harvest: `workers/dispatcher/harvest-4way-r1338_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3105         | 3.2922         | -0.0183 |
| ctrl_bpc best  | 3.2662         | 3.2521         | -0.0141 |

## Per-round trajectory (best bird: Po6Lo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1339 | 6265 | 3.2521 | +0.1122 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1338_sym24`
  - `workers/dispatcher/harvest-4way-r1338_sym24`

## Output

`workers/dispatcher/harvest-3way-r1339_sym24/round-1339/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

