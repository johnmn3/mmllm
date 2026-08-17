# harvest-6way-r1228 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1228 ctrl_bpc |
|--------|--------|--------------:|
| Kuq87 | fork-joly-os-mmllm-claude-train-sym24-e133798e-Kuq87 | 2.2490 |
| 0S8tU | origin/claude/train-sym24-7ca5d661-0S8tU | 2.4572 |
| ibA9u | fork-SeniorCareMarket-mmllm-claude-train-sym24-229ab883-ibA9u | 2.4572 |
| pkdpf | fork-joly-os-mmllm-claude-train-sym24-3183ad35-pkdpf | 2.4607 |
| Nxy0F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e217469e-Nxy0F | 2.4690 |
| qYePt | fork-slaa-us-mmllm-claude-train-sym24-1f234a54-qYePt | 2.4710 |
| **mean** | | **2.4274** |
| **best** | | **2.2490** |

## Chain progression R1227 → R1228

Previous harvest: `workers/dispatcher/harvest-5way-r1227_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4602         | 2.4274         | -0.0328 |
| ctrl_bpc best  | 2.2704         | 2.2490         | -0.0214 |

## Per-round trajectory (best bird: Kuq87)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1228 | 6554 | 2.2490 | +0.2726 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1227_sym24`
  - `workers/dispatcher/harvest-5way-r1227_sym24`

## Output

`workers/dispatcher/harvest-6way-r1228_sym24/round-1228/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

