# harvest-6way-r1118 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1118 ctrl_bpc |
|--------|--------|--------------:|
| nK63S | fork-slaa-us-mmllm-claude-train-sym24-a291e96c-nK63S | 2.3683 |
| 4HcaU | origin/claude/train-sym24-84f4d79d-4HcaU | 2.3737 |
| TEduK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-923aad99-TEduK | 2.3768 |
| FKXeB | fork-joly-os-mmllm-claude-train-sym24-bbe60620-FKXeB | 2.3922 |
| WyAws | origin/claude/train-sym24-742c4365-WyAws | 2.7838 |
| 6FOLI | fork-SeniorCareMarket-mmllm-claude-train-sym24-a861d538-6FOLI | 2.8009 |
| **mean** | | **2.5160** |
| **best** | | **2.3683** |

## Chain progression R1117 → R1118

Previous harvest: `workers/dispatcher/harvest-5way-r1117_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4157         | 2.5160         | +0.1002 |
| ctrl_bpc best  | 2.3677         | 2.3683         | +0.0006 |

## Per-round trajectory (best bird: nK63S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1118 | 6555 | 2.3683 | +0.2476 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1117_sym24`
  - `workers/dispatcher/harvest-4way-r1117_sym24`
  - `workers/dispatcher/harvest-5way-r1117_sym24`

## Output

`workers/dispatcher/harvest-6way-r1118_sym24/round-1118/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

