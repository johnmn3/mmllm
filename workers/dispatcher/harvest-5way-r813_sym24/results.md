# harvest-5way-r813 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R813 ctrl_bpc |
|--------|--------|--------------:|
| 0lY8U | fork-SeniorCareMarket-mmllm-claude-train-sym24-24fa234d-0lY8U | 3.0582 |
| lR3Ye | fork-joly-os-mmllm-claude-train-sym24-64a0261e-lR3Ye | 3.0667 |
| 8uo5Y | fork-davidwuchn-mmllm-claude-train-sym24-3e5d535d-8uo5Y | 3.0810 |
| YA4N5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-824337f9-YA4N5 | 3.4169 |
| r49gI | fork-slaa-us-mmllm-claude-train-sym24-e46ef798-r49gI | 3.4371 |
| **mean** | | **3.2120** |
| **best** | | **3.0582** |

## Chain progression R812 → R813

Previous harvest: `workers/dispatcher/harvest-20way-r812_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2149         | 3.2120         | -0.0029 |
| ctrl_bpc best  | 3.0552         | 3.0582         | +0.0030 |

## Per-round trajectory (best bird: 0lY8U)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 813 | 6334 | 3.0582 | +0.4330 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-15way-r812_sym24`
  - `workers/dispatcher/harvest-6way-r812_sym24`

## Output

`workers/dispatcher/harvest-5way-r813_sym24/round-813/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

