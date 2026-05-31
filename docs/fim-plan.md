# mmllm FIM (Fill-in-the-Middle) — corpus, eval, community fan-out plan

## Why FIM is the right next move

Standard causal LM training conditions only on past tokens. The model
must **commit** to a structural choice (open `{`, open `[`, output a
key) before it knows what closes it. That's the format_validity wall —
even at val_bpc 0.27 on xlam, the model can't synthesize valid JSON
envelopes because byte-statistical fit doesn't enforce structural
consistency at decode time.

**FIM** (Bavarian et al, arxiv:2207.14255) trains the model to fill a
middle span given **both** prefix and suffix:

```
   prefix              middle       suffix
   ───────             ──────       ──────
   <|user|> ...        ⟨FILL⟩       <|end|>
   {"tool_calls":[{    ⟨FILL⟩       ]}<|end|>
   def foo(x):\n       ⟨FILL⟩       \n\nclass Bar:
```

This is **bidirectional structural conditioning**. For JSON envelopes
the model sees the closing `]}<|end|>` as part of its conditioning
context, not as something it must blindly emit. For code, function
bodies are constrained on both sides by the signature line and the
next def. FIM has been the technique behind every strong code-completion
model (Codex, StarCoder, DeepSeek-Coder, etc.).

mmllm should benefit disproportionately because:
- **Byte-level** means we don't need to retokenize for FIM markers — any
  rare byte sequence works as a delimiter
- **PKM bank** retrieval is conditioned on the middle's prefix in our
  attention path, so the bank can cache "structural fill patterns" the
  model has seen for a given prefix+suffix shape
- **NetBank** is exactly the right tier to consolidate cross-language
  FIM patterns — the shared cerebellum pattern store

## FIM mechanics

Take a sequence and split at random points `i < j`. Reformat:

**PSM (Prefix-Suffix-Middle):**
```
   <|fim_pre|> prefix <|fim_suf|> suffix <|fim_mid|> middle <|fim_eom|>
```

**SPM (Suffix-Prefix-Middle):**
```
   <|fim_suf|> suffix <|fim_pre|> prefix <|fim_mid|> middle <|fim_eom|>
```

Train causal LM over the rearranged sequence. At inference, feed up to
`<|fim_mid|>` and sample until `<|fim_eom|>`.

**Marker bytes** — we already use `<|user|>` `<|asst|>` `<|end|>`
as multi-byte escape sequences (no special vocab needed at byte level).
Add four FIM markers in the same style:
```
   <|fim_pre|>   length 11 bytes
   <|fim_suf|>   length 11 bytes
   <|fim_mid|>   length 11 bytes
   <|fim_eom|>   length 11 bytes
```

Total marker overhead per FIM example: 4 × 11 = 44 bytes. At T=128
windows, FIM examples are 30-100% utilization (depending on chunk
size). Acceptable.

## Phase 1 — data infrastructure

### 1a. Marker constants

Add `src/mmllm/fim/markers.py`:

```python
FIM_PRE = b"<|fim_pre|>"
FIM_SUF = b"<|fim_suf|>"
FIM_MID = b"<|fim_mid|>"
FIM_EOM = b"<|fim_eom|>"
ALL_FIM_MARKERS = [FIM_PRE, FIM_SUF, FIM_MID, FIM_EOM]
```

### 1b. Generic byte-level FIM generator

`src/mmllm/fim/generator.py`:

```python
def make_fim_example(doc: bytes, *, mode: str = "psm",
                     min_middle: int = 8,
                     max_middle: int = 256,
                     rng: random.Random) -> bytes:
    """Convert raw doc to FIM-formatted bytes via random middle-span pick.
    Returns the rearranged bytes ready for training."""
```

```python
def fim_corpus(input_paths: list[Path], output_path: Path, *,
               psm_ratio: float = 0.5,            # fraction PSM vs SPM
               fim_ratio: float = 0.5,            # fraction FIM vs raw causal
               doc_split: callable | None = None, # optional structure-aware splitter
               max_doc_bytes: int = 8192,
               rng_seed: int = 0):
    """Stream-generate a FIM corpus from raw doc files.
    Mixes FIM (PSM + SPM) with raw causal at the configured ratio.
    Writes uint8 byte stream to output_path."""
```

