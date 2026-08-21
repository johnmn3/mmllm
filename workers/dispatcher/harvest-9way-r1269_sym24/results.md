# harvest-9way-r1269 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1269 ctrl_bpc |
|--------|--------|--------------:|
| LiNlO | fork-joly-os-mmllm-claude-train-sym24-ec803cfd-LiNlO | 2.2426 |
| sxyac | fork-SeniorCareMarket-mmllm-claude-train-sym24-e7761a54-sxyac | 2.2428 |
| fSkue | fork-joly-os-mmllm-claude-train-sym24-87606a35-fSkue | 2.2486 |
| B7XD1 | origin/claude/train-sym24-4f444b1c-B7XD1 | 2.4203 |
| tXXP1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6022ef5d-tXXP1 | 2.4226 |
| JE9mH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-738b5d27-JE9mH | 2.4247 |
| 0lbEa | fork-slaa-us-mmllm-claude-train-sym24-0f66a8d2-0lbEa | 2.6192 |
| t5EAk | fork-slaa-us-mmllm-claude-train-sym24-6dd27f5d-t5EAk | 2.6218 |
| BhldL | fork-SeniorCareMarket-mmllm-claude-train-sym24-ed4aff60-BhldL | 2.6252 |
| **mean** | | **2.4298** |
| **best** | | **2.2426** |

## Chain progression R1268 → R1269

Previous harvest: `workers/dispatcher/harvest-6way-r1268_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4263         | 2.4298         | +0.0035 |
| ctrl_bpc best  | 2.2296         | 2.2426         | +0.0130 |

## Per-round trajectory (best bird: LiNlO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1269 | 6723 | 2.2426 | +0.2410 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1268_sym24`
  - `workers/dispatcher/harvest-6way-r1268_sym24`

## Output

`workers/dispatcher/harvest-9way-r1269_sym24/round-1269/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

