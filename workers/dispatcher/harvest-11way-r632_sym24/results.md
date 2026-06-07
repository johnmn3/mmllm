# harvest-11way-r632 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R632 ctrl_bpc |
|--------|--------|--------------:|
| WhpTw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-83b5d2f2-WhpTw | 2.1131 |
| nliRw | fork-joly-os-mmllm-claude-train-sym24-311e66e8-nliRw | 2.1133 |
| tbY6X | fork-davidwuchn-mmllm-claude-train-sym24-137cfcaa-tbY6X | 2.1179 |
| lDNEV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a08c447b-lDNEV | 2.1306 |
| UpHrm | fork-slaa-us-mmllm-claude-train-sym24-fe28b47f-UpHrm | 2.1307 |
| Bx72g | fork-SeniorCareMarket-mmllm-claude-train-sym24-9a842680-Bx72g | 2.1337 |
| R1XYh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1c128bc3-R1XYh | 2.1342 |
| 5KGYH | fork-davidwuchn-mmllm-claude-train-sym24-dca11b81-5KGYH | 2.3295 |
| 3ZGEw | fork-joly-os-mmllm-claude-train-sym24-cb94ee60-3ZGEw | 2.3314 |
| j5a9j | fork-slaa-us-mmllm-claude-train-sym24-02e1a03b-j5a9j | 2.3326 |
| s42iF | fork-slaa-us-mmllm-claude-train-sym24-ca1418bd-s42iF | 2.5836 |
| **mean** | | **2.2228** |
| **best** | | **2.1131** |

## Chain progression R610 → R632

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.2228         | +0.0856 |
| ctrl_bpc best  | 2.1268         | 2.1131         | -0.0137 |

## Per-round trajectory (best bird: WhpTw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 632 | 5164 | 2.1131 | +0.0539 |

## Cumulative training contribution

- This harvest: **550 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **550 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r631_sym24`

## Output

`workers/dispatcher/harvest-11way-r632_sym24/round-632/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

