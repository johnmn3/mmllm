# harvest-6way-r1269 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1269 ctrl_bpc |
|--------|--------|--------------:|
| LiNlO | fork-joly-os-mmllm-claude-train-sym24-ec803cfd-LiNlO | 2.2426 |
| sxyac | fork-SeniorCareMarket-mmllm-claude-train-sym24-e7761a54-sxyac | 2.2428 |
| fSkue | fork-joly-os-mmllm-claude-train-sym24-87606a35-fSkue | 2.2486 |
| B7XD1 | origin/claude/train-sym24-4f444b1c-B7XD1 | 2.4203 |
| tXXP1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6022ef5d-tXXP1 | 2.4226 |
| 0lbEa | fork-slaa-us-mmllm-claude-train-sym24-0f66a8d2-0lbEa | 2.6192 |
| **mean** | | **2.3660** |
| **best** | | **2.2426** |

## Chain progression R1268 → R1269

Previous harvest: `workers/dispatcher/harvest-6way-r1268_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4263         | 2.3660         | -0.0603 |
| ctrl_bpc best  | 2.2296         | 2.2426         | +0.0130 |

## Per-round trajectory (best bird: LiNlO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1269 | 6723 | 2.2426 | +0.2410 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1268_sym24`
  - `workers/dispatcher/harvest-6way-r1268_sym24`

## Output

`workers/dispatcher/harvest-6way-r1269_sym24/round-1269/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

