# harvest-2way-r888 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R888 ctrl_bpc |
|--------|--------|--------------:|
| kpYvJ | origin/claude/train-sym24-4f5fb866-kpYvJ | 2.8457 |
| kkpTp | fork-slaa-us-mmllm-claude-train-sym24-dbe87f9e-kkpTp | 2.9938 |
| **mean** | | **2.9197** |
| **best** | | **2.8457** |

## Chain progression R887 → R888

Previous harvest: `workers/dispatcher/harvest-4way-r887_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0667         | 2.9197         | -0.1470 |
| ctrl_bpc best  | 2.8444         | 2.8457         | +0.0013 |

## Per-round trajectory (best bird: kpYvJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 888 | 6325 | 2.8457 | +0.1927 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r887_sym24`

## Output

`workers/dispatcher/harvest-2way-r888_sym24/round-888/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

