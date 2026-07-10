# harvest-10way-r880 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R880 ctrl_bpc |
|--------|--------|--------------:|
| hJUwF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cf918033-hJUwF | 2.8392 |
| uo1Lv | origin/claude/train-sym24-c266363f-uo1Lv | 2.8543 |
| XVqBC | fork-SeniorCareMarket-mmllm-claude-train-sym24-9034cd48-XVqBC | 3.0003 |
| 7gkjn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e73afdfa-7gkjn | 3.0043 |
| VMLJK | fork-slaa-us-mmllm-claude-train-sym24-ecd04936-VMLJK | 3.0101 |
| WrKRm | origin/claude/train-sym24-e9d7de88-WrKRm | 3.0153 |
| 18ZFZ | fork-slaa-us-mmllm-claude-train-sym24-90a28c70-18ZFZ | 3.0162 |
| c8Dvf | fork-SeniorCareMarket-mmllm-claude-train-sym24-12857e69-c8Dvf | 3.0611 |
| Sq3h7 | origin/claude/train-sym24-3504e6f9-Sq3h7 | 3.2129 |
| OiQX7 | fork-joly-os-mmllm-claude-train-sym24-c45d0173-OiQX7 | 3.2295 |
| **mean** | | **3.0243** |
| **best** | | **2.8392** |

## Chain progression R879 → R880

Previous harvest: `workers/dispatcher/harvest-2way-r879_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0155         | 3.0243         | +0.0088 |
| ctrl_bpc best  | 3.0137         | 2.8392         | -0.1745 |

## Per-round trajectory (best bird: hJUwF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 880 | 6695 | 2.8392 | +0.2840 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r879_sym24`
  - `workers/dispatcher/harvest-2way-r879_sym24`

## Output

`workers/dispatcher/harvest-10way-r880_sym24/round-880/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

