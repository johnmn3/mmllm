# harvest-2way-r1337 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1337 ctrl_bpc |
|--------|--------|--------------:|
| BbfAE | origin/claude/train-sym24-04e3e7a1-BbfAE | 3.2950 |
| r24v2 | fork-joly-os-mmllm-claude-train-sym24-a71d6f82-r24v2 | 3.3670 |
| **mean** | | **3.3310** |
| **best** | | **3.2950** |

## Chain progression R1336 → R1337

Previous harvest: `workers/dispatcher/harvest-1way-r1336_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6172         | 3.3310         | -0.2862 |
| ctrl_bpc best  | 3.6172         | 3.2950         | -0.3222 |

## Per-round trajectory (best bird: BbfAE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1337 | 6600 | 3.2950 | +0.1087 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1336_sym24`

## Output

`workers/dispatcher/harvest-2way-r1337_sym24/round-1337/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

