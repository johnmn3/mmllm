# harvest-5way-r1002 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1002 ctrl_bpc |
|--------|--------|--------------:|
| iDvLl | fork-slaa-us-mmllm-claude-train-sym24-8dbcf429-iDvLl | 2.5607 |
| 6VGas | fork-joly-os-mmllm-claude-train-sym24-c7d2cf73-6VGas | 2.5743 |
| YOMgS | origin/claude/train-sym24-920edfb4-YOMgS | 2.7366 |
| OfeuA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f1372b4-OfeuA | 2.7398 |
| zbd5u | fork-SeniorCareMarket-mmllm-claude-train-sym24-209a96de-zbd5u | 2.9446 |
| **mean** | | **2.7112** |
| **best** | | **2.5607** |

## Chain progression R1001 → R1002

Previous harvest: `workers/dispatcher/harvest-6way-r1001_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7599         | 2.7112         | -0.0487 |
| ctrl_bpc best  | 2.5630         | 2.5607         | -0.0023 |

## Per-round trajectory (best bird: iDvLl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1002 | 6358 | 2.5607 | +0.1680 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1001_sym24`
  - `workers/dispatcher/harvest-6way-r1001_sym24`

## Output

`workers/dispatcher/harvest-5way-r1002_sym24/round-1002/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

