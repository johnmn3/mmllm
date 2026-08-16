# harvest-16way-r1224 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R1224 ctrl_bpc |
|--------|--------|--------------:|
| X8WGp | origin/claude/train-sym24-c9d24915-X8WGp | 2.2554 |
| DB8qq | origin/claude/train-sym24-4f3d903a-DB8qq | 2.2578 |
| xGXgJ | origin/claude/train-sym24-6c6d29c8-xGXgJ | 2.2625 |
| Jy5Iy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98dae8db-Jy5Iy | 2.2750 |
| Xx2KL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-560b051d-Xx2KL | 2.2800 |
| BWZfd | fork-SeniorCareMarket-mmllm-claude-train-sym24-71c57b49-BWZfd | 2.2811 |
| rYWAA | fork-joly-os-mmllm-claude-train-sym24-8ad2355d-rYWAA | 2.4622 |
| WCdkA | fork-SeniorCareMarket-mmllm-claude-train-sym24-5ea9c3fb-WCdkA | 2.4631 |
| 77nvG | fork-slaa-us-mmllm-claude-train-sym24-7571f223-77nvG | 2.4643 |
| EVEpx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e6bc31e5-EVEpx | 2.4648 |
| nvhhd | fork-joly-os-mmllm-claude-train-sym24-af5214b0-nvhhd | 2.4718 |
| uUkVQ | fork-joly-os-mmllm-claude-train-sym24-aee7c9c8-uUkVQ | 2.4749 |
| Odj7d | fork-slaa-us-mmllm-claude-train-sym24-27e26fd6-Odj7d | 2.4754 |
| k0qnG | fork-joly-os-mmllm-claude-train-sym24-7105207c-k0qnG | 2.6563 |
| HV75w | fork-SeniorCareMarket-mmllm-claude-train-sym24-691b9fe1-HV75w | 2.6747 |
| 7W1tv | fork-slaa-us-mmllm-claude-train-sym24-ff5b672b-7W1tv | 9.0999 |
| **mean** | | **2.8325** |
| **best** | | **2.2554** |

## Chain progression R1223 → R1224

Previous harvest: `workers/dispatcher/harvest-9way-r1223_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3570         | 2.8325         | +0.4755 |
| ctrl_bpc best  | 2.2555         | 2.2554         | -0.0001 |

## Per-round trajectory (best bird: X8WGp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1224 | 6833 | 2.2554 | +0.2514 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **2000 steps** from 25 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1223_sym24`
  - `workers/dispatcher/harvest-2way-r1223_sym24`
  - `workers/dispatcher/harvest-9way-r1223_sym24`

## Output

`workers/dispatcher/harvest-16way-r1224_sym24/round-1224/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

