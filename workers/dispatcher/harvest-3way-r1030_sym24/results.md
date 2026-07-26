# harvest-3way-r1030 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1030 ctrl_bpc |
|--------|--------|--------------:|
| AMnQB | fork-SeniorCareMarket-mmllm-claude-train-sym24-81db6857-AMnQB | 2.8950 |
| zyzDx | fork-joly-os-mmllm-claude-train-sym24-ac433cc0-zyzDx | 2.8989 |
| fZ6X9 | origin/claude/train-sym24-1160bc4f-fZ6X9 | 2.9050 |
| **mean** | | **2.8996** |
| **best** | | **2.8950** |

## Chain progression R1029 → R1030

Previous harvest: `workers/dispatcher/harvest-10way-r1029_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7078         | 2.8996         | +0.1918 |
| ctrl_bpc best  | 2.5083         | 2.8950         | +0.3867 |

## Per-round trajectory (best bird: AMnQB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1030 | 6740 | 2.8950 | +0.1666 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1029_sym24`

## Output

`workers/dispatcher/harvest-3way-r1030_sym24/round-1030/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

