# harvest-fold7way-r36 — fold of 2 sibling harvest(s)

## Folded inputs

| harvest | round | direct birds | best ctrl_bpc | mean ctrl_bpc |
|---------|------:|-------------:|--------------:|--------------:|
| `harvest-3way-r36` | 36 | 3 | 1.0954 | 1.1237 |
| `harvest-3way-r35` | 35 | 3 | 1.0027 | 1.1172 |

## Cumulative across full ancestry (deduped by bird_id)

- Unique birds:   **7**
- Total steps:    **224**
- Target round:   **36**  (input round gap: 1)
- ctrl_bpc mean: **1.1204**
- ctrl_bpc best: **1.0027**

## Output

`workers/dispatcher/harvest-fold7way-r36/round-36/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg of 2 arms)
- `dense.pt` (per-element mean of 2 arms)

