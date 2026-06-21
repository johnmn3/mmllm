# harvest-11way-r726 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R726 ctrl_bpc |
|--------|--------|--------------:|
| C0FjE | origin/claude/train-sym24-1e0c5574-C0FjE | 3.4630 |
| dW8A0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-72368bd0-dW8A0 | 3.4809 |
| ciHfH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5e77e5b2-ciHfH | 3.5105 |
| Y4XKo | fork-davidwuchn-mmllm-claude-train-sym24-e50b3487-Y4XKo | 3.5123 |
| 7TU1R | fork-slaa-us-mmllm-claude-train-sym24-2dfef189-7TU1R | 3.5170 |
| Bz4Yr | fork-slaa-us-mmllm-claude-train-sym24-6bbf728b-Bz4Yr | 3.5215 |
| xCGqz | fork-joly-os-mmllm-claude-train-sym24-44fe5cd0-xCGqz | 3.5259 |
| 5d59i | fork-davidwuchn-mmllm-claude-train-sym24-a4bd65c5-5d59i | 3.5376 |
| kYXv4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5db1939c-kYXv4 | 3.5666 |
| W00L4 | fork-joly-os-mmllm-claude-train-sym24-10c7cc46-W00L4 | 3.7894 |
| RKZBC | origin/claude/train-sym24-1820433a-RKZBC | 3.8122 |
| **mean** | | **3.5670** |
| **best** | | **3.4630** |

## Chain progression R725 → R726

Previous harvest: `workers/dispatcher/harvest-9way-r725_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5081         | 3.5670         | +0.0589 |
| ctrl_bpc best  | 3.4821         | 3.4630         | -0.0191 |

## Per-round trajectory (best bird: C0FjE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 726 | 6360 | 3.4630 | +0.9329 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r725_sym24`
  - `workers/dispatcher/harvest-9way-r725_sym24`

## Output

`workers/dispatcher/harvest-11way-r726_sym24/round-726/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

