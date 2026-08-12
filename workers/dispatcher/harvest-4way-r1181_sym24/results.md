# harvest-4way-r1181 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1181 ctrl_bpc |
|--------|--------|--------------:|
| smf56 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2d32bcb2-smf56 | 2.3155 |
| l4csn | origin/claude/train-sym24-b67d0493-l4csn | 2.3265 |
| ND09S | fork-joly-os-mmllm-claude-train-sym24-3cc3ae2a-ND09S | 2.5071 |
| FaAiC | fork-slaa-us-mmllm-claude-train-sym24-02c7fac8-FaAiC | 2.5099 |
| **mean** | | **2.4147** |
| **best** | | **2.3155** |

## Chain progression R1180 → R1181

Previous harvest: `workers/dispatcher/harvest-6way-r1180_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4759         | 2.4147         | -0.0612 |
| ctrl_bpc best  | 2.3118         | 2.3155         | +0.0037 |

## Per-round trajectory (best bird: smf56)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1181 | 4302 | 2.3155 | +0.2477 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1180_sym24`
  - `workers/dispatcher/harvest-4way-r1180_sym24`

## Output

`workers/dispatcher/harvest-4way-r1181_sym24/round-1181/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

