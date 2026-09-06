# harvest-1way-r1402 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1402 ctrl_bpc |
|--------|--------|--------------:|
| J64Fs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc0a73e6-J64Fs | 3.3330 |
| **mean** | | **3.3330** |
| **best** | | **3.3330** |

## Chain progression R1401 → R1402

Previous harvest: `workers/dispatcher/harvest-1way-r1401_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6187         | 3.3330         | -0.2857 |
| ctrl_bpc best  | 3.6187         | 3.3330         | -0.2857 |

## Per-round trajectory (best bird: J64Fs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1402 | 5287 | 3.3330 | +0.1038 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1401_sym24`

## Output

`workers/dispatcher/harvest-1way-r1402_sym24/round-1402/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

