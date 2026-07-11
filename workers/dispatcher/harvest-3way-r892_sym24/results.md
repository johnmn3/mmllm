# harvest-3way-r892 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R892 ctrl_bpc |
|--------|--------|--------------:|
| xtOCE | fork-SeniorCareMarket-mmllm-claude-train-sym24-c0b5162a-xtOCE | 3.1832 |
| k86uI | origin/claude/train-sym24-f42bb67f-k86uI | 3.1847 |
| ZKRGX | fork-joly-os-mmllm-claude-train-sym24-1c4f6d4a-ZKRGX | 3.1876 |
| **mean** | | **3.1852** |
| **best** | | **3.1832** |

## Chain progression R891 → R892

Previous harvest: `workers/dispatcher/harvest-3way-r891_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9523         | 3.1852         | +0.2329 |
| ctrl_bpc best  | 2.8174         | 3.1832         | +0.3658 |

## Per-round trajectory (best bird: xtOCE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 892 | 6535 | 3.1832 | +0.3018 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r891_sym24`

## Output

`workers/dispatcher/harvest-3way-r892_sym24/round-892/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

