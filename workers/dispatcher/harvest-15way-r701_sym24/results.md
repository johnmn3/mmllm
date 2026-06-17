# harvest-15way-r701 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R701 ctrl_bpc |
|--------|--------|--------------:|
| VGEcw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d7530412-VGEcw | 3.6058 |
| pFG80 | origin/claude/train-sym24-a337aabf-pFG80 | 3.6070 |
| lc6Ia | fork-joly-os-mmllm-claude-train-sym24-896df9e4-lc6Ia | 3.6128 |
| asyRl | fork-davidwuchn-mmllm-claude-train-sym24-1f340167-asyRl | 3.6247 |
| oj8Qa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a898ed42-oj8Qa | 3.6541 |
| ZDLc8 | origin/claude/train-sym24-ef1c0dde-ZDLc8 | 3.6569 |
| Psusl | fork-slaa-us-mmllm-claude-train-sym24-7c045284-Psusl | 3.6598 |
| RIJO2 | fork-joly-os-mmllm-claude-train-sym24-b859542a-RIJO2 | 3.6600 |
| WSx5S | fork-joly-os-mmllm-claude-train-sym24-6ddcad76-WSx5S | 3.6708 |
| VrRFw | fork-davidwuchn-mmllm-claude-train-sym24-5325dd15-VrRFw | 3.6824 |
| UidfG | fork-davidwuchn-mmllm-claude-train-sym24-e28bcc54-UidfG | 3.9601 |
| z8Lej | fork-SeniorCareMarket-mmllm-claude-train-sym24-aa012092-z8Lej | 3.9637 |
| MEJ7w | fork-joly-os-mmllm-claude-train-sym24-b5a5efd7-MEJ7w | 3.9825 |
| fvlVC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ba159d80-fvlVC | 3.9839 |
| j8PBC | fork-slaa-us-mmllm-claude-train-sym24-e3009edb-j8PBC | 3.9869 |
| **mean** | | **3.7541** |
| **best** | | **3.6058** |

## Chain progression R700 → R701

Previous harvest: `workers/dispatcher/harvest-6way-r700_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7717         | 3.7541         | -0.0176 |
| ctrl_bpc best  | 3.6314         | 3.6058         | -0.0256 |

## Per-round trajectory (best bird: VGEcw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 701 | 6673 | 3.6058 | +0.6785 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r700_sym24`
  - `workers/dispatcher/harvest-4way-r700_sym24`
  - `workers/dispatcher/harvest-6way-r700_sym24`

## Output

`workers/dispatcher/harvest-15way-r701_sym24/round-701/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

