# harvest-6way-r801 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R801 ctrl_bpc |
|--------|--------|--------------:|
| rFDaO | origin/claude/train-sym24-ce4d5288-rFDaO | 3.0870 |
| W4F8z | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f45c3ecf-W4F8z | 3.1022 |
| i0zi2 | fork-slaa-us-mmllm-claude-train-sym24-5d20d6f8-i0zi2 | 3.2330 |
| v5s4Z | fork-SeniorCareMarket-mmllm-claude-train-sym24-60ad5d49-v5s4Z | 3.2336 |
| 9ktXw | fork-joly-os-mmllm-claude-train-sym24-af42139c-9ktXw | 3.4626 |
| Qfn9y | fork-davidwuchn-mmllm-claude-train-sym24-7a089d34-Qfn9y | 3.5000 |
| **mean** | | **3.2697** |
| **best** | | **3.0870** |

## Chain progression R800 → R801

Previous harvest: `workers/dispatcher/harvest-8way-r800_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3643         | 3.2697         | -0.0946 |
| ctrl_bpc best  | 3.1059         | 3.0870         | -0.0189 |

## Per-round trajectory (best bird: rFDaO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 801 | 6659 | 3.0870 | +0.5701 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r800_sym24`
  - `workers/dispatcher/harvest-8way-r800_sym24`

## Output

`workers/dispatcher/harvest-6way-r801_sym24/round-801/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

