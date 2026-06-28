# harvest-5way-r792 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R792 ctrl_bpc |
|--------|--------|--------------:|
| b5zbH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c2c75ac4-b5zbH | 3.1350 |
| SHOC6 | fork-joly-os-mmllm-claude-train-sym24-123d40dc-SHOC6 | 3.1395 |
| h5P1K | fork-davidwuchn-mmllm-claude-train-sym24-b6d876ef-h5P1K | 3.2664 |
| lHdqc | fork-slaa-us-mmllm-claude-train-sym24-a8281424-lHdqc | 3.2699 |
| WKM6i | origin/claude/train-sym24-d92b4bc2-WKM6i | 3.5321 |
| **mean** | | **3.2686** |
| **best** | | **3.1350** |

## Chain progression R791 → R792

Previous harvest: `workers/dispatcher/harvest-12way-r791_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2349         | 3.2686         | +0.0337 |
| ctrl_bpc best  | 3.1162         | 3.1350         | +0.0188 |

## Per-round trajectory (best bird: b5zbH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 792 | 6630 | 3.1350 | +0.6186 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r791_sym24`
  - `workers/dispatcher/harvest-5way-r791_sym24`

## Output

`workers/dispatcher/harvest-5way-r792_sym24/round-792/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

