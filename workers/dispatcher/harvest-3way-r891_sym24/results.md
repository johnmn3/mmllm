# harvest-3way-r891 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R891 ctrl_bpc |
|--------|--------|--------------:|
| LXQTB | fork-slaa-us-mmllm-claude-train-sym24-ccfaecd1-LXQTB | 2.8174 |
| SMzrn | origin/claude/train-sym24-d660d321-SMzrn | 2.8384 |
| 0PMD5 | fork-joly-os-mmllm-claude-train-sym24-47ae7e83-0PMD5 | 3.2010 |
| **mean** | | **2.9523** |
| **best** | | **2.8174** |

## Chain progression R890 → R891

Previous harvest: `workers/dispatcher/harvest-4way-r890_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9303         | 2.9523         | +0.0220 |
| ctrl_bpc best  | 2.8163         | 2.8174         | +0.0011 |

## Per-round trajectory (best bird: LXQTB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 891 | 6633 | 2.8174 | +0.2345 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r890_sym24`

## Output

`workers/dispatcher/harvest-3way-r891_sym24/round-891/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

