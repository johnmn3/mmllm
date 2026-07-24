# harvest-8way-r1011 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1011 ctrl_bpc |
|--------|--------|--------------:|
| 9Qckv | origin/claude/train-sym24-7cae2b7c-9Qckv | 2.5378 |
| WfKp3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3c82d442-WfKp3 | 2.5557 |
| Re9Az | origin/claude/train-sym24-71ec90d7-Re9Az | 2.5596 |
| OOMGU | origin/claude/train-sym24-f479c473-OOMGU | 2.5630 |
| 9JeRx | fork-slaa-us-mmllm-claude-train-sym24-99e14188-9JeRx | 2.5642 |
| QKDzS | fork-joly-os-mmllm-claude-train-sym24-a5273038-QKDzS | 2.5643 |
| NbfWS | origin/claude/train-sym24-eed39fa1-NbfWS | 2.7636 |
| PMl35 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-023cd74b-PMl35 | 2.9991 |
| **mean** | | **2.6384** |
| **best** | | **2.5378** |

## Chain progression R1010 → R1011

Previous harvest: `workers/dispatcher/harvest-5way-r1010_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7164         | 2.6384         | -0.0780 |
| ctrl_bpc best  | 2.5728         | 2.5378         | -0.0350 |

## Per-round trajectory (best bird: 9Qckv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1011 | 6653 | 2.5378 | +0.1817 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1010_sym24`
  - `workers/dispatcher/harvest-5way-r1010_sym24`

## Output

`workers/dispatcher/harvest-8way-r1011_sym24/round-1011/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

