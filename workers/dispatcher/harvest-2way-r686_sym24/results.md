# harvest-2way-r686 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R686 ctrl_bpc |
|--------|--------|--------------:|
| x79jr | fork-slaa-us-mmllm-claude-train-sym24-7d130260-x79jr | 3.7816 |
| 7apeO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1ac10edf-7apeO | 3.7847 |
| **mean** | | **3.7832** |
| **best** | | **3.7816** |

## Chain progression R685 → R686

Previous harvest: `workers/dispatcher/harvest-9way-r685_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8264         | 3.7832         | -0.0433 |
| ctrl_bpc best  | 3.7363         | 3.7816         | +0.0453 |

## Per-round trajectory (best bird: x79jr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 686 | 5324 | 3.7816 | +0.3870 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r685_sym24`

## Output

`workers/dispatcher/harvest-2way-r686_sym24/round-686/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

