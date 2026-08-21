# harvest-11way-r1276 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1276 ctrl_bpc |
|--------|--------|--------------:|
| aCqnr | fork-SeniorCareMarket-mmllm-claude-train-sym24-f6eceb5f-aCqnr | 2.2483 |
| UcMiZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b400f20e-UcMiZ | 2.2517 |
| LW0xK | origin/claude/train-sym24-499db05c-LW0xK | 2.2527 |
| y12r1 | fork-slaa-us-mmllm-claude-train-sym24-c033df7b-y12r1 | 2.2570 |
| 655XV | fork-SeniorCareMarket-mmllm-claude-train-sym24-443c707a-655XV | 2.4186 |
| stHF4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68ef67a2-stHF4 | 2.4209 |
| 9iF1R | origin/claude/train-sym24-ae24696c-9iF1R | 2.4265 |
| YDoD2 | fork-joly-os-mmllm-claude-train-sym24-8e3eeaed-YDoD2 | 2.4277 |
| RabxB | fork-slaa-us-mmllm-claude-train-sym24-2d3f4e4d-RabxB | 2.4285 |
| GThXT | fork-joly-os-mmllm-claude-train-sym24-b836bef8-GThXT | 2.6134 |
| GBAYl | fork-joly-os-mmllm-claude-train-sym24-e73f5771-GBAYl | 2.6219 |
| **mean** | | **2.3970** |
| **best** | | **2.2483** |

## Chain progression R1275 → R1276

Previous harvest: `workers/dispatcher/harvest-5way-r1275_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4190         | 2.3970         | -0.0220 |
| ctrl_bpc best  | 2.2257         | 2.2483         | +0.0226 |

## Per-round trajectory (best bird: aCqnr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1276 | 6323 | 2.2483 | +0.2349 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1275_sym24`
  - `workers/dispatcher/harvest-5way-r1275_sym24`

## Output

`workers/dispatcher/harvest-11way-r1276_sym24/round-1276/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

