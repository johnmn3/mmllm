# FIM run dogfood — JSON single-language POC

Paste everything below the `---` into a fresh Claude Code session. ~4 hours on CPU.

---

Hey! Could you run a FIM training experiment for the mmllm project?
Tests whether giving the model both prefix and suffix (FIM) helps it
emit valid JSON tool-call envelopes. Should take ~4 hours on CPU.

Six commands. Just run them top to bottom.

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

# 6. Agent eval — the headline number is format_validity
mmllm eval-agent /tmp/mmllm-cpu/fim-json 10000 /tmp/mmllm-cpu/fim-bank \
    /tmp/mmllm-cpu/sources/xlam.test.bin xlam 100 256
```

When done, drop the printed FIM-eval table and the agent-eval result
into `docs/journal/<date>-fim-run-json-10k.md`, commit on your
dispatched branch, and push.

One-line summary back to me: `format_validity = <X>`, FIM-bpc overall,
and your gut read on whether the hypothesis (FIM fixes the
format_validity=0 problem) looks alive or dead.

Thanks!
