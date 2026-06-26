# harvest-7way-r773 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R773 ctrl_bpc |
|--------|--------|--------------:|
| oQDIk | fork-SeniorCareMarket-mmllm-claude-train-sym24-ff188f78-oQDIk | 3.2035 |
| a5iQK | fork-slaa-us-mmllm-claude-train-sym24-3d28b33d-a5iQK | 3.2133 |
| KDQHJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d923efd4-KDQHJ | 3.2566 |
| i6AgT | fork-davidwuchn-mmllm-claude-train-sym24-dcc57613-i6AgT | 3.2637 |
| GLfcR | fork-joly-os-mmllm-claude-train-sym24-f45528f5-GLfcR | 3.3546 |
| 6Vqxm | origin/claude/train-sym24-92fb2797-6Vqxm | 3.5969 |
| OYwcc | fork-joly-os-mmllm-claude-train-sym24-63413d80-OYwcc | 3.6120 |
| **mean** | | **3.3572** |
| **best** | | **3.2035** |

## Chain progression R772 → R773

Previous harvest: `workers/dispatcher/harvest-4way-r772_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2608         | 3.3572         | +0.0964 |
| ctrl_bpc best  | 3.2130         | 3.2035         | -0.0095 |

## Per-round trajectory (best bird: oQDIk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 773 | 6801 | 3.2035 | +0.5280 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r772_sym24`
  - `workers/dispatcher/harvest-2way-r772_sym24`

## Output

`workers/dispatcher/harvest-7way-r773_sym24/round-773/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

