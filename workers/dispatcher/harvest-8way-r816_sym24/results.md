# harvest-8way-r816 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R816 ctrl_bpc |
|--------|--------|--------------:|
| eDfmo | fork-joly-os-mmllm-claude-train-sym24-2f867e8d-eDfmo | 3.0290 |
| nlZKz | fork-slaa-us-mmllm-claude-train-sym24-c08673e7-nlZKz | 3.0399 |
| rDLIy | origin/claude/train-sym24-90ee88f8-rDLIy | 3.0491 |
| BMwVP | origin/claude/train-sym24-c0472120-BMwVP | 3.0501 |
| mUWxB | fork-SeniorCareMarket-mmllm-claude-train-sym24-7968473f-mUWxB | 3.0510 |
| 12deu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c2514301-12deu | 3.1861 |
| 8el1A | fork-davidwuchn-mmllm-claude-train-sym24-01c7cb0a-8el1A | 3.3974 |
| OkLCg | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7fd79807-OkLCg | 3.4204 |
| **mean** | | **3.1529** |
| **best** | | **3.0290** |

## Chain progression R815 → R816

Previous harvest: `workers/dispatcher/harvest-10way-r815_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2202         | 3.1529         | -0.0673 |
| ctrl_bpc best  | 3.0507         | 3.0290         | -0.0217 |

## Per-round trajectory (best bird: eDfmo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 816 | 6424 | 3.0290 | +0.5567 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r815_sym24`

## Output

`workers/dispatcher/harvest-8way-r816_sym24/round-816/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

