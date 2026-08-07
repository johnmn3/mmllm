# harvest-13way-r1137 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R1137 ctrl_bpc |
|--------|--------|--------------:|
| daqNg | origin/claude/train-sym24-d55b4744-daqNg | 2.3423 |
| DMF9H | origin/claude/train-sym24-3f1aa917-DMF9H | 2.3467 |
| Yys7i | fork-SeniorCareMarket-mmllm-claude-train-sym24-3910032b-Yys7i | 2.3496 |
| Gl0u5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-04e950e5-Gl0u5 | 2.3664 |
| dV6O4 | fork-slaa-us-mmllm-claude-train-sym24-4a809d77-dV6O4 | 2.3691 |
| B7b7X | fork-SeniorCareMarket-mmllm-claude-train-sym24-fe7d4f4f-B7b7X | 2.3697 |
| JlwZ3 | fork-joly-os-mmllm-claude-train-sym24-7de3b412-JlwZ3 | 2.3724 |
| 15Pt8 | fork-slaa-us-mmllm-claude-train-sym24-4736f009-15Pt8 | 2.5420 |
| KJKH3 | fork-joly-os-mmllm-claude-train-sym24-c2582eb2-KJKH3 | 2.5456 |
| i5Zhl | fork-joly-os-mmllm-claude-train-sym24-50314e83-i5Zhl | 2.5459 |
| s0wWS | fork-slaa-us-mmllm-claude-train-sym24-9f1752fc-s0wWS | 2.5479 |
| UfCk1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0c9638c1-UfCk1 | 2.7398 |
| 5iyB5 | origin/claude/train-sym24-1d4503b3-5iyB5 | 2.7605 |
| **mean** | | **2.4768** |
| **best** | | **2.3423** |

## Chain progression R1136 → R1137

Previous harvest: `workers/dispatcher/harvest-9way-r1136_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5065         | 2.4768         | -0.0297 |
| ctrl_bpc best  | 2.3420         | 2.3423         | +0.0003 |

## Per-round trajectory (best bird: daqNg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1137 | 6476 | 2.3423 | +0.2497 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1136_sym24`
  - `workers/dispatcher/harvest-6way-r1136_sym24`
  - `workers/dispatcher/harvest-9way-r1136_sym24`

## Output

`workers/dispatcher/harvest-13way-r1137_sym24/round-1137/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

