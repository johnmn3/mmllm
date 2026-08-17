# harvest-10way-r1234 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1234 ctrl_bpc |
|--------|--------|--------------:|
| Jg0wn | fork-slaa-us-mmllm-claude-train-sym24-aba03083-Jg0wn | 2.2531 |
| vfzgo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-16d243a7-vfzgo | 2.2628 |
| mZaq1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-412b0a69-mZaq1 | 2.2658 |
| HrPWm | origin/claude/train-sym24-e2b1318e-HrPWm | 2.2779 |
| qoh2Q | fork-joly-os-mmllm-claude-train-sym24-5bfb2533-qoh2Q | 2.4522 |
| PFAvK | origin/claude/train-sym24-f5523c15-PFAvK | 2.4614 |
| cT8Ws | fork-joly-os-mmllm-claude-train-sym24-2908014c-cT8Ws | 2.4624 |
| ag5Pe | fork-slaa-us-mmllm-claude-train-sym24-b77a50b2-ag5Pe | 2.4653 |
| Vrstf | fork-SeniorCareMarket-mmllm-claude-train-sym24-49d274a3-Vrstf | 2.6555 |
| 3jqqw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-903104d2-3jqqw | 2.6602 |
| **mean** | | **2.4217** |
| **best** | | **2.2531** |

## Chain progression R1233 → R1234

Previous harvest: `workers/dispatcher/harvest-10way-r1233_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3988         | 2.4217         | +0.0229 |
| ctrl_bpc best  | 2.2453         | 2.2531         | +0.0078 |

## Per-round trajectory (best bird: Jg0wn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1234 | 6326 | 2.2531 | +0.2669 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1233_sym24`
  - `workers/dispatcher/harvest-7way-r1233_sym24`

## Output

`workers/dispatcher/harvest-10way-r1234_sym24/round-1234/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

