# harvest-5way-r1049 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1049 ctrl_bpc |
|--------|--------|--------------:|
| V9TU8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-39c2fabf-V9TU8 | 2.4705 |
| e2akY | origin/claude/train-sym24-b14ef3e6-e2akY | 2.5101 |
| YeDek | origin/claude/train-sym24-0f3d9804-YeDek | 2.6688 |
| bVN6I | fork-slaa-us-mmllm-claude-train-sym24-98759897-bVN6I | 2.7009 |
| WRTeK | fork-SeniorCareMarket-mmllm-claude-train-sym24-7f627775-WRTeK | 2.8614 |
| **mean** | | **2.6423** |
| **best** | | **2.4705** |

## Chain progression R1048 → R1049

Previous harvest: `workers/dispatcher/harvest-4way-r1048_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7717         | 2.6423         | -0.1294 |
| ctrl_bpc best  | 2.5021         | 2.4705         | -0.0316 |

## Per-round trajectory (best bird: V9TU8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1049 | 6580 | 2.4705 | +0.2271 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1048_sym24`
  - `workers/dispatcher/harvest-4way-r1048_sym24`

## Output

`workers/dispatcher/harvest-5way-r1049_sym24/round-1049/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

