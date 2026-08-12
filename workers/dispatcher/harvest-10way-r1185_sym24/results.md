# harvest-10way-r1185 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1185 ctrl_bpc |
|--------|--------|--------------:|
| 7WVty | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9376197d-7WVty | 2.2968 |
| sqoyy | fork-joly-os-mmllm-claude-train-sym24-d753be63-sqoyy | 2.3051 |
| GzDVs | origin/claude/train-sym24-ef831967-GzDVs | 2.3143 |
| OF6Oa | fork-SeniorCareMarket-mmllm-claude-train-sym24-746c8d68-OF6Oa | 2.3189 |
| LNKvL | origin/claude/train-sym24-4947b6e3-LNKvL | 2.4965 |
| pmcsp | fork-joly-os-mmllm-claude-train-sym24-506cc3ad-pmcsp | 2.5007 |
| D7Iop | fork-SeniorCareMarket-mmllm-claude-train-sym24-8c7c277f-D7Iop | 2.5028 |
| 7Yvlo | origin/claude/train-sym24-d7e23c0a-7Yvlo | 2.5046 |
| 0u80m | fork-slaa-us-mmllm-claude-train-sym24-36efe6d9-0u80m | 2.6884 |
| YY0pf | fork-slaa-us-mmllm-claude-train-sym24-35285155-YY0pf | 2.6911 |
| **mean** | | **2.4619** |
| **best** | | **2.2968** |

## Chain progression R1184 → R1185

Previous harvest: `workers/dispatcher/harvest-3way-r1184_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4293         | 2.4619         | +0.0326 |
| ctrl_bpc best  | 2.3010         | 2.2968         | -0.0042 |

## Per-round trajectory (best bird: 7WVty)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1185 | 6584 | 2.2968 | +0.2522 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1184_sym24`
  - `workers/dispatcher/harvest-3way-r1184_sym24`

## Output

`workers/dispatcher/harvest-10way-r1185_sym24/round-1185/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

