# harvest-5way-r1265 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1265 ctrl_bpc |
|--------|--------|--------------:|
| nxGaB | fork-SeniorCareMarket-mmllm-claude-train-sym24-ae286a0a-nxGaB | 2.2267 |
| fSGt6 | fork-joly-os-mmllm-claude-train-sym24-580efb15-fSGt6 | 2.2406 |
| tSr1j | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e3cbe4a3-tSr1j | 2.2515 |
| ugHQD | fork-slaa-us-mmllm-claude-train-sym24-1e305d84-ugHQD | 2.4316 |
| R7iqR | origin/claude/train-sym24-73b5ed55-R7iqR | 2.6356 |
| **mean** | | **2.3572** |
| **best** | | **2.2267** |

## Chain progression R1264 → R1265

Previous harvest: `workers/dispatcher/harvest-8way-r1264_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3201         | 2.3572         | +0.0371 |
| ctrl_bpc best  | 2.2423         | 2.2267         | -0.0156 |

## Per-round trajectory (best bird: nxGaB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1265 | 6718 | 2.2267 | +0.2456 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1264_sym24`

## Output

`workers/dispatcher/harvest-5way-r1265_sym24/round-1265/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

