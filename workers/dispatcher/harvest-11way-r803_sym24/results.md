# harvest-11way-r803 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R803 ctrl_bpc |
|--------|--------|--------------:|
| Gloss | origin/claude/train-sym24-8833f098-Gloss | 3.0874 |
| QRCjk | fork-SeniorCareMarket-mmllm-claude-train-sym24-4bd597b3-QRCjk | 3.0881 |
| pRkXh | fork-davidwuchn-mmllm-claude-train-sym24-5e219719-pRkXh | 3.0894 |
| yA9VM | origin/claude/train-sym24-8e0c5a6a-yA9VM | 3.1168 |
| OW31o | fork-slaa-us-mmllm-claude-train-sym24-856b7742-OW31o | 3.1175 |
| TGUbc | fork-davidwuchn-mmllm-claude-train-sym24-439cbaff-TGUbc | 3.1884 |
| sj4Vf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a88ade91-sj4Vf | 3.2148 |
| f8BeR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-24c87309-f8BeR | 3.2329 |
| 0UCn2 | fork-joly-os-mmllm-claude-train-sym24-201f18fc-0UCn2 | 3.4705 |
| CqyDK | fork-slaa-us-mmllm-claude-train-sym24-25a44f5c-CqyDK | 3.4769 |
| GZrfY | fork-joly-os-mmllm-claude-train-sym24-898dc45f-GZrfY | 3.4886 |
| **mean** | | **3.2338** |
| **best** | | **3.0874** |

## Chain progression R802 → R803

Previous harvest: `workers/dispatcher/harvest-8way-r802_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2538         | 3.2338         | -0.0200 |
| ctrl_bpc best  | 3.1114         | 3.0874         | -0.0240 |

## Per-round trajectory (best bird: Gloss)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 803 | 6549 | 3.0874 | +0.4902 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r802_sym24`
  - `workers/dispatcher/harvest-8way-r802_sym24`

## Output

`workers/dispatcher/harvest-11way-r803_sym24/round-803/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

