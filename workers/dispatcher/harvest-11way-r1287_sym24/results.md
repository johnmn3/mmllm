# harvest-11way-r1287 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1287 ctrl_bpc |
|--------|--------|--------------:|
| T6r3M | fork-joly-os-mmllm-claude-train-sym24-0961503a-T6r3M | 2.2147 |
| lrrF4 | origin/claude/train-sym24-d0f5da99-lrrF4 | 2.2258 |
| Hh6JH | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9742db5-Hh6JH | 2.2270 |
| EavOq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d4930477-EavOq | 2.2295 |
| pwmtl | fork-slaa-us-mmllm-claude-train-sym24-07e7a2b0-pwmtl | 2.2310 |
| wvTLY | fork-joly-os-mmllm-claude-train-sym24-3e917495-wvTLY | 2.2323 |
| VcP9h | fork-slaa-us-mmllm-claude-train-sym24-faf04225-VcP9h | 2.2325 |
| Ruetv | fork-slaa-us-mmllm-claude-train-sym24-c778b5c4-Ruetv | 2.4217 |
| drgkZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1f6a454e-drgkZ | 2.4224 |
| LzZ7b | origin/claude/train-sym24-79d9e53a-LzZ7b | 2.6122 |
| UTbF0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f028b58e-UTbF0 | 2.6129 |
| **mean** | | **2.3329** |
| **best** | | **2.2147** |

## Chain progression R1286 → R1287

Previous harvest: `workers/dispatcher/harvest-6way-r1286_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2931         | 2.3329         | +0.0398 |
| ctrl_bpc best  | 2.2207         | 2.2147         | -0.0060 |

## Per-round trajectory (best bird: T6r3M)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1287 | 6385 | 2.2147 | +0.2594 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1286_sym24`
  - `workers/dispatcher/harvest-6way-r1286_sym24`

## Output

`workers/dispatcher/harvest-11way-r1287_sym24/round-1287/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

