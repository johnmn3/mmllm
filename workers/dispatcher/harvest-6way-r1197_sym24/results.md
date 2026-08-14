# harvest-6way-r1197 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1197 ctrl_bpc |
|--------|--------|--------------:|
| iLn4i | origin/claude/train-sym24-2a21fdd3-iLn4i | 2.2859 |
| NXzAx | fork-slaa-us-mmllm-claude-train-sym24-050ad5bd-NXzAx | 2.2887 |
| mUjCU | fork-slaa-us-mmllm-claude-train-sym24-929c54f1-mUjCU | 2.3041 |
| qF414 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d45bc811-qF414 | 2.3062 |
| N762M | fork-joly-os-mmllm-claude-train-sym24-62f77520-N762M | 2.3163 |
| mC8D9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-15b32558-mC8D9 | 2.4929 |
| **mean** | | **2.3324** |
| **best** | | **2.2859** |

## Chain progression R1196 → R1197

Previous harvest: `workers/dispatcher/harvest-9way-r1196_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4521         | 2.3324         | -0.1197 |
| ctrl_bpc best  | 2.2848         | 2.2859         | +0.0011 |

## Per-round trajectory (best bird: iLn4i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1197 | 3737 | 2.2859 | +0.2512 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1196_sym24`
  - `workers/dispatcher/harvest-9way-r1196_sym24`

## Output

`workers/dispatcher/harvest-6way-r1197_sym24/round-1197/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

