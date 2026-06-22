# harvest-5way-r735 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R735 ctrl_bpc |
|--------|--------|--------------:|
| cIFsE | fork-joly-os-mmllm-claude-train-sym24-b3b6a2bd-cIFsE | 3.3996 |
| iegEG | origin/claude/train-sym24-14b753e7-iegEG | 3.4573 |
| E2XKf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5c49346-E2XKf | 3.4727 |
| njbe1 | fork-slaa-us-mmllm-claude-train-sym24-202b387d-njbe1 | 3.4972 |
| ZpjRP | fork-davidwuchn-mmllm-claude-train-sym24-ab2a4e4e-ZpjRP | 3.7587 |
| **mean** | | **3.5171** |
| **best** | | **3.3996** |

## Chain progression R734 → R735

Previous harvest: `workers/dispatcher/harvest-17way-r734_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5798         | 3.5171         | -0.0627 |
| ctrl_bpc best  | 3.4155         | 3.3996         | -0.0159 |

## Per-round trajectory (best bird: cIFsE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 735 | 6772 | 3.3996 | +0.6641 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r734_sym24`
  - `workers/dispatcher/harvest-5way-r734_sym24`

## Output

`workers/dispatcher/harvest-5way-r735_sym24/round-735/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

