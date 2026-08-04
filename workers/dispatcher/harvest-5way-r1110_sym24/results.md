# harvest-5way-r1110 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1110 ctrl_bpc |
|--------|--------|--------------:|
| S9KJg | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a38e69f-S9KJg | 2.3773 |
| dm9Sn | fork-slaa-us-mmllm-claude-train-sym24-3b0f25a1-dm9Sn | 2.3828 |
| kcpml | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-16f6e862-kcpml | 2.3983 |
| c0s8d | fork-joly-os-mmllm-claude-train-sym24-0a1550a1-c0s8d | 2.4138 |
| mrmAn | origin/claude/train-sym24-969927ed-mrmAn | 2.5936 |
| **mean** | | **2.4332** |
| **best** | | **2.3773** |

## Chain progression R1109 → R1110

Previous harvest: `workers/dispatcher/harvest-5way-r1109_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4786         | 2.4332         | -0.0454 |
| ctrl_bpc best  | 2.4030         | 2.3773         | -0.0257 |

## Per-round trajectory (best bird: S9KJg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1110 | 3638 | 2.3773 | +0.2414 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1109_sym24`
  - `workers/dispatcher/harvest-3way-r1109_sym24`
  - `workers/dispatcher/harvest-5way-r1109_sym24`

## Output

`workers/dispatcher/harvest-5way-r1110_sym24/round-1110/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

