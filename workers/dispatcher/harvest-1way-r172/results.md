# harvest-1way-r172 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R172 ctrl_bpc |
|--------|--------|--------------:|
| hWtoB | fork-davidwuchn-mmllm-claude-train-9756c954-hWtoB | 1.1676 |
| **mean** | | **1.1676** |
| **best** | | **1.1676** |

## Chain progression R169 → R172

Previous harvest: `workers/dispatcher/harvest-1way-r169`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1415         | 1.1676         | +0.0261 |
| ctrl_bpc best  | 1.1415         | 1.1676         | +0.0261 |

## Per-round trajectory (best bird: hWtoB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 168 | 620 | 1.1334 | -0.0020 |
| 169 | 551 | 1.1415 | -0.0019 |
| 170 | 545 | 1.1305 | +0.0006 |
| 171 | 507 | 1.1575 | +0.0006 |
| 172 | 541 | 1.1676 | +0.0053 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3551 steps** from 97 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r167`

## Output

`workers/dispatcher/harvest-1way-r172/round-172/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

