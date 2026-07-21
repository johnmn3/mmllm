# harvest-7way-r986 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R986 ctrl_bpc |
|--------|--------|--------------:|
| vdJmb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8487efd2-vdJmb | 2.5851 |
| LBtMi | origin/claude/train-sym24-0bf61510-LBtMi | 2.6038 |
| Aj0Cc | fork-SeniorCareMarket-mmllm-claude-train-sym24-2fd91cd4-Aj0Cc | 2.6060 |
| tYBy0 | origin/claude/train-sym24-598f8b09-tYBy0 | 2.6119 |
| 2ntqe | fork-joly-os-mmllm-claude-train-sym24-1bc30f12-2ntqe | 2.7960 |
| lWMLL | origin/claude/train-sym24-b098afb2-lWMLL | 2.9674 |
| Z3eEl | fork-slaa-us-mmllm-claude-train-sym24-2d0c1bd5-Z3eEl | 2.9758 |
| **mean** | | **2.7351** |
| **best** | | **2.5851** |

## Chain progression R985 → R986

Previous harvest: `workers/dispatcher/harvest-6way-r985_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7615         | 2.7351         | -0.0264 |
| ctrl_bpc best  | 2.6128         | 2.5851         | -0.0277 |

## Per-round trajectory (best bird: vdJmb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 986 | 5390 | 2.5851 | +0.1896 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r985_sym24`
  - `workers/dispatcher/harvest-2way-r985_sym24`

## Output

`workers/dispatcher/harvest-7way-r986_sym24/round-986/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

