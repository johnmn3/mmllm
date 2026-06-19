# harvest-6way-r716 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R716 ctrl_bpc |
|--------|--------|--------------:|
| zIX2b | fork-slaa-us-mmllm-claude-train-sym24-1cb703b3-zIX2b | 3.5587 |
| ehJKO | fork-joly-os-mmllm-claude-train-sym24-5bfe97fc-ehJKO | 3.5625 |
| 7S2W2 | origin/claude/train-sym24-bad88302-7S2W2 | 3.5701 |
| ziVwt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1516b110-ziVwt | 3.5872 |
| Ra4Mx | fork-davidwuchn-mmllm-claude-train-sym24-6b78abb1-Ra4Mx | 3.5876 |
| Hpqmk | fork-joly-os-mmllm-claude-train-sym24-32364c14-Hpqmk | 3.5954 |
| **mean** | | **3.5769** |
| **best** | | **3.5587** |

## Chain progression R715 → R716

Previous harvest: `workers/dispatcher/harvest-6way-r715_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8194         | 3.5769         | -0.2425 |
| ctrl_bpc best  | 3.5700         | 3.5587         | -0.0113 |

## Per-round trajectory (best bird: zIX2b)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 716 | 6498 | 3.5587 | +0.8729 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r715_sym24`
  - `workers/dispatcher/harvest-6way-r715_sym24`

## Output

`workers/dispatcher/harvest-6way-r716_sym24/round-716/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

