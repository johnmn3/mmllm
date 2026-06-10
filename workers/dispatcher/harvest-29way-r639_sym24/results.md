# harvest-29way-r639 — sparse-delta merge of 29 birds

## Worker endpoints

| handle | branch | R639 ctrl_bpc |
|--------|--------|--------------:|
| SYF6a | fork-joly-os-mmllm-claude-train-sym24-9961b020-SYF6a | 5.8516 |
| NIRik | fork-slaa-us-mmllm-claude-train-sym24-436bc7ec-NIRik | 5.8591 |
| vh2K0 | fork-davidwuchn-mmllm-claude-train-sym24-68d1960e-vh2K0 | 5.8695 |
| RyOfd | fork-joly-os-mmllm-claude-train-sym24-800329d7-RyOfd | 5.8697 |
| vDQff | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5bc231f0-vDQff | 5.8715 |
| n66fM | fork-davidwuchn-mmllm-claude-train-sym24-b4eaebc1-n66fM | 5.8911 |
| RUroH | fork-slaa-us-mmllm-claude-train-sym24-4a21dfdb-RUroH | 5.8975 |
| Yf7DO | fork-slaa-us-mmllm-claude-train-sym24-d14b3fbc-Yf7DO | 5.9003 |
| 8ZPnN | fork-davidwuchn-mmllm-claude-train-sym24-e7aa4dde-8ZPnN | 5.9057 |
| DK7oJ | fork-joly-os-mmllm-claude-train-sym24-dd3f0f43-DK7oJ | 5.9213 |
| rqOhg | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b1a73448-rqOhg | 6.0069 |
| gU4G3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-da735e80-gU4G3 | 6.0089 |
| KHg4Z | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a1e30506-KHg4Z | 6.0458 |
| fRYgX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43a91cc6-fRYgX | 6.1401 |
| zsDxa | fork-joly-os-mmllm-claude-train-sym24-9c032f83-zsDxa | 6.1456 |
| wQz0q | fork-davidwuchn-mmllm-claude-train-sym24-77a5ebf7-wQz0q | 6.1679 |
| LjhUF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-acd2a47b-LjhUF | 6.1853 |
| Uvmfo | fork-joly-os-mmllm-claude-train-sym24-6e75a665-Uvmfo | 6.1889 |
| cij2r | fork-SeniorCareMarket-mmllm-claude-train-sym24-87a7f23d-cij2r | 6.1944 |
| J4vUv | origin/claude/train-sym24-6afa292c-J4vUv | 6.8014 |
| lfEpb | origin/claude/train-sym24-c28a96d2-lfEpb | 6.8337 |
| 1dxFe | fork-SeniorCareMarket-mmllm-claude-train-sym24-9680f8dd-1dxFe | 6.8429 |
| DOo3z | fork-joly-os-mmllm-claude-train-sym24-5b2ef9ce-DOo3z | 6.8539 |
| FmKcU | origin/claude/train-sym24-2a29e3e6-FmKcU | 6.8650 |
| mlW2U | fork-slaa-us-mmllm-claude-train-sym24-8340f8bf-mlW2U | 6.8802 |
| mBMgM | fork-slaa-us-mmllm-claude-train-sym24-6bc2063d-mBMgM | 6.8832 |
| vVrR8 | fork-slaa-us-mmllm-claude-train-sym24-caac05fd-vVrR8 | 6.8870 |
| JGF6S | fork-slaa-us-mmllm-claude-train-sym24-144c35be-JGF6S | 6.9231 |
| LIVW6 | origin/claude/train-sym24-LIVW6 | — |
| **mean** | | **6.2747** |
| **best** | | **5.8516** |

## Chain progression R610 → R639

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 6.2747         | +4.1375 |
| ctrl_bpc best  | 2.1268         | 5.8516         | +3.7248 |

## Per-round trajectory (best bird: SYF6a)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 639 | 2639 | 5.8516 | +0.0002 |

## Cumulative training contribution

- This harvest: **2240 steps** from 29 bird(s)
- Across full ancestry (deduped by bird_id): **2240 steps** from 29 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r638_sym24`

## Output

`workers/dispatcher/harvest-29way-r639_sym24/round-639/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 29 workers)
- `dense.pt` (averaged across 29 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

