# harvest-1way-r1073 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1073 ctrl_bpc |
|--------|--------|--------------:|
| HsMr3 | fork-slaa-us-mmllm-claude-train-sym24-eb47626f-HsMr3 | 2.6377 |
| **mean** | | **2.6377** |
| **best** | | **2.6377** |

## Chain progression R1072 → R1073

Previous harvest: `workers/dispatcher/harvest-3way-r1072_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5136         | 2.6377         | +0.1241 |
| ctrl_bpc best  | 2.4406         | 2.6377         | +0.1971 |

## Per-round trajectory (best bird: HsMr3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1073 | 3735 | 2.6377 | +0.2025 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1072_sym24`

## Output

`workers/dispatcher/harvest-1way-r1073_sym24/round-1073/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

