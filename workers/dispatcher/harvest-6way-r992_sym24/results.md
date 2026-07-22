# harvest-6way-r992 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R992 ctrl_bpc |
|--------|--------|--------------:|
| j7Zgv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3333b328-j7Zgv | 2.5721 |
| ufoMA | fork-joly-os-mmllm-claude-train-sym24-612964ac-ufoMA | 2.5839 |
| zJ4KM | origin/claude/train-sym24-ecfe2dcb-zJ4KM | 2.5935 |
| sgIHf | origin/claude/train-sym24-86d29b10-sgIHf | 2.9601 |
| XErcm | origin/claude/train-sym24-b53716b0-XErcm | 2.9621 |
| ootUu | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6d77aa1-ootUu | 2.9705 |
| **mean** | | **2.7737** |
| **best** | | **2.5721** |

## Chain progression R991 → R992

Previous harvest: `workers/dispatcher/harvest-5way-r991_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7361         | 2.7737         | +0.0376 |
| ctrl_bpc best  | 2.5847         | 2.5721         | -0.0126 |

## Per-round trajectory (best bird: j7Zgv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 992 | 6637 | 2.5721 | +0.1763 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r991_sym24`
  - `workers/dispatcher/harvest-4way-r991_sym24`

## Output

`workers/dispatcher/harvest-6way-r992_sym24/round-992/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

