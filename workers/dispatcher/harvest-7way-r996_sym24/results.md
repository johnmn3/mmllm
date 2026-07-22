# harvest-7way-r996 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R996 ctrl_bpc |
|--------|--------|--------------:|
| vHozX | fork-joly-os-mmllm-claude-train-sym24-3ee75233-vHozX | 2.5694 |
| A1Afi | origin/claude/train-sym24-2112edde-A1Afi | 2.5872 |
| iQa1t | origin/claude/train-sym24-aee8ecac-iQa1t | 2.7441 |
| EFd1V | fork-joly-os-mmllm-claude-train-sym24-c481fd8b-EFd1V | 2.7559 |
| 0vHZ7 | fork-slaa-us-mmllm-claude-train-sym24-9b331ffd-0vHZ7 | 2.7560 |
| O0jLJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-84efe4f3-O0jLJ | 2.9449 |
| nLF9d | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5d18df7-nLF9d | 2.9630 |
| **mean** | | **2.7601** |
| **best** | | **2.5694** |

## Chain progression R995 → R996

Previous harvest: `workers/dispatcher/harvest-3way-r995_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6392         | 2.7601         | +0.1209 |
| ctrl_bpc best  | 2.5605         | 2.5694         | +0.0089 |

## Per-round trajectory (best bird: vHozX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 996 | 6704 | 2.5694 | +0.1692 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r995_sym24`
  - `workers/dispatcher/harvest-3way-r995_sym24`

## Output

`workers/dispatcher/harvest-7way-r996_sym24/round-996/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

