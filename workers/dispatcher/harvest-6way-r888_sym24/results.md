# harvest-6way-r888 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R888 ctrl_bpc |
|--------|--------|--------------:|
| RY0uc | fork-SeniorCareMarket-mmllm-claude-train-sym24-8aa5f58c-RY0uc | 2.8096 |
| kpYvJ | origin/claude/train-sym24-4f5fb866-kpYvJ | 2.8457 |
| kkpTp | fork-slaa-us-mmllm-claude-train-sym24-dbe87f9e-kkpTp | 2.9938 |
| RSFEx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8143907c-RSFEx | 3.0029 |
| OyrwL | origin/claude/train-sym24-7b6e1a6b-OyrwL | 3.0079 |
| gfAtC | fork-joly-os-mmllm-claude-train-sym24-2a591554-gfAtC | 3.2096 |
| **mean** | | **2.9783** |
| **best** | | **2.8096** |

## Chain progression R887 → R888

Previous harvest: `workers/dispatcher/harvest-4way-r887_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0667         | 2.9783         | -0.0884 |
| ctrl_bpc best  | 2.8444         | 2.8096         | -0.0348 |

## Per-round trajectory (best bird: RY0uc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 888 | 6369 | 2.8096 | +0.2635 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r887_sym24`

## Output

`workers/dispatcher/harvest-6way-r888_sym24/round-888/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

