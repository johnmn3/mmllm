# harvest-5way-r1259 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1259 ctrl_bpc |
|--------|--------|--------------:|
| S5Toe | origin/claude/train-sym24-82886c6f-S5Toe | 2.2385 |
| cf63x | origin/claude/train-sym24-a17337d5-cf63x | 2.4313 |
| BJfpQ | fork-slaa-us-mmllm-claude-train-sym24-2030c19e-BJfpQ | 2.4350 |
| pLHR6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6f9ce77-pLHR6 | 2.4408 |
| PCohz | fork-joly-os-mmllm-claude-train-sym24-022f5331-PCohz | 2.4446 |
| **mean** | | **2.3980** |
| **best** | | **2.2385** |

## Chain progression R1258 → R1259

Previous harvest: `workers/dispatcher/harvest-8way-r1258_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2931         | 2.3980         | +0.1049 |
| ctrl_bpc best  | 2.2323         | 2.2385         | +0.0062 |

## Per-round trajectory (best bird: S5Toe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1259 | 4250 | 2.2385 | +0.2701 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1258_sym24`

## Output

`workers/dispatcher/harvest-5way-r1259_sym24/round-1259/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

