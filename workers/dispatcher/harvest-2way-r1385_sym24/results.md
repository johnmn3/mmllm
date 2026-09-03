# harvest-2way-r1385 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1385 ctrl_bpc |
|--------|--------|--------------:|
| yG6sp | origin/claude/train-sym24-027aa4ac-yG6sp | 3.0910 |
| UIO6f | fork-joly-os-mmllm-claude-train-sym24-7f9b01f2-UIO6f | 3.1418 |
| **mean** | | **3.1164** |
| **best** | | **3.0910** |

## Chain progression R1384 → R1385

Previous harvest: `workers/dispatcher/harvest-1way-r1384_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2102         | 3.1164         | -0.0938 |
| ctrl_bpc best  | 3.2102         | 3.0910         | -0.1192 |

## Per-round trajectory (best bird: yG6sp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1385 | 4358 | 3.0910 | +0.1499 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1384_sym24`

## Output

`workers/dispatcher/harvest-2way-r1385_sym24/round-1385/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

