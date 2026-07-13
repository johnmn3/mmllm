# harvest-6way-r909 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R909 ctrl_bpc |
|--------|--------|--------------:|
| qCIte | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a44a4ab5-qCIte | 2.7607 |
| UmoSv | fork-slaa-us-mmllm-claude-train-sym24-b2db8e22-UmoSv | 2.7616 |
| AFhMG | fork-joly-os-mmllm-claude-train-sym24-9d35d885-AFhMG | 2.7701 |
| iEJyS | origin/claude/train-sym24-2eae9db7-iEJyS | 2.7864 |
| JSpy2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-084234e1-JSpy2 | 2.9486 |
| ESs0M | fork-joly-os-mmllm-claude-train-sym24-9e1954b0-ESs0M | 3.0053 |
| **mean** | | **2.8388** |
| **best** | | **2.7607** |

## Chain progression R908 → R909

Previous harvest: `workers/dispatcher/harvest-4way-r908_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0133         | 2.8388         | -0.1745 |
| ctrl_bpc best  | 2.7763         | 2.7607         | -0.0156 |

## Per-round trajectory (best bird: qCIte)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 909 | 6747 | 2.7607 | +0.3468 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r908_sym24`
  - `workers/dispatcher/harvest-4way-r908_sym24`

## Output

`workers/dispatcher/harvest-6way-r909_sym24/round-909/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

