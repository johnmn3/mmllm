# harvest-9way-r1245 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1245 ctrl_bpc |
|--------|--------|--------------:|
| qiRJM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2f932484-qiRJM | 2.2568 |
| 02myJ | origin/claude/train-sym24-1e4e1f6b-02myJ | 2.2580 |
| kXP5F | fork-slaa-us-mmllm-claude-train-sym24-e7afe12a-kXP5F | 2.2611 |
| p4RcS | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1dacae1-p4RcS | 2.2639 |
| WWXlp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82311bf0-WWXlp | 2.2647 |
| P6S2l | fork-slaa-us-mmllm-claude-train-sym24-3e3ef559-P6S2l | 2.4356 |
| MTVcN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82e55136-MTVcN | 2.4474 |
| bBgdP | fork-SeniorCareMarket-mmllm-claude-train-sym24-55b5d8c3-bBgdP | 2.4527 |
| o5AOA | fork-joly-os-mmllm-claude-train-sym24-bb868b04-o5AOA | 2.6464 |
| **mean** | | **2.3652** |
| **best** | | **2.2568** |

## Chain progression R1244 → R1245

Previous harvest: `workers/dispatcher/harvest-9way-r1244_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3417         | 2.3652         | +0.0235 |
| ctrl_bpc best  | 2.2409         | 2.2568         | +0.0159 |

## Per-round trajectory (best bird: qiRJM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1245 | 6524 | 2.2568 | +0.2449 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1244_sym24`
  - `workers/dispatcher/harvest-9way-r1244_sym24`

## Output

`workers/dispatcher/harvest-9way-r1245_sym24/round-1245/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

