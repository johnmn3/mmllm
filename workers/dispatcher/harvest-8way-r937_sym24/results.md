# harvest-8way-r937 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R937 ctrl_bpc |
|--------|--------|--------------:|
| U1mhs | fork-joly-os-mmllm-claude-train-sym24-69a25a4c-U1mhs | 2.6889 |
| YHujZ | fork-slaa-us-mmllm-claude-train-sym24-8c6152b6-YHujZ | 2.6959 |
| qEtnD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ff3b316c-qEtnD | 2.7008 |
| LRHV0 | origin/claude/train-sym24-dcddbc0c-LRHV0 | 2.7038 |
| oXiJs | fork-SeniorCareMarket-mmllm-claude-train-sym24-c1162de0-oXiJs | 2.7054 |
| VtPxO | origin/claude/train-sym24-95223c03-VtPxO | 2.7160 |
| TYeHs | origin/claude/train-sym24-f7dad57f-TYeHs | 2.8188 |
| h6zmk | fork-joly-os-mmllm-claude-train-sym24-56732107-h6zmk | 3.0732 |
| **mean** | | **2.7629** |
| **best** | | **2.6889** |

## Chain progression R936 → R937

Previous harvest: `workers/dispatcher/harvest-6way-r936_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8016         | 2.7629         | -0.0387 |
| ctrl_bpc best  | 2.6920         | 2.6889         | -0.0031 |

## Per-round trajectory (best bird: U1mhs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 937 | 6596 | 2.6889 | +0.1901 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r936_sym24`
  - `workers/dispatcher/harvest-6way-r936_sym24`

## Output

`workers/dispatcher/harvest-8way-r937_sym24/round-937/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

