# harvest-11way-r724 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R724 ctrl_bpc |
|--------|--------|--------------:|
| njaiM | fork-davidwuchn-mmllm-claude-train-sym24-72054069-njaiM | 3.4694 |
| RBBKR | fork-slaa-us-mmllm-claude-train-sym24-35308e24-RBBKR | 3.4778 |
| UeQea | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f061e2d-UeQea | 3.4801 |
| 8GUpf | origin/claude/train-sym24-62d50189-8GUpf | 3.4991 |
| bpcNG | fork-joly-os-mmllm-claude-train-sym24-f18deb52-bpcNG | 3.4995 |
| EwhSY | fork-slaa-us-mmllm-claude-train-sym24-014e4397-EwhSY | 3.5232 |
| 52GaJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6bb9dd0b-52GaJ | 3.5553 |
| vm4D4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ac4b4710-vm4D4 | 3.5562 |
| 3ke2P | origin/claude/train-sym24-68132ca0-3ke2P | 3.6398 |
| zoQqw | fork-joly-os-mmllm-claude-train-sym24-0bc6bc80-zoQqw | 3.8146 |
| htXuc | fork-davidwuchn-mmllm-claude-train-sym24-73fa512f-htXuc | 3.8258 |
| **mean** | | **3.5764** |
| **best** | | **3.4694** |

## Chain progression R723 → R724

Previous harvest: `workers/dispatcher/harvest-9way-r723_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5584         | 3.5764         | +0.0180 |
| ctrl_bpc best  | 3.5068         | 3.4694         | -0.0374 |

## Per-round trajectory (best bird: njaiM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 724 | 6544 | 3.4694 | +0.8678 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r723_sym24`
  - `workers/dispatcher/harvest-9way-r723_sym24`

## Output

`workers/dispatcher/harvest-11way-r724_sym24/round-724/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

