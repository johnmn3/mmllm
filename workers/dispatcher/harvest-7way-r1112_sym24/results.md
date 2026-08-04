# harvest-7way-r1112 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1112 ctrl_bpc |
|--------|--------|--------------:|
| 4VrID | origin/claude/train-sym24-a00ec442-4VrID | 2.3729 |
| 6LZbt | fork-slaa-us-mmllm-claude-train-sym24-fc1b03de-6LZbt | 2.3913 |
| C5fuC | fork-joly-os-mmllm-claude-train-sym24-faa52fdb-C5fuC | 2.3980 |
| 6Fbvj | origin/claude/train-sym24-ec51753d-6Fbvj | 2.5738 |
| gyhC0 | fork-joly-os-mmllm-claude-train-sym24-902a0d90-gyhC0 | 2.5776 |
| uNrOF | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc35b598-uNrOF | 2.5778 |
| oLjuz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0599c6b2-oLjuz | 2.7856 |
| **mean** | | **2.5253** |
| **best** | | **2.3729** |

## Chain progression R1111 → R1112

Previous harvest: `workers/dispatcher/harvest-7way-r1111_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6122         | 2.5253         | -0.0869 |
| ctrl_bpc best  | 2.3767         | 2.3729         | -0.0038 |

## Per-round trajectory (best bird: 4VrID)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1112 | 6711 | 2.3729 | +0.2488 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1111_sym24`
  - `workers/dispatcher/harvest-4way-r1111_sym24`
  - `workers/dispatcher/harvest-7way-r1111_sym24`

## Output

`workers/dispatcher/harvest-7way-r1112_sym24/round-1112/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

