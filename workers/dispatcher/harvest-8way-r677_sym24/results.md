# harvest-8way-r677 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R677 ctrl_bpc |
|--------|--------|--------------:|
| Hmc9Q | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e6d8726-Hmc9Q | 3.8053 |
| x6cNk | fork-slaa-us-mmllm-claude-train-sym24-e469b8cf-x6cNk | 3.8468 |
| Au0ez | origin/claude/train-sym24-e26081aa-Au0ez | 3.8538 |
| rNhuy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e346e6f2-rNhuy | 3.8759 |
| i8pjs | fork-joly-os-mmllm-claude-train-sym24-34e712e6-i8pjs | 3.8776 |
| wMrAE | fork-davidwuchn-mmllm-claude-train-sym24-c72c238b-wMrAE | 3.8909 |
| hHQC9 | fork-slaa-us-mmllm-claude-train-sym24-88144682-hHQC9 | 4.1512 |
| 6FjeZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1d074cc3-6FjeZ | 4.1552 |
| **mean** | | **3.9321** |
| **best** | | **3.8053** |

## Chain progression R676 → R677

Previous harvest: `workers/dispatcher/harvest-7way-r676_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8577         | 3.9321         | +0.0744 |
| ctrl_bpc best  | 3.8016         | 3.8053         | +0.0037 |

## Per-round trajectory (best bird: Hmc9Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 677 | 6629 | 3.8053 | +0.2486 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r676_sym24`

## Output

`workers/dispatcher/harvest-8way-r677_sym24/round-677/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

