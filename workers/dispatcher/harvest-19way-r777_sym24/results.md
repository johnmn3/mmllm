# harvest-19way-r777 — sparse-delta merge of 19 birds

## Worker endpoints

| handle | branch | R777 ctrl_bpc |
|--------|--------|--------------:|
| MlBta | fork-davidwuchn-mmllm-claude-train-sym24-21843b07-MlBta | 3.2230 |
| 6GcFq | fork-slaa-us-mmllm-claude-train-sym24-8f4af5a8-6GcFq | 3.2271 |
| 9yD9R | origin/claude/train-sym24-7b29bcec-9yD9R | 3.2420 |
| OqwUw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27b87f63-OqwUw | 3.2443 |
| zRVzE | fork-davidwuchn-mmllm-claude-train-sym24-1366d0c8-zRVzE | 3.2469 |
| GLbBX | origin/claude/train-sym24-f81cc49e-GLbBX | 3.2493 |
| kRQrT | fork-joly-os-mmllm-claude-train-sym24-9d5ebe88-kRQrT | 3.3253 |
| cesgU | fork-joly-os-mmllm-claude-train-sym24-6193b0f0-cesgU | 3.3255 |
| kqvip | fork-joly-os-mmllm-claude-train-sym24-c6314cfb-kqvip | 3.3293 |
| jOqwb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1035e71a-jOqwb | 3.3310 |
| eOujr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6f0ba026-eOujr | 3.3354 |
| TsPZ0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3cfe50d0-TsPZ0 | 3.3355 |
| TgRVa | origin/claude/train-sym24-ec359c57-TgRVa | 3.3363 |
| hMack | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4cc6cc0e-hMack | 3.5699 |
| JosI0 | fork-slaa-us-mmllm-claude-train-sym24-cc0fdcd4-JosI0 | 3.5868 |
| 7IH97 | fork-slaa-us-mmllm-claude-train-sym24-ca45c1d1-7IH97 | 3.5874 |
| Rrkik | origin/claude/train-sym24-36e34bc5-Rrkik | 3.5903 |
| J1DNm | fork-davidwuchn-mmllm-claude-train-sym24-33069797-J1DNm | 3.6071 |
| 22qAk | fork-SeniorCareMarket-mmllm-claude-train-sym24-cda8035f-22qAk | 3.6126 |
| **mean** | | **3.3845** |
| **best** | | **3.2230** |

## Chain progression R776 → R777

Previous harvest: `workers/dispatcher/harvest-5way-r776_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3518         | 3.3845         | +0.0327 |
| ctrl_bpc best  | 3.2216         | 3.2230         | +0.0014 |

## Per-round trajectory (best bird: MlBta)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 777 | 6324 | 3.2230 | +0.5604 |

## Cumulative training contribution

- This harvest: **1520 steps** from 19 bird(s)
- Across full ancestry (deduped by bird_id): **1920 steps** from 24 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r776_sym24`
  - `workers/dispatcher/harvest-1way-r776_sym24`
  - `workers/dispatcher/harvest-5way-r776_sym24`

## Output

`workers/dispatcher/harvest-19way-r777_sym24/round-777/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 19 workers)
- `dense.pt` (averaged across 19 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

