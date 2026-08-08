# harvest-10way-r1146 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1146 ctrl_bpc |
|--------|--------|--------------:|
| YPH2x | origin/claude/train-sym24-54a71c80-YPH2x | 2.3402 |
| p2j5u | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e23e9f07-p2j5u | 2.3448 |
| lScLN | fork-slaa-us-mmllm-claude-train-sym24-0e8be808-lScLN | 2.3664 |
| DqvTT | fork-SeniorCareMarket-mmllm-claude-train-sym24-cf84f43c-DqvTT | 2.3704 |
| 7Thkf | origin/claude/train-sym24-ead363b3-7Thkf | 2.5330 |
| otLuS | fork-SeniorCareMarket-mmllm-claude-train-sym24-9ecafc50-otLuS | 2.5349 |
| Mrqe5 | fork-joly-os-mmllm-claude-train-sym24-f6221420-Mrqe5 | 2.5418 |
| GsomJ | fork-slaa-us-mmllm-claude-train-sym24-f86b2962-GsomJ | 2.7309 |
| qk2AM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe7b2dea-qk2AM | 2.7408 |
| snrsv | fork-slaa-us-mmllm-claude-train-sym24-3237ba95-snrsv | 2.7434 |
| **mean** | | **2.5247** |
| **best** | | **2.3402** |

## Chain progression R1145 → R1146

Previous harvest: `workers/dispatcher/harvest-16way-r1145_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5223         | 2.5247         | +0.0024 |
| ctrl_bpc best  | 2.3357         | 2.3402         | +0.0045 |

## Per-round trajectory (best bird: YPH2x)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1146 | 6572 | 2.3402 | +0.2533 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1145_sym24`
  - `workers/dispatcher/harvest-6way-r1145_sym24`

## Output

`workers/dispatcher/harvest-10way-r1146_sym24/round-1146/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

