# harvest-8way-r792 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R792 ctrl_bpc |
|--------|--------|--------------:|
| b5zbH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c2c75ac4-b5zbH | 3.1350 |
| SHOC6 | fork-joly-os-mmllm-claude-train-sym24-123d40dc-SHOC6 | 3.1395 |
| i2paT | fork-slaa-us-mmllm-claude-train-sym24-26b115b6-i2paT | 3.1461 |
| XKqrT | fork-joly-os-mmllm-claude-train-sym24-17be0a80-XKqrT | 3.1820 |
| h5P1K | fork-davidwuchn-mmllm-claude-train-sym24-b6d876ef-h5P1K | 3.2664 |
| vxkAd | fork-davidwuchn-mmllm-claude-train-sym24-cc78a123-vxkAd | 3.2698 |
| lHdqc | fork-slaa-us-mmllm-claude-train-sym24-a8281424-lHdqc | 3.2699 |
| WKM6i | origin/claude/train-sym24-d92b4bc2-WKM6i | 3.5321 |
| **mean** | | **3.2426** |
| **best** | | **3.1350** |

## Chain progression R791 → R792

Previous harvest: `workers/dispatcher/harvest-5way-r791_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2362         | 3.2426         | +0.0064 |
| ctrl_bpc best  | 3.1802         | 3.1350         | -0.0452 |

## Per-round trajectory (best bird: b5zbH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 792 | 6630 | 3.1350 | +0.6186 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r791_sym24`
  - `workers/dispatcher/harvest-5way-r791_sym24`

## Output

`workers/dispatcher/harvest-8way-r792_sym24/round-792/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

