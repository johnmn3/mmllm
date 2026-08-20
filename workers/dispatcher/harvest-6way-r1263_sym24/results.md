# harvest-6way-r1263 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1263 ctrl_bpc |
|--------|--------|--------------:|
| UsSWm | fork-SeniorCareMarket-mmllm-claude-train-sym24-94599a75-UsSWm | 2.2288 |
| 0N2M4 | fork-joly-os-mmllm-claude-train-sym24-15c8212f-0N2M4 | 2.2299 |
| NUYW3 | fork-slaa-us-mmllm-claude-train-sym24-bf2e15ae-NUYW3 | 2.4337 |
| ttDP9 | origin/claude/train-sym24-d6e485e7-ttDP9 | 2.4338 |
| jwmH7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-37856e33-jwmH7 | 2.6260 |
| Smp3m | origin/claude/train-sym24-436d6582-Smp3m | 2.6297 |
| **mean** | | **2.4303** |
| **best** | | **2.2288** |

## Chain progression R1262 → R1263

Previous harvest: `workers/dispatcher/harvest-6way-r1262_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2994         | 2.4303         | +0.1309 |
| ctrl_bpc best  | 2.2318         | 2.2288         | -0.0030 |

## Per-round trajectory (best bird: UsSWm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1263 | 6558 | 2.2288 | +0.2558 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1262_sym24`

## Output

`workers/dispatcher/harvest-6way-r1263_sym24/round-1263/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

