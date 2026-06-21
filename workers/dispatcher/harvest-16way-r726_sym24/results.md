# harvest-16way-r726 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R726 ctrl_bpc |
|--------|--------|--------------:|
| tf6vQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fb7b6162-tf6vQ | 3.4616 |
| C0FjE | origin/claude/train-sym24-1e0c5574-C0FjE | 3.4630 |
| dW8A0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-72368bd0-dW8A0 | 3.4809 |
| WNI5F | fork-slaa-us-mmllm-claude-train-sym24-258f49de-WNI5F | 3.5048 |
| ciHfH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5e77e5b2-ciHfH | 3.5105 |
| Y4XKo | fork-davidwuchn-mmllm-claude-train-sym24-e50b3487-Y4XKo | 3.5123 |
| 7TU1R | fork-slaa-us-mmllm-claude-train-sym24-2dfef189-7TU1R | 3.5170 |
| Bz4Yr | fork-slaa-us-mmllm-claude-train-sym24-6bbf728b-Bz4Yr | 3.5215 |
| 6uVl5 | fork-joly-os-mmllm-claude-train-sym24-190b87d7-6uVl5 | 3.5232 |
| xCGqz | fork-joly-os-mmllm-claude-train-sym24-44fe5cd0-xCGqz | 3.5259 |
| 5d59i | fork-davidwuchn-mmllm-claude-train-sym24-a4bd65c5-5d59i | 3.5376 |
| kYXv4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5db1939c-kYXv4 | 3.5666 |
| W00L4 | fork-joly-os-mmllm-claude-train-sym24-10c7cc46-W00L4 | 3.7894 |
| CBizr | origin/claude/train-sym24-199a1cf5-CBizr | 3.7988 |
| RKZBC | origin/claude/train-sym24-1820433a-RKZBC | 3.8122 |
| 4UrAR | fork-davidwuchn-mmllm-claude-train-sym24-694afc27-4UrAR | 3.8318 |
| **mean** | | **3.5848** |
| **best** | | **3.4616** |

## Chain progression R725 → R726

Previous harvest: `workers/dispatcher/harvest-9way-r725_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5081         | 3.5848         | +0.0767 |
| ctrl_bpc best  | 3.4821         | 3.4616         | -0.0205 |

## Per-round trajectory (best bird: tf6vQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 726 | 4227 | 3.4616 | +1.1658 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **2000 steps** from 25 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-17way-r725_sym24`
  - `workers/dispatcher/harvest-4way-r725_sym24`
  - `workers/dispatcher/harvest-9way-r725_sym24`

## Output

`workers/dispatcher/harvest-16way-r726_sym24/round-726/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

