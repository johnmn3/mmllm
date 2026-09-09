# harvest-8way-r1418 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1418 ctrl_bpc |
|--------|--------|--------------:|
| QDQ3i | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-475f02c8-QDQ3i | 3.1174 |
| geACe | fork-SeniorCareMarket-mmllm-claude-train-sym24-50c79242-geACe | 3.1378 |
| ZdbZV | origin/claude/train-sym24-3e455cb5-ZdbZV | 3.1467 |
| jNK08 | fork-joly-os-mmllm-claude-train-sym24-e2014e5b-jNK08 | 3.1639 |
| UHTHG | fork-joly-os-mmllm-claude-train-sym24-67c40e4d-UHTHG | 3.1985 |
| jcErN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7ec45ab-jcErN | 3.2710 |
| Mty2W | origin/claude/train-sym24-1cf0efa7-Mty2W | 3.4814 |
| VCnIt | fork-SeniorCareMarket-mmllm-claude-train-sym24-2153b7c1-VCnIt | 3.5525 |
| **mean** | | **3.2587** |
| **best** | | **3.1174** |

## Chain progression R1417 → R1418

Previous harvest: `workers/dispatcher/harvest-4way-r1417_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1753         | 3.2587         | +0.0834 |
| ctrl_bpc best  | 3.1065         | 3.1174         | +0.0109 |

## Per-round trajectory (best bird: QDQ3i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1418 | 6537 | 3.1174 | +0.1437 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1417_sym24`
  - `workers/dispatcher/harvest-4way-r1417_sym24`

## Output

`workers/dispatcher/harvest-8way-r1418_sym24/round-1418/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

