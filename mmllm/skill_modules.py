"""Backend-agnostic skill-module contract.

Single source of truth shared by BOTH backends so they stay interoperable
(same modules, same on-disk V_net files → the harvester FedAvg-merges the
right ones across torch birds and MLX birds):

  * torch path  — mmllm.netbank.ModularNetBank   (GH CI birds)
  * MLX path    — mmllm.mlx.banks.netbank_forward_modular + mmllm.mlx.bridge
                  (Apple-Silicon local birds)

torch-FREE on purpose: MLX birds keep V_net as raw numpy memmaps with no
torch import at all (see mmllm/mlx/bridge.py), so this module must import
cleanly with neither torch nor mlx present.

Provides:
  - which modules exist           (MMLLM_NET_MODULES; empty → pre-fork single bank)
  - corpus → module routing        (genesis tag-routing; learned router later)
  - per-module per-layer V_net file naming (the cross-backend, harvest-visible contract)
"""
import os

# Genesis default: 3 maximally-distinct foundational atoms (language / math /
# dialogue). Later cooling stages append more module names here.
DEFAULT_MODULES = ("gutenberg-prose", "amps-math", "stackexchange-dialogue")

# corpus key (datasets.py registry) → skill-module name. Many corpora may map
# to one module (e.g. gsm8k + amps-math → the math module). Compound skills map
# to a SET via module_set_for_corpus once composition lands.
CORPUS_TO_MODULE = {
    "gutenberg-prose":        "gutenberg-prose",
    "amps-math":              "amps-math",
    "gsm8k":                  "amps-math",            # arithmetic word-problems → math
    "stackexchange-dialogue": "stackexchange-dialogue",
    # NEXT MODULE (extension on the frozen substrate): "code" — maximally DISTINCT
    # from prose/math/dialogue so it routes cleanly (cf. the dolly/prose overlap
    # that left a small routing tax). Prep magicoder → code.bin (routing key "code").
    "code":                   "code",
    "magicoder":              "code",
    "commitpackft-py":        "code",
    "the-stack-v2-py":        "code",
    # extended as modules are added in later cooling stages
}


def parse_modules(env: "str | None" = None) -> "list[str]":
    """MMLLM_NET_MODULES='a,b,c' → ['a','b','c'].

    Empty/unset → [] meaning "no partition" = the legacy single monolithic
    NetBank (pre-fork behavior, so unset is a zero-change default)."""
    raw = (env if env is not None
           else os.environ.get("MMLLM_NET_MODULES", "")).strip()
    return [m.strip() for m in raw.split(",") if m.strip()] if raw else []


def module_for_corpus(corpus_key: str, modules: "list[str]") -> "str | None":
    """Route a corpus key to its active module name. Falls back to the corpus
    key itself if that's a module; None if it maps to nothing in `modules`
    (caller decides: skip net path, or consult all / a general module)."""
    m = CORPUS_TO_MODULE.get(corpus_key, corpus_key)
    return m if m in modules else None


def netbank_v_path(prefix: str, module: str, layer: int) -> str:
    """THE per-module per-layer V_net mmap path — ONE convention for torch,
    MLX, and the harvester.

    `prefix` is the SAME path prefix the single-bank path uses (e.g.
    `<dir>/V_net`). The legacy single bank writes `<prefix>.<layer>.bin`; a
    module just inserts its name → `<prefix>.<module>.<layer>.bin`. So with
    prefix=`<dir>/V_net` this yields `<dir>/V_net.<module>.<layer>.bin`, which
    the harvester globs per-module across torch + MLX birds alike."""
    return f"{prefix}.{module}.{layer}.bin"
