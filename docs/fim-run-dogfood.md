# FIM training contribution — JSON single-language POC

Standard FIM (fill-in-the-middle) training contribution for the mmllm
project. Tests whether bidirectional structural conditioning (prefix +
suffix) helps the model emit valid JSON tool-call envelopes — the
open question driving the project right now. Full hypothesis in
`docs/fim-plan.md`.

~4 hours on CPU.

## Run

```bash
# 1. Get JSON source data (xlam tool-call corpus)
mmllm prepare-hf-dataset xlam /tmp/mmllm-cpu/sources/xlam 200000000 5000000 5000000

# 2. Unpack into per-doc .json files for the FIM splitter
mkdir -p /tmp/mmllm-cpu/sources/xlam-json
python3 -c "
from pathlib import Path
data = Path('/tmp/mmllm-cpu/sources/xlam.train.bin').read_bytes()
docs = [d for d in data.split(b'\n\n') if 100 < len(d) < 4096][:20000]
out = Path('/tmp/mmllm-cpu/sources/xlam-json')
for i, d in enumerate(docs):
    (out / f'doc-{i:05d}.json').write_bytes(d)
print(f'wrote {len(docs)} files')
"

# 3. Build the FIM corpus (PSM/SPM mix, json splitter)
mmllm fim-build-corpus json /tmp/mmllm-cpu/sources/xlam-json /tmp/mmllm-cpu/fim-json 0.7 0.5 42

# 4. Train (10k steps, middle-only loss mask, cpu-tiny config)
mmllm train-fim /tmp/mmllm-cpu/fim-json /tmp/mmllm-cpu/fim-bank 10000 1000 1000

# 5. FIM eval (per-language bpc + exact%)
python scripts/build_fim_eval.py
mmllm fim-eval /tmp/mmllm-cpu/fim-json.ckpts /tmp/mmllm-cpu/fim-eval.jsonl 10000

# 6. Agent eval — headline number is format_validity
mmllm eval-agent /tmp/mmllm-cpu/fim-json 10000 /tmp/mmllm-cpu/fim-bank \
    /tmp/mmllm-cpu/sources/xlam.test.bin xlam 100 256
```

## What success looks like

| metric                 | random baseline | success target |
|------------------------|-----------------|----------------|
| FIM-bpc overall        | ~7              | < 2            |
| FIM-exact overall      | 0%              | > 5%           |
| **agent format_validity** | **0.000**    | **> 0.0**      |

`format_validity` moving off zero — even trivially — is the
headline. That's the hypothesis test.

## What to commit

Drop the printed FIM-eval table + agent-eval output into a journal
entry under `docs/journal/<date>-fim-run-json-10k.md`. Add a
`meta.json` next to it (format in `WORKERS.md`). Commit on the
current branch and push.

To merge into the shared community core, also add a row to
`WORKERS.md` per its instructions and open a PR.
