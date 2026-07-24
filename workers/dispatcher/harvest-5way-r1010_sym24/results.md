# harvest-5way-r1010 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1010 ctrl_bpc |
|--------|--------|--------------:|
| 3ivL5 | fork-joly-os-mmllm-claude-train-sym24-75e754ad-3ivL5 | 2.5728 |
| LBuhv | origin/claude/train-sym24-a193c09f-LBuhv | 2.5773 |
| sTFRv | fork-SeniorCareMarket-mmllm-claude-train-sym24-e590bfe5-sTFRv | 2.7249 |
| 6UE8A | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-02a1f559-6UE8A | 2.7824 |
| oiMYF | fork-slaa-us-mmllm-claude-train-sym24-6ac848e5-oiMYF | 2.9247 |
| **mean** | | **2.7164** |
| **best** | | **2.5728** |

## Chain progression R1009 → R1010

Previous harvest: `workers/dispatcher/harvest-6way-r1009_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7386         | 2.7164         | -0.0222 |
| ctrl_bpc best  | 2.5354         | 2.5728         | +0.0374 |

## Per-round trajectory (best bird: 3ivL5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1010 | 6390 | 2.5728 | +0.1623 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1009_sym24`
  - `workers/dispatcher/harvest-6way-r1009_sym24`

## Output

`workers/dispatcher/harvest-5way-r1010_sym24/round-1010/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

