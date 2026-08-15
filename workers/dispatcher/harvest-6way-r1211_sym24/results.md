# harvest-6way-r1211 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1211 ctrl_bpc |
|--------|--------|--------------:|
| tPeor | fork-joly-os-mmllm-claude-train-sym24-5ff321e5-tPeor | 2.2716 |
| ZqROy | fork-slaa-us-mmllm-claude-train-sym24-30b91ff1-ZqROy | 2.2744 |
| SuCGp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a9dbcbbf-SuCGp | 2.4627 |
| aYtKJ | fork-slaa-us-mmllm-claude-train-sym24-7af7825a-aYtKJ | 2.4644 |
| DTH9V | fork-SeniorCareMarket-mmllm-claude-train-sym24-5be4f6de-DTH9V | 2.4692 |
| 89n0c | origin/claude/train-sym24-d1cdb74e-89n0c | 2.4693 |
| **mean** | | **2.4019** |
| **best** | | **2.2716** |

## Chain progression R1210 → R1211

Previous harvest: `workers/dispatcher/harvest-10way-r1210_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4646         | 2.4019         | -0.0627 |
| ctrl_bpc best  | 2.2869         | 2.2716         | -0.0153 |

## Per-round trajectory (best bird: tPeor)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1211 | 6701 | 2.2716 | +0.2647 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1210_sym24`
  - `workers/dispatcher/harvest-7way-r1210_sym24`

## Output

`workers/dispatcher/harvest-6way-r1211_sym24/round-1211/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