The generic version picks split points uniformly at random in `[0, len)`.
That's the FIM v0 baseline.

### 1c. Language-aware split-point pickers

Generic random-split FIM works but wastes budget on non-structural cuts
(splitting in the middle of an identifier, etc.). For specific languages
we can prefer structural boundaries:

```
src/mmllm/fim/splitters/
  __init__.py
  generic.py    — random byte-offset picker (baseline)
  clojure.py    — split at form boundaries (between top-level forms)
                  + at sub-form boundaries inside long forms (paren-balanced)
  python.py    — split at function-def / class-def / blank lines
  json.py      — split at top-level keys / array elements / object-value
                  boundaries (parser-driven)
  c_family.py  — split at brace-balanced statement boundaries (C/C++/Java/JS)
```

Each splitter is a `(doc: bytes) -> Iterator[(prefix_end, suffix_start)]`
generator. The corpus generator uses it to pick splits, falling back to
generic if the splitter yields nothing.

For `clojure.py`: walk the byte stream tracking paren depth; emit
candidate splits at depth=0 form boundaries (between top-level defs)
and at depth=1 sub-form boundaries inside long forms.

For `json.py`: a simple state machine over `{`, `}`, `[`, `]`, `:`, `,`
positions — pick splits at value boundaries (after `:` and before `,` or `}`).

### 1d. Source corpus pipeline

```
sources/
  clojure/        ← `mmllm clone-clojure` already exists
  python/         ← bigcode/the-stack-v2-dedup (filter to lang=Python, MIT-only)
  java/           ← same, lang=Java
  json/           ← synthesize: union of existing tool-call corpora
                    (xlam.bin, glaive-funcall.bin, format-anchor.bin)
                    + parsed example schemas (OpenAPI specs, JSON-Schema
                    catalog, FastAPI sample apps)
  c-family/       ← the-stack subsets
```

`mmllm fim-build-corpus <lang> <output-prefix>`:
1. Pull or read the source data
2. Apply language-aware splitter (or generic for fallback langs)
3. Stream-write `output-prefix.{train,val,test}.bin` in FIM format
4. Print summary: doc count, byte count, FIM/causal ratio, marker overhead

Realistic sizes:
- Clojure-FIM corpus: ~500 MB (from cloned repos + sub-form splits)
- Python-FIM corpus: ~5 GB (filtered The-Stack subset)
- JSON-FIM corpus: ~200 MB (from existing tool-call corpora + sample schemas)
- C-family-FIM corpus: ~10 GB (filtered The-Stack)

Total target: 10-20 GB across languages. Each contributor pulls only
the slice they want to train on.

## Phase 2 — training integration

The FIM corpus is just bytes — training treats it identically to any
other corpus. Two integration points:

### 2a. Marker-aware loss masking (optional, recommended)

Currently `train-step` computes CE over all bytes equally. For FIM we
prefer to mask the loss to ONLY the middle portion (between `<|fim_mid|>`
and `<|fim_eom|>`). The model learns to predict middle bytes; prefix and
suffix are conditioning context.

Add `MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY` env var (default false). When
true, the train-step searches each batch for `<|fim_mid|>` ... `<|fim_eom|>`
spans and zeroes the per-position CE outside them.

Implementation: a small Python helper `mmllm/fim/loss_mask.py` that
takes `(x, y)` and returns a `(B, T)` weight tensor with 1.0 inside
middle spans, 0.0 outside.

For mixed corpora (50% FIM + 50% causal), the mask ignores causal docs
(no `<|fim_mid|>` marker present → all-1 mask, behaves as standard CE).

### 2b. CLI: `train-fim`

A thin wrapper around `train-cpu` / `train-long` that:
- Sets `MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY=true`
- Defaults the corpus prefix to `<workspace>/fim-corpus`
- Otherwise identical knobs

```bash
mmllm train-fim /tmp/fim-clojure-corpus /tmp/fim-bank 5000 500 1000
```

## Phase 3 — FIM evals

### 3a. Held-out FIM eval set

