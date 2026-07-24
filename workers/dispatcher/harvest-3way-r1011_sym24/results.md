# harvest-3way-r1011 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1011 ctrl_bpc |
|--------|--------|--------------:|
| 9Qckv | origin/claude/train-sym24-7cae2b7c-9Qckv | 2.5378 |
| 9JeRx | fork-slaa-us-mmllm-claude-train-sym24-99e14188-9JeRx | 2.5642 |
| NbfWS | origin/claude/train-sym24-eed39fa1-NbfWS | 2.7636 |
| **mean** | | **2.6219** |
| **best** | | **2.5378** |

## Chain progression R1010 → R1011

Previous harvest: `workers/dispatcher/harvest-5way-r1010_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7164         | 2.6219         | -0.0945 |
| ctrl_bpc best  | 2.5728         | 2.5378         | -0.0350 |

## Per-round trajectory (best bird: 9Qckv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1011 | 6653 | 2.5378 | +0.1817 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1010_sym24`

## Output

`workers/dispatcher/harvest-3way-r1011_sym24/round-1011/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

