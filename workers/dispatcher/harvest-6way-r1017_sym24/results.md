# harvest-6way-r1017 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1017 ctrl_bpc |
|--------|--------|--------------:|
| nmI3J | origin/claude/train-sym24-f2f1fad8-nmI3J | 2.5254 |
| 9WDnU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c7dd98ef-9WDnU | 2.5260 |
| NrYJB | fork-joly-os-mmllm-claude-train-sym24-4b758bc4-NrYJB | 2.5461 |
| HnchH | fork-SeniorCareMarket-mmllm-claude-train-sym24-6f53fb85-HnchH | 2.5483 |
| UPg0w | origin/claude/train-sym24-2992c2ce-UPg0w | 2.5522 |
| YUGND | fork-slaa-us-mmllm-claude-train-sym24-aab4b1d8-YUGND | 2.9047 |
| **mean** | | **2.6004** |
| **best** | | **2.5254** |

## Chain progression R1016 → R1017

Previous harvest: `workers/dispatcher/harvest-9way-r1016_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6777         | 2.6004         | -0.0773 |
| ctrl_bpc best  | 2.5242         | 2.5254         | +0.0012 |

## Per-round trajectory (best bird: nmI3J)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1017 | 6687 | 2.5254 | +0.1694 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1016_sym24`
  - `workers/dispatcher/harvest-8way-r1016_sym24`
  - `workers/dispatcher/harvest-9way-r1016_sym24`

## Output

`workers/dispatcher/harvest-6way-r1017_sym24/round-1017/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

