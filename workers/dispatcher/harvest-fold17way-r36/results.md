# harvest-fold17way-r36 — mega-fold of all r36 bird contributions

Manual one-shot consolidation of every train-* branch with r36 bird payload,
including ones the hourly harvest cron orphaned via its `MAX_BIRDS=3` cap.

## Why this exists

`harvest-3way-r36` (the cron-produced harvest) FedAvg'd only 3 of 16 r36 birds.
The 13 unharvested birds included qGhOx (ctrl_bpc=0.9619, sub-1.0 for the first
time in the chain's history) and 4 others below 1.05. The cron-picked 3 ranked
~7th, 10th, 13th of 16 — so the official harvest happened to capture the worse
end of the r36 distribution.

## Folded inputs (17 birds at r36)

Sorted by worker-reported ctrl_bpc:

| handle | ctrl_bpc | Δ_net | bird_id |
|--------|---------:|-------:|---------|
| qGhOx  | 0.9619  | +0.0039 | 24b5e7d1d7c8411d |
| 0CjdM  | 1.0126  | +0.0078 | dff885721dac4657 |
| IYINg  | 1.0156  | +0.0071 | 94bdb050653844f3 |
| IgfYM  | 1.0346  | +0.0097 | c4669772b16c423a |
| sfBW4  | 1.0980  | +0.0037 | b3a938573c40441e |
| HjyYS  | 1.0954  | +0.0103 | ee69a8519e1048b2 |
| vsIrH  | 1.1056  | +0.0111 | d54f4fe7f0244653 |
| QWyjW  | 1.1126  | +0.0044 | ac24c4a32db34b4b |
| cua3D  | 1.1166  | +0.0082 | 6d90a4a97dcb44b5 |
| bccSP  | 1.1230  | +0.0092 | 19ea2995e5324b25 |
| 1ah1i  | 1.1524  | +0.0067 | 7f81a31ab329455c |
| oQeuA  | 1.1527  | +0.0087 | 0ec357cb8ccc4100 |
| iuah5  | 1.1620  | +0.0093 | a3bb21c892fa4e94 |
| FmYdP  | 1.1660  | +0.0070 | b3fa9c9db5714632 |
| E3NoP  | 1.1725  | +0.0116 | b4827362cd404e05 |
| OEbNR  | 1.1747  | +0.0064 | f756860f033349da |
| 3l9vK  | 1.2336  | +0.0070 | c6af3d35e9dc40f2 |

mean = 1.1112, best = 0.9619.

## Measured ctrl_bpc on this fold

Eval: `core.eval_bpc(m, fim-json-v3.val, T=1024, B=16, cap=25000)`, cold-start
(Local Bank at seed init — Δ_local was ~0.0 in every worker's own meta).

| state | measured ctrl_bpc |
|---|---:|
| `harvest-3way-r36` (cron, 3 birds) | 1.0709 |
| `harvest-fold7way-r36` (r35+r36 fold) | 1.0443 |
| **`harvest-fold17way-r36` (this dir)** | **1.0254** |

The mega fold beats the cron-harvest by **0.045 bpc** purely by including
contributions that already existed.

## Cumulative tally

- Direct contributors: **17 birds at r36**
- Cumulative unique birds across ancestry: **18** (17 + DEQ1e via r30)
- Cumulative steps: **616** (vs 140 in `harvest-3way-r36`, vs 224 in `fold7way-r36`)

## Also stranded at higher rounds (not folded here)

Four birds have continued past r36 to **r41** and remain unharvested:

| handle | r41 ctrl_bpc |
|---|---:|
| qVkDu | **0.9657** |
| R9IEG | 1.1498 |
| 115sE | 1.1621 |
| M0MzG | 1.2053 |

qVkDu at r41 = 0.9657 — also sub-1.0, five rounds further along. The
chain has been quietly making real progress; the hourly harvest just
hasn't been picking it up.

## Underlying issues (not fixed here)

1. **`MAX_BIRDS=3` cap in `scripts/harvest_action.sh`** (added 2026-05-20 for
   OOM mitigation) — drops most worker contributions. Needs either lifting
   or a re-harvest-with-all-birds pass.
2. **`MMLLM_STEPS_PER_ROUND=7` default in `scripts/train.sh:137`** — at 7
   steps/round the wake/sleep schedule has only 5 Local-phase + 2 Net-phase
   steps. Δ_local stays at 0.0000 (V_local doesn't move) and Δ_net stays at
   +0.004 to +0.012. The original spork recipe targets 100 steps/round; at
   that depth Δ_net = +0.05 per round was achievable.
