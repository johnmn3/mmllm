# harvest-3way-r798 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R798 ctrl_bpc |
|--------|--------|--------------:|
| 9Qokt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-58da584b-9Qokt | 3.1143 |
| EShSp | origin/claude/train-sym24-eedf5491-EShSp | 3.1305 |
| e79SU | fork-joly-os-mmllm-claude-train-sym24-e8ce2079-e79SU | 3.5025 |
| **mean** | | **3.2491** |
| **best** | | **3.1143** |

## Chain progression R797 → R798

Previous harvest: `workers/dispatcher/harvest-3way-r797_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4189         | 3.2491         | -0.1698 |
| ctrl_bpc best  | 3.2583         | 3.1143         | -0.1440 |

## Per-round trajectory (best bird: 9Qokt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 798 | 4158 | 3.1143 | +0.4943 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r797_sym24`

## Output

`workers/dispatcher/harvest-3way-r798_sym24/round-798/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

