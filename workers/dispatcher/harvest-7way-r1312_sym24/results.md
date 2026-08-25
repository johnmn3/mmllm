# harvest-7way-r1312 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1312 ctrl_bpc |
|--------|--------|--------------:|
| WBgX7 | fork-joly-os-mmllm-claude-train-sym24-257f2a14-WBgX7 | 3.4164 |
| 2x5j5 | origin/claude/train-sym24-4bcaa68d-2x5j5 | 3.4964 |
| Gx1ZT | fork-slaa-us-mmllm-claude-train-sym24-da805b57-Gx1ZT | 3.5189 |
| 6s9Ka | origin/claude/train-sym24-8602cfdd-6s9Ka | 3.5348 |
| xFqZW | fork-joly-os-mmllm-claude-train-sym24-23e0a0f3-xFqZW | 3.5365 |
| Howbg | fork-SeniorCareMarket-mmllm-claude-train-sym24-c595c17a-Howbg | 3.5398 |
| q4n8s | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e4257d9f-q4n8s | 3.5444 |
| **mean** | | **3.5125** |
| **best** | | **3.4164** |

## Chain progression R1311 → R1312

Previous harvest: `workers/dispatcher/harvest-8way-r1311_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5868         | 3.5125         | -0.0743 |
| ctrl_bpc best  | 3.4361         | 3.4164         | -0.0197 |

## Per-round trajectory (best bird: WBgX7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1312 | 6236 | 3.4164 | +0.0483 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1311_sym24`
  - `workers/dispatcher/harvest-8way-r1311_sym24`

## Output

`workers/dispatcher/harvest-7way-r1312_sym24/round-1312/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

