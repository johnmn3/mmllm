# harvest-12way-r1284 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R1284 ctrl_bpc |
|--------|--------|--------------:|
| EwJVr | fork-slaa-us-mmllm-claude-train-sym24-7a7e80d7-EwJVr | 2.2154 |
| KFxM7 | fork-joly-os-mmllm-claude-train-sym24-7c639866-KFxM7 | 2.2170 |
| EDI3t | fork-joly-os-mmllm-claude-train-sym24-21cd078c-EDI3t | 2.2177 |
| G306T | fork-SeniorCareMarket-mmllm-claude-train-sym24-9a1e7f79-G306T | 2.2214 |
| 7qiAb | origin/claude/train-sym24-384bbfe0-7qiAb | 2.2378 |
| mrM39 | fork-slaa-us-mmllm-claude-train-sym24-451fb64e-mrM39 | 2.2416 |
| MEdMh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a7de9afc-MEdMh | 2.4111 |
| WT7A0 | fork-joly-os-mmllm-claude-train-sym24-9354c3bb-WT7A0 | 2.4153 |
| mepId | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-df7dd809-mepId | 2.4170 |
| Y3ZGt | fork-slaa-us-mmllm-claude-train-sym24-ec928fdc-Y3ZGt | 2.4180 |
| EuoYN | fork-SeniorCareMarket-mmllm-claude-train-sym24-391d8eaf-EuoYN | 2.4213 |
| Okql4 | origin/claude/train-sym24-5395ab17-Okql4 | 2.6077 |
| **mean** | | **2.3368** |
| **best** | | **2.2154** |

## Chain progression R1283 → R1284

Previous harvest: `workers/dispatcher/harvest-7way-r1283_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3355         | 2.3368         | +0.0013 |
| ctrl_bpc best  | 2.2156         | 2.2154         | -0.0002 |

## Per-round trajectory (best bird: EwJVr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1284 | 5324 | 2.2154 | +0.2448 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1283_sym24`
  - `workers/dispatcher/harvest-7way-r1283_sym24`

## Output

`workers/dispatcher/harvest-12way-r1284_sym24/round-1284/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

