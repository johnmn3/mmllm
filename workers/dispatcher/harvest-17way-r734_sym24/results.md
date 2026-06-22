# harvest-17way-r734 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R734 ctrl_bpc |
|--------|--------|--------------:|
| 72Fim | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e289975c-72Fim | 3.4155 |
| dnaE9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-04ab93ab-dnaE9 | 3.4465 |
| XWvpw | origin/claude/train-sym24-3e3290b2-XWvpw | 3.4487 |
| Y3BrM | fork-joly-os-mmllm-claude-train-sym24-6699943a-Y3BrM | 3.4659 |
| 1xFFn | fork-davidwuchn-mmllm-claude-train-sym24-ab83ece3-1xFFn | 3.4736 |
| VRxCN | origin/claude/train-sym24-71e7cfbf-VRxCN | 3.4748 |
| OCmS9 | fork-davidwuchn-mmllm-claude-train-sym24-b05a70e7-OCmS9 | 3.4771 |
| 5gQ4Y | fork-SeniorCareMarket-mmllm-claude-train-sym24-0160e3bb-5gQ4Y | 3.4800 |
| MvwVP | fork-joly-os-mmllm-claude-train-sym24-65db43a5-MvwVP | 3.4885 |
| rbqSu | fork-joly-os-mmllm-claude-train-sym24-c0bf733e-rbqSu | 3.4900 |
| Cj6eQ | fork-slaa-us-mmllm-claude-train-sym24-156ae9cd-Cj6eQ | 3.5172 |
| DlTss | fork-davidwuchn-mmllm-claude-train-sym24-50e6a3d2-DlTss | 3.7599 |
| q5fRT | origin/claude/train-sym24-8f3cd1f7-q5fRT | 3.7614 |
| x7CgX | fork-slaa-us-mmllm-claude-train-sym24-f5c1f114-x7CgX | 3.7646 |
| 8odTk | fork-SeniorCareMarket-mmllm-claude-train-sym24-6b12a5b9-8odTk | 3.7693 |
| 34BjT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-de2408f7-34BjT | 3.7788 |
| fftC7 | fork-slaa-us-mmllm-claude-train-sym24-9603b59e-fftC7 | 3.8447 |
| **mean** | | **3.5798** |
| **best** | | **3.4155** |

## Chain progression R733 → R734

Previous harvest: `workers/dispatcher/harvest-4way-r733_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5263         | 3.5798         | +0.0535 |
| ctrl_bpc best  | 3.4251         | 3.4155         | -0.0096 |

## Per-round trajectory (best bird: 72Fim)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 734 | 6342 | 3.4155 | +0.6980 |

## Cumulative training contribution

- This harvest: **1360 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r733_sym24`
  - `workers/dispatcher/harvest-16way-r733_sym24`
  - `workers/dispatcher/harvest-4way-r733_sym24`

## Output

`workers/dispatcher/harvest-17way-r734_sym24/round-734/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

