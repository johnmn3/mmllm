"""Generate sample text from the R90 harvested checkpoint.

Loads cpu-mini config + inf-spork-r90.{fim,bank} staging, runs
generate-style inference on a handful of prompts spanning the
9-corpus training mix (FIM tool-call, English textbook, code,
math, story).

Usage:  MMLLM_ENABLE_PKM_CPP=true python3 scripts/sample_r90.py
"""
import os, sys, time
os.environ.setdefault("MMLLM_ENABLE_PKM_CPP", "true")
os.environ.setdefault("MMLLM_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NET_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NETBANK_ENABLED", "true")
os.environ.setdefault("MMLLM_LONG_TIER_MIX", "switch")
os.environ.setdefault("MMLLM_ALPHA_NET", "true")
os.environ.setdefault("MMLLM_GATE_NET_DEFAULT", "true")
os.environ.setdefault("MMLLM_NET_SQRT_N", "64")
os.environ.setdefault("MMLLM_NET_C_NET", "8")
os.environ.setdefault("MMLLM_NET_TOP_K", "64")
os.environ.setdefault("MMLLM_NET_SUB_TOP_K", "8")

from mmllm._entry import _patch_torch
_patch_torch()
from basilisp.main import init
init()

import torch
import mmllm.core as core
import basilisp.lang.keyword as bkw

def K(s): return bkw.keyword(s)

INF_BASE = "/tmp/mmllm-cpu/inf-spork-r90.fim"
INF_BANK = "/tmp/mmllm-cpu/inf-spork-r90.bank"

cfg = core.default_config_cpu_mini
cfg = cfg.assoc(K("memory-mmap-path"), INF_BANK)
cfg = cfg.assoc(K("device"), "cpu")
cfg = cfg.assoc(K("bank-on-gpu"), False)
cfg = cfg.assoc(K("net-bank-on-gpu"), False)

print("Loading R90 harvested cpu-mini …")
m = core.build_model(cfg)
saved = list(torch.load(f"{INF_BASE}.ckpts/step-1/dense.pt", map_location="cpu", weights_only=False))
for p, s in zip(core.parameters(m), saved):
    if p.data.shape == s.shape:
        p.data.copy_(s)
core.set_eval_mode__BANG__(m)
torch.set_grad_enabled(False)
print("Model ready.\n")

PROMPTS = [
    ("FIM tool-call (Glaive-style)",
     "<|fim_pre|><|sys|>\nYou are a helpful assistant with access to tools.\n<|end|>\n<|user|>\nWhat is the weather in San Francisco?\n<|end|>\n<|asst|>\n<|fim_suf|><|fim_mid|>",
     0.0),
    ("English textbook (cosmopedia-style)",
     "<|sys|>\nYou are a textbook author. Produce clear, accurate prose.\n<|end|>\n<|asst|>\nThe water cycle describes how water moves through Earth's atmosphere, surface, and underground.",
     0.6),
    ("Python code (magicoder-style)",
     "<|sys|>\nYou are a code author. Source file (Python).\n<|end|>\n<|asst|>\ndef fibonacci(n):\n    \"\"\"Return the nth Fibonacci number.\"\"\"\n    if n <= 1:\n        return n\n    return ",
     0.0),
    ("Math (open-web-math style)",
     "<|sys|>\nYou are a math tutor working through a problem step by step.\n<|end|>\n<|asst|>\nTo find the derivative of f(x) = 3x^2 + 2x + 1, we apply the power rule.",
     0.6),
    ("Children's story (tiny-stories)",
     "<|sys|>\nYou are telling a short children's story.\n<|end|>\n<|asst|>\nOnce upon a time, there was a little frog named Pip who",
     0.7),
    ("Aesop fable / Clojure",
     "<|sys|>\nYou are telling a fable.\n<|end|>\n<|user|>\nUse the form (def x 42).\n<|end|>\n<|asst|>\n",
     0.7),
]

N_CHARS = 250

for label, prompt, temp in PROMPTS:
    print("=" * 78)
    print(f"  {label}   (temp={temp})")
    print("=" * 78)
    print("PROMPT:")
    print(prompt)
    print("-" * 78)
    print("GENERATION:")
    t0 = time.time()
    out = core.sample(m, prompt, N_CHARS, core.forward, temp)
    dt = time.time() - t0
    print(out)
    print(f"-- ({N_CHARS} chars in {dt:.1f}s = {N_CHARS/dt:.1f} char/s)")
    print()
