# harvest-3way-r36 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R36 ctrl_bpc |
|--------|--------|--------------:|
| HjyYS | fork-SeniorCareMarket-mmllm-claude-train-ee69a851-HjyYS | 1.0954 |
| bccSP | origin/claude/train-19ea2995-bccSP | 1.1230 |
| oQeuA | origin/claude/train-0ec357cb-oQeuA | 1.1527 |
| **mean** | | **1.1237** |
| **best** | | **1.0954** |

## Chain progression R31 → R36

Previous harvest: `workers/dispatcher/harvest-2way-r31`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.2092         | 1.1237         | -0.0855 |
| ctrl_bpc best  | 1.1196         | 1.0954         | -0.0242 |

## Per-round trajectory (best bird: HjyYS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 32 | 525 | 1.1019 | +0.0049 |
| 33 | 530 | 1.1374 | +0.0108 |
| 34 | 552 | 1.0991 | +0.0070 |
| 35 | 484 | 1.1084 | +0.0078 |
| 36 | 522 | 1.0954 | +0.0103 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **140 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r31`

## Output

`workers/dispatcher/harvest-3way-r36/round-36/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

