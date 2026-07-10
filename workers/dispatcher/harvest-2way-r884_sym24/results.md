# harvest-2way-r884 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R884 ctrl_bpc |
|--------|--------|--------------:|
| AXMJd | fork-joly-os-mmllm-claude-train-sym24-a0d72084-AXMJd | 2.9967 |
| dtDeL | fork-slaa-us-mmllm-claude-train-sym24-11022a3a-dtDeL | 3.2181 |
| **mean** | | **3.1074** |
| **best** | | **2.9967** |

## Chain progression R883 → R884

Previous harvest: `workers/dispatcher/harvest-6way-r883_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9553         | 3.1074         | +0.1521 |
| ctrl_bpc best  | 2.8263         | 2.9967         | +0.1704 |

## Per-round trajectory (best bird: AXMJd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 884 | 6555 | 2.9967 | +0.2886 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r883_sym24`

## Output

`workers/dispatcher/harvest-2way-r884_sym24/round-884/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

