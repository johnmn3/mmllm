# harvest-3way-r644 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R644 ctrl_bpc |
|--------|--------|--------------:|
| tZwGH | fork-davidwuchn-mmllm-claude-train-sym24-e33ce37a-tZwGH | 4.5335 |
| cb7mI | fork-joly-os-mmllm-claude-train-sym24-0886cbc0-cb7mI | 4.5374 |
| RS2zA | fork-slaa-us-mmllm-claude-train-sym24-8cb77f4e-RS2zA | 4.5414 |
| **mean** | | **4.5374** |
| **best** | | **4.5335** |

## Chain progression R643 → R644

Previous harvest: `workers/dispatcher/harvest-11way-r643_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.7135         | 4.5374         | -0.1761 |
| ctrl_bpc best  | 4.5742         | 4.5335         | -0.0407 |

## Per-round trajectory (best bird: tZwGH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 644 | 6288 | 4.5335 | +0.0426 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r643_sym24`

## Output

`workers/dispatcher/harvest-3way-r644_sym24/round-644/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

