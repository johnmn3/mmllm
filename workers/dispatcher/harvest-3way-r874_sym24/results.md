# harvest-3way-r874 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R874 ctrl_bpc |
|--------|--------|--------------:|
| Pbmao | origin/claude/train-sym24-cfe3daa7-Pbmao | 3.0236 |
| SQvJM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ee2ef70c-SQvJM | 3.0543 |
| Tn4LD | fork-joly-os-mmllm-claude-train-sym24-6d840fc5-Tn4LD | 3.2453 |
| **mean** | | **3.1077** |
| **best** | | **3.0236** |

## Chain progression R873 → R874

Previous harvest: `workers/dispatcher/harvest-10way-r873_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0001         | 3.1077         | +0.1076 |
| ctrl_bpc best  | 2.8543         | 3.0236         | +0.1693 |

## Per-round trajectory (best bird: Pbmao)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 874 | 6644 | 3.0236 | +0.2630 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r873_sym24`
  - `workers/dispatcher/harvest-6way-r873_sym24`

## Output

`workers/dispatcher/harvest-3way-r874_sym24/round-874/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

