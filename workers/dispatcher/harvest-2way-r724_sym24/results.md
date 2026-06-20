# harvest-2way-r724 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R724 ctrl_bpc |
|--------|--------|--------------:|
| njaiM | fork-davidwuchn-mmllm-claude-train-sym24-72054069-njaiM | 3.4694 |
| zoQqw | fork-joly-os-mmllm-claude-train-sym24-0bc6bc80-zoQqw | 3.8146 |
| **mean** | | **3.6420** |
| **best** | | **3.4694** |

## Chain progression R723 → R724

Previous harvest: `workers/dispatcher/harvest-12way-r723_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5756         | 3.6420         | +0.0664 |
| ctrl_bpc best  | 3.5068         | 3.4694         | -0.0374 |

## Per-round trajectory (best bird: njaiM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 724 | 6544 | 3.4694 | +0.8678 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r723_sym24`

## Output

`workers/dispatcher/harvest-2way-r724_sym24/round-724/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

