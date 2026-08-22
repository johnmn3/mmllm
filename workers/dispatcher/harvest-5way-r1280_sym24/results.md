# harvest-5way-r1280 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1280 ctrl_bpc |
|--------|--------|--------------:|
| xdUo2 | origin/claude/train-sym24-509c6fc6-xdUo2 | 2.2393 |
| F2EUA | fork-slaa-us-mmllm-claude-train-sym24-4279b51b-F2EUA | 2.4158 |
| mvPEF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f2ca899-mvPEF | 2.6170 |
| kpGUB | fork-joly-os-mmllm-claude-train-sym24-3abc2404-kpGUB | 2.6186 |
| 8qt2H | fork-SeniorCareMarket-mmllm-claude-train-sym24-26c3aaf1-8qt2H | 2.6240 |
| **mean** | | **2.5029** |
| **best** | | **2.2393** |

## Chain progression R1279 → R1280

Previous harvest: `workers/dispatcher/harvest-8way-r1279_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4284         | 2.5029         | +0.0745 |
| ctrl_bpc best  | 2.2426         | 2.2393         | -0.0033 |

## Per-round trajectory (best bird: xdUo2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1280 | 6552 | 2.2393 | +0.2514 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1279_sym24`
  - `workers/dispatcher/harvest-8way-r1279_sym24`

## Output

`workers/dispatcher/harvest-5way-r1280_sym24/round-1280/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

