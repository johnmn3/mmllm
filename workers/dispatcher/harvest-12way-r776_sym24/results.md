# harvest-12way-r776 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R776 ctrl_bpc |
|--------|--------|--------------:|
| 61qoX | fork-slaa-us-mmllm-claude-train-sym24-ebd5817e-61qoX | 3.2060 |
| 2Sd8N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b420b794-2Sd8N | 3.2216 |
| 4AJp9 | fork-joly-os-mmllm-claude-train-sym24-9a20e074-4AJp9 | 3.2373 |
| rk3gT | fork-slaa-us-mmllm-claude-train-sym24-4daeebbb-rk3gT | 3.2423 |
| yaaxV | fork-joly-os-mmllm-claude-train-sym24-fd67ccfb-yaaxV | 3.2456 |
| Fyv0q | fork-SeniorCareMarket-mmllm-claude-train-sym24-fd9e32e5-Fyv0q | 3.2496 |
| w6N9D | origin/claude/train-sym24-b853bda6-w6N9D | 3.2551 |
| agQhY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2e4cddd-agQhY | 3.3236 |
| 0oDPE | fork-davidwuchn-mmllm-claude-train-sym24-fbfeadd4-0oDPE | 3.3473 |
| XjUVG | origin/claude/train-sym24-10285b51-XjUVG | 3.3509 |
| 8BSZ9 | fork-slaa-us-mmllm-claude-train-sym24-f2976c3d-8BSZ9 | 3.3549 |
| j2xGs | fork-davidwuchn-mmllm-claude-train-sym24-3fd29166-j2xGs | 3.6037 |
| **mean** | | **3.3032** |
| **best** | | **3.2060** |

## Chain progression R775 → R776

Previous harvest: `workers/dispatcher/harvest-6way-r775_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3253         | 3.3032         | -0.0221 |
| ctrl_bpc best  | 3.1992         | 3.2060         | +0.0068 |

## Per-round trajectory (best bird: 61qoX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 776 | 6476 | 3.2060 | +0.4808 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r775_sym24`
  - `workers/dispatcher/harvest-6way-r775_sym24`

## Output

`workers/dispatcher/harvest-12way-r776_sym24/round-776/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

