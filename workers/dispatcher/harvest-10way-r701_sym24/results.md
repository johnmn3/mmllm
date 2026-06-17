# harvest-10way-r701 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R701 ctrl_bpc |
|--------|--------|--------------:|
| pFG80 | origin/claude/train-sym24-a337aabf-pFG80 | 3.6070 |
| lc6Ia | fork-joly-os-mmllm-claude-train-sym24-896df9e4-lc6Ia | 3.6128 |
| oj8Qa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a898ed42-oj8Qa | 3.6541 |
| ZDLc8 | origin/claude/train-sym24-ef1c0dde-ZDLc8 | 3.6569 |
| VrRFw | fork-davidwuchn-mmllm-claude-train-sym24-5325dd15-VrRFw | 3.6824 |
| UidfG | fork-davidwuchn-mmllm-claude-train-sym24-e28bcc54-UidfG | 3.9601 |
| z8Lej | fork-SeniorCareMarket-mmllm-claude-train-sym24-aa012092-z8Lej | 3.9637 |
| MEJ7w | fork-joly-os-mmllm-claude-train-sym24-b5a5efd7-MEJ7w | 3.9825 |
| fvlVC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ba159d80-fvlVC | 3.9839 |
| j8PBC | fork-slaa-us-mmllm-claude-train-sym24-e3009edb-j8PBC | 3.9869 |
| **mean** | | **3.8090** |
| **best** | | **3.6070** |

## Chain progression R700 → R701

Previous harvest: `workers/dispatcher/harvest-6way-r700_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7717         | 3.8090         | +0.0373 |
| ctrl_bpc best  | 3.6314         | 3.6070         | -0.0244 |

## Per-round trajectory (best bird: pFG80)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 701 | 6654 | 3.6070 | +0.7694 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r700_sym24`
  - `workers/dispatcher/harvest-6way-r700_sym24`

## Output

`workers/dispatcher/harvest-10way-r701_sym24/round-701/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

