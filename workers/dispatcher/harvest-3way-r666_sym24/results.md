# harvest-3way-r666 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R666 ctrl_bpc |
|--------|--------|--------------:|
| s5oDr | fork-slaa-us-mmllm-claude-train-sym24-eb2a5166-s5oDr | 3.9071 |
| 5Zvb1 | fork-davidwuchn-mmllm-claude-train-sym24-2366472c-5Zvb1 | 3.9500 |
| FuzhD | fork-joly-os-mmllm-claude-train-sym24-b26b367e-FuzhD | 4.3846 |
| **mean** | | **4.0806** |
| **best** | | **3.9071** |

## Chain progression R665 → R666

Previous harvest: `workers/dispatcher/harvest-13way-r665_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0372         | 4.0806         | +0.0434 |
| ctrl_bpc best  | 3.9294         | 3.9071         | -0.0223 |

## Per-round trajectory (best bird: s5oDr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 666 | 6436 | 3.9071 | +0.2395 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r665_sym24`

## Output

`workers/dispatcher/harvest-3way-r666_sym24/round-666/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

