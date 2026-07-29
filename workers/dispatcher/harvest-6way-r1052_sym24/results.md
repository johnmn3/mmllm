# harvest-6way-r1052 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1052 ctrl_bpc |
|--------|--------|--------------:|
| TH3OE | origin/claude/train-sym24-eac1afde-TH3OE | 2.4646 |
| dYfLq | fork-joly-os-mmllm-claude-train-sym24-3c4e9dca-dYfLq | 2.4693 |
| h07jU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d8fc7724-h07jU | 2.4883 |
| FraAs | fork-slaa-us-mmllm-claude-train-sym24-02eb1b82-FraAs | 2.8512 |
| 4ysAr | fork-joly-os-mmllm-claude-train-sym24-51d565d4-4ysAr | 2.8575 |
| XDpkL | fork-SeniorCareMarket-mmllm-claude-train-sym24-d55b4c59-XDpkL | 2.9691 |
| **mean** | | **2.6833** |
| **best** | | **2.4646** |

## Chain progression R1051 → R1052

Previous harvest: `workers/dispatcher/harvest-5way-r1051_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5218         | 2.6833         | +0.1615 |
| ctrl_bpc best  | 2.4703         | 2.4646         | -0.0057 |

## Per-round trajectory (best bird: TH3OE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1052 | 6770 | 2.4646 | +0.2173 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1051_sym24`
  - `workers/dispatcher/harvest-5way-r1051_sym24`

## Output

`workers/dispatcher/harvest-6way-r1052_sym24/round-1052/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

