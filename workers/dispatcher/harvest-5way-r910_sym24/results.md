# harvest-5way-r910 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R910 ctrl_bpc |
|--------|--------|--------------:|
| FM8Uw | origin/claude/train-sym24-dcc8226e-FM8Uw | 2.7511 |
| eZjWa | fork-slaa-us-mmllm-claude-train-sym24-e4c6616e-eZjWa | 2.7620 |
| BxZgW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-aa414364-BxZgW | 2.7652 |
| umeQa | fork-joly-os-mmllm-claude-train-sym24-d781b9b3-umeQa | 2.7719 |
| hNmcw | origin/claude/train-sym24-d7ffa2de-hNmcw | 2.8108 |
| **mean** | | **2.7722** |
| **best** | | **2.7511** |

## Chain progression R909 → R910

Previous harvest: `workers/dispatcher/harvest-6way-r909_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8388         | 2.7722         | -0.0666 |
| ctrl_bpc best  | 2.7607         | 2.7511         | -0.0096 |

## Per-round trajectory (best bird: FM8Uw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 910 | 6713 | 2.7511 | +0.2301 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r909_sym24`
  - `workers/dispatcher/harvest-6way-r909_sym24`

## Output

`workers/dispatcher/harvest-5way-r910_sym24/round-910/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

