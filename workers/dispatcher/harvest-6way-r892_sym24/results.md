# harvest-6way-r892 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R892 ctrl_bpc |
|--------|--------|--------------:|
| b9er8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d44179d8-b9er8 | 2.8377 |
| R1og0 | origin/claude/train-sym24-c261ae58-R1og0 | 2.9842 |
| p0wWW | fork-slaa-us-mmllm-claude-train-sym24-54263276-p0wWW | 2.9898 |
| xtOCE | fork-SeniorCareMarket-mmllm-claude-train-sym24-c0b5162a-xtOCE | 3.1832 |
| k86uI | origin/claude/train-sym24-f42bb67f-k86uI | 3.1847 |
| ZKRGX | fork-joly-os-mmllm-claude-train-sym24-1c4f6d4a-ZKRGX | 3.1876 |
| **mean** | | **3.0612** |
| **best** | | **2.8377** |

## Chain progression R891 → R892

Previous harvest: `workers/dispatcher/harvest-3way-r891_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9523         | 3.0612         | +0.1089 |
| ctrl_bpc best  | 2.8174         | 2.8377         | +0.0203 |

## Per-round trajectory (best bird: b9er8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 892 | 4120 | 2.8377 | +0.2453 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r891_sym24`
  - `workers/dispatcher/harvest-2way-r891_sym24`
  - `workers/dispatcher/harvest-3way-r891_sym24`

## Output

`workers/dispatcher/harvest-6way-r892_sym24/round-892/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

