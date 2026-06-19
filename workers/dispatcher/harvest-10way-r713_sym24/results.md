# harvest-10way-r713 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R713 ctrl_bpc |
|--------|--------|--------------:|
| 7nAJw | origin/claude/train-sym24-65254146-7nAJw | 3.5473 |
| Xus8P | origin/claude/train-sym24-5e7e117c-Xus8P | 3.5500 |
| kYCJE | fork-slaa-us-mmllm-claude-train-sym24-b815a265-kYCJE | 3.5763 |
| O0Pza | fork-joly-os-mmllm-claude-train-sym24-d0f57865-O0Pza | 3.5833 |
| dH23b | fork-slaa-us-mmllm-claude-train-sym24-f5db8026-dH23b | 3.5860 |
| nS1ec | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c64652d1-nS1ec | 3.6456 |
| VZHfH | fork-davidwuchn-mmllm-claude-train-sym24-98089b95-VZHfH | 3.8645 |
| BmchJ | fork-davidwuchn-mmllm-claude-train-sym24-6bd8a329-BmchJ | 3.8801 |
| StYSq | fork-joly-os-mmllm-claude-train-sym24-b208aeff-StYSq | 3.8856 |
| 75kuu | fork-SeniorCareMarket-mmllm-claude-train-sym24-eb27f83d-75kuu | 3.8944 |
| **mean** | | **3.7013** |
| **best** | | **3.5473** |

## Chain progression R712 → R713

Previous harvest: `workers/dispatcher/harvest-3way-r712_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7722         | 3.7013         | -0.0709 |
| ctrl_bpc best  | 3.5411         | 3.5473         | +0.0062 |

## Per-round trajectory (best bird: 7nAJw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 713 | 6606 | 3.5473 | +1.5115 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r712_sym24`

## Output

`workers/dispatcher/harvest-10way-r713_sym24/round-713/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

