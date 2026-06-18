# harvest-3way-r707 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R707 ctrl_bpc |
|--------|--------|--------------:|
| ST2KR | fork-davidwuchn-mmllm-claude-train-sym24-1c4b3c06-ST2KR | 3.9301 |
| wkSQv | origin/claude/train-sym24-a38c7691-wkSQv | 3.9326 |
| EW3WZ | fork-joly-os-mmllm-claude-train-sym24-29bd5b21-EW3WZ | 3.9379 |
| **mean** | | **3.9335** |
| **best** | | **3.9301** |

## Chain progression R706 → R707

Previous harvest: `workers/dispatcher/harvest-6way-r706_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7610         | 3.9335         | +0.1725 |
| ctrl_bpc best  | 3.5805         | 3.9301         | +0.3496 |

## Per-round trajectory (best bird: ST2KR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 707 | 6369 | 3.9301 | +0.9529 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r706_sym24`

## Output

`workers/dispatcher/harvest-3way-r707_sym24/round-707/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

