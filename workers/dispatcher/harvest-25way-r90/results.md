# harvest-25way-r90 — battery results

FedAvg of 25 workers' round-90 endpoints from the chain-diverse
extension wave (rounds 81–90, 8-corpus mix).

## Worker endpoints (individual round-90 ctrl_bpc)

| handle                       | branch                                                | R90 ctrl_bpc |
|------------------------------|-------------------------------------------------------|-------------:|
| opus47-asym-v                | claude/chaindiverse-opus47-asym-v-r90                 |       1.0376 |
| claude-ext                   | claude/chaindiverse-claude-ext-r90                    |       1.0461 |
| claude-r90ext                | claude/chaindiverse-claude-r90ext-r90                 |       1.0603 |
| kbk3y                        | claude/chaindiverse-kbk3y-r90                         |       1.0641 |
| round81to90-XWlpt            | claude/chaindiverse-round81to90-XWlpt-r90             |       1.0659 |
| opus-r90-a                   | claude/chaindiverse-opus-r90-a-r90                    |       1.0663 |
| opus47-may13                 | claude/chaindiverse-opus47-may13-r90                  |       1.0676 |
| chain-extender               | claude/chaindiverse-chain-extender-r90                |       1.0698 |
| opus47-lwcsa                 | claude/chaindiverse-opus47-lwcsa-r90                  |       1.0702 |
| uy6mw                        | claude/chaindiverse-uy6mw-r90                         |       1.0707 |
| azvzi                        | claude/chaindiverse-azvzi-r90                         |       1.0734 |
| claude-chaindiverse-T3giJ    | claude/chaindiverse-claude-chaindiverse-T3giJ-r90     |       1.0735 |
| ic0b5                        | claude/chaindiverse-ic0b5-r90                         |       1.0769 |
| opus-asym-v-mgate-r90        | claude/chaindiverse-opus-asym-v-mgate-r90-r90         |       1.0795 |
| byf1b                        | claude/chaindiverse-byf1b-r90                         |       1.0834 |
| kbykh                        | claude/chaindiverse-kbykh-r90                         |       1.0839 |
| round81to90                  | claude/chaindiverse-round81to90-r90                   |       1.0839 |
| wazkn                        | claude/chaindiverse-wazkn-r90                         |       1.0953 |
| opus47                       | claude/chaindiverse-opus47-r90                        |       1.0959 |
| opus47-1m                    | claude/chaindiverse-opus47-1m-r90                     |       1.1115 |
| fri7y                        | claude/chaindiverse-fri7y-r90                         |       1.1205 |
| opus-asym-r90                | claude/chaindiverse-opus-asym-r90-r90                 |       1.1248 |
| opus47-s1inr                 | claude/chaindiverse-opus47-s1inr-r90                  |       1.1381 |
| c2pmy                        | claude/chaindiverse-c2pmy-r90                         |       1.1807 |
| opus47-onpxv                 | claude/chaindiverse-opus47-onpxv-r90                  |       2.0331 |
| **mean**                     |                                                       |   **1.1229** |

## State similarity (pairwise across the 25 workers)

| component         | cos (pairwise mean) | range          |
|-------------------|--------------------:|---------------:|
| dense.pt          | 0.9959              | 0.9944–0.9966 |
| V_net layer 0     | 0.9508              | 0.9109–0.9702 |
| V_net layer 12    | 0.9998              | 0.9996–0.9999 |
| V_net layer 31    | 0.8706              | 0.7933–0.9082 |

## R80 harvest vs R90 harvest — full 7-dataset battery

| dataset            | R80 harvest | R90 harvest | Δ bpc   | Δ %      |
|--------------------|------------:|------------:|--------:|---------:|
| glaive-fim-val     |      1.2368 | **1.1958**  | -0.041  |  -3.3%  |
| cosmopedia         |      2.1394 | **2.0884**  | -0.051  |  -2.4%  |
| fineweb-edu        |      2.4306 | **2.3978**  | -0.033  |  -1.3%  |
| magicoder          |      2.3244 | **2.2820**  | -0.042  |  -1.8%  |
| hermes-funcall     |      2.2148 | **2.1616**  | -0.053  |  -2.4%  |
| toolace            |      2.0901 | **2.0328**  | -0.057  |  -2.7%  |
| tiny-stories       |      2.1565 | **2.0879**  | -0.069  |  -3.2%  |
| aesop-fables       |      1.3123 | **1.2483**  | -0.064  |  -4.9%  |
| open-web-math      |      2.5225 | **2.4809**  | -0.042  |  -1.6%  |
| **OOD mean (7)**   |      2.1488 |  **2.0975** | -0.051  |  -2.4%  |
| **ALL mean (8)**   |      2.0475 |  **1.9973** | -0.050  |  -2.5%  |

## Headlines

- **OOD mean dropped 2.4%** across 10 rounds.
- **Glaive in-domain improved by 3.3%** (diverse training acts as regularization).
- **Best individual worker**: `opus47-asym-v` (1.0376 ctrl_bpc).
- **FedAvg state** harvested from 25 workers.

## Final state

- `/tmp/mmllm-cpu/harvested-r90.bank-net.{0..31}.bin` — FedAvg V_net (32 × 128 KB)
- `/tmp/mmllm-cpu/harvested-r90.dense.pt` — FedAvg dense params (~2.45 MB)
- `/tmp/mmllm-cpu/inf-spork-r90.{fim,bank}` — staged inf-spork format
- `workers/dispatcher/harvest-25way-r90/round-90/` — published starting state for next dispatch wave
- `workers/dispatcher/harvest-25way-r90/eval_battery.jsonl` — battery results

Auto-generated by `scripts/generate_harvest_results.py`.
