# harvest-2way-r1291 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1291 ctrl_bpc |
|--------|--------|--------------:|
| AVTAf | fork-joly-os-mmllm-claude-train-sym24-1ed22664-AVTAf | 4.8323 |
| R1FMf | origin/claude/train-sym24-9c90744e-R1FMf | 4.8439 |
| **mean** | | **4.8381** |
| **best** | | **4.8323** |

## Chain progression R1290 → R1291

Previous harvest: `workers/dispatcher/harvest-13way-r1290_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6005         | 4.8381         | +1.2376 |
| ctrl_bpc best  | 2.2117         | 4.8323         | +2.6206 |

## Per-round trajectory (best bird: AVTAf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1291 | 6354 | 4.8323 | +0.0197 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-8way-r1290_sym24`

## Output

`workers/dispatcher/harvest-2way-r1291_sym24/round-1291/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

