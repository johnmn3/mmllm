# harvest-2way-r710 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R710 ctrl_bpc |
|--------|--------|--------------:|
| opR6X | fork-joly-os-mmllm-claude-train-sym24-a48f33f2-opR6X | 3.5599 |
| 5CNsN | fork-davidwuchn-mmllm-claude-train-sym24-d45b670b-5CNsN | 3.6106 |
| **mean** | | **3.5852** |
| **best** | | **3.5599** |

## Chain progression R709 → R710

Previous harvest: `workers/dispatcher/harvest-13way-r709_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6962         | 3.5852         | -0.1110 |
| ctrl_bpc best  | 3.5610         | 3.5599         | -0.0011 |

## Per-round trajectory (best bird: opR6X)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 710 | 6534 | 3.5599 | +0.5949 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r709_sym24`

## Output

`workers/dispatcher/harvest-2way-r710_sym24/round-710/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

