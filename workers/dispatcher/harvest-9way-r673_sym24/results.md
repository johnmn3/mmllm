# harvest-9way-r673 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R673 ctrl_bpc |
|--------|--------|--------------:|
| TUvH9 | origin/claude/train-sym24-810c9f8c-TUvH9 | 3.8499 |
| VZ9xB | fork-joly-os-mmllm-claude-train-sym24-096d4f36-VZ9xB | 3.8532 |
| geWFo | fork-SeniorCareMarket-mmllm-claude-train-sym24-18c50ad4-geWFo | 3.8605 |
| CAWKu | origin/claude/train-sym24-ab90ecd2-CAWKu | 3.8656 |
| AxllG | fork-davidwuchn-mmllm-claude-train-sym24-52dc2462-AxllG | 3.8701 |
| qedfy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-baf9196a-qedfy | 3.8802 |
| rH8UA | fork-joly-os-mmllm-claude-train-sym24-63eb1854-rH8UA | 3.8964 |
| 2Ov6s | fork-davidwuchn-mmllm-claude-train-sym24-b3bb3983-2Ov6s | 3.8984 |
| Fa1fh | fork-slaa-us-mmllm-claude-train-sym24-b8ac5ae2-Fa1fh | 3.9233 |
| **mean** | | **3.8775** |
| **best** | | **3.8499** |

## Chain progression R672 → R673

Previous harvest: `workers/dispatcher/harvest-4way-r672_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9684         | 3.8775         | -0.0909 |
| ctrl_bpc best  | 3.8554         | 3.8499         | -0.0055 |

## Per-round trajectory (best bird: TUvH9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 673 | 6370 | 3.8499 | +0.5988 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r672_sym24`
  - `workers/dispatcher/harvest-4way-r672_sym24`

## Output

`workers/dispatcher/harvest-9way-r673_sym24/round-673/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

