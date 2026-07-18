# harvest-2way-r955 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R955 ctrl_bpc |
|--------|--------|--------------:|
| N9GLa | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fe36b14-N9GLa | 2.6675 |
| hp2mJ | fork-joly-os-mmllm-claude-train-sym24-62d0e993-hp2mJ | 3.0457 |
| **mean** | | **2.8566** |
| **best** | | **2.6675** |

## Chain progression R954 → R955

Previous harvest: `workers/dispatcher/harvest-9way-r954_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7679         | 2.8566         | +0.0887 |
| ctrl_bpc best  | 2.6476         | 2.6675         | +0.0199 |

## Per-round trajectory (best bird: N9GLa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 955 | 6575 | 2.6675 | +0.1714 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r954_sym24`

## Output

`workers/dispatcher/harvest-2way-r955_sym24/round-955/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