`scripts/build_fim_eval.py`: deterministic generator that produces a
small eval set across multiple languages. Each eval example is a
`(prefix, suffix, gold_middle)` tuple stored as JSONL.

### 3b. Eval metrics

Two flavors, both runnable on any ckpt:

1. **FIM-bpc** (byte-level CE on the gold middle, conditioned on prefix
   + suffix). This is the FIM equivalent of perplexity on the val set.

2. **FIM-exact** (does greedy / beam decoding produce gold middle?).
   For structured corpora (JSON, code) this is the actual test of
   structural-fill capability.

Add `mmllm fim-eval <ckpt-dir> <eval-jsonl>` CLI verb. Outputs a
per-language breakdown.

### 3c. Integration with eval-watcher

The Modal eval-watcher should automatically run FIM-eval on every new
ckpt, alongside the existing bpc + agent evals. This gives us a clean
trajectory of FIM capability over training.

## Phase 4 — community fan-out for FIM

The architecture already supports per-worker / shared-cerebellum split.
For FIM, we extend the worker contribution model with **language
specialization**:

```
                     ┌────────────────────────┐
                     │  shared NetBank        │
                     │  (cerebellum)          │
                     │                        │
                     │  rows specialize:      │
                     │   K_a/K_b → byte-      │
                     │   trigram structure    │
                     │   V → fill patterns    │
                     └────▲──────▲──────▲─────┘
                          │      │      │
              ┌───────────┘      │      └───────────┐
              │                  │                  │
       ┌──────┴──────┐    ┌──────┴───────┐   ┌──────┴───────┐
       │ Clojure     │    │ Python       │   │ JSON         │
       │ contributor │    │ contributor  │   │ contributor  │
       │             │    │              │   │              │
       │ Local Bank  │    │ Local Bank   │   │ Local Bank   │
       │ trained on  │    │ trained on   │   │ trained on   │
       │ Clj-FIM     │    │ Py-FIM       │   │ JSON-FIM     │
       └─────────────┘    └──────────────┘   └──────────────┘
```

### 4a. Per-language corpus generation on contributor box

Each contributor picks a language. The generator is local — no
giant download:

```bash
# Pull a small slice of source code for the chosen language
mmllm fim-fetch-source clojure /tmp/sources/clojure  # ~100 MB
# Or for Python:
mmllm fim-fetch-source python /tmp/sources/python   # ~500 MB

# Generate FIM corpus from local source (no network after this)
mmllm fim-build-corpus clojure /tmp/sources/clojure /tmp/fim-corpus
```

The fetch step uses HuggingFace Hub for small slices of The-Stack /
existing corpora; alternative is `clone-clojure` for live repos.

### 4b. FIM-aware `train-cpu`

Same as the consolidation-dogfood pattern, but on the FIM corpus:

```bash
MMLLM_DEVICE=cpu MMLLM_NETBANK_ENABLED=true \
  MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY=true \
  ... (rest of consolidation knobs from triune-brain-architecture.md)
mmllm train-cpu /tmp/fim-corpus /tmp/bank 10000 1000 1000
```

### 4c. Per-worker contribution payload

Same as v1 community fanout but with two additions to `meta.json`:

```json
{
  "tokens_trained": 5120000,
  "steps": 10000,
  "label": "your-handle",
  "fim": {
    "language": "clojure",
    "fim_ratio": 0.5,
    "splitter": "clojure-form-boundary",
    "fim_eval_bpc": 1.42,         # measured locally before upload
    "fim_eval_exact_pct": 12.3
  }
}
```

The harvester:
- Continues to FedAvg dense across all workers
- Continues to weighted-average NetBank V across all workers (per-row
  patterns from different languages compose because PKM rows are
  language-agnostic in structure — Clojure-form patterns and JSON-fill
  patterns can coexist in the same V row table)
- Uses `meta.fim.fim_eval_bpc` as additional weighting signal: workers
  that produced lower FIM-bpc (better consolidation) get higher weight
  in the merge

### 4d. Discovery: WORKERS.md index

Contributors open a one-line PR adding their entry to `WORKERS.md`:

