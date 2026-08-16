# harvest-7way-r1219 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1219 ctrl_bpc |
|--------|--------|--------------:|
| Uqz69 | origin/claude/train-sym24-d6da7fe6-Uqz69 | 2.2691 |
| usjw4 | origin/claude/train-sym24-600e977f-usjw4 | 2.2863 |
| SKmTc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-30e49d28-SKmTc | 2.2878 |
| Q8UOf | fork-joly-os-mmllm-claude-train-sym24-677cb0fa-Q8UOf | 2.4643 |
| gJk6W | fork-SeniorCareMarket-mmllm-claude-train-sym24-837bcb29-gJk6W | 2.4680 |
| 9FgDI | fork-SeniorCareMarket-mmllm-claude-train-sym24-9895305e-9FgDI | 2.6619 |
| VS0VS | fork-slaa-us-mmllm-claude-train-sym24-83fd3d27-VS0VS | 2.6741 |
| **mean** | | **2.4445** |
| **best** | | **2.2691** |

## Chain progression R1218 → R1219

Previous harvest: `workers/dispatcher/harvest-7way-r1218_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3910         | 2.4445         | +0.0535 |
| ctrl_bpc best  | 2.2675         | 2.2691         | +0.0016 |

## Per-round trajectory (best bird: Uqz69)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1219 | 6685 | 2.2691 | +0.2568 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1218_sym24`
  - `workers/dispatcher/harvest-5way-r1218_sym24`

## Output

`workers/dispatcher/harvest-7way-r1219_sym24/round-1219/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

