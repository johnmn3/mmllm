# harvest-3way-r1072 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1072 ctrl_bpc |
|--------|--------|--------------:|
| DsPJ5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a9d8ddad-DsPJ5 | 2.4406 |
| hnWnW | fork-SeniorCareMarket-mmllm-claude-train-sym24-9b7c38ae-hnWnW | 2.4693 |
| MFdvv | origin/claude/train-sym24-33e2a8f2-MFdvv | 2.6309 |
| **mean** | | **2.5136** |
| **best** | | **2.4406** |

## Chain progression R1071 → R1072

Previous harvest: `workers/dispatcher/harvest-3way-r1071_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5702         | 2.5136         | -0.0566 |
| ctrl_bpc best  | 2.4404         | 2.4406         | +0.0002 |

## Per-round trajectory (best bird: DsPJ5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1072 | 6811 | 2.4406 | +0.2294 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1071_sym24`

## Output

`workers/dispatcher/harvest-3way-r1072_sym24/round-1072/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

