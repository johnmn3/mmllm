# harvest-6way-r1192 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1192 ctrl_bpc |
|--------|--------|--------------:|
| uEnGD | fork-slaa-us-mmllm-claude-train-sym24-73adf2a4-uEnGD | 2.2912 |
| ahuZE | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6ee18ca-ahuZE | 2.4799 |
| nU1Xf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c392040e-nU1Xf | 2.4903 |
| feUDP | fork-joly-os-mmllm-claude-train-sym24-317fe1c4-feUDP | 2.4930 |
| 87es4 | fork-joly-os-mmllm-claude-train-sym24-f08bcfac-87es4 | 2.6926 |
| 5bQyF | origin/claude/train-sym24-e6b36641-5bQyF | 2.6928 |
| **mean** | | **2.5233** |
| **best** | | **2.2912** |

## Chain progression R1191 → R1192

Previous harvest: `workers/dispatcher/harvest-6way-r1191_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5261         | 2.5233         | -0.0028 |
| ctrl_bpc best  | 2.3077         | 2.2912         | -0.0165 |

## Per-round trajectory (best bird: uEnGD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1192 | 6541 | 2.2912 | +0.2601 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1191_sym24`
  - `workers/dispatcher/harvest-6way-r1191_sym24`

## Output

`workers/dispatcher/harvest-6way-r1192_sym24/round-1192/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

