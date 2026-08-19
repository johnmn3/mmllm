# harvest-11way-r1251 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1251 ctrl_bpc |
|--------|--------|--------------:|
| aTL34 | fork-SeniorCareMarket-mmllm-claude-train-sym24-52ac00b6-aTL34 | 2.2391 |
| ZTjMK | origin/claude/train-sym24-5976271c-ZTjMK | 2.2418 |
| WYg88 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d5daecdf-WYg88 | 2.2612 |
| no42h | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c9abe932-no42h | 2.4421 |
| BrQkw | fork-slaa-us-mmllm-claude-train-sym24-ba37e048-BrQkw | 2.4495 |
| BEHpo | fork-slaa-us-mmllm-claude-train-sym24-9612c628-BEHpo | 2.6307 |
| IuTDe | fork-joly-os-mmllm-claude-train-sym24-97938e8b-IuTDe | 2.6367 |
| 2xHWQ | origin/claude/train-sym24-2a5597fb-2xHWQ | 2.6387 |
| 7dNFg | origin/claude/train-sym24-abbd6c2b-7dNFg | 2.6391 |
| KMzTv | fork-joly-os-mmllm-claude-train-sym24-b0cd4e17-KMzTv | 2.6397 |
| 3i5ij | fork-SeniorCareMarket-mmllm-claude-train-sym24-9e942794-3i5ij | 2.6408 |
| **mean** | | **2.4963** |
| **best** | | **2.2391** |

## Chain progression R1250 → R1251

Previous harvest: `workers/dispatcher/harvest-7way-r1250_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4697         | 2.4963         | +0.0266 |
| ctrl_bpc best  | 2.2456         | 2.2391         | -0.0065 |

## Per-round trajectory (best bird: aTL34)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1251 | 5361 | 2.2391 | +0.2538 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1250_sym24`
  - `workers/dispatcher/harvest-7way-r1250_sym24`

## Output

`workers/dispatcher/harvest-11way-r1251_sym24/round-1251/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

