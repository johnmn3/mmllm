# harvest-3way-r1201 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1201 ctrl_bpc |
|--------|--------|--------------:|
| pZxpe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-85c7379b-pZxpe | 2.2929 |
| 5nie1 | fork-slaa-us-mmllm-claude-train-sym24-3ec2b6ea-5nie1 | 2.3220 |
| wyhrX | fork-SeniorCareMarket-mmllm-claude-train-sym24-5004591c-wyhrX | 2.6759 |
| **mean** | | **2.4303** |
| **best** | | **2.2929** |

## Chain progression R1200 → R1201

Previous harvest: `workers/dispatcher/harvest-9way-r1200_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3938         | 2.4303         | +0.0365 |
| ctrl_bpc best  | 2.2786         | 2.2929         | +0.0143 |

## Per-round trajectory (best bird: pZxpe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1201 | 6721 | 2.2929 | +0.2361 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1200_sym24`

## Output

`workers/dispatcher/harvest-3way-r1201_sym24/round-1201/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

