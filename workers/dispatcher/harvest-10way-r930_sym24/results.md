# harvest-10way-r930 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R930 ctrl_bpc |
|--------|--------|--------------:|
| A6Dvu | origin/claude/train-sym24-a7004437-A6Dvu | 2.7118 |
| F8XaF | fork-slaa-us-mmllm-claude-train-sym24-fbfc25a5-F8XaF | 2.7166 |
| pbOaj | origin/claude/train-sym24-052b6ec5-pbOaj | 2.7171 |
| ofnpX | origin/claude/train-sym24-ad42fd74-ofnpX | 2.7176 |
| SU2qG | fork-slaa-us-mmllm-claude-train-sym24-a8d69614-SU2qG | 2.8955 |
| KV30y | fork-joly-os-mmllm-claude-train-sym24-547fccb0-KV30y | 2.9013 |
| lQtbb | fork-SeniorCareMarket-mmllm-claude-train-sym24-bea77e09-lQtbb | 2.9065 |
| a4udj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b696a9c-a4udj | 2.9080 |
| ooBco | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73578095-ooBco | 3.1070 |
| J9aKm | fork-SeniorCareMarket-mmllm-claude-train-sym24-880c788f-J9aKm | 3.1194 |
| **mean** | | **2.8701** |
| **best** | | **2.7118** |

## Chain progression R929 → R930

Previous harvest: `workers/dispatcher/harvest-9way-r929_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8687         | 2.8701         | +0.0014 |
| ctrl_bpc best  | 2.7103         | 2.7118         | +0.0015 |

## Per-round trajectory (best bird: A6Dvu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 930 | 6602 | 2.7118 | +0.2099 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r929_sym24`
  - `workers/dispatcher/harvest-5way-r929_sym24`
  - `workers/dispatcher/harvest-9way-r929_sym24`

## Output

`workers/dispatcher/harvest-10way-r930_sym24/round-930/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

