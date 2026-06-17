# harvest-10way-r699 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R699 ctrl_bpc |
|--------|--------|--------------:|
| st0WW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0e0b3b74-st0WW | 3.6203 |
| PZWVq | fork-SeniorCareMarket-mmllm-claude-train-sym24-27fb1ec7-PZWVq | 3.6251 |
| FrDvW | fork-slaa-us-mmllm-claude-train-sym24-caf30bfb-FrDvW | 3.6713 |
| RW35w | origin/claude/train-sym24-967783da-RW35w | 3.6745 |
| fSTmm | fork-davidwuchn-mmllm-claude-train-sym24-b7734822-fSTmm | 3.6829 |
| Hbo13 | fork-joly-os-mmllm-claude-train-sym24-5ec7fd25-Hbo13 | 3.6886 |
| yjLm7 | fork-slaa-us-mmllm-claude-train-sym24-6f81f11f-yjLm7 | 3.9678 |
| Qdqp9 | origin/claude/train-sym24-f408aeab-Qdqp9 | 3.9682 |
| 1W3A1 | fork-joly-os-mmllm-claude-train-sym24-c75e2b72-1W3A1 | 3.9782 |
| xKsy3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4ecbfe7d-xKsy3 | 3.9889 |
| **mean** | | **3.7866** |
| **best** | | **3.6203** |

## Chain progression R698 → R699

Previous harvest: `workers/dispatcher/harvest-6way-r698_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8357         | 3.7866         | -0.0491 |
| ctrl_bpc best  | 3.6856         | 3.6203         | -0.0653 |

## Per-round trajectory (best bird: st0WW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 699 | 6670 | 3.6203 | +0.6347 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r698_sym24`
  - `workers/dispatcher/harvest-6way-r698_sym24`

## Output

`workers/dispatcher/harvest-10way-r699_sym24/round-699/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

