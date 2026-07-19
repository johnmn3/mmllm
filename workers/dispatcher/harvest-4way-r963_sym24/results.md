# harvest-4way-r963 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R963 ctrl_bpc |
|--------|--------|--------------:|
| fDDhs | fork-joly-os-mmllm-claude-train-sym24-a52ff188-fDDhs | 2.8219 |
| ENs0Q | origin/claude/train-sym24-d5edbc32-ENs0Q | 2.8237 |
| ckKVh | fork-SeniorCareMarket-mmllm-claude-train-sym24-d92b3c53-ckKVh | 2.8248 |
| Z5m9x | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-153ad27d-Z5m9x | 3.0061 |
| **mean** | | **2.8691** |
| **best** | | **2.8219** |

## Chain progression R962 → R963

Previous harvest: `workers/dispatcher/harvest-4way-r962_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7809         | 2.8691         | +0.0882 |
| ctrl_bpc best  | 2.6221         | 2.8219         | +0.1998 |

## Per-round trajectory (best bird: fDDhs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 963 | 6869 | 2.8219 | +0.1319 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r962_sym24`
  - `workers/dispatcher/harvest-4way-r962_sym24`

## Output

`workers/dispatcher/harvest-4way-r963_sym24/round-963/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

