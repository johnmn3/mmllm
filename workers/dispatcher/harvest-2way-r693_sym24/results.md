# harvest-2way-r693 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R693 ctrl_bpc |
|--------|--------|--------------:|
| JcR03 | fork-slaa-us-mmllm-claude-train-sym24-e900300e-JcR03 | 3.6653 |
| j0IJR | fork-SeniorCareMarket-mmllm-claude-train-sym24-19347084-j0IJR | 3.7200 |
| **mean** | | **3.6926** |
| **best** | | **3.6653** |

## Chain progression R692 → R693

Previous harvest: `workers/dispatcher/harvest-10way-r692_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7425         | 3.6926         | -0.0499 |
| ctrl_bpc best  | 3.6828         | 3.6653         | -0.0175 |

## Per-round trajectory (best bird: JcR03)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 693 | 6397 | 3.6653 | +0.5499 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r692_sym24`

## Output

`workers/dispatcher/harvest-2way-r693_sym24/round-693/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

