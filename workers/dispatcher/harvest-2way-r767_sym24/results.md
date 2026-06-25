# harvest-2way-r767 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R767 ctrl_bpc |
|--------|--------|--------------:|
| oDTNG | fork-joly-os-mmllm-claude-train-sym24-a7430f76-oDTNG | 3.2381 |
| YUlAP | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9190db4-YUlAP | 3.2874 |
| **mean** | | **3.2628** |
| **best** | | **3.2381** |

## Chain progression R766 → R767

Previous harvest: `workers/dispatcher/harvest-10way-r766_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4375         | 3.2628         | -0.1747 |
| ctrl_bpc best  | 3.2492         | 3.2381         | -0.0111 |

## Per-round trajectory (best bird: oDTNG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 767 | 6472 | 3.2381 | +0.6085 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r766_sym24`

## Output

`workers/dispatcher/harvest-2way-r767_sym24/round-767/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

