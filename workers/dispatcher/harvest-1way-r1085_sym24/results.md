# harvest-1way-r1085 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1085 ctrl_bpc |
|--------|--------|--------------:|
| TKac7 | fork-joly-os-mmllm-claude-train-sym24-dffa3260-TKac7 | 2.4578 |
| **mean** | | **2.4578** |
| **best** | | **2.4578** |

## Chain progression R1084 → R1085

Previous harvest: `workers/dispatcher/harvest-10way-r1084_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5525         | 2.4578         | -0.0947 |
| ctrl_bpc best  | 2.4276         | 2.4578         | +0.0302 |

## Per-round trajectory (best bird: TKac7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1085 | 6576 | 2.4578 | +0.2238 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1084_sym24`

## Output

`workers/dispatcher/harvest-1way-r1085_sym24/round-1085/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

