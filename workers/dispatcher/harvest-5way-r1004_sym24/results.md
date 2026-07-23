# harvest-5way-r1004 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1004 ctrl_bpc |
|--------|--------|--------------:|
| hsCGF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-da570f2f-hsCGF | 2.5704 |
| rrs2b | fork-joly-os-mmllm-claude-train-sym24-92ddac87-rrs2b | 2.7376 |
| OOejO | fork-slaa-us-mmllm-claude-train-sym24-862f6200-OOejO | 2.9363 |
| E6lTY | origin/claude/train-sym24-8af5a548-E6lTY | 2.9385 |
| q4fIe | fork-SeniorCareMarket-mmllm-claude-train-sym24-eb912253-q4fIe | 2.9517 |
| **mean** | | **2.8269** |
| **best** | | **2.5704** |

## Chain progression R1003 → R1004

Previous harvest: `workers/dispatcher/harvest-8way-r1003_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7355         | 2.8269         | +0.0914 |
| ctrl_bpc best  | 2.5522         | 2.5704         | +0.0182 |

## Per-round trajectory (best bird: hsCGF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1004 | 6431 | 2.5704 | +0.1549 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1003_sym24`

## Output

`workers/dispatcher/harvest-5way-r1004_sym24/round-1004/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

