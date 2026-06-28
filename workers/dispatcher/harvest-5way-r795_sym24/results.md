# harvest-5way-r795 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R795 ctrl_bpc |
|--------|--------|--------------:|
| j2c3I | fork-SeniorCareMarket-mmllm-claude-train-sym24-88d2ffc4-j2c3I | 3.1174 |
| 8LPN0 | fork-joly-os-mmllm-claude-train-sym24-85894239-8LPN0 | 3.1206 |
| eq1uN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87f6799b-eq1uN | 3.1340 |
| O10rf | origin/claude/train-sym24-483f7535-O10rf | 3.1487 |
| 1eQV7 | fork-slaa-us-mmllm-claude-train-sym24-37b440b5-1eQV7 | 3.2595 |
| **mean** | | **3.1560** |
| **best** | | **3.1174** |

## Chain progression R794 → R795

Previous harvest: `workers/dispatcher/harvest-13way-r794_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2757         | 3.1560         | -0.1197 |
| ctrl_bpc best  | 3.1174         | 3.1174         | +0.0000 |

## Per-round trajectory (best bird: j2c3I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 795 | 6713 | 3.1174 | +0.3857 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r794_sym24`

## Output

`workers/dispatcher/harvest-5way-r795_sym24/round-795/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

