# harvest-fold33way-r77 — fold of 3 sibling harvest(s)

## Folded inputs

| harvest | round | direct birds | best ctrl_bpc | mean ctrl_bpc |
|---------|------:|-------------:|--------------:|--------------:|
| `harvest-fold15way-r77` | 77 | 15 | 0.9015 | 0.9811 |
| `harvest-fold24way-r77` | 77 | 8 | 0.9015 | 0.9802 |
| `harvest-fold4way-r76` | 76 | 4 | 0.9654 | 0.9934 |

## Cumulative across full ancestry (deduped by bird_id)

- Unique birds:   **33**
- Total steps:    **1289**
- Target round:   **77**  (input round gap: 1)
- ctrl_bpc mean: **0.9826**
- ctrl_bpc best: **0.9015**

## Output

`workers/dispatcher/harvest-fold33way-r77/round-77/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg of 3 arms)
- `dense.pt` (per-element mean of 3 arms)

