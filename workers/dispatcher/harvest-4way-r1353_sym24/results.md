# harvest-4way-r1353 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1353 ctrl_bpc |
|--------|--------|--------------:|
| C0md8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-c7a23249-C0md8 | 3.2853 |
| kxYdF | fork-joly-os-mmllm-claude-train-sym24-33edb9a6-kxYdF | 3.2946 |
| VZrQ0 | origin/claude/train-sym24-0e069120-VZrQ0 | 3.3210 |
| WX3Yi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9996754c-WX3Yi | 3.6116 |
| **mean** | | **3.3781** |
| **best** | | **3.2853** |

## Chain progression R1352 → R1353

Previous harvest: `workers/dispatcher/harvest-7way-r1352_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3058         | 3.3781         | +0.0723 |
| ctrl_bpc best  | 3.2234         | 3.2853         | +0.0619 |

## Per-round trajectory (best bird: C0md8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1353 | 6777 | 3.2853 | +0.1200 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1352_sym24`
  - `workers/dispatcher/harvest-5way-r1352_sym24`

## Output

`workers/dispatcher/harvest-4way-r1353_sym24/round-1353/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

