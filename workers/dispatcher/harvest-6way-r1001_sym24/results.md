# harvest-6way-r1001 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1001 ctrl_bpc |
|--------|--------|--------------:|
| ANpBt | fork-SeniorCareMarket-mmllm-claude-train-sym24-5db10f78-ANpBt | 2.5630 |
| zqyDJ | origin/claude/train-sym24-a5cc39bc-zqyDJ | 2.5713 |
| uEHVI | fork-joly-os-mmllm-claude-train-sym24-047de7ec-uEHVI | 2.5798 |
| UbTp4 | origin/claude/train-sym24-69e50580-UbTp4 | 2.9453 |
| 5DWu3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bfbc8f93-5DWu3 | 2.9496 |
| jyM2i | fork-slaa-us-mmllm-claude-train-sym24-500bc7d0-jyM2i | 2.9507 |
| **mean** | | **2.7599** |
| **best** | | **2.5630** |

## Chain progression R1000 → R1001

Previous harvest: `workers/dispatcher/harvest-5way-r1000_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7252         | 2.7599         | +0.0347 |
| ctrl_bpc best  | 2.5585         | 2.5630         | +0.0045 |

## Per-round trajectory (best bird: ANpBt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1001 | 6268 | 2.5630 | +0.1866 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1000_sym24`
  - `workers/dispatcher/harvest-5way-r1000_sym24`

## Output

`workers/dispatcher/harvest-6way-r1001_sym24/round-1001/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

