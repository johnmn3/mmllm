# harvest-8way-r746 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R746 ctrl_bpc |
|--------|--------|--------------:|
| qejRN | fork-slaa-us-mmllm-claude-train-sym24-f4816add-qejRN | 3.3555 |
| xQnSx | fork-joly-os-mmllm-claude-train-sym24-d7261401-xQnSx | 3.3591 |
| PDauo | fork-joly-os-mmllm-claude-train-sym24-38d77c20-PDauo | 3.3832 |
| iAKwe | origin/claude/train-sym24-f59216cc-iAKwe | 3.3890 |
| aIXK1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc893224-aIXK1 | 3.4277 |
| WoS1N | fork-davidwuchn-mmllm-claude-train-sym24-4279d767-WoS1N | 3.4357 |
| Z4i2J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3c693f6b-Z4i2J | 3.7011 |
| npje0 | origin/claude/train-sym24-22bfaaba-npje0 | 3.7143 |
| **mean** | | **3.4707** |
| **best** | | **3.3555** |

## Chain progression R745 → R746

Previous harvest: `workers/dispatcher/harvest-9way-r745_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4370         | 3.4707         | +0.0337 |
| ctrl_bpc best  | 3.3522         | 3.3555         | +0.0033 |

## Per-round trajectory (best bird: qejRN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 746 | 6436 | 3.3555 | +0.7142 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r745_sym24`
  - `workers/dispatcher/harvest-9way-r745_sym24`

## Output

`workers/dispatcher/harvest-8way-r746_sym24/round-746/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

