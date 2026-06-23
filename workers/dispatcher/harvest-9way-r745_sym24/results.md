# harvest-9way-r745 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R745 ctrl_bpc |
|--------|--------|--------------:|
| OWQOa | fork-joly-os-mmllm-claude-train-sym24-190490b9-OWQOa | 3.3522 |
| KpsDw | origin/claude/train-sym24-aa3cc493-KpsDw | 3.3637 |
| N5yBV | origin/claude/train-sym24-e1a407fa-N5yBV | 3.3771 |
| rilz1 | fork-joly-os-mmllm-claude-train-sym24-eafa1d64-rilz1 | 3.3784 |
| xQj5d | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-684d1f92-xQj5d | 3.4003 |
| Z13cV | fork-davidwuchn-mmllm-claude-train-sym24-9ffa8f6d-Z13cV | 3.4340 |
| GLMzO | fork-slaa-us-mmllm-claude-train-sym24-aea1b7d1-GLMzO | 3.4460 |
| oxF8E | fork-davidwuchn-mmllm-claude-train-sym24-5b78d026-oxF8E | 3.4474 |
| Obdzb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a2b07ec5-Obdzb | 3.7337 |
| **mean** | | **3.4370** |
| **best** | | **3.3522** |

## Chain progression R744 → R745

Previous harvest: `workers/dispatcher/harvest-5way-r744_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6056         | 3.4370         | -0.1686 |
| ctrl_bpc best  | 3.4064         | 3.3522         | -0.0542 |

## Per-round trajectory (best bird: OWQOa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 745 | 6433 | 3.3522 | +0.4694 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r744_sym24`
  - `workers/dispatcher/harvest-5way-r744_sym24`

## Output

`workers/dispatcher/harvest-9way-r745_sym24/round-745/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

