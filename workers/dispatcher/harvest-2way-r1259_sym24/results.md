# harvest-2way-r1259 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1259 ctrl_bpc |
|--------|--------|--------------:|
| cf63x | origin/claude/train-sym24-a17337d5-cf63x | 2.4313 |
| PCohz | fork-joly-os-mmllm-claude-train-sym24-022f5331-PCohz | 2.4446 |
| **mean** | | **2.4379** |
| **best** | | **2.4313** |

## Chain progression R1258 → R1259

Previous harvest: `workers/dispatcher/harvest-8way-r1258_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2931         | 2.4379         | +0.1448 |
| ctrl_bpc best  | 2.2323         | 2.4313         | +0.1990 |

## Per-round trajectory (best bird: cf63x)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1259 | 4381 | 2.4313 | +0.2342 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1258_sym24`

## Output

`workers/dispatcher/harvest-2way-r1259_sym24/round-1259/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

