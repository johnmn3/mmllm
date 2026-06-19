# harvest-6way-r715 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R715 ctrl_bpc |
|--------|--------|--------------:|
| drleb | fork-slaa-us-mmllm-claude-train-sym24-738c2c00-drleb | 3.5700 |
| g3WGf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c59e94da-g3WGf | 3.8635 |
| GT5H3 | fork-davidwuchn-mmllm-claude-train-sym24-c6cceef9-GT5H3 | 3.8679 |
| npI3p | origin/claude/train-sym24-87c334e5-npI3p | 3.8708 |
| BMNuk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f46120da-BMNuk | 3.8713 |
| aLn5d | fork-joly-os-mmllm-claude-train-sym24-82e41e6e-aLn5d | 3.8732 |
| **mean** | | **3.8194** |
| **best** | | **3.5700** |

## Chain progression R714 → R715

Previous harvest: `workers/dispatcher/harvest-10way-r714_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5706         | 3.8194         | +0.2488 |
| ctrl_bpc best  | 3.5379         | 3.5700         | +0.0321 |

## Per-round trajectory (best bird: drleb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 715 | 6692 | 3.5700 | +0.8475 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r714_sym24`
  - `workers/dispatcher/harvest-3way-r714_sym24`

## Output

`workers/dispatcher/harvest-6way-r715_sym24/round-715/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

