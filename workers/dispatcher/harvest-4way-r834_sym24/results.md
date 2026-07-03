# harvest-4way-r834 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R834 ctrl_bpc |
|--------|--------|--------------:|
| xeZse | fork-joly-os-mmllm-claude-train-sym24-5e5f95be-xeZse | 2.9712 |
| 6BTVk | fork-slaa-us-mmllm-claude-train-sym24-75452e8c-6BTVk | 3.1378 |
| y19Su | origin/claude/train-sym24-a189a8c5-y19Su | 3.3533 |
| owlmM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0a176d75-owlmM | 3.3961 |
| **mean** | | **3.2146** |
| **best** | | **2.9712** |

## Chain progression R833 → R834

Previous harvest: `workers/dispatcher/harvest-9way-r833_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0785         | 3.2146         | +0.1361 |
| ctrl_bpc best  | 2.9703         | 2.9712         | +0.0009 |

## Per-round trajectory (best bird: xeZse)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 834 | 4398 | 2.9712 | +0.5953 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r833_sym24`

## Output

`workers/dispatcher/harvest-4way-r834_sym24/round-834/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

