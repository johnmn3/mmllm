# harvest-7way-r693 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R693 ctrl_bpc |
|--------|--------|--------------:|
| vHAjX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2dc5ec19-vHAjX | 3.6493 |
| JcR03 | fork-slaa-us-mmllm-claude-train-sym24-e900300e-JcR03 | 3.6653 |
| DZpzX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f573f515-DZpzX | 3.6940 |
| j0IJR | fork-SeniorCareMarket-mmllm-claude-train-sym24-19347084-j0IJR | 3.7200 |
| rV90c | fork-joly-os-mmllm-claude-train-sym24-e742f680-rV90c | 4.0093 |
| L5CdJ | fork-davidwuchn-mmllm-claude-train-sym24-8450428f-L5CdJ | 4.0123 |
| JeNZA | origin/claude/train-sym24-c43b9e60-JeNZA | 4.0215 |
| **mean** | | **3.8245** |
| **best** | | **3.6493** |

## Chain progression R692 → R693

Previous harvest: `workers/dispatcher/harvest-5way-r692_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7681         | 3.8245         | +0.0564 |
| ctrl_bpc best  | 3.6828         | 3.6493         | -0.0335 |

## Per-round trajectory (best bird: vHAjX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 693 | 6918 | 3.6493 | +0.4607 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r692_sym24`
  - `workers/dispatcher/harvest-5way-r692_sym24`

## Output

`workers/dispatcher/harvest-7way-r693_sym24/round-693/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

