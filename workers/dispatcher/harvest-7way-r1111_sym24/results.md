# harvest-7way-r1111 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1111 ctrl_bpc |
|--------|--------|--------------:|
| 1EzqS | origin/claude/train-sym24-45e43896-1EzqS | 2.3767 |
| BnHgJ | fork-slaa-us-mmllm-claude-train-sym24-9449f6f7-BnHgJ | 2.5802 |
| PgUNT | fork-joly-os-mmllm-claude-train-sym24-23b62890-PgUNT | 2.5847 |
| 64THD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0da4af72-64THD | 2.5852 |
| AxCSi | fork-SeniorCareMarket-mmllm-claude-train-sym24-56a6abcd-AxCSi | 2.5868 |
| KJxuH | origin/claude/train-sym24-0f8f4197-KJxuH | 2.7791 |
| jjwtv | origin/claude/train-sym24-552c0f8a-jjwtv | 2.7925 |
| **mean** | | **2.6122** |
| **best** | | **2.3767** |

## Chain progression R1110 → R1111

Previous harvest: `workers/dispatcher/harvest-6way-r1110_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4961         | 2.6122         | +0.1161 |
| ctrl_bpc best  | 2.3773         | 2.3767         | -0.0006 |

## Per-round trajectory (best bird: 1EzqS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1111 | 6621 | 2.3767 | +0.2451 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1110_sym24`
  - `workers/dispatcher/harvest-6way-r1110_sym24`

## Output

`workers/dispatcher/harvest-7way-r1111_sym24/round-1111/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

