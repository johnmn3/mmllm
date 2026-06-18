# harvest-4way-r703 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R703 ctrl_bpc |
|--------|--------|--------------:|
| VO8On | fork-davidwuchn-mmllm-claude-train-sym24-5b472cdb-VO8On | 3.5916 |
| 96Pyd | fork-joly-os-mmllm-claude-train-sym24-776188b3-96Pyd | 3.6528 |
| meR2g | fork-slaa-us-mmllm-claude-train-sym24-e9e1416f-meR2g | 3.6567 |
| OhEy8 | fork-joly-os-mmllm-claude-train-sym24-f6f4a10d-OhEy8 | 3.9574 |
| **mean** | | **3.7146** |
| **best** | | **3.5916** |

## Chain progression R702 → R703

Previous harvest: `workers/dispatcher/harvest-15way-r702_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7474         | 3.7146         | -0.0328 |
| ctrl_bpc best  | 3.6065         | 3.5916         | -0.0149 |

## Per-round trajectory (best bird: VO8On)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 703 | 6598 | 3.5916 | +0.6748 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r702_sym24`
  - `workers/dispatcher/harvest-8way-r702_sym24`

## Output

`workers/dispatcher/harvest-4way-r703_sym24/round-703/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

