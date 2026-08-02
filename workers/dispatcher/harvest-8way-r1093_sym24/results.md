# harvest-8way-r1093 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1093 ctrl_bpc |
|--------|--------|--------------:|
| Sub9I | origin/claude/train-sym24-e12fbe44-Sub9I | 2.4075 |
| ypqCJ | fork-slaa-us-mmllm-claude-train-sym24-fb5a646b-ypqCJ | 2.4268 |
| WXDyh | origin/claude/train-sym24-6aef565c-WXDyh | 2.4309 |
| 9RiO6 | fork-joly-os-mmllm-claude-train-sym24-a6f673c7-9RiO6 | 2.6068 |
| rCtNZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8cd5bdfd-rCtNZ | 2.7917 |
| tzR3c | origin/claude/train-sym24-6b204f05-tzR3c | 2.8065 |
| llweP | fork-joly-os-mmllm-claude-train-sym24-968faa00-llweP | 2.8111 |
| WAv9R | fork-SeniorCareMarket-mmllm-claude-train-sym24-160596ad-WAv9R | 2.8140 |
| **mean** | | **2.6369** |
| **best** | | **2.4075** |

## Chain progression R1092 → R1093

Previous harvest: `workers/dispatcher/harvest-3way-r1092_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6131         | 2.6369         | +0.0238 |
| ctrl_bpc best  | 2.4116         | 2.4075         | -0.0041 |

## Per-round trajectory (best bird: Sub9I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1093 | 5282 | 2.4075 | +0.2383 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1092_sym24`
  - `workers/dispatcher/harvest-3way-r1092_sym24`

## Output

`workers/dispatcher/harvest-8way-r1093_sym24/round-1093/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

