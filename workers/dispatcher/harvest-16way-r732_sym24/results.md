# harvest-16way-r732 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R732 ctrl_bpc |
|--------|--------|--------------:|
| zyefQ | origin/claude/train-sym24-7147a1da-zyefQ | 3.4177 |
| pkT86 | fork-slaa-us-mmllm-claude-train-sym24-6c6e0eb4-pkT86 | 3.4310 |
| d5QeS | fork-davidwuchn-mmllm-claude-train-sym24-64c0bd34-d5QeS | 3.4419 |
| OdC7N | fork-slaa-us-mmllm-claude-train-sym24-95e7dc94-OdC7N | 3.4555 |
| 6JMyZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-40233e77-6JMyZ | 3.4653 |
| wa90Q | fork-joly-os-mmllm-claude-train-sym24-751e3464-wa90Q | 3.4658 |
| MlqwC | fork-joly-os-mmllm-claude-train-sym24-f419da75-MlqwC | 3.4669 |
| fu4GW | fork-davidwuchn-mmllm-claude-train-sym24-cb1f3a08-fu4GW | 3.4671 |
| o4upt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e799421-o4upt | 3.4877 |
| wSAnx | origin/claude/train-sym24-40631641-wSAnx | 3.4905 |
| Rkjm3 | fork-joly-os-mmllm-claude-train-sym24-e7faf430-Rkjm3 | 3.4906 |
| eSmVF | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1b228e7-eSmVF | 3.4946 |
| m9wfa | fork-davidwuchn-mmllm-claude-train-sym24-ddfcf5f1-m9wfa | 3.5236 |
| rGtRz | fork-slaa-us-mmllm-claude-train-sym24-035e8f0b-rGtRz | 3.7768 |
| cAeiE | origin/claude/train-sym24-61e17b37-cAeiE | 3.7905 |
| v2LOl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2df3350-v2LOl | 3.7949 |
| **mean** | | **3.5288** |
| **best** | | **3.4177** |

## Chain progression R731 → R732

Previous harvest: `workers/dispatcher/harvest-3way-r731_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7065         | 3.5288         | -0.1777 |
| ctrl_bpc best  | 3.5010         | 3.4177         | -0.0833 |

## Per-round trajectory (best bird: zyefQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 732 | 6643 | 3.4177 | +0.6268 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r731_sym24`
  - `workers/dispatcher/harvest-3way-r731_sym24`

## Output

`workers/dispatcher/harvest-16way-r732_sym24/round-732/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

