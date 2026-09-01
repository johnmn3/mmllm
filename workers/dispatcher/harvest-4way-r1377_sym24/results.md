# harvest-4way-r1377 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1377 ctrl_bpc |
|--------|--------|--------------:|
| dPTp6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-97cbc5e4-dPTp6 | 3.0703 |
| dc0v3 | fork-joly-os-mmllm-claude-train-sym24-6349cb7c-dc0v3 | 3.2407 |
| p95bp | origin/claude/train-sym24-1cb977dc-p95bp | 3.4927 |
| OSaqk | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6b325ab-OSaqk | 3.4997 |
| **mean** | | **3.3258** |
| **best** | | **3.0703** |

## Chain progression R1376 → R1377

Previous harvest: `workers/dispatcher/harvest-1way-r1376_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2101         | 3.3258         | +0.1157 |
| ctrl_bpc best  | 3.2101         | 3.0703         | -0.1398 |

## Per-round trajectory (best bird: dPTp6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1377 | 6665 | 3.0703 | +0.1083 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1376_sym24`

## Output

`workers/dispatcher/harvest-4way-r1377_sym24/round-1377/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

