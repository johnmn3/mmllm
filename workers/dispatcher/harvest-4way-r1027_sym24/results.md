# harvest-4way-r1027 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1027 ctrl_bpc |
|--------|--------|--------------:|
| n4ngp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-04aa4c85-n4ngp | 2.5032 |
| hTfQW | origin/claude/train-sym24-a23a5bd8-hTfQW | 2.5037 |
| dEBkY | fork-slaa-us-mmllm-claude-train-sym24-663ea4c4-dEBkY | 2.7035 |
| oigVL | fork-SeniorCareMarket-mmllm-claude-train-sym24-a7c5518d-oigVL | 2.7058 |
| **mean** | | **2.6040** |
| **best** | | **2.5032** |

## Chain progression R1026 → R1027

Previous harvest: `workers/dispatcher/harvest-1way-r1026_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5105         | 2.6040         | +0.0936 |
| ctrl_bpc best  | 2.5105         | 2.5032         | -0.0073 |

## Per-round trajectory (best bird: n4ngp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1027 | 5357 | 2.5032 | +0.1837 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1026_sym24`

## Output

`workers/dispatcher/harvest-4way-r1027_sym24/round-1027/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

