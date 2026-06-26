# harvest-6way-r777 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R777 ctrl_bpc |
|--------|--------|--------------:|
| MlBta | fork-davidwuchn-mmllm-claude-train-sym24-21843b07-MlBta | 3.2230 |
| 9yD9R | origin/claude/train-sym24-7b29bcec-9yD9R | 3.2420 |
| OqwUw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27b87f63-OqwUw | 3.2443 |
| kqvip | fork-joly-os-mmllm-claude-train-sym24-c6314cfb-kqvip | 3.3293 |
| TsPZ0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3cfe50d0-TsPZ0 | 3.3355 |
| Rrkik | origin/claude/train-sym24-36e34bc5-Rrkik | 3.5903 |
| **mean** | | **3.3274** |
| **best** | | **3.2230** |

## Chain progression R776 → R777

Previous harvest: `workers/dispatcher/harvest-12way-r776_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3032         | 3.3274         | +0.0242 |
| ctrl_bpc best  | 3.2060         | 3.2230         | +0.0170 |

## Per-round trajectory (best bird: MlBta)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 777 | 6324 | 3.2230 | +0.5604 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r776_sym24`

## Output

`workers/dispatcher/harvest-6way-r777_sym24/round-777/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

