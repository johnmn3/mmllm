# harvest-6way-r730 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R730 ctrl_bpc |
|--------|--------|--------------:|
| R74uJ | origin/claude/train-sym24-8e08e408-R74uJ | 3.4270 |
| HOK26 | fork-slaa-us-mmllm-claude-train-sym24-2303cd91-HOK26 | 3.4541 |
| 3fOke | fork-SeniorCareMarket-mmllm-claude-train-sym24-52576282-3fOke | 3.4716 |
| 33UBM | fork-joly-os-mmllm-claude-train-sym24-d83dc5aa-33UBM | 3.4783 |
| qD07E | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e7fc60a6-qD07E | 3.5097 |
| e6iqX | fork-davidwuchn-mmllm-claude-train-sym24-ae385df8-e6iqX | 3.8058 |
| **mean** | | **3.5244** |
| **best** | | **3.4270** |

## Chain progression R729 → R730

Previous harvest: `workers/dispatcher/harvest-9way-r729_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5224         | 3.5244         | +0.0020 |
| ctrl_bpc best  | 3.4433         | 3.4270         | -0.0163 |

## Per-round trajectory (best bird: R74uJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 730 | 6345 | 3.4270 | +0.5425 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r729_sym24`

## Output

`workers/dispatcher/harvest-6way-r730_sym24/round-730/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

