# harvest-6way-r1407 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1407 ctrl_bpc |
|--------|--------|--------------:|
| MhRvK | fork-joly-os-mmllm-claude-train-sym24-97fb8abb-MhRvK | 3.2006 |
| HDRIp | origin/claude/train-sym24-871f85ec-HDRIp | 3.2180 |
| Xjpsr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-85edbe8d-Xjpsr | 3.3280 |
| br5Cl | fork-SeniorCareMarket-mmllm-claude-train-sym24-63e5cd21-br5Cl | 3.3550 |
| Qi6m4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-354ab9b5-Qi6m4 | 3.5304 |
| f7dTJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dd351127-f7dTJ | 3.6191 |
| **mean** | | **3.3752** |
| **best** | | **3.2006** |

## Chain progression R1406 → R1407

Previous harvest: `workers/dispatcher/harvest-4way-r1406_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3332         | 3.3752         | +0.0420 |
| ctrl_bpc best  | 3.2151         | 3.2006         | -0.0145 |

## Per-round trajectory (best bird: MhRvK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1407 | 6241 | 3.2006 | +0.1084 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1406_sym24`
  - `workers/dispatcher/harvest-4way-r1406_sym24`

## Output

`workers/dispatcher/harvest-6way-r1407_sym24/round-1407/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

