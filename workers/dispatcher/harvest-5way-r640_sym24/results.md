# harvest-5way-r640 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R640 ctrl_bpc |
|--------|--------|--------------:|
| NRIPb | fork-slaa-us-mmllm-claude-train-sym24-143741b3-NRIPb | 4.9453 |
| 0daEP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-296b8297-0daEP | 4.9481 |
| vd3dw | origin/claude/train-sym24-30aa7747-vd3dw | 5.1270 |
| tonwQ | fork-joly-os-mmllm-claude-train-sym24-3ccb841a-tonwQ | 5.5258 |
| SJXvF | fork-davidwuchn-mmllm-claude-train-sym24-0dd191bb-SJXvF | 5.5319 |
| **mean** | | **5.2156** |
| **best** | | **4.9453** |

## Chain progression R639 → R640

Previous harvest: `workers/dispatcher/harvest-29way-r639_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 6.2747         | 5.2156         | -1.0591 |
| ctrl_bpc best  | 5.8516         | 4.9453         | -0.9063 |

## Per-round trajectory (best bird: NRIPb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 640 | 5005 | 4.9453 | +0.0058 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **2640 steps** from 33 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-29way-r639_sym24`

## Output

`workers/dispatcher/harvest-5way-r640_sym24/round-640/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

