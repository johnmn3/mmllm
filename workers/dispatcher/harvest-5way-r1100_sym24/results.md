# harvest-5way-r1100 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1100 ctrl_bpc |
|--------|--------|--------------:|
| PflfR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-03528719-PflfR | 2.3944 |
| dG3w8 | origin/claude/train-sym24-4386c381-dG3w8 | 2.3981 |
| 6F2gu | origin/claude/train-sym24-e7cb87ee-6F2gu | 2.4005 |
| Rwbmk | fork-joly-os-mmllm-claude-train-sym24-a3700bd4-Rwbmk | 2.4276 |
| 1VmYj | fork-SeniorCareMarket-mmllm-claude-train-sym24-f4d5a5ed-1VmYj | 2.7895 |
| **mean** | | **2.4820** |
| **best** | | **2.3944** |

## Chain progression R1099 → R1100

Previous harvest: `workers/dispatcher/harvest-3way-r1099_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4805         | 2.4820         | +0.0015 |
| ctrl_bpc best  | 2.4171         | 2.3944         | -0.0227 |

## Per-round trajectory (best bird: PflfR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1100 | 6509 | 2.3944 | +0.2340 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1099_sym24`
  - `workers/dispatcher/harvest-3way-r1099_sym24`

## Output

`workers/dispatcher/harvest-5way-r1100_sym24/round-1100/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

