# harvest-3way-r629 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R629 ctrl_bpc |
|--------|--------|--------------:|
| 5iTdS | fork-slaa-us-mmllm-claude-train-sym24-1b6e0d00-5iTdS | 2.3368 |
| GipBj | fork-davidwuchn-mmllm-claude-train-sym24-e2943a0d-GipBj | 2.5796 |
| khUx8 | fork-joly-os-mmllm-claude-train-sym24-12f44447-khUx8 | 2.5885 |
| **mean** | | **2.5016** |
| **best** | | **2.3368** |

## Chain progression R628 → R629

Previous harvest: `workers/dispatcher/harvest-5way-r628_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1654         | 2.5016         | +0.3362 |
| ctrl_bpc best  | 2.1174         | 2.3368         | +0.2194 |

## Per-round trajectory (best bird: 5iTdS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 629 | 5343 | 2.3368 | +0.0432 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1050 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r628_sym24`

## Output

`workers/dispatcher/harvest-3way-r629_sym24/round-629/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

