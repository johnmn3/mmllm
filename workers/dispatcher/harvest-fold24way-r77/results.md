# harvest-fold24way-r77 — fold of 2 sibling harvest(s)

## Folded inputs

| harvest | round | direct birds | best ctrl_bpc | mean ctrl_bpc |
|---------|------:|-------------:|--------------:|--------------:|
| `harvest-fold5way-r77` | 77 | 5 | 0.9281 | 1.0075 |
| `harvest-3way-r77` | 77 | 3 | 0.9015 | 0.9347 |

## Cumulative across full ancestry (deduped by bird_id)

- Unique birds:   **24**
- Total steps:    **890**
- Target round:   **77**  (input round gap: 0)
- ctrl_bpc mean: **0.9802**
- ctrl_bpc best: **0.9015**

## Output

`workers/dispatcher/harvest-fold24way-r77/round-77/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg of 2 arms)
- `dense.pt` (per-element mean of 2 arms)

