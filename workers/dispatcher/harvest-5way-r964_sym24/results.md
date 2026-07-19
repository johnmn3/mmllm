# harvest-5way-r964 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R964 ctrl_bpc |
|--------|--------|--------------:|
| 88wR9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4c390709-88wR9 | 2.6209 |
| L0VVZ | fork-joly-os-mmllm-claude-train-sym24-75f632cd-L0VVZ | 2.6944 |
| HfQsz | fork-SeniorCareMarket-mmllm-claude-train-sym24-ce5cfc39-HfQsz | 2.8301 |
| KrLFO | origin/claude/train-sym24-f4707f43-KrLFO | 3.0202 |
| Ejpzm | origin/claude/train-sym24-f9a5b8ed-Ejpzm | 3.0223 |
| **mean** | | **2.8376** |
| **best** | | **2.6209** |

## Chain progression R963 → R964

Previous harvest: `workers/dispatcher/harvest-4way-r963_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8691         | 2.8376         | -0.0315 |
| ctrl_bpc best  | 2.8219         | 2.6209         | -0.2010 |

## Per-round trajectory (best bird: 88wR9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 964 | 6654 | 2.6209 | +0.1698 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r963_sym24`

## Output

`workers/dispatcher/harvest-5way-r964_sym24/round-964/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

