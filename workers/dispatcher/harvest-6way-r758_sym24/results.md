# harvest-6way-r758 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R758 ctrl_bpc |
|--------|--------|--------------:|
| b9u6J | fork-joly-os-mmllm-claude-train-sym24-0d7e98ab-b9u6J | 3.2876 |
| 4hJOn | fork-SeniorCareMarket-mmllm-claude-train-sym24-8910e41d-4hJOn | 3.3268 |
| uUI77 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-de04382c-uUI77 | 3.3273 |
| a9RBc | fork-slaa-us-mmllm-claude-train-sym24-2bcc98fd-a9RBc | 3.3602 |
| SU4s4 | origin/claude/train-sym24-efc10080-SU4s4 | 3.3883 |
| jmbHT | fork-davidwuchn-mmllm-claude-train-sym24-02423117-jmbHT | 3.6726 |
| **mean** | | **3.3938** |
| **best** | | **3.2876** |

## Chain progression R757 → R758

Previous harvest: `workers/dispatcher/harvest-9way-r757_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3177         | 3.3938         | +0.0761 |
| ctrl_bpc best  | 3.2940         | 3.2876         | -0.0064 |

## Per-round trajectory (best bird: b9u6J)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 758 | 6422 | 3.2876 | +0.6109 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r757_sym24`

## Output

`workers/dispatcher/harvest-6way-r758_sym24/round-758/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

