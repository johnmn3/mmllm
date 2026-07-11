# harvest-4way-r896 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R896 ctrl_bpc |
|--------|--------|--------------:|
| HulMN | fork-joly-os-mmllm-claude-train-sym24-93f7af40-HulMN | 2.8282 |
| WC69D | fork-slaa-us-mmllm-claude-train-sym24-833bbbfe-WC69D | 2.8317 |
| EdfKL | origin/claude/train-sym24-974f5abe-EdfKL | 2.8390 |
| Az6lx | fork-SeniorCareMarket-mmllm-claude-train-sym24-232ff8ce-Az6lx | 3.1943 |
| **mean** | | **2.9233** |
| **best** | | **2.8282** |

## Chain progression R895 → R896

Previous harvest: `workers/dispatcher/harvest-12way-r895_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9473         | 2.9233         | -0.0240 |
| ctrl_bpc best  | 2.7892         | 2.8282         | +0.0390 |

## Per-round trajectory (best bird: HulMN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 896 | 6461 | 2.8282 | +0.1218 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r895_sym24`

## Output

`workers/dispatcher/harvest-4way-r896_sym24/round-896/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

