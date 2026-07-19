# harvest-3way-r961 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R961 ctrl_bpc |
|--------|--------|--------------:|
| E3w3S | origin/claude/train-sym24-2c6d3c59-E3w3S | 2.6222 |
| uc1hp | origin/claude/train-sym24-5288a93f-uc1hp | 3.0225 |
| SJAuT | fork-joly-os-mmllm-claude-train-sym24-cb58b1b5-SJAuT | 3.0302 |
| **mean** | | **2.8916** |
| **best** | | **2.6222** |

## Chain progression R960 → R961

Previous harvest: `workers/dispatcher/harvest-11way-r960_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8917         | 2.8916         | -0.0001 |
| ctrl_bpc best  | 2.6345         | 2.6222         | -0.0123 |

## Per-round trajectory (best bird: E3w3S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 961 | 5379 | 2.6222 | +0.1687 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r960_sym24`

## Output

`workers/dispatcher/harvest-3way-r961_sym24/round-961/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

