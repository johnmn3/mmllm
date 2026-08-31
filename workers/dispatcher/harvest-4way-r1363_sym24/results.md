# harvest-4way-r1363 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1363 ctrl_bpc |
|--------|--------|--------------:|
| Cj5aC | origin/claude/train-sym24-7e900abd-Cj5aC | 3.1271 |
| hKji1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b95b4c13-hKji1 | 3.1458 |
| ddq06 | fork-joly-os-mmllm-claude-train-sym24-a48c12da-ddq06 | 3.1931 |
| 07fIk | origin/claude/train-sym24-93ca8692-07fIk | 3.5214 |
| **mean** | | **3.2468** |
| **best** | | **3.1271** |

## Chain progression R1362 → R1363

Previous harvest: `workers/dispatcher/harvest-4way-r1362_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3538         | 3.2468         | -0.1070 |
| ctrl_bpc best  | 3.1484         | 3.1271         | -0.0213 |

## Per-round trajectory (best bird: Cj5aC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1363 | 5304 | 3.1271 | +0.1201 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1362_sym24`
  - `workers/dispatcher/harvest-4way-r1362_sym24`

## Output

`workers/dispatcher/harvest-4way-r1363_sym24/round-1363/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

