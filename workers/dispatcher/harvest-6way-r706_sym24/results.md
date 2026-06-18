# harvest-6way-r706 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R706 ctrl_bpc |
|--------|--------|--------------:|
| 4iaKr | origin/claude/train-sym24-a0e7a411-4iaKr | 3.5805 |
| FbqdQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-179717f8-FbqdQ | 3.5935 |
| FTzkY | fork-davidwuchn-mmllm-claude-train-sym24-09ccad9b-FTzkY | 3.6228 |
| ZbBKP | fork-SeniorCareMarket-mmllm-claude-train-sym24-ed33d7f1-ZbBKP | 3.9154 |
| aDsYD | fork-slaa-us-mmllm-claude-train-sym24-99ada46b-aDsYD | 3.9219 |
| Kl3A9 | fork-joly-os-mmllm-claude-train-sym24-793966c9-Kl3A9 | 3.9321 |
| **mean** | | **3.7610** |
| **best** | | **3.5805** |

## Chain progression R705 → R706

Previous harvest: `workers/dispatcher/harvest-1way-r705_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6627         | 3.7610         | +0.0983 |
| ctrl_bpc best  | 3.6627         | 3.5805         | -0.0822 |

## Per-round trajectory (best bird: 4iaKr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 706 | 6310 | 3.5805 | +0.8044 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r705_sym24`

## Output

`workers/dispatcher/harvest-6way-r706_sym24/round-706/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

