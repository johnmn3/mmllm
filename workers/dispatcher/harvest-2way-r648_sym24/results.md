# harvest-2way-r648 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R648 ctrl_bpc |
|--------|--------|--------------:|
| mILVN | fork-joly-os-mmllm-claude-train-sym24-8997d026-mILVN | 4.3865 |
| G3uzH | fork-SeniorCareMarket-mmllm-claude-train-sym24-a682b1df-G3uzH | 4.8156 |
| **mean** | | **4.6010** |
| **best** | | **4.3865** |

## Chain progression R647 → R648

Previous harvest: `workers/dispatcher/harvest-5way-r647_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.5329         | 4.6010         | +0.0682 |
| ctrl_bpc best  | 4.4195         | 4.3865         | -0.0330 |

## Per-round trajectory (best bird: mILVN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 648 | 6330 | 4.3865 | +0.0725 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r647_sym24`

## Output

`workers/dispatcher/harvest-2way-r648_sym24/round-648/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

