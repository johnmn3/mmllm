# harvest-8way-r1029 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1029 ctrl_bpc |
|--------|--------|--------------:|
| bkRtX | fork-slaa-us-mmllm-claude-train-sym24-48fac693-bkRtX | 2.5272 |
| B8uL5 | origin/claude/train-sym24-4c50f705-B8uL5 | 2.5333 |
| wy8SW | fork-joly-os-mmllm-claude-train-sym24-0bc3a656-wy8SW | 2.7016 |
| YQdp4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a5f51eb-YQdp4 | 2.7063 |
| t75N7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-c92cc9b3-t75N7 | 2.7159 |
| qFXVV | fork-slaa-us-mmllm-claude-train-sym24-cc678abc-qFXVV | 2.8933 |
| aF0gW | origin/claude/train-sym24-55436892-aF0gW | 2.8981 |
| JmGJg | origin/claude/train-sym24-8a96ee1a-JmGJg | 2.9009 |
| **mean** | | **2.7346** |
| **best** | | **2.5272** |

## Chain progression R1028 → R1029

Previous harvest: `workers/dispatcher/harvest-5way-r1028_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6323         | 2.7346         | +0.1023 |
| ctrl_bpc best  | 2.5027         | 2.5272         | +0.0245 |

## Per-round trajectory (best bird: bkRtX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1029 | 6706 | 2.5272 | +0.2036 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1028_sym24`
  - `workers/dispatcher/harvest-4way-r1028_sym24`
  - `workers/dispatcher/harvest-5way-r1028_sym24`

## Output

`workers/dispatcher/harvest-8way-r1029_sym24/round-1029/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

