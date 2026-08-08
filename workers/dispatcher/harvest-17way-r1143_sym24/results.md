# harvest-17way-r1143 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R1143 ctrl_bpc |
|--------|--------|--------------:|
| SPHB3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-042d776d-SPHB3 | 2.3368 |
| LbBui | origin/claude/train-sym24-c4c3a88b-LbBui | 2.3400 |
| wygXC | fork-joly-os-mmllm-claude-train-sym24-c595f2e9-wygXC | 2.3442 |
| logEX | fork-SeniorCareMarket-mmllm-claude-train-sym24-eb2c30e1-logEX | 2.3444 |
| xhvY5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e43a38fd-xhvY5 | 2.3459 |
| 9KyJr | fork-SeniorCareMarket-mmllm-claude-train-sym24-15d3414c-9KyJr | 2.3464 |
| OeHEv | fork-joly-os-mmllm-claude-train-sym24-30573601-OeHEv | 2.3472 |
| pvpfz | fork-joly-os-mmllm-claude-train-sym24-bc2fa324-pvpfz | 2.3486 |
| V87Ux | fork-slaa-us-mmllm-claude-train-sym24-4038060e-V87Ux | 2.3593 |
| sQrCC | origin/claude/train-sym24-588854e0-sQrCC | 2.3600 |
| fwuLH | origin/claude/train-sym24-39f97d7a-fwuLH | 2.3686 |
| bGQWZ | fork-slaa-us-mmllm-claude-train-sym24-a8f4061a-bGQWZ | 2.5383 |
| 9u4gT | fork-slaa-us-mmllm-claude-train-sym24-94e13dd1-9u4gT | 2.5437 |
| 7xVmd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-acf3f5f4-7xVmd | 2.5443 |
| AEDhg | origin/claude/train-sym24-3c512251-AEDhg | 2.5459 |
| 3B6rF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4c7b8654-3B6rF | 2.7283 |
| qzd8w | fork-joly-os-mmllm-claude-train-sym24-eb3d22f6-qzd8w | 2.7414 |
| **mean** | | **2.4402** |
| **best** | | **2.3368** |

## Chain progression R1142 → R1143

Previous harvest: `workers/dispatcher/harvest-6way-r1142_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6540         | 2.4402         | -0.2138 |
| ctrl_bpc best  | 2.5373         | 2.3368         | -0.2005 |

## Per-round trajectory (best bird: SPHB3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1143 | 3788 | 2.3368 | +0.2421 |

## Cumulative training contribution

- This harvest: **1360 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **1840 steps** from 23 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1142_sym24`
  - `workers/dispatcher/harvest-6way-r1142_sym24`

## Output

`workers/dispatcher/harvest-17way-r1143_sym24/round-1143/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

