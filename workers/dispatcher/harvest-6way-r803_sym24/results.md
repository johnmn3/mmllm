# harvest-6way-r803 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R803 ctrl_bpc |
|--------|--------|--------------:|
| Gloss | origin/claude/train-sym24-8833f098-Gloss | 3.0874 |
| QRCjk | fork-SeniorCareMarket-mmllm-claude-train-sym24-4bd597b3-QRCjk | 3.0881 |
| pRkXh | fork-davidwuchn-mmllm-claude-train-sym24-5e219719-pRkXh | 3.0894 |
| OW31o | fork-slaa-us-mmllm-claude-train-sym24-856b7742-OW31o | 3.1175 |
| sj4Vf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a88ade91-sj4Vf | 3.2148 |
| GZrfY | fork-joly-os-mmllm-claude-train-sym24-898dc45f-GZrfY | 3.4886 |
| **mean** | | **3.1810** |
| **best** | | **3.0874** |

## Chain progression R802 → R803

Previous harvest: `workers/dispatcher/harvest-13way-r802_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2373         | 3.1810         | -0.0563 |
| ctrl_bpc best  | 3.1107         | 3.0874         | -0.0233 |

## Per-round trajectory (best bird: Gloss)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 803 | 6549 | 3.0874 | +0.4902 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r802_sym24`

## Output

`workers/dispatcher/harvest-6way-r803_sym24/round-803/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

