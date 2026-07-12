# harvest-10way-r897 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R897 ctrl_bpc |
|--------|--------|--------------:|
| dTnXJ | origin/claude/train-sym24-32e0d865-dTnXJ | 2.7877 |
| bWHYo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0f5a47f3-bWHYo | 2.7932 |
| 8rkSb | fork-joly-os-mmllm-claude-train-sym24-a97fba48-8rkSb | 2.8082 |
| FMfCT | fork-slaa-us-mmllm-claude-train-sym24-da257070-FMfCT | 2.8182 |
| aTzEG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-47e956c4-aTzEG | 2.8264 |
| t357o | fork-SeniorCareMarket-mmllm-claude-train-sym24-f5067f1e-t357o | 2.8386 |
| AC6ho | origin/claude/train-sym24-e7aa2e8c-AC6ho | 3.1694 |
| FunLQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-cf42b5bb-FunLQ | 3.1737 |
| IQ06u | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe9f712c-IQ06u | 3.1741 |
| BMzom | fork-joly-os-mmllm-claude-train-sym24-54bc6fe9-BMzom | 3.1883 |
| **mean** | | **2.9578** |
| **best** | | **2.7877** |

## Chain progression R896 → R897

Previous harvest: `workers/dispatcher/harvest-9way-r896_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9484         | 2.9578         | +0.0094 |
| ctrl_bpc best  | 2.8208         | 2.7877         | -0.0331 |

## Per-round trajectory (best bird: dTnXJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 897 | 6704 | 2.7877 | +0.2576 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r896_sym24`
  - `workers/dispatcher/harvest-4way-r896_sym24`
  - `workers/dispatcher/harvest-9way-r896_sym24`

## Output

`workers/dispatcher/harvest-10way-r897_sym24/round-897/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

