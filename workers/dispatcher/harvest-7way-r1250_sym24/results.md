# harvest-7way-r1250 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1250 ctrl_bpc |
|--------|--------|--------------:|
| Aiuoy | fork-slaa-us-mmllm-claude-train-sym24-4e613d61-Aiuoy | 2.2456 |
| UA07u | fork-SeniorCareMarket-mmllm-claude-train-sym24-f60bf901-UA07u | 2.2533 |
| kqQR1 | origin/claude/train-sym24-d3d6fe4c-kqQR1 | 2.4347 |
| K4LCf | fork-joly-os-mmllm-claude-train-sym24-432e7d01-K4LCf | 2.4437 |
| RXzDl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65c38320-RXzDl | 2.6289 |
| J443I | fork-slaa-us-mmllm-claude-train-sym24-d9584554-J443I | 2.6394 |
| G45pf | fork-joly-os-mmllm-claude-train-sym24-6b8a22a4-G45pf | 2.6423 |
| **mean** | | **2.4697** |
| **best** | | **2.2456** |

## Chain progression R1249 → R1250

Previous harvest: `workers/dispatcher/harvest-5way-r1249_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3684         | 2.4697         | +0.1013 |
| ctrl_bpc best  | 2.2424         | 2.2456         | +0.0032 |

## Per-round trajectory (best bird: Aiuoy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1250 | 3627 | 2.2456 | +0.2346 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1249_sym24`
  - `workers/dispatcher/harvest-5way-r1249_sym24`

## Output

`workers/dispatcher/harvest-7way-r1250_sym24/round-1250/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

