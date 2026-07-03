# harvest-5way-r836 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R836 ctrl_bpc |
|--------|--------|--------------:|
| ADZD0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6b1f802-ADZD0 | 2.9654 |
| 3Sh4q | fork-slaa-us-mmllm-claude-train-sym24-e58743de-3Sh4q | 2.9780 |
| 2wiWn | fork-joly-os-mmllm-claude-train-sym24-fffe446b-2wiWn | 2.9838 |
| YX4pR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a4a30b50-YX4pR | 3.1299 |
| ezHff | origin/claude/train-sym24-ed806dad-ezHff | 3.1487 |
| **mean** | | **3.0412** |
| **best** | | **2.9654** |

## Chain progression R835 → R836

Previous harvest: `workers/dispatcher/harvest-4way-r835_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1169         | 3.0412         | -0.0757 |
| ctrl_bpc best  | 2.9673         | 2.9654         | -0.0019 |

## Per-round trajectory (best bird: ADZD0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 836 | 6288 | 2.9654 | +0.4321 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r835_sym24`

## Output

`workers/dispatcher/harvest-5way-r836_sym24/round-836/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

