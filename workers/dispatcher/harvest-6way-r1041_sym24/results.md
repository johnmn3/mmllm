# harvest-6way-r1041 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1041 ctrl_bpc |
|--------|--------|--------------:|
| dn766 | fork-slaa-us-mmllm-claude-train-sym24-f5da513d-dn766 | 2.4803 |
| 4CXMd | fork-joly-os-mmllm-claude-train-sym24-d7baaa66-4CXMd | 2.5046 |
| uhwyw | fork-slaa-us-mmllm-claude-train-sym24-4e064d77-uhwyw | 2.5117 |
| aTdM2 | origin/claude/train-sym24-b4519bcc-aTdM2 | 2.5137 |
| obn5a | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6ef0d6a-obn5a | 2.8730 |
| a4dsw | fork-SeniorCareMarket-mmllm-claude-train-sym24-974be485-a4dsw | 2.8766 |
| **mean** | | **2.6266** |
| **best** | | **2.4803** |

## Chain progression R1040 → R1041

Previous harvest: `workers/dispatcher/harvest-7way-r1040_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6142         | 2.6266         | +0.0124 |
| ctrl_bpc best  | 2.5029         | 2.4803         | -0.0226 |

## Per-round trajectory (best bird: dn766)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1041 | 7003 | 2.4803 | +0.2258 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1040_sym24`
  - `workers/dispatcher/harvest-6way-r1040_sym24`

## Output

`workers/dispatcher/harvest-6way-r1041_sym24/round-1041/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

