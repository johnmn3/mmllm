# harvest-2way-r1019 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1019 ctrl_bpc |
|--------|--------|--------------:|
| odIcF | fork-joly-os-mmllm-claude-train-sym24-26f394f4-odIcF | 2.9191 |
| agP7i | origin/claude/train-sym24-2e1bbfbf-agP7i | 2.9228 |
| **mean** | | **2.9209** |
| **best** | | **2.9191** |

## Chain progression R1018 → R1019

Previous harvest: `workers/dispatcher/harvest-5way-r1018_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8012         | 2.9209         | +0.1197 |
| ctrl_bpc best  | 2.5171         | 2.9191         | +0.4020 |

## Per-round trajectory (best bird: odIcF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1019 | 6647 | 2.9191 | +0.1638 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1018_sym24`

## Output

`workers/dispatcher/harvest-2way-r1019_sym24/round-1019/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

