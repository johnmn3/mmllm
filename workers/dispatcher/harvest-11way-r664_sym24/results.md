# harvest-11way-r664 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R664 ctrl_bpc |
|--------|--------|--------------:|
| iwqaE | fork-davidwuchn-mmllm-claude-train-sym24-e5481368-iwqaE | 3.9325 |
| kcQwZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-9de3c302-kcQwZ | 3.9470 |
| YQA4R | origin/claude/train-sym24-5c8244d9-YQA4R | 3.9597 |
| RvnQA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68c0d5cd-RvnQA | 3.9660 |
| kqrK9 | origin/claude/train-sym24-9901af6c-kqrK9 | 3.9806 |
| hOm9R | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f2718d95-hOm9R | 3.9816 |
| QLLRb | fork-joly-os-mmllm-claude-train-sym24-3511d77c-QLLRb | 3.9869 |
| oGZr2 | fork-joly-os-mmllm-claude-train-sym24-8302b374-oGZr2 | 3.9967 |
| f8Roq | fork-joly-os-mmllm-claude-train-sym24-d25e376a-f8Roq | 4.0386 |
| Qp7RJ | fork-slaa-us-mmllm-claude-train-sym24-3a29fd25-Qp7RJ | 4.2869 |
| eAvz3 | fork-davidwuchn-mmllm-claude-train-sym24-a1e761c2-eAvz3 | 4.3102 |
| **mean** | | **4.0352** |
| **best** | | **3.9325** |

## Chain progression R663 → R664

Previous harvest: `workers/dispatcher/harvest-7way-r663_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1668         | 4.0352         | -0.1316 |
| ctrl_bpc best  | 3.9529         | 3.9325         | -0.0204 |

## Per-round trajectory (best bird: iwqaE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 664 | 6451 | 3.9325 | +0.1897 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r663_sym24`
  - `workers/dispatcher/harvest-7way-r663_sym24`

## Output

`workers/dispatcher/harvest-11way-r664_sym24/round-664/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

