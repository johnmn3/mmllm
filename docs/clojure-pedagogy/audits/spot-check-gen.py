"""Generate one rendered record per subject for manual spot-check."""
import importlib
import sys

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import generate_subject

with open("/home/user/mmllm/docs/clojure-pedagogy/audits/spot-check.md", "w") as f:
    f.write("# Spot-check: 1 sample record per tortoise-hare subject\n\n")
    f.write("Manual-review dump. Each subject gets one rendered record.\n\n")
    f.write("---\n\n")
    for n in range(1, 13):
        mod = importlib.import_module(
            f"mmllm.aesop.curriculum.tortoise_hare.grade_{n}"
        )
        f.write(f"## Grade {n}\n\n")
        for sid, sub in mod.SUBJECTS.items():
            recs = generate_subject(sub, n_per_example=1, seed=int(sid[3:].replace("-","")) * 13)
            r = recs[0]
            f.write(f"### {sid}: {sub.subject_title}\n\n")
            f.write(f"**form**: `{r.code_str}`  •  **expected**: `{r.expected!r}`\n\n")
            f.write("```\n")
            f.write(r.user_msg.rstrip() + "\n\n---\n\n")
            f.write(r.assistant_msg.rstrip() + "\n```\n\n")
print("done")
