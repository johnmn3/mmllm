# harvest-5way-r1249 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1249 ctrl_bpc |
|--------|--------|--------------:|
| U03pm | fork-slaa-us-mmllm-claude-train-sym24-6ce76a16-U03pm | 2.2424 |
| OXcGe | fork-joly-os-mmllm-claude-train-sym24-bf79024b-OXcGe | 2.2475 |
| MD8BY | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6e6caea-MD8BY | 2.2549 |
| LzQOx | origin/claude/train-sym24-6601260f-LzQOx | 2.4413 |
| XQtig | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc6d2664-XQtig | 2.6557 |
| **mean** | | **2.3684** |
| **best** | | **2.2424** |

## Chain progression R1248 → R1249

Previous harvest: `workers/dispatcher/harvest-14way-r1248_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4582         | 2.3684         | -0.0898 |
| ctrl_bpc best  | 2.2415         | 2.2424         | +0.0009 |

## Per-round trajectory (best bird: U03pm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1249 | 4196 | 2.2424 | +0.2514 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1248_sym24`
  - `workers/dispatcher/harvest-8way-r1248_sym24`

## Output

`workers/dispatcher/harvest-5way-r1249_sym24/round-1249/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

