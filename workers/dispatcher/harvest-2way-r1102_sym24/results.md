# harvest-2way-r1102 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1102 ctrl_bpc |
|--------|--------|--------------:|
| pkisN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d7ba6ab9-pkisN | 2.3941 |
| eQx7n | fork-slaa-us-mmllm-claude-train-sym24-68a6c7fa-eQx7n | 2.7972 |
| **mean** | | **2.5957** |
| **best** | | **2.3941** |

## Chain progression R1101 → R1102

Previous harvest: `workers/dispatcher/harvest-6way-r1101_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5380         | 2.5957         | +0.0577 |
| ctrl_bpc best  | 2.4013         | 2.3941         | -0.0072 |

## Per-round trajectory (best bird: pkisN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1102 | 6723 | 2.3941 | +0.2444 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1101_sym24`

## Output

`workers/dispatcher/harvest-2way-r1102_sym24/round-1102/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

