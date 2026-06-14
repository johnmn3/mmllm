# harvest-13way-r673 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R673 ctrl_bpc |
|--------|--------|--------------:|
| TUvH9 | origin/claude/train-sym24-810c9f8c-TUvH9 | 3.8499 |
| VZ9xB | fork-joly-os-mmllm-claude-train-sym24-096d4f36-VZ9xB | 3.8532 |
| geWFo | fork-SeniorCareMarket-mmllm-claude-train-sym24-18c50ad4-geWFo | 3.8605 |
| 95gkV | fork-slaa-us-mmllm-claude-train-sym24-473534ae-95gkV | 3.8606 |
| CAWKu | origin/claude/train-sym24-ab90ecd2-CAWKu | 3.8656 |
| AxllG | fork-davidwuchn-mmllm-claude-train-sym24-52dc2462-AxllG | 3.8701 |
| qedfy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-baf9196a-qedfy | 3.8802 |
| ViuAC | fork-joly-os-mmllm-claude-train-sym24-e90d54f7-ViuAC | 3.8924 |
| rH8UA | fork-joly-os-mmllm-claude-train-sym24-63eb1854-rH8UA | 3.8964 |
| 2Ov6s | fork-davidwuchn-mmllm-claude-train-sym24-b3bb3983-2Ov6s | 3.8984 |
| Blx7m | fork-davidwuchn-mmllm-claude-train-sym24-0a725765-Blx7m | 3.9113 |
| Fa1fh | fork-slaa-us-mmllm-claude-train-sym24-b8ac5ae2-Fa1fh | 3.9233 |
| KmxUy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-da5452d5-KmxUy | 4.1886 |
| **mean** | | **3.9039** |
| **best** | | **3.8499** |

## Chain progression R672 → R673

Previous harvest: `workers/dispatcher/harvest-4way-r672_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9684         | 3.9039         | -0.0645 |
| ctrl_bpc best  | 3.8554         | 3.8499         | -0.0055 |

## Per-round trajectory (best bird: TUvH9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 673 | 6370 | 3.8499 | +0.5988 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r672_sym24`
  - `workers/dispatcher/harvest-4way-r672_sym24`

## Output

`workers/dispatcher/harvest-13way-r673_sym24/round-673/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

