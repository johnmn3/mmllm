# harvest-5way-r1012 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1012 ctrl_bpc |
|--------|--------|--------------:|
| 7FhfN | origin/claude/train-sym24-00491636-7FhfN | 2.5317 |
| Ajanr | fork-SeniorCareMarket-mmllm-claude-train-sym24-effcd105-Ajanr | 2.5503 |
| fBkYJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-93ac48e5-fBkYJ | 2.5601 |
| F01Os | origin/claude/train-sym24-0d8061bf-F01Os | 2.6357 |
| lsjiV | fork-slaa-us-mmllm-claude-train-sym24-8006fd81-lsjiV | 2.7217 |
| **mean** | | **2.5999** |
| **best** | | **2.5317** |

## Chain progression R1011 → R1012

Previous harvest: `workers/dispatcher/harvest-8way-r1011_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6384         | 2.5999         | -0.0385 |
| ctrl_bpc best  | 2.5378         | 2.5317         | -0.0061 |

## Per-round trajectory (best bird: 7FhfN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1012 | 6606 | 2.5317 | +0.1761 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1011_sym24`
  - `workers/dispatcher/harvest-7way-r1011_sym24`

## Output

`workers/dispatcher/harvest-5way-r1012_sym24/round-1012/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

