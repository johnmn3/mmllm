# harvest-3way-r906 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R906 ctrl_bpc |
|--------|--------|--------------:|
| lxWjg | origin/claude/train-sym24-8f3c5a4d-lxWjg | 2.7693 |
| PMzcn | fork-joly-os-mmllm-claude-train-sym24-f54706d8-PMzcn | 2.7776 |
| TlkS5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-32f5952c-TlkS5 | 2.7807 |
| **mean** | | **2.7759** |
| **best** | | **2.7693** |

## Chain progression R905 → R906

Previous harvest: `workers/dispatcher/harvest-5way-r905_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8930         | 2.7759         | -0.1171 |
| ctrl_bpc best  | 2.7738         | 2.7693         | -0.0045 |

## Per-round trajectory (best bird: lxWjg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 906 | 4661 | 2.7693 | +0.3314 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r905_sym24`

## Output

`workers/dispatcher/harvest-3way-r906_sym24/round-906/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

