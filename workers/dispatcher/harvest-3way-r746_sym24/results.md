# harvest-3way-r746 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R746 ctrl_bpc |
|--------|--------|--------------:|
| xQnSx | fork-joly-os-mmllm-claude-train-sym24-d7261401-xQnSx | 3.3591 |
| iAKwe | origin/claude/train-sym24-f59216cc-iAKwe | 3.3890 |
| aIXK1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc893224-aIXK1 | 3.4277 |
| **mean** | | **3.3919** |
| **best** | | **3.3591** |

## Chain progression R745 → R746

Previous harvest: `workers/dispatcher/harvest-9way-r745_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4370         | 3.3919         | -0.0451 |
| ctrl_bpc best  | 3.3522         | 3.3591         | +0.0069 |

## Per-round trajectory (best bird: xQnSx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 746 | 6681 | 3.3591 | +0.5787 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r745_sym24`

## Output

`workers/dispatcher/harvest-3way-r746_sym24/round-746/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

