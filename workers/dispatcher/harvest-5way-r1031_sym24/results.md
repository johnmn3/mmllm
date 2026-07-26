# harvest-5way-r1031 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1031 ctrl_bpc |
|--------|--------|--------------:|
| FsBGF | fork-SeniorCareMarket-mmllm-claude-train-sym24-aeefcaa2-FsBGF | 2.4946 |
| qJj1H | origin/claude/train-sym24-b4516a0a-qJj1H | 2.4981 |
| v1UTC | fork-slaa-us-mmllm-claude-train-sym24-d5686eee-v1UTC | 2.5075 |
| NpqFl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95c69427-NpqFl | 2.5119 |
| M2BBU | fork-joly-os-mmllm-claude-train-sym24-ed0845d7-M2BBU | 2.7025 |
| **mean** | | **2.5429** |
| **best** | | **2.4946** |

## Chain progression R1030 → R1031

Previous harvest: `workers/dispatcher/harvest-6way-r1030_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8657         | 2.5429         | -0.3228 |
| ctrl_bpc best  | 2.7134         | 2.4946         | -0.2188 |

## Per-round trajectory (best bird: FsBGF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1031 | 6575 | 2.4946 | +0.1884 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1030_sym24`
  - `workers/dispatcher/harvest-6way-r1030_sym24`

## Output

`workers/dispatcher/harvest-5way-r1031_sym24/round-1031/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

