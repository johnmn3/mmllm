# harvest-12way-r674 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R674 ctrl_bpc |
|--------|--------|--------------:|
| j7lgy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-54a90b4e-j7lgy | 3.8302 |
| Z2dGu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7f801f0b-Z2dGu | 3.8396 |
| 8k5Rs | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9016ae5-8k5Rs | 3.8446 |
| iZNxX | origin/claude/train-sym24-94d17e23-iZNxX | 3.8449 |
| DrIeP | origin/claude/train-sym24-20133ae8-DrIeP | 3.8630 |
| 9Tch7 | fork-davidwuchn-mmllm-claude-train-sym24-3f54da0e-9Tch7 | 3.8664 |
| WQ2YO | fork-joly-os-mmllm-claude-train-sym24-0b1fc8ea-WQ2YO | 3.8692 |
| lpaR0 | origin/claude/train-sym24-06421ae4-lpaR0 | 3.8783 |
| CfVru | fork-davidwuchn-mmllm-claude-train-sym24-85d4dddb-CfVru | 3.8847 |
| qpDSN | fork-slaa-us-mmllm-claude-train-sym24-707b5ebf-qpDSN | 3.9872 |
| 4xYLm | fork-slaa-us-mmllm-claude-train-sym24-89fa86eb-4xYLm | 4.1647 |
| jT47Y | fork-joly-os-mmllm-claude-train-sym24-dc262255-jT47Y | 4.1907 |
| **mean** | | **3.9220** |
| **best** | | **3.8302** |

## Chain progression R673 → R674

Previous harvest: `workers/dispatcher/harvest-9way-r673_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8775         | 3.9220         | +0.0445 |
| ctrl_bpc best  | 3.8499         | 3.8302         | -0.0197 |

## Per-round trajectory (best bird: j7lgy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 674 | 5340 | 3.8302 | +0.4391 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r673_sym24`
  - `workers/dispatcher/harvest-9way-r673_sym24`

## Output

`workers/dispatcher/harvest-12way-r674_sym24/round-674/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

