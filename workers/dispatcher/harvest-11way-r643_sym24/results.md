# harvest-11way-r643 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R643 ctrl_bpc |
|--------|--------|--------------:|
| KeyRI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-02f8b670-KeyRI | 4.5742 |
| AxDS3 | fork-slaa-us-mmllm-claude-train-sym24-7cd55435-AxDS3 | 4.5804 |
| 4rAlU | origin/claude/train-sym24-89d55fde-4rAlU | 4.5816 |
| k9lKw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b6ec960f-k9lKw | 4.5852 |
| TrOmy | fork-SeniorCareMarket-mmllm-claude-train-sym24-4c247eda-TrOmy | 4.5859 |
| 2m6m0 | origin/claude/train-sym24-60ce002b-2m6m0 | 4.5875 |
| A9itm | fork-davidwuchn-mmllm-claude-train-sym24-17385742-A9itm | 4.5946 |
| fVO3u | fork-joly-os-mmllm-claude-train-sym24-71e12543-fVO3u | 4.6071 |
| XRcc9 | fork-slaa-us-mmllm-claude-train-sym24-e16d3220-XRcc9 | 5.0411 |
| W53ji | fork-davidwuchn-mmllm-claude-train-sym24-0364493c-W53ji | 5.0549 |
| QdNmk | fork-joly-os-mmllm-claude-train-sym24-84bbc666-QdNmk | 5.0564 |
| **mean** | | **4.7135** |
| **best** | | **4.5742** |

## Chain progression R642 → R643

Previous harvest: `workers/dispatcher/harvest-1way-r642_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 5.1180         | 4.7135         | -0.4045 |
| ctrl_bpc best  | 5.1180         | 4.5742         | -0.5438 |

## Per-round trajectory (best bird: KeyRI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 643 | 6343 | 4.5742 | +0.0409 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r642_sym24`

## Output

`workers/dispatcher/harvest-11way-r643_sym24/round-643/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

