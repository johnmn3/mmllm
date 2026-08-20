# harvest-7way-r1259 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1259 ctrl_bpc |
|--------|--------|--------------:|
| GCIFm | fork-SeniorCareMarket-mmllm-claude-train-sym24-43d0b6d2-GCIFm | 2.2343 |
| S5Toe | origin/claude/train-sym24-82886c6f-S5Toe | 2.2385 |
| oU2uA | fork-joly-os-mmllm-claude-train-sym24-d2abb29e-oU2uA | 2.2543 |
| cf63x | origin/claude/train-sym24-a17337d5-cf63x | 2.4313 |
| BJfpQ | fork-slaa-us-mmllm-claude-train-sym24-2030c19e-BJfpQ | 2.4350 |
| pLHR6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6f9ce77-pLHR6 | 2.4408 |
| PCohz | fork-joly-os-mmllm-claude-train-sym24-022f5331-PCohz | 2.4446 |
| **mean** | | **2.3541** |
| **best** | | **2.2343** |

## Chain progression R1258 → R1259

Previous harvest: `workers/dispatcher/harvest-8way-r1258_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2931         | 2.3541         | +0.0610 |
| ctrl_bpc best  | 2.2323         | 2.2343         | +0.0020 |

## Per-round trajectory (best bird: GCIFm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1259 | 6696 | 2.2343 | +0.2556 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1258_sym24`
  - `workers/dispatcher/harvest-8way-r1258_sym24`

## Output

`workers/dispatcher/harvest-7way-r1259_sym24/round-1259/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

