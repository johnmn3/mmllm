# harvest-11way-r753 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R753 ctrl_bpc |
|--------|--------|--------------:|
| JJCvw | fork-davidwuchn-mmllm-claude-train-sym24-28ed0e0c-JJCvw | 3.3141 |
| yS3lP | fork-slaa-us-mmllm-claude-train-sym24-dbcf695b-yS3lP | 3.3173 |
| jcF62 | origin/claude/train-sym24-faa42397-jcF62 | 3.3286 |
| OAGGR | fork-SeniorCareMarket-mmllm-claude-train-sym24-6cc7f798-OAGGR | 3.3395 |
| NsZHR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7a0d83ee-NsZHR | 3.3516 |
| wErBV | origin/claude/train-sym24-c013b12a-wErBV | 3.3533 |
| JMcxP | fork-slaa-us-mmllm-claude-train-sym24-4d59f47b-JMcxP | 3.3534 |
| himFr | fork-joly-os-mmllm-claude-train-sym24-30367c08-himFr | 3.3544 |
| eyhUD | fork-slaa-us-mmllm-claude-train-sym24-91aab3c7-eyhUD | 3.3911 |
| IvU3t | fork-joly-os-mmllm-claude-train-sym24-07ab6a39-IvU3t | 3.4057 |
| 6TcJB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3013fc6d-6TcJB | 3.4239 |
| **mean** | | **3.3575** |
| **best** | | **3.3141** |

## Chain progression R752 → R753

Previous harvest: `workers/dispatcher/harvest-2way-r752_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3580         | 3.3575         | -0.0005 |
| ctrl_bpc best  | 3.3561         | 3.3141         | -0.0420 |

## Per-round trajectory (best bird: JJCvw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 753 | 6510 | 3.3141 | +0.5733 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r752_sym24`
  - `workers/dispatcher/harvest-2way-r752_sym24`

## Output

`workers/dispatcher/harvest-11way-r753_sym24/round-753/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

