# harvest-3way-r1312 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1312 ctrl_bpc |
|--------|--------|--------------:|
| Gx1ZT | fork-slaa-us-mmllm-claude-train-sym24-da805b57-Gx1ZT | 3.5189 |
| 6s9Ka | origin/claude/train-sym24-8602cfdd-6s9Ka | 3.5348 |
| xFqZW | fork-joly-os-mmllm-claude-train-sym24-23e0a0f3-xFqZW | 3.5365 |
| **mean** | | **3.5301** |
| **best** | | **3.5189** |

## Chain progression R1311 → R1312

Previous harvest: `workers/dispatcher/harvest-8way-r1311_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5868         | 3.5301         | -0.0567 |
| ctrl_bpc best  | 3.4361         | 3.5189         | +0.0828 |

## Per-round trajectory (best bird: Gx1ZT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1312 | 6426 | 3.5189 | +0.0390 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1311_sym24`

## Output

`workers/dispatcher/harvest-3way-r1312_sym24/round-1312/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

