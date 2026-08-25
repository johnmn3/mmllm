# harvest-1way-r1322 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1322 ctrl_bpc |
|--------|--------|--------------:|
| qqnDx | fork-joly-os-mmllm-claude-train-sym24-159d151b-qqnDx | 3.4565 |
| **mean** | | **3.4565** |
| **best** | | **3.4565** |

## Chain progression R1321 → R1322

Previous harvest: `workers/dispatcher/harvest-5way-r1321_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4374         | 3.4565         | +0.0191 |
| ctrl_bpc best  | 3.3979         | 3.4565         | +0.0586 |

## Per-round trajectory (best bird: qqnDx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1322 | 3710 | 3.4565 | +0.0607 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1321_sym24`

## Output

`workers/dispatcher/harvest-1way-r1322_sym24/round-1322/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

