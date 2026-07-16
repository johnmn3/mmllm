# harvest-7way-r939 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R939 ctrl_bpc |
|--------|--------|--------------:|
| E6gFr | fork-SeniorCareMarket-mmllm-claude-train-sym24-61fc7ec7-E6gFr | 2.6890 |
| qaR9W | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c7f7de14-qaR9W | 2.6913 |
| Eb3bF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-97186403-Eb3bF | 2.6914 |
| 4UUcP | fork-slaa-us-mmllm-claude-train-sym24-adabf390-4UUcP | 2.6958 |
| LqEwK | fork-joly-os-mmllm-claude-train-sym24-380234b6-LqEwK | 2.7029 |
| Qsmxc | fork-joly-os-mmllm-claude-train-sym24-87d11e36-Qsmxc | 3.0864 |
| MtNL5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-533cd722-MtNL5 | 3.1029 |
| **mean** | | **2.8085** |
| **best** | | **2.6890** |

## Chain progression R610 → R939

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.8085         | +0.6713 |
| ctrl_bpc best  | 2.1268         | 2.6890         | +0.5622 |

## Per-round trajectory (best bird: E6gFr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 939 | 6981 | 2.6890 | +0.1935 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r938_sym24`
  - `workers/dispatcher/harvest-6way-r938_sym24`
  - `workers/dispatcher/harvest-9way-r938_sym24`

## Output

`workers/dispatcher/harvest-7way-r939_sym24/round-939/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

