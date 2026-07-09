# harvest-4way-r880 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R880 ctrl_bpc |
|--------|--------|--------------:|
| uo1Lv | origin/claude/train-sym24-c266363f-uo1Lv | 2.8543 |
| XVqBC | fork-SeniorCareMarket-mmllm-claude-train-sym24-9034cd48-XVqBC | 3.0003 |
| Sq3h7 | origin/claude/train-sym24-3504e6f9-Sq3h7 | 3.2129 |
| OiQX7 | fork-joly-os-mmllm-claude-train-sym24-c45d0173-OiQX7 | 3.2295 |
| **mean** | | **3.0742** |
| **best** | | **2.8543** |

## Chain progression R879 → R880

Previous harvest: `workers/dispatcher/harvest-2way-r879_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0155         | 3.0742         | +0.0587 |
| ctrl_bpc best  | 3.0137         | 2.8543         | -0.1594 |

## Per-round trajectory (best bird: uo1Lv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 880 | 5342 | 2.8543 | +0.3970 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r879_sym24`
  - `workers/dispatcher/harvest-2way-r879_sym24`

## Output

`workers/dispatcher/harvest-4way-r880_sym24/round-880/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

