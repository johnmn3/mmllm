# harvest-4way-r990 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R990 ctrl_bpc |
|--------|--------|--------------:|
| 1VoVQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe195af6-1VoVQ | 2.5864 |
| UwkH0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-4449f39a-UwkH0 | 2.6003 |
| Q3mJO | fork-joly-os-mmllm-claude-train-sym24-c315b417-Q3mJO | 2.6091 |
| PyWEG | origin/claude/train-sym24-1af20b06-PyWEG | 2.7902 |
| **mean** | | **2.6465** |
| **best** | | **2.5864** |

## Chain progression R989 → R990

Previous harvest: `workers/dispatcher/harvest-4way-r989_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6795         | 2.6465         | -0.0330 |
| ctrl_bpc best  | 2.5785         | 2.5864         | +0.0079 |

## Per-round trajectory (best bird: 1VoVQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 990 | 6856 | 2.5864 | +0.1815 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r989_sym24`
  - `workers/dispatcher/harvest-4way-r989_sym24`

## Output

`workers/dispatcher/harvest-4way-r990_sym24/round-990/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

