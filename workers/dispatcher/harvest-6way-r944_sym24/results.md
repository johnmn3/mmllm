# harvest-6way-r944 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R944 ctrl_bpc |
|--------|--------|--------------:|
| VuFiB | origin/claude/train-sym24-d4d09028-VuFiB | 2.6655 |
| 7CFG9 | fork-slaa-us-mmllm-claude-train-sym24-19410b56-7CFG9 | 2.6709 |
| aMcHf | origin/claude/train-sym24-5a9cb754-aMcHf | 2.6887 |
| AwtHw | fork-SeniorCareMarket-mmllm-claude-train-sym24-04263967-AwtHw | 2.8685 |
| utyqi | fork-joly-os-mmllm-claude-train-sym24-7b7f6a70-utyqi | 2.8757 |
| DVz1O | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4ff46a2a-DVz1O | 2.8792 |
| **mean** | | **2.7747** |
| **best** | | **2.6655** |

## Chain progression R610 → R944

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.7747         | +0.6375 |
| ctrl_bpc best  | 2.1268         | 2.6655         | +0.5387 |

## Per-round trajectory (best bird: VuFiB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 944 | 6566 | 2.6655 | +0.1905 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r943_sym24`
  - `workers/dispatcher/harvest-3way-r943_sym24`

## Output

`workers/dispatcher/harvest-6way-r944_sym24/round-944/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

