# harvest-2way-r742 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R742 ctrl_bpc |
|--------|--------|--------------:|
| zlabk | fork-SeniorCareMarket-mmllm-claude-train-sym24-077af999-zlabk | 3.4191 |
| Hewby | fork-joly-os-mmllm-claude-train-sym24-3e9f1ab8-Hewby | 3.4264 |
| **mean** | | **3.4227** |
| **best** | | **3.4191** |

## Chain progression R741 → R742

Previous harvest: `workers/dispatcher/harvest-12way-r741_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4675         | 3.4227         | -0.0448 |
| ctrl_bpc best  | 3.3649         | 3.4191         | +0.0542 |

## Per-round trajectory (best bird: zlabk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 742 | 6465 | 3.4191 | +0.5179 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r741_sym24`

## Output

`workers/dispatcher/harvest-2way-r742_sym24/round-742/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

