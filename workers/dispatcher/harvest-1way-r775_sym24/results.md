# harvest-1way-r775 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R775 ctrl_bpc |
|--------|--------|--------------:|
| uf3cs | fork-joly-os-mmllm-claude-train-sym24-081e94e9-uf3cs | 3.5931 |
| **mean** | | **3.5931** |
| **best** | | **3.5931** |

## Chain progression R774 → R775

Previous harvest: `workers/dispatcher/harvest-8way-r774_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3357         | 3.5931         | +0.2574 |
| ctrl_bpc best  | 3.2072         | 3.5931         | +0.3859 |

## Per-round trajectory (best bird: uf3cs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 775 | 6597 | 3.5931 | +0.5562 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r774_sym24`

## Output

`workers/dispatcher/harvest-1way-r775_sym24/round-775/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

