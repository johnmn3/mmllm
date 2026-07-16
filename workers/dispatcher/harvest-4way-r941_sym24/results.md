# harvest-4way-r941 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R941 ctrl_bpc |
|--------|--------|--------------:|
| UfdvA | origin/claude/train-sym24-a22432ac-UfdvA | 2.6712 |
| eQpSa | origin/claude/train-sym24-378f1104-eQpSa | 2.7046 |
| TroSY | fork-joly-os-mmllm-claude-train-sym24-03bd97ab-TroSY | 2.7089 |
| LXpkE | fork-joly-os-mmllm-claude-train-sym24-ea56bc59-LXpkE | 2.8769 |
| **mean** | | **2.7404** |
| **best** | | **2.6712** |

## Chain progression R940 → R941

Previous harvest: `workers/dispatcher/harvest-1way-r940_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8931         | 2.7404         | -0.1527 |
| ctrl_bpc best  | 2.8931         | 2.6712         | -0.2219 |

## Per-round trajectory (best bird: UfdvA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 941 | 5306 | 2.6712 | +0.2112 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r940_sym24`

## Output

`workers/dispatcher/harvest-4way-r941_sym24/round-941/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

