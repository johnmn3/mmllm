# harvest-3way-r1372 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1372 ctrl_bpc |
|--------|--------|--------------:|
| CGxkI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a6889df5-CGxkI | 3.1144 |
| wmmuH | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1dd121a-wmmuH | 3.1195 |
| irLEm | fork-joly-os-mmllm-claude-train-sym24-82a8eb16-irLEm | 3.4577 |
| **mean** | | **3.2305** |
| **best** | | **3.1144** |

## Chain progression R1371 → R1372

Previous harvest: `workers/dispatcher/harvest-5way-r1371_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2592         | 3.2305         | -0.0287 |
| ctrl_bpc best  | 3.1489         | 3.1144         | -0.0345 |

## Per-round trajectory (best bird: CGxkI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1372 | 6805 | 3.1144 | +0.1240 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1371_sym24`

## Output

`workers/dispatcher/harvest-3way-r1372_sym24/round-1372/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

