# harvest-2way-r1172 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1172 ctrl_bpc |
|--------|--------|--------------:|
| Mc0i0 | fork-joly-os-mmllm-claude-train-sym24-a2dbb7bb-Mc0i0 | 2.3400 |
| gchFc | origin/claude/train-sym24-4cd713c8-gchFc | 2.7083 |
| **mean** | | **2.5241** |
| **best** | | **2.3400** |

## Chain progression R1171 → R1172

Previous harvest: `workers/dispatcher/harvest-7way-r1171_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4683         | 2.5241         | +0.0558 |
| ctrl_bpc best  | 2.3347         | 2.3400         | +0.0053 |

## Per-round trajectory (best bird: Mc0i0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1172 | 6435 | 2.3400 | +0.2431 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1171_sym24`

## Output

`workers/dispatcher/harvest-2way-r1172_sym24/round-1172/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

