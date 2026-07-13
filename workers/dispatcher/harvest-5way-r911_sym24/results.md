# harvest-5way-r911 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R911 ctrl_bpc |
|--------|--------|--------------:|
| SdD6g | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c44193a8-SdD6g | 2.7544 |
| iuZKM | fork-slaa-us-mmllm-claude-train-sym24-8ef3b8a8-iuZKM | 2.7713 |
| 74wyA | origin/claude/train-sym24-2baf051a-74wyA | 2.8100 |
| FEYqS | origin/claude/train-sym24-f3840cbc-FEYqS | 2.9442 |
| Hivqz | fork-joly-os-mmllm-claude-train-sym24-a68dd579-Hivqz | 3.1348 |
| **mean** | | **2.8829** |
| **best** | | **2.7544** |

## Chain progression R910 → R911

Previous harvest: `workers/dispatcher/harvest-5way-r910_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7722         | 2.8829         | +0.1107 |
| ctrl_bpc best  | 2.7511         | 2.7544         | +0.0033 |

## Per-round trajectory (best bird: SdD6g)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 911 | 6402 | 2.7544 | +0.2305 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r910_sym24`

## Output

`workers/dispatcher/harvest-5way-r911_sym24/round-911/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

