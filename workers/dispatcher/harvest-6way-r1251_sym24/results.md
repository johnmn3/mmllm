# harvest-6way-r1251 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1251 ctrl_bpc |
|--------|--------|--------------:|
| aTL34 | fork-SeniorCareMarket-mmllm-claude-train-sym24-52ac00b6-aTL34 | 2.2391 |
| WYg88 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d5daecdf-WYg88 | 2.2612 |
| BrQkw | fork-slaa-us-mmllm-claude-train-sym24-ba37e048-BrQkw | 2.4495 |
| 2xHWQ | origin/claude/train-sym24-2a5597fb-2xHWQ | 2.6387 |
| 7dNFg | origin/claude/train-sym24-abbd6c2b-7dNFg | 2.6391 |
| KMzTv | fork-joly-os-mmllm-claude-train-sym24-b0cd4e17-KMzTv | 2.6397 |
| **mean** | | **2.4779** |
| **best** | | **2.2391** |

## Chain progression R1250 → R1251

Previous harvest: `workers/dispatcher/harvest-7way-r1250_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4697         | 2.4779         | +0.0082 |
| ctrl_bpc best  | 2.2456         | 2.2391         | -0.0065 |

## Per-round trajectory (best bird: aTL34)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1251 | 5361 | 2.2391 | +0.2538 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1250_sym24`

## Output

`workers/dispatcher/harvest-6way-r1251_sym24/round-1251/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

