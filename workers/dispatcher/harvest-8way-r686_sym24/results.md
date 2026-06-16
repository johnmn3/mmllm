# harvest-8way-r686 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R686 ctrl_bpc |
|--------|--------|--------------:|
| b1BPL | fork-slaa-us-mmllm-claude-train-sym24-66f8a689-b1BPL | 3.7412 |
| oaFzi | fork-davidwuchn-mmllm-claude-train-sym24-a3615c43-oaFzi | 3.7464 |
| ofbis | origin/claude/train-sym24-17899e70-ofbis | 3.7529 |
| aXYxt | fork-joly-os-mmllm-claude-train-sym24-e611e4a8-aXYxt | 3.7556 |
| x79jr | fork-slaa-us-mmllm-claude-train-sym24-7d130260-x79jr | 3.7816 |
| 7apeO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1ac10edf-7apeO | 3.7847 |
| DZQ38 | origin/claude/train-sym24-38f6a648-DZQ38 | 3.7997 |
| ehXHn | fork-joly-os-mmllm-claude-train-sym24-963e2639-ehXHn | 4.1220 |
| **mean** | | **3.8105** |
| **best** | | **3.7412** |

## Chain progression R685 → R686

Previous harvest: `workers/dispatcher/harvest-9way-r685_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8264         | 3.8105         | -0.0159 |
| ctrl_bpc best  | 3.7363         | 3.7412         | +0.0049 |

## Per-round trajectory (best bird: b1BPL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 686 | 6511 | 3.7412 | +0.2759 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r685_sym24`

## Output

`workers/dispatcher/harvest-8way-r686_sym24/round-686/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

