# harvest-6way-r1145 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1145 ctrl_bpc |
|--------|--------|--------------:|
| 9rdnF | fork-joly-os-mmllm-claude-train-sym24-85302f7a-9rdnF | 2.3428 |
| dmiHo | origin/claude/train-sym24-fe37f5d5-dmiHo | 2.3637 |
| etYZ3 | fork-slaa-us-mmllm-claude-train-sym24-28f40175-etYZ3 | 2.5333 |
| fOaW0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ca40ddf9-fOaW0 | 2.7321 |
| FYJOl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-90f584b5-FYJOl | 2.7344 |
| sDKVR | fork-slaa-us-mmllm-claude-train-sym24-91b6b98e-sDKVR | 2.7420 |
| **mean** | | **2.5747** |
| **best** | | **2.3428** |

## Chain progression R1144 → R1145

Previous harvest: `workers/dispatcher/harvest-13way-r1144_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4797         | 2.5747         | +0.0950 |
| ctrl_bpc best  | 2.3381         | 2.3428         | +0.0047 |

## Per-round trajectory (best bird: 9rdnF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1145 | 6515 | 2.3428 | +0.2408 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1144_sym24`
  - `workers/dispatcher/harvest-9way-r1144_sym24`

## Output

`workers/dispatcher/harvest-6way-r1145_sym24/round-1145/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

