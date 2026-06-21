# harvest-10way-r732 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R732 ctrl_bpc |
|--------|--------|--------------:|
| pkT86 | fork-slaa-us-mmllm-claude-train-sym24-6c6e0eb4-pkT86 | 3.4310 |
| d5QeS | fork-davidwuchn-mmllm-claude-train-sym24-64c0bd34-d5QeS | 3.4419 |
| wa90Q | fork-joly-os-mmllm-claude-train-sym24-751e3464-wa90Q | 3.4658 |
| MlqwC | fork-joly-os-mmllm-claude-train-sym24-f419da75-MlqwC | 3.4669 |
| wSAnx | origin/claude/train-sym24-40631641-wSAnx | 3.4905 |
| eSmVF | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1b228e7-eSmVF | 3.4946 |
| m9wfa | fork-davidwuchn-mmllm-claude-train-sym24-ddfcf5f1-m9wfa | 3.5236 |
| rGtRz | fork-slaa-us-mmllm-claude-train-sym24-035e8f0b-rGtRz | 3.7768 |
| cAeiE | origin/claude/train-sym24-61e17b37-cAeiE | 3.7905 |
| v2LOl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2df3350-v2LOl | 3.7949 |
| **mean** | | **3.5677** |
| **best** | | **3.4310** |

## Chain progression R731 → R732

Previous harvest: `workers/dispatcher/harvest-10way-r731_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5622         | 3.5677         | +0.0055 |
| ctrl_bpc best  | 3.4225         | 3.4310         | +0.0085 |

## Per-round trajectory (best bird: pkT86)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 732 | 6478 | 3.4310 | +0.5816 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r731_sym24`
  - `workers/dispatcher/harvest-3way-r731_sym24`

## Output

`workers/dispatcher/harvest-10way-r732_sym24/round-732/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

