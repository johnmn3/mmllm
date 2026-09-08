# harvest-1way-r1414 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1414 ctrl_bpc |
|--------|--------|--------------:|
| NtlVL | fork-SeniorCareMarket-mmllm-claude-train-sym24-efc17d7f-NtlVL | 3.2114 |
| **mean** | | **3.2114** |
| **best** | | **3.2114** |

## Chain progression R1413 → R1414

Previous harvest: `workers/dispatcher/harvest-2way-r1413_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5116         | 3.2114         | -0.3002 |
| ctrl_bpc best  | 3.3182         | 3.2114         | -0.1068 |

## Per-round trajectory (best bird: NtlVL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1414 | 6418 | 3.2114 | +0.1599 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1413_sym24`

## Output

`workers/dispatcher/harvest-1way-r1414_sym24/round-1414/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

