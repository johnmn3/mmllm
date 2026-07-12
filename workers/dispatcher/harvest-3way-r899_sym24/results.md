# harvest-3way-r899 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R899 ctrl_bpc |
|--------|--------|--------------:|
| tnvOa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68f94186-tnvOa | 2.8029 |
| DQlXJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-2f1c521e-DQlXJ | 2.9634 |
| 19oCC | fork-joly-os-mmllm-claude-train-sym24-9c2dba47-19oCC | 2.9797 |
| **mean** | | **2.9153** |
| **best** | | **2.8029** |

## Chain progression R898 → R899

Previous harvest: `workers/dispatcher/harvest-8way-r898_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9122         | 2.9153         | +0.0031 |
| ctrl_bpc best  | 2.7995         | 2.8029         | +0.0034 |

## Per-round trajectory (best bird: tnvOa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 899 | 4478 | 2.8029 | +0.2132 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r898_sym24`
  - `workers/dispatcher/harvest-8way-r898_sym24`

## Output

`workers/dispatcher/harvest-3way-r899_sym24/round-899/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

