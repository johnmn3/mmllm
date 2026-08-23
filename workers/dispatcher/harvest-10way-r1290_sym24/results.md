# harvest-10way-r1290 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1290 ctrl_bpc |
|--------|--------|--------------:|
| 0EIPl | fork-SeniorCareMarket-mmllm-claude-train-sym24-100f9200-0EIPl | 2.2117 |
| Lhga4 | fork-slaa-us-mmllm-claude-train-sym24-cc985235-Lhga4 | 2.2242 |
| ZrgSa | fork-joly-os-mmllm-claude-train-sym24-38697e30-ZrgSa | 2.2276 |
| lfcUr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-70dbfe95-lfcUr | 2.4097 |
| 1RBzS | origin/claude/train-sym24-77d67d19-1RBzS | 2.4124 |
| VrKqd | origin/claude/train-sym24-d51c8192-VrKqd | 2.6125 |
| AkitE | fork-joly-os-mmllm-claude-train-sym24-30979194-AkitE | 2.6234 |
| B6smP | fork-slaa-us-mmllm-claude-train-sym24-4afd6c39-B6smP | 5.3646 |
| 7Yy16 | fork-SeniorCareMarket-mmllm-claude-train-sym24-77182169-7Yy16 | 5.3710 |
| YUPYN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-338a3089-YUPYN | 5.7296 |
| **mean** | | **3.3187** |
| **best** | | **2.2117** |

## Chain progression R1289 → R1290

Previous harvest: `workers/dispatcher/harvest-5way-r1289_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.2089         | 3.3187         | -0.8902 |
| ctrl_bpc best  | 2.2241         | 2.2117         | -0.0124 |

## Per-round trajectory (best bird: 0EIPl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1290 | 6644 | 2.2117 | +0.2575 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1289_sym24`
  - `workers/dispatcher/harvest-1way-r1289_sym24`
  - `workers/dispatcher/harvest-5way-r1289_sym24`

## Output

`workers/dispatcher/harvest-10way-r1290_sym24/round-1290/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

