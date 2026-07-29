# harvest-5way-r1060 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1060 ctrl_bpc |
|--------|--------|--------------:|
| 9bFRr | origin/claude/train-sym24-c520240a-9bFRr | 2.4603 |
| rKeS1 | fork-joly-os-mmllm-claude-train-sym24-4afbe2c0-rKeS1 | 2.5564 |
| mZpsN | fork-SeniorCareMarket-mmllm-claude-train-sym24-591b4255-mZpsN | 2.6443 |
| oUMl9 | origin/claude/train-sym24-0ea2abd4-oUMl9 | 2.6458 |
| mh4QB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e69178af-mh4QB | 2.6490 |
| **mean** | | **2.5912** |
| **best** | | **2.4603** |

## Chain progression R1059 → R1060

Previous harvest: `workers/dispatcher/harvest-5way-r1059_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5504         | 2.5912         | +0.0408 |
| ctrl_bpc best  | 2.4619         | 2.4603         | -0.0016 |

## Per-round trajectory (best bird: 9bFRr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1060 | 6401 | 2.4603 | +0.2097 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1059_sym24`

## Output

`workers/dispatcher/harvest-5way-r1060_sym24/round-1060/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

