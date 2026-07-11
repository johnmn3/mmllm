# harvest-5way-r889 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R889 ctrl_bpc |
|--------|--------|--------------:|
| jtGzE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-521a46be-jtGzE | 2.8175 |
| 9JCUd | fork-SeniorCareMarket-mmllm-claude-train-sym24-dc34e09f-9JCUd | 2.8395 |
| V3MAN | fork-joly-os-mmllm-claude-train-sym24-86dbfc20-V3MAN | 2.9767 |
| tbMru | fork-joly-os-mmllm-claude-train-sym24-6fcb8659-tbMru | 3.0220 |
| gQApy | origin/claude/train-sym24-9fec3b21-gQApy | 3.2219 |
| **mean** | | **2.9755** |
| **best** | | **2.8175** |

## Chain progression R888 → R889

Previous harvest: `workers/dispatcher/harvest-6way-r888_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9783         | 2.9755         | -0.0028 |
| ctrl_bpc best  | 2.8096         | 2.8175         | +0.0079 |

## Per-round trajectory (best bird: jtGzE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 889 | 6521 | 2.8175 | +0.3215 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r888_sym24`
  - `workers/dispatcher/harvest-6way-r888_sym24`

## Output

`workers/dispatcher/harvest-5way-r889_sym24/round-889/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

