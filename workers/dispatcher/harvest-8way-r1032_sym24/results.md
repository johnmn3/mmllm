# harvest-8way-r1032 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1032 ctrl_bpc |
|--------|--------|--------------:|
| df330 | fork-joly-os-mmllm-claude-train-sym24-09522446-df330 | 2.4974 |
| FhEbz | fork-slaa-us-mmllm-claude-train-sym24-fabda9aa-FhEbz | 2.5042 |
| 6SkdO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1cea3005-6SkdO | 2.5364 |
| jfxqU | origin/claude/train-sym24-0c86286e-jfxqU | 2.6876 |
| DVap7 | fork-slaa-us-mmllm-claude-train-sym24-2a5dc236-DVap7 | 2.8843 |
| QbRGT | origin/claude/train-sym24-5199ac07-QbRGT | 2.8923 |
| rnARC | fork-SeniorCareMarket-mmllm-claude-train-sym24-9762b0cb-rnARC | 2.9029 |
| U8psg | fork-joly-os-mmllm-claude-train-sym24-bf84260d-U8psg | 2.9212 |
| **mean** | | **2.7283** |
| **best** | | **2.4974** |

## Chain progression R1031 → R1032

Previous harvest: `workers/dispatcher/harvest-5way-r1031_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5429         | 2.7283         | +0.1854 |
| ctrl_bpc best  | 2.4946         | 2.4974         | +0.0028 |

## Per-round trajectory (best bird: df330)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1032 | 6714 | 2.4974 | +0.2045 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1031_sym24`
  - `workers/dispatcher/harvest-5way-r1031_sym24`

## Output

`workers/dispatcher/harvest-8way-r1032_sym24/round-1032/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

