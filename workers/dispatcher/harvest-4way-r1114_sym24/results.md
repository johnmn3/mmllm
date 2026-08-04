# harvest-4way-r1114 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1114 ctrl_bpc |
|--------|--------|--------------:|
| YS4Nt | origin/claude/train-sym24-99b16eef-YS4Nt | 2.3835 |
| 6CWcN | fork-joly-os-mmllm-claude-train-sym24-44958197-6CWcN | 2.3901 |
| JHhr5 | fork-slaa-us-mmllm-claude-train-sym24-b78771cd-JHhr5 | 2.5695 |
| N4jA3 | fork-joly-os-mmllm-claude-train-sym24-ffbd8f85-N4jA3 | 2.5718 |
| **mean** | | **2.4787** |
| **best** | | **2.3835** |

## Chain progression R1113 → R1114

Previous harvest: `workers/dispatcher/harvest-9way-r1113_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5449         | 2.4787         | -0.0662 |
| ctrl_bpc best  | 2.3935         | 2.3835         | -0.0100 |

## Per-round trajectory (best bird: YS4Nt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1114 | 6817 | 2.3835 | +0.2365 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1113_sym24`
  - `workers/dispatcher/harvest-7way-r1113_sym24`

## Output

`workers/dispatcher/harvest-4way-r1114_sym24/round-1114/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

