# harvest-4way-r1394 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1394 ctrl_bpc |
|--------|--------|--------------:|
| bEhaH | fork-joly-os-mmllm-claude-train-sym24-d6ec9aa4-bEhaH | 3.6153 |
| sISZO | fork-SeniorCareMarket-mmllm-claude-train-sym24-dee52e1d-sISZO | 3.6166 |
| sGja3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-784e0c9e-sGja3 | 3.6568 |
| k0VN4 | origin/claude/train-sym24-a457c1d0-k0VN4 | 4.0118 |
| **mean** | | **3.7251** |
| **best** | | **3.6153** |

## Chain progression R1393 → R1394

Previous harvest: `workers/dispatcher/harvest-2way-r1393_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7417         | 3.7251         | -0.0166 |
| ctrl_bpc best  | 3.6921         | 3.6153         | -0.0768 |

## Per-round trajectory (best bird: bEhaH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1394 | 6741 | 3.6153 | +0.0286 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1393_sym24`

## Output

`workers/dispatcher/harvest-4way-r1394_sym24/round-1394/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

