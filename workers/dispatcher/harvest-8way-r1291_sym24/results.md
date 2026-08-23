# harvest-8way-r1291 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1291 ctrl_bpc |
|--------|--------|--------------:|
| K7t0L | fork-slaa-us-mmllm-claude-train-sym24-5624b249-K7t0L | 4.8221 |
| AVTAf | fork-joly-os-mmllm-claude-train-sym24-1ed22664-AVTAf | 4.8323 |
| R1FMf | origin/claude/train-sym24-9c90744e-R1FMf | 4.8439 |
| 7oDyn | fork-SeniorCareMarket-mmllm-claude-train-sym24-c261fc0e-7oDyn | 4.8636 |
| k5no4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc5adbc4-k5no4 | 4.8769 |
| DbJwl | origin/claude/train-sym24-b7bcbd6a-DbJwl | 4.8802 |
| mBAQB | fork-slaa-us-mmllm-claude-train-sym24-64b6c742-mBAQB | 4.8956 |
| HAqKe | fork-joly-os-mmllm-claude-train-sym24-a3c9a1ed-HAqKe | 5.3384 |
| **mean** | | **4.9191** |
| **best** | | **4.8221** |

## Chain progression R1290 → R1291

Previous harvest: `workers/dispatcher/harvest-8way-r1290_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5433         | 4.9191         | +1.3758 |
| ctrl_bpc best  | 2.2117         | 4.8221         | +2.6104 |

## Per-round trajectory (best bird: K7t0L)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1291 | 6832 | 4.8221 | +0.0294 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1290_sym24`
  - `workers/dispatcher/harvest-13way-r1290_sym24`
  - `workers/dispatcher/harvest-8way-r1290_sym24`

## Output

`workers/dispatcher/harvest-8way-r1291_sym24/round-1291/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

