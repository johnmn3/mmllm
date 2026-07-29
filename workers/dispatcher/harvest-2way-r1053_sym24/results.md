# harvest-2way-r1053 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1053 ctrl_bpc |
|--------|--------|--------------:|
| QvMoI | origin/claude/train-sym24-1ef95df8-QvMoI | 2.8597 |
| ANppI | fork-joly-os-mmllm-claude-train-sym24-fbd9d332-ANppI | 2.8618 |
| **mean** | | **2.8608** |
| **best** | | **2.8597** |

## Chain progression R1052 → R1053

Previous harvest: `workers/dispatcher/harvest-6way-r1052_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6833         | 2.8608         | +0.1775 |
| ctrl_bpc best  | 2.4646         | 2.8597         | +0.3951 |

## Per-round trajectory (best bird: QvMoI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1053 | 6597 | 2.8597 | +0.1979 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1052_sym24`

## Output

`workers/dispatcher/harvest-2way-r1053_sym24/round-1053/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

