# harvest-5way-r1201 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1201 ctrl_bpc |
|--------|--------|--------------:|
| pZxpe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-85c7379b-pZxpe | 2.2929 |
| E7oKc | fork-joly-os-mmllm-claude-train-sym24-29384adc-E7oKc | 2.3021 |
| 5nie1 | fork-slaa-us-mmllm-claude-train-sym24-3ec2b6ea-5nie1 | 2.3220 |
| 1hncw | origin/claude/train-sym24-4925aff1-1hncw | 2.4824 |
| wyhrX | fork-SeniorCareMarket-mmllm-claude-train-sym24-5004591c-wyhrX | 2.6759 |
| **mean** | | **2.4151** |
| **best** | | **2.2929** |

## Chain progression R1200 → R1201

Previous harvest: `workers/dispatcher/harvest-9way-r1200_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3938         | 2.4151         | +0.0213 |
| ctrl_bpc best  | 2.2786         | 2.2929         | +0.0143 |

## Per-round trajectory (best bird: pZxpe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1201 | 6721 | 2.2929 | +0.2361 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1200_sym24`
  - `workers/dispatcher/harvest-6way-r1200_sym24`

## Output

`workers/dispatcher/harvest-5way-r1201_sym24/round-1201/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

