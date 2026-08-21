# harvest-6way-r1270 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1270 ctrl_bpc |
|--------|--------|--------------:|
| 9k4as | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f0e8db6-9k4as | 2.2241 |
| zUo9d | fork-slaa-us-mmllm-claude-train-sym24-7b47756a-zUo9d | 2.2347 |
| 0g5Yg | origin/claude/train-sym24-56ed36da-0g5Yg | 2.2453 |
| vpnUW | origin/claude/train-sym24-93cc2547-vpnUW | 2.2463 |
| 6LZmz | fork-SeniorCareMarket-mmllm-claude-train-sym24-067bbb4a-6LZmz | 2.4264 |
| XTHCT | fork-joly-os-mmllm-claude-train-sym24-a19cb42e-XTHCT | 2.4272 |
| **mean** | | **2.3007** |
| **best** | | **2.2241** |

## Chain progression R1269 → R1270

Previous harvest: `workers/dispatcher/harvest-9way-r1269_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4298         | 2.3007         | -0.1291 |
| ctrl_bpc best  | 2.2426         | 2.2241         | -0.0185 |

## Per-round trajectory (best bird: 9k4as)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1270 | 4119 | 2.2241 | +0.2485 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1269_sym24`
  - `workers/dispatcher/harvest-6way-r1269_sym24`

## Output

`workers/dispatcher/harvest-6way-r1270_sym24/round-1270/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

