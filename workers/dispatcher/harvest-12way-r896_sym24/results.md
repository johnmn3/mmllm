# harvest-12way-r896 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R896 ctrl_bpc |
|--------|--------|--------------:|
| ZY4PM | fork-joly-os-mmllm-claude-train-sym24-3f31dc7b-ZY4PM | 2.7845 |
| w7l3W | fork-joly-os-mmllm-claude-train-sym24-d19061a0-w7l3W | 2.8208 |
| U5FUk | origin/claude/train-sym24-aa991072-U5FUk | 2.8230 |
| HulMN | fork-joly-os-mmllm-claude-train-sym24-93f7af40-HulMN | 2.8282 |
| WC69D | fork-slaa-us-mmllm-claude-train-sym24-833bbbfe-WC69D | 2.8317 |
| 9zK8j | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-59586ec1-9zK8j | 2.8317 |
| EdfKL | origin/claude/train-sym24-974f5abe-EdfKL | 2.8390 |
| 1N3lG | origin/claude/train-sym24-725d2acc-1N3lG | 2.9790 |
| efLVH | fork-SeniorCareMarket-mmllm-claude-train-sym24-a44c399a-efLVH | 3.1799 |
| XlUmD | fork-slaa-us-mmllm-claude-train-sym24-40fadf97-XlUmD | 3.1801 |
| NeTNH | fork-slaa-us-mmllm-claude-train-sym24-0d30bc8b-NeTNH | 3.1874 |
| Az6lx | fork-SeniorCareMarket-mmllm-claude-train-sym24-232ff8ce-Az6lx | 3.1943 |
| **mean** | | **2.9566** |
| **best** | | **2.7845** |

## Chain progression R895 → R896

Previous harvest: `workers/dispatcher/harvest-9way-r895_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9106         | 2.9566         | +0.0460 |
| ctrl_bpc best  | 2.7954         | 2.7845         | -0.0109 |

## Per-round trajectory (best bird: ZY4PM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 896 | 6417 | 2.7845 | +0.3218 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r895_sym24`
  - `workers/dispatcher/harvest-5way-r895_sym24`
  - `workers/dispatcher/harvest-9way-r895_sym24`

## Output

`workers/dispatcher/harvest-12way-r896_sym24/round-896/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

