# harvest-5way-r1348 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1348 ctrl_bpc |
|--------|--------|--------------:|
| yWZmZ | origin/claude/train-sym24-ed98ef48-yWZmZ | 3.2271 |
| Fasza | origin/claude/train-sym24-246b56d5-Fasza | 3.2433 |
| ilqvU | origin/claude/train-sym24-4a7b29e2-ilqvU | 3.2718 |
| 5KViK | fork-SeniorCareMarket-mmllm-claude-train-sym24-b6d6a334-5KViK | 3.3214 |
| FoQ6n | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1e5698ae-FoQ6n | 3.7492 |
| **mean** | | **3.3626** |
| **best** | | **3.2271** |

## Chain progression R1347 → R1348

Previous harvest: `workers/dispatcher/harvest-4way-r1347_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2444         | 3.3626         | +0.1182 |
| ctrl_bpc best  | 3.1834         | 3.2271         | +0.0437 |

## Per-round trajectory (best bird: yWZmZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1348 | 5241 | 3.2271 | +0.0912 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1347_sym24`
  - `workers/dispatcher/harvest-3way-r1347_sym24`
  - `workers/dispatcher/harvest-4way-r1347_sym24`

## Output

`workers/dispatcher/harvest-5way-r1348_sym24/round-1348/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

