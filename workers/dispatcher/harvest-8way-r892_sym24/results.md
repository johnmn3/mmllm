# harvest-8way-r892 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R892 ctrl_bpc |
|--------|--------|--------------:|
| s5tOj | fork-joly-os-mmllm-claude-train-sym24-5135102c-s5tOj | 2.8053 |
| 95f3b | origin/claude/train-sym24-b1f259db-95f3b | 2.8278 |
| b9er8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d44179d8-b9er8 | 2.8377 |
| R1og0 | origin/claude/train-sym24-c261ae58-R1og0 | 2.9842 |
| p0wWW | fork-slaa-us-mmllm-claude-train-sym24-54263276-p0wWW | 2.9898 |
| xtOCE | fork-SeniorCareMarket-mmllm-claude-train-sym24-c0b5162a-xtOCE | 3.1832 |
| k86uI | origin/claude/train-sym24-f42bb67f-k86uI | 3.1847 |
| ZKRGX | fork-joly-os-mmllm-claude-train-sym24-1c4f6d4a-ZKRGX | 3.1876 |
| **mean** | | **3.0000** |
| **best** | | **2.8053** |

## Chain progression R891 → R892

Previous harvest: `workers/dispatcher/harvest-3way-r891_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9523         | 3.0000         | +0.0477 |
| ctrl_bpc best  | 2.8174         | 2.8053         | -0.0121 |

## Per-round trajectory (best bird: s5tOj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 892 | 6312 | 2.8053 | +0.3257 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r891_sym24`
  - `workers/dispatcher/harvest-2way-r891_sym24`
  - `workers/dispatcher/harvest-3way-r891_sym24`

## Output

`workers/dispatcher/harvest-8way-r892_sym24/round-892/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

