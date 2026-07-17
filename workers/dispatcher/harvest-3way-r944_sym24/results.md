# harvest-3way-r944 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R944 ctrl_bpc |
|--------|--------|--------------:|
| VuFiB | origin/claude/train-sym24-d4d09028-VuFiB | 2.6655 |
| utyqi | fork-joly-os-mmllm-claude-train-sym24-7b7f6a70-utyqi | 2.8757 |
| DVz1O | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4ff46a2a-DVz1O | 2.8792 |
| **mean** | | **2.8068** |
| **best** | | **2.6655** |

## Chain progression R943 → R944

Previous harvest: `workers/dispatcher/harvest-3way-r943_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8284         | 2.8068         | -0.0216 |
| ctrl_bpc best  | 2.6902         | 2.6655         | -0.0247 |

## Per-round trajectory (best bird: VuFiB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 944 | 6566 | 2.6655 | +0.1905 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r943_sym24`
  - `workers/dispatcher/harvest-3way-r943_sym24`

## Output

`workers/dispatcher/harvest-3way-r944_sym24/round-944/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

