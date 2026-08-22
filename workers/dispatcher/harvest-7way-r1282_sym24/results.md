# harvest-7way-r1282 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1282 ctrl_bpc |
|--------|--------|--------------:|
| mh5Cn | fork-joly-os-mmllm-claude-train-sym24-dcd16bbb-mh5Cn | 2.2278 |
| k8FqI | fork-slaa-us-mmllm-claude-train-sym24-41e179b3-k8FqI | 2.2315 |
| 59HkE | fork-slaa-us-mmllm-claude-train-sym24-c7048ae3-59HkE | 2.2441 |
| 0mT3P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31786fb8-0mT3P | 2.2448 |
| yRsvA | fork-SeniorCareMarket-mmllm-claude-train-sym24-45d3fb60-yRsvA | 2.4166 |
| gUMCz | fork-joly-os-mmllm-claude-train-sym24-c9e235c8-gUMCz | 2.4170 |
| dkQ1R | origin/claude/train-sym24-88afacc7-dkQ1R | 2.6280 |
| **mean** | | **2.3443** |
| **best** | | **2.2278** |

## Chain progression R1281 → R1282

Previous harvest: `workers/dispatcher/harvest-6way-r1281_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2956         | 2.3443         | +0.0487 |
| ctrl_bpc best  | 2.2222         | 2.2278         | +0.0056 |

## Per-round trajectory (best bird: mh5Cn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1282 | 6786 | 2.2278 | +0.2507 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1281_sym24`
  - `workers/dispatcher/harvest-6way-r1281_sym24`

## Output

`workers/dispatcher/harvest-7way-r1282_sym24/round-1282/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

