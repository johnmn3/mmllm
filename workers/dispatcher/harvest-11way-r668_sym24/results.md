# harvest-11way-r668 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R668 ctrl_bpc |
|--------|--------|--------------:|
| w2Ytv | fork-slaa-us-mmllm-claude-train-sym24-7a12ba47-w2Ytv | 3.8806 |
| GHItg | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1b5bf6a1-GHItg | 3.9163 |
| y1SyD | fork-davidwuchn-mmllm-claude-train-sym24-143a9bcd-y1SyD | 3.9269 |
| Xtv32 | origin/claude/train-sym24-6256eda3-Xtv32 | 3.9562 |
| xQyis | fork-SeniorCareMarket-mmllm-claude-train-sym24-ef26f6e0-xQyis | 3.9625 |
| sAnII | fork-slaa-us-mmllm-claude-train-sym24-60e24e2e-sAnII | 4.0710 |
| tut30 | fork-joly-os-mmllm-claude-train-sym24-032cdc46-tut30 | 4.2313 |
| wUC7r | fork-joly-os-mmllm-claude-train-sym24-ea9bae1d-wUC7r | 4.2346 |
| bJwN0 | origin/claude/train-sym24-aff1c2d5-bJwN0 | 4.2370 |
| vhs3H | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-405672a8-vhs3H | 4.2481 |
| wS5SF | fork-davidwuchn-mmllm-claude-train-sym24-fe6fe8b5-wS5SF | 4.2493 |
| **mean** | | **4.0831** |
| **best** | | **3.8806** |

## Chain progression R667 → R668

Previous harvest: `workers/dispatcher/harvest-9way-r667_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0067         | 4.0831         | +0.0764 |
| ctrl_bpc best  | 3.8934         | 3.8806         | -0.0128 |

## Per-round trajectory (best bird: w2Ytv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 668 | 6626 | 3.8806 | +0.2720 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r667_sym24`
  - `workers/dispatcher/harvest-9way-r667_sym24`

## Output

`workers/dispatcher/harvest-11way-r668_sym24/round-668/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

