# harvest-3way-r754 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R754 ctrl_bpc |
|--------|--------|--------------:|
| iMbFp | fork-joly-os-mmllm-claude-train-sym24-821011d5-iMbFp | 3.4089 |
| lzrXF | origin/claude/train-sym24-c394d870-lzrXF | 3.4137 |
| EiEf0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27d1df1e-EiEf0 | 3.7075 |
| **mean** | | **3.5100** |
| **best** | | **3.4089** |

## Chain progression R753 → R754

Previous harvest: `workers/dispatcher/harvest-11way-r753_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3575         | 3.5100         | +0.1525 |
| ctrl_bpc best  | 3.3141         | 3.4089         | +0.0948 |

## Per-round trajectory (best bird: iMbFp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 754 | 6440 | 3.4089 | +0.8069 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r753_sym24`

## Output

`workers/dispatcher/harvest-3way-r754_sym24/round-754/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

