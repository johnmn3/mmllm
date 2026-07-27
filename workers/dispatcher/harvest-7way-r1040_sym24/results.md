# harvest-7way-r1040 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1040 ctrl_bpc |
|--------|--------|--------------:|
| 3WYn0 | origin/claude/train-sym24-9356795b-3WYn0 | 2.5029 |
| dok2N | fork-slaa-us-mmllm-claude-train-sym24-1be32fb2-dok2N | 2.5088 |
| 8omjO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a59e008f-8omjO | 2.5098 |
| sTVEU | fork-joly-os-mmllm-claude-train-sym24-0a5dcecf-sTVEU | 2.5249 |
| UdEve | fork-SeniorCareMarket-mmllm-claude-train-sym24-4c06dae9-UdEve | 2.6826 |
| yYYEO | origin/claude/train-sym24-d748577c-yYYEO | 2.6959 |
| hTyRJ | fork-joly-os-mmllm-claude-train-sym24-5f73fca8-hTyRJ | 2.8746 |
| **mean** | | **2.6142** |
| **best** | | **2.5029** |

## Chain progression R1039 → R1040

Previous harvest: `workers/dispatcher/harvest-5way-r1039_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5471         | 2.6142         | +0.0671 |
| ctrl_bpc best  | 2.4825         | 2.5029         | +0.0204 |

## Per-round trajectory (best bird: 3WYn0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1040 | 6533 | 2.5029 | +0.2019 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1039_sym24`
  - `workers/dispatcher/harvest-5way-r1039_sym24`

## Output

`workers/dispatcher/harvest-7way-r1040_sym24/round-1040/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