```markdown
| Handle      | Language | Steps  | FIM bpc | NetBank | HF link              |
|-------------|----------|--------|---------|---------|----------------------|
| @alice      | clojure  |  10000 | 1.42    | yes     | hf:.../alice/step-10000 |
| @bob        | python   |   5000 | 1.81    | yes     | hf:.../bob/step-5000  |
| @carol      | json     |  20000 | 0.93    | yes     | hf:.../carol/step-20000 |
```

The harvester reads `WORKERS.md`, pulls the listed contributions, and
produces merged ckpts. Anyone can run the harvester independently to
verify.

## Phase 5 — validation

### 5a. Single-language proof of concept

Train on Clojure-FIM corpus only (~500 MB). After 50k steps measure:

| metric | pre-FIM | post-FIM target |
|---|---|---|
| FIM-bpc on Clojure eval | high (random, ~7) | < 2 |
| FIM-exact on Clojure eval | 0% | > 20% |
| **format_validity on agent eval (xlam)** | **0.000** | **> 0.0** |

The third row is the headline test. If FIM training on Clojure code
moves agent-eval format_validity above zero — even a tiny bit — that's
strong evidence that bidirectional structural conditioning is the
missing piece.

### 5b. Multi-language consolidation

Train K workers on different languages (Clojure, Python, JSON, C++),
harvest, evaluate. Test:

- Does the merged model FIM-bpc better than any single-language worker?
- Does NetBank actually merge useful cross-language structure?
- Does format_validity on agent eval improve more than single-language?

### 5c. Ablation: FIM vs causal at matched compute

Twin runs on identical hardware:
- Run A: 50k steps on causal-only corpus
- Run B: 50k steps on FIM corpus (mixed PSM + SPM)

Compare on the agent eval (format_validity, xlam exact_match). If B
substantially > A, the hypothesis holds and FIM should be promoted to
the default training mix.

## Implementation order

| Phase | Effort | Outcome |
|---|---|---|
| **1a-b** marker + generic FIM gen | half day | small Clojure-FIM corpus produces |
| **1c** Clojure splitter | half day | structure-aware Clojure-FIM |
| **1c** JSON splitter | half day | structure-aware JSON-FIM (the headline) |
| **2a-b** loss mask + train-fim CLI | half day | training works on FIM corpus |
| **3a-c** FIM eval pipeline + watcher integration | 1 day | trajectories visible per ckpt |
| **5a** single-language POC run | 1 day wall (CPU on sandbox) | first FIM-bpc number |
| **4** community fanout | 1 day | per-language workers possible |
| **5b/c** multi-lang + ablation | 2-3 days wall | hypothesis validated or refuted |

Total: ~1 week of dev work + a few days of compute. The cheapest path
to **first format_validity > 0** sighting is:

1. Build JSON-FIM splitter + corpus (Day 1)
2. Train a single CPU run on JSON-FIM only (Day 2 — overnight on
   sandbox)
3. Eval format_validity on the resulting ckpt

If that single experiment shows any movement off zero, the rest of the
plan is justified. If it doesn't, FIM isn't the missing piece and we
re-think.

## Open questions

1. **Marker collision** — `<|fim_pre|>` etc. could appear naturally in
   text (someone writes a doc about FIM). Realistically rare but worth
   checking. Can use even-rarer multi-byte sequences (e.g. invisible
   Unicode separators).

2. **Window length T** — FIM examples need prefix+suffix+middle+4markers
   to all fit in the training window. With T=128, prefix+suffix+middle
   ≤ 84 bytes — quite short. Larger T (e.g. T=512) would help but
   triples memory. Worth testing T=256.

3. **Mix ratio FIM vs causal** — Bavarian recommends 50% FIM. We could
   start at 50/50 and ablate.

4. **Per-language NetBank shards vs one shared NetBank** — keeping one
   shared NetBank is simpler; sharding by language gives each language
   a guaranteed slot of capacity. Not clear yet which is better;
   start with shared, ablate later.

5. **Training-time vs inference-time FIM** — at inference, the user
   provides prefix and suffix; the model fills middle. This means our
   `sample` function needs a FIM-aware variant. Trivial to implement
   (just feed `<|fim_pre|>prefix<|fim_suf|>suffix<|fim_mid|>` and
   sample to `<|fim_eom|>`), but adds a CLI surface.
