# harvest-6way-r1032 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1032 ctrl_bpc |
|--------|--------|--------------:|
| 6SkdO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1cea3005-6SkdO | 2.5364 |
| jfxqU | origin/claude/train-sym24-0c86286e-jfxqU | 2.6876 |
| DVap7 | fork-slaa-us-mmllm-claude-train-sym24-2a5dc236-DVap7 | 2.8843 |
| QbRGT | origin/claude/train-sym24-5199ac07-QbRGT | 2.8923 |
| rnARC | fork-SeniorCareMarket-mmllm-claude-train-sym24-9762b0cb-rnARC | 2.9029 |
| U8psg | fork-joly-os-mmllm-claude-train-sym24-bf84260d-U8psg | 2.9212 |
| **mean** | | **2.8041** |
| **best** | | **2.5364** |

## Chain progression R1031 → R1032

Previous harvest: `workers/dispatcher/harvest-5way-r1031_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5429         | 2.8041         | +0.2612 |
| ctrl_bpc best  | 2.4946         | 2.5364         | +0.0418 |

## Per-round trajectory (best bird: 6SkdO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1032 | 6536 | 2.5364 | +0.1757 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1031_sym24`
  - `workers/dispatcher/harvest-5way-r1031_sym24`

## Output

`workers/dispatcher/harvest-6way-r1032_sym24/round-1032/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

