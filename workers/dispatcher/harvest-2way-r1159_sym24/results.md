# harvest-2way-r1159 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1159 ctrl_bpc |
|--------|--------|--------------:|
| fWymG | origin/claude/train-sym24-067a91b5-fWymG | 2.5238 |
| Y8RaR | fork-joly-os-mmllm-claude-train-sym24-5476341a-Y8RaR | 2.7123 |
| **mean** | | **2.6181** |
| **best** | | **2.5238** |

## Chain progression R1158 → R1159

Previous harvest: `workers/dispatcher/harvest-9way-r1158_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4916         | 2.6181         | +0.1265 |
| ctrl_bpc best  | 2.3258         | 2.5238         | +0.1980 |

## Per-round trajectory (best bird: fWymG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1159 | 6601 | 2.5238 | +0.2322 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1158_sym24`

## Output

`workers/dispatcher/harvest-2way-r1159_sym24/round-1159/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

