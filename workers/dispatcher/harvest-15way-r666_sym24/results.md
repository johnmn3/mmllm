# harvest-15way-r666 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R666 ctrl_bpc |
|--------|--------|--------------:|
| s5oDr | fork-slaa-us-mmllm-claude-train-sym24-eb2a5166-s5oDr | 3.9071 |
| krYD7 | origin/claude/train-sym24-cb3ec425-krYD7 | 3.9160 |
| YtJ1h | fork-slaa-us-mmllm-claude-train-sym24-b7b46459-YtJ1h | 3.9294 |
| 8JFMV | fork-joly-os-mmllm-claude-train-sym24-3e1ef01e-8JFMV | 3.9318 |
| UxlEe | origin/claude/train-sym24-d408cfed-UxlEe | 3.9401 |
| 5Zvb1 | fork-davidwuchn-mmllm-claude-train-sym24-2366472c-5Zvb1 | 3.9500 |
| 5o2I4 | fork-slaa-us-mmllm-claude-train-sym24-8d5ec2bb-5o2I4 | 3.9605 |
| 3BaXy | fork-davidwuchn-mmllm-claude-train-sym24-2dad0d8d-3BaXy | 3.9642 |
| riGJs | fork-davidwuchn-mmllm-claude-train-sym24-7f1a145a-riGJs | 3.9674 |
| NYkJZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ddf27a6c-NYkJZ | 3.9694 |
| r8l0P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4fd50511-r8l0P | 3.9745 |
| bd1Qw | fork-SeniorCareMarket-mmllm-claude-train-sym24-28a0aeb7-bd1Qw | 3.9753 |
| rA1nP | origin/claude/train-sym24-03e79948-rA1nP | 4.2568 |
| vNJce | fork-joly-os-mmllm-claude-train-sym24-c4a47eb7-vNJce | 4.3739 |
| FuzhD | fork-joly-os-mmllm-claude-train-sym24-b26b367e-FuzhD | 4.3846 |
| **mean** | | **4.0267** |
| **best** | | **3.9071** |

## Chain progression R665 → R666

Previous harvest: `workers/dispatcher/harvest-5way-r665_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1504         | 4.0267         | -0.1237 |
| ctrl_bpc best  | 3.9679         | 3.9071         | -0.0608 |

## Per-round trajectory (best bird: s5oDr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 666 | 6436 | 3.9071 | +0.2395 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r665_sym24`
  - `workers/dispatcher/harvest-13way-r665_sym24`
  - `workers/dispatcher/harvest-5way-r665_sym24`

## Output

`workers/dispatcher/harvest-15way-r666_sym24/round-666/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

