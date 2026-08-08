# harvest-16way-r1145 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R1145 ctrl_bpc |
|--------|--------|--------------:|
| egptx | fork-joly-os-mmllm-claude-train-sym24-04548737-egptx | 2.3357 |
| EXiZ8 | origin/claude/train-sym24-a3134222-EXiZ8 | 2.3406 |
| 9rdnF | fork-joly-os-mmllm-claude-train-sym24-85302f7a-9rdnF | 2.3428 |
| svU2m | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f491568e-svU2m | 2.3605 |
| dmiHo | origin/claude/train-sym24-fe37f5d5-dmiHo | 2.3637 |
| 72ouS | fork-SeniorCareMarket-mmllm-claude-train-sym24-74b8e829-72ouS | 2.3653 |
| zWlew | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0f78faad-zWlew | 2.3677 |
| d47tl | fork-joly-os-mmllm-claude-train-sym24-07671512-d47tl | 2.3767 |
| etYZ3 | fork-slaa-us-mmllm-claude-train-sym24-28f40175-etYZ3 | 2.5333 |
| vN49M | origin/claude/train-sym24-16842c10-vN49M | 2.5559 |
| SU66L | fork-joly-os-mmllm-claude-train-sym24-1cb4b104-SU66L | 2.7197 |
| fOaW0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ca40ddf9-fOaW0 | 2.7321 |
| FYJOl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-90f584b5-FYJOl | 2.7344 |
| GcBqc | fork-slaa-us-mmllm-claude-train-sym24-4c7ef279-GcBqc | 2.7350 |
| sDKVR | fork-slaa-us-mmllm-claude-train-sym24-91b6b98e-sDKVR | 2.7420 |
| yuPF9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-2fec5af2-yuPF9 | 2.7506 |
| **mean** | | **2.5223** |
| **best** | | **2.3357** |

## Chain progression R1144 → R1145

Previous harvest: `workers/dispatcher/harvest-9way-r1144_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4810         | 2.5223         | +0.0413 |
| ctrl_bpc best  | 2.3381         | 2.3357         | -0.0024 |

## Per-round trajectory (best bird: egptx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1145 | 6558 | 2.3357 | +0.2545 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **2000 steps** from 25 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r1144_sym24`
  - `workers/dispatcher/harvest-4way-r1144_sym24`
  - `workers/dispatcher/harvest-9way-r1144_sym24`

## Output

`workers/dispatcher/harvest-16way-r1145_sym24/round-1145/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

