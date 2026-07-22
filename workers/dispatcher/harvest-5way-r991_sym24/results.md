# harvest-5way-r991 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R991 ctrl_bpc |
|--------|--------|--------------:|
| 3Gc0i | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-565c99a6-3Gc0i | 2.5847 |
| t7VOI | origin/claude/train-sym24-be391c96-t7VOI | 2.7666 |
| 9hmHe | fork-joly-os-mmllm-claude-train-sym24-48c52338-9hmHe | 2.7677 |
| fh5Q7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e1752984-fh5Q7 | 2.7778 |
| 9FYYa | fork-slaa-us-mmllm-claude-train-sym24-c7ce80cc-9FYYa | 2.7836 |
| **mean** | | **2.7361** |
| **best** | | **2.5847** |

## Chain progression R990 → R991

Previous harvest: `workers/dispatcher/harvest-6way-r990_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6573         | 2.7361         | +0.0788 |
| ctrl_bpc best  | 2.5818         | 2.5847         | +0.0029 |

## Per-round trajectory (best bird: 3Gc0i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 991 | 6363 | 2.5847 | +0.1555 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r990_sym24`
  - `workers/dispatcher/harvest-4way-r990_sym24`
  - `workers/dispatcher/harvest-6way-r990_sym24`

## Output

`workers/dispatcher/harvest-5way-r991_sym24/round-991/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

