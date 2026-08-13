# harvest-11way-r1191 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1191 ctrl_bpc |
|--------|--------|--------------:|
| YIjmo | fork-slaa-us-mmllm-claude-train-sym24-51edd137-YIjmo | 2.2894 |
| nfRnb | origin/claude/train-sym24-2aed4ce7-nfRnb | 2.3015 |
| TiE19 | origin/claude/train-sym24-ffc2aaab-TiE19 | 2.3077 |
| w4CBh | origin/claude/train-sym24-551462cb-w4CBh | 2.4864 |
| yANRB | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fda58e-yANRB | 2.4911 |
| HtgyP | origin/claude/train-sym24-3e4af9e8-HtgyP | 2.4921 |
| knZfV | fork-joly-os-mmllm-claude-train-sym24-35475cf3-knZfV | 2.4951 |
| grpwJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-ba07bd53-grpwJ | 2.5014 |
| dtERI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-36ea4a1d-dtERI | 2.6772 |
| r2Hx6 | fork-slaa-us-mmllm-claude-train-sym24-3360166f-r2Hx6 | 2.6847 |
| Nf7nj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27e3ff20-Nf7nj | 2.6916 |
| **mean** | | **2.4926** |
| **best** | | **2.2894** |

## Chain progression R1190 → R1191

Previous harvest: `workers/dispatcher/harvest-1way-r1190_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2908         | 2.4926         | +0.2018 |
| ctrl_bpc best  | 2.2908         | 2.2894         | -0.0014 |

## Per-round trajectory (best bird: YIjmo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1191 | 6356 | 2.2894 | +0.2546 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1190_sym24`

## Output

`workers/dispatcher/harvest-11way-r1191_sym24/round-1191/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

