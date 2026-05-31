# Spork-chain dogfood prompt (cpu-mini × N=16 × 10 rounds)

Paste this into a fresh Claude Code (web or CLI) session. Self-contained
instructions — the agent will produce a 10-round chain whose end-state
V_net can be harvested back into the dispatcher's chain.

The dispatcher (the session that gave you this prompt) has already
completed a 10-round chain at:

    archive: /tmp/mmllm-cpu/chain-stack-0507/  (in the dispatcher's sandbox)
    final ctrl bpc: 1.60   ppl: 3.03
    final Δ_net:    +0.22
    branch:         claude/fim-training-cycle-T3giJ at 5d1318c

Your run will produce a parallel 10-round chain with a DIFFERENT seed.
We'll average your V_net into the dispatcher's V_net (FedAvg of NetBank
content), test whether two parallel chains' V_nets harvest into a
better consolidated bank than either alone.

---

You are running a 10-round shared-trunk "spork chain" on the **mmllm**
project (https://github.com/johnmn3/mmllm — branch
`claude/fim-training-cycle-T3giJ`). Read `CLAUDE.md` first; it contains
the recipe rules, the meaning of "spork" / "chain" / "Δ_local" / "Δ_net",
and explicit "don't break existing property" constraints.

## What you're producing

A 10-round chain at the **cpu-mini × N=16** configuration with the
**stack-3e-2-5.0 + mag-coef-on** recipe (documented in CLAUDE.md
"Winning bank-engagement recipes"). The infrastructure exists — DO NOT
change the recipe or swap configs.

After 10 rounds, you'll publish the round-10 archive to the repo under
`workers/<YOUR-HANDLE>/spork-chain-10/` so the dispatcher can harvest
the V_net into a merged bank.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- src/ scripts/ tests/ CLAUDE.md
pip install -e . --quiet
```

Confirm:
- `scripts/run_chain_stack.sh` exists (the cpu-mini × N=16 chain runner)
- `scripts/extend_chain.sh` exists (continues an existing archive)
- `src/mmllm/_pkm_kernels.cpp` exists (optional C++ kernel; opt-in via
  `MMLLM_ENABLE_PKM_CPP=true`, default OFF — leave off, no speedup at
  cpu-mini)
- `CLAUDE.md` "Winning bank-engagement recipes" section is present

## Pre-flight: corpus

You need the FIM-built byte corpus at `/tmp/mmllm-cpu/fim-json-v3.{train,val,test}.bin`.
If it's not there:

```bash
bash scripts/build_glaive_fim_corpus.sh
```

This takes ~5–10 min and produces a 110 MB train + 10 MB val + 10 MB test
byte-level FIM corpus from the Glaive function-calling dataset.

## Run

```bash
# Rounds 1–3 (initial chain — sets up the archive and runs rounds 1, 2, 3)
bash scripts/run_chain_stack.sh 3 100

# Capture the archive dir (it's timestamped):
ARCHIVE=$(ls -td /tmp/mmllm-cpu/chain-stack-* | head -1)
echo "ARCHIVE = $ARCHIVE"

# Extend with 7 more rounds (4–10):
bash scripts/extend_chain.sh "$ARCHIVE" 7 100
```

Total wall time: ~40 min at cpu-mini (each round ≈ 230s with the
ABL_CAP=25k default).

DO NOT pass any env overrides. The default recipe IS the winning recipe.
Specifically, do not set:
- `MMLLM_LR` (default 3e-2 is the winner — do not lower or raise)
- `MMLLM_LR_NET_MULT_END` (default 5.0 — peak Δ_net knob)
- `MMLLM_DISTILL_MAGNITUDE_COEF` (default 1.0 — mag-coef-on winner)
- `MMLLM_BATCH` (default 1, B_eff=16 — B=2 caused 1.34× slowdown)
- `MMLLM_ABLATION_EVAL_CAP` (default 25000 — saves 25% wall)
- `MMLLM_ENABLE_PKM_CPP` (leave unset — C++ kernels are 0% gain at cpu-mini)

## Watch for

Per-round wall ≈ 225–235s. If any round takes >400s, something's wrong —
check disk usage (`df -h /tmp`) and free memory (`free -g`). The cpu-mini
chain takes ~6 GB peak RSS — fine on a 15 GB sandbox.

Each round prints an ablation summary like:

```
── round 1 ablation summary (wall 230s) ──
══ ablation summary ══
  control  bpc=4.5554 ppl=23.51
  Δ_local: +0.0015
  Δ_net:   +0.2362
  Δ_both:  +0.2434  (synergy: +0.0057)
```

Expected reference trajectory (dispatcher's run, for sanity-check):

| round | ctrl bpc | Δ_net |
|------:|---------:|------:|
|     1 |    4.56  | +0.236 |
|     5 |    2.48  | +0.177 |
|    10 |    1.60  | +0.220 |

YOUR numbers will differ (different RNG seed for V_local init each round
— the script uses `np.random.default_rng(42 + round_num)`). Aim for the
ORDER OF MAGNITUDE to match: ctrl bpc ending in the 1.5–2.5 range,
Δ_net ending in the 0.15–0.30 range, monotonic-ish bpc descent across
rounds. If round-10 ctrl bpc > 3.5, training diverged — abort and dump
the train logs into the chat for diagnosis.

## Publishing the result

After round 10 completes, stage the artifacts:

```bash
HANDLE="<your-handle>"   # pick anything; lowercase, no spaces
DEST="workers/$HANDLE/spork-chain-10"
mkdir -p "$DEST"

# V_net for harvest (32 layers × 64²×8 × 4 bytes = 128 KB each, ~4 MB total)
cp "$ARCHIVE"/round-10/V_net.*.bin "$DEST/"

# Dense (the shared 2.4 MB router)
cp "$ARCHIVE"/round-10/dense.pt "$DEST/"

# Optimizer state for V_net (so chain extension is possible later)
cp "$ARCHIVE"/round-10/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round logs (so the dispatcher can reconstruct your trajectory)
for r in $(seq 1 10); do
  cp "$ARCHIVE"/round-$r/log.jsonl "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

# Meta file: dispatcher uses this to weight V_nets if harvesting > 1
cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "n_rounds": 10,
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)",
  "final_ctrl_bpc": "<read from round-10/log.jsonl 'ablation' event>",
  "final_delta_net": "<same>",
  "wall_per_round_s": [<comma-list from $ARCHIVE/wall.tsv>]
}
EOF
```

Then commit + push to your branch (NOT to the dispatcher's branch):

```bash
git checkout -b sporkchain-$HANDLE 2>/dev/null || git checkout sporkchain-$HANDLE
git add "$DEST"
git commit -m "spork-chain × 10 rounds — handle=$HANDLE final_ctrl_bpc=<...> final_delta_net=<...>"
git push -u origin "sporkchain-$HANDLE"
```

## What you report back

Two things in the chat:
1. The final-round ablation table (round 1 through round 10) — same columns
   as the reference trajectory above.
2. The branch name `sporkchain-<HANDLE>` so the dispatcher can `git fetch
   origin sporkchain-<HANDLE>` and run the harvester.

## Hard rules

- DO NOT change the recipe (CLAUDE.md "Winning bank-engagement recipes")
- DO NOT swap configs to cpu-tiny (the dispatcher's chain is at cpu-mini
  by deliberate choice — the small-router hypothesis is the point)
- DO NOT skip rounds, do not run < 10 rounds (the harvest comparison
  needs the same N_ROUNDS as the dispatcher)
- DO NOT modify the C++ kernels, scripts, or core.lpy unless something
  is genuinely broken — and if so, post the error in chat first, don't
  silently work around it
- DO commit and push every artifact under `workers/$HANDLE/spork-chain-10/`
  even if the run partially failed (a failed run with logs is more
  valuable than a missing run)
