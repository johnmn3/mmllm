# harvest-6way-r1116 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1116 ctrl_bpc |
|--------|--------|--------------:|
| U6AbG | fork-SeniorCareMarket-mmllm-claude-train-sym24-51ece93a-U6AbG | 2.3779 |
| XWKOz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-de99d9de-XWKOz | 2.3925 |
| DH6cL | origin/claude/train-sym24-ff2df38e-DH6cL | 2.3941 |
| 5fyiq | fork-joly-os-mmllm-claude-train-sym24-6d63091a-5fyiq | 2.5663 |
| l6KxD | fork-slaa-us-mmllm-claude-train-sym24-1f643dbd-l6KxD | 2.7747 |
| mss7c | origin/claude/train-sym24-dd09664b-mss7c | 2.8369 |
| **mean** | | **2.5571** |
| **best** | | **2.3779** |

## Chain progression R1115 → R1116

Previous harvest: `workers/dispatcher/harvest-6way-r1115_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4778         | 2.5571         | +0.0793 |
| ctrl_bpc best  | 2.3667         | 2.3779         | +0.0112 |

## Per-round trajectory (best bird: U6AbG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1116 | 6429 | 2.3779 | +0.2414 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1115_sym24`
  - `workers/dispatcher/harvest-6way-r1115_sym24`

## Output

`workers/dispatcher/harvest-6way-r1116_sym24/round-1116/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

