# harvest-3way-r1071 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1071 ctrl_bpc |
|--------|--------|--------------:|
| TRRx3 | origin/claude/train-sym24-f5998394-TRRx3 | 2.4404 |
| INgrW | fork-joly-os-mmllm-claude-train-sym24-2520123a-INgrW | 2.4456 |
| Vm7JP | origin/claude/train-sym24-474abefa-Vm7JP | 2.8247 |
| **mean** | | **2.5702** |
| **best** | | **2.4404** |

## Chain progression R1070 → R1071

Previous harvest: `workers/dispatcher/harvest-7way-r1070_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5612         | 2.5702         | +0.0090 |
| ctrl_bpc best  | 2.4377         | 2.4404         | +0.0027 |

## Per-round trajectory (best bird: TRRx3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1071 | 6567 | 2.4404 | +0.2302 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1070_sym24`

## Output

`workers/dispatcher/harvest-3way-r1071_sym24/round-1071/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

