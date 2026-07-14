# harvest-11way-r921 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R921 ctrl_bpc |
|--------|--------|--------------:|
| ZrM4q | fork-joly-os-mmllm-claude-train-sym24-291804e4-ZrM4q | 2.7224 |
| 5zt1m | origin/claude/train-sym24-5433879f-5zt1m | 2.7251 |
| ng2kT | fork-slaa-us-mmllm-claude-train-sym24-9faea251-ng2kT | 2.7340 |
| LZ37B | origin/claude/train-sym24-7067fa8a-LZ37B | 2.7459 |
| dGIp6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-bb5f7da6-dGIp6 | 2.8454 |
| acunE | fork-slaa-us-mmllm-claude-train-sym24-5e157cfa-acunE | 2.9255 |
| 024z9 | fork-joly-os-mmllm-claude-train-sym24-68882b55-024z9 | 2.9311 |
| lvTmw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ba512cf9-lvTmw | 2.9326 |
| TpMny | origin/claude/train-sym24-e79bb4b7-TpMny | 3.1202 |
| 3uv84 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3ad4761e-3uv84 | 3.1317 |
| AZwsT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-429bbb1b-AZwsT | 3.1456 |
| **mean** | | **2.9054** |
| **best** | | **2.7224** |

## Chain progression R920 → R921

Previous harvest: `workers/dispatcher/harvest-8way-r920_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9647         | 2.9054         | -0.0593 |
| ctrl_bpc best  | 2.7414         | 2.7224         | -0.0190 |

## Per-round trajectory (best bird: ZrM4q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 921 | 4444 | 2.7224 | +0.1809 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r920_sym24`
  - `workers/dispatcher/harvest-7way-r920_sym24`
  - `workers/dispatcher/harvest-8way-r920_sym24`

## Output

`workers/dispatcher/harvest-11way-r921_sym24/round-921/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

