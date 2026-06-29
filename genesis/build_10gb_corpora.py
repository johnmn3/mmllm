"""Build the 4 matured ~10GB skill-bank corpora: text · math · agentic · code.

BYTE-LEVEL model → raw UTF-8; each bank mixes MANY datasets (diversity) into one
{bank}-10g.bin.{train,val,test}.bin. Reuses mmllm.datasets.prepare_hf_dataset
per-source (byte-capped to its allocation) + concatenates the per-source splits so
val/test stay representative across all sources.

Existing registry keys are reused as-is (they already emit the <|sys|>…<|asst|>…
<|end|> + JSON tool-call envelope); MISSING sources are injected into the registry at
runtime (NO edit to the shared source file → the running cg5 line is untouched).

Usage:
  probe : stream each source to a 5MB cap, report records/skipped + a sample  (CHEAP schema check)
  probe text|math|agentic|code : probe one bank
  build text|math|agentic|code  : full build of one bank
  build all                     : full build of all four (~40GB)

Gated sources (xlam, starcoderdata) need: accept ToS on the HF page + HF token
(`huggingface-cli login` or HF_TOKEN env). Probe will FAIL loudly on those w/o auth.
"""
import sys, os, shutil, time
sys.path.insert(0, "/tmp/mmllm-trend/src")
from mmllm.datasets import (DATASET_REGISTRY, prepare_hf_dataset, _iter_hf,
                            _GLAIVE_FUNCALL_RE, _HERMES_TOOLCALL_RE)
import json, re, ast
_GLAIVE_FC = re.compile(r"<functioncall>\s*(\{.*\})", re.DOTALL)   # real glaive: <functioncall> {…} <|endoftext|> (NO closing tag)

def _loads(s):
    """Parse JSON or Python-repr (single-quoted dicts in glaive/toucan) → obj or None."""
    try: return json.loads(s)
    except Exception:
        try: return ast.literal_eval(s)
        except Exception: return None

G = "/Users/john/models/genesis"
TMP = f"{G}/_build10g"

# ══ Hermes / ChatML — THE canonical tool-calling wire format (vLLM/SGLang hermes
#    parser, Qwen2.5/3, NousResearch Hermes; what OpenCode sends open weights). ══
#    Turn frame: <|im_start|>{role}\n … <|im_end|>\n   (<|im_end|> = gen stop)
#    Call: <tool_call>\n{"name":…, "arguments":{obj}}\n</tool_call> (stacked = parallel)
#    Result: <tool_response>\n{"name":…, "content":…}\n</tool_response> under `tool` role
#    Tool decl: OpenAI {"type":"function","function":{…}} JSON, one per line in <tools>.
HE = "<|im_end|>\n"
def h_sys(c):  return f"<|im_start|>system\n{c}{HE}"
def h_user(c): return f"<|im_start|>user\n{c}{HE}"
def h_asst(c): return f"<|im_start|>assistant\n{c}{HE}"
def h_tool(c): return f"<|im_start|>tool\n{c}{HE}"
_TC_INSTR = ('You are a function calling AI model. You are provided with function signatures '
    'within <tools></tools> XML tags. You may call one or more functions to assist with the '
    "user query. Don't make assumptions about what values to plug into functions. Here are the "
    'available tools:\n<tools>\n{tools}\n</tools>\nFor each function call, return a json object '
    'with function name and arguments within <tool_call></tool_call> XML tags as follows:\n'
    '<tool_call>\n{{"name": <function-name>, "arguments": <args-json-object>}}\n</tool_call>')

def _dump(o): return json.dumps(o, ensure_ascii=False)

def h_tools_block(tools):
    """Any-shape tool schemas → one OpenAI {"type":"function","function":{…}} per line."""
    if isinstance(tools, str):            # xlam/toucan ship `tools` as a JSON STRING — parse it,
        tools = _loads(tools) or []       # else `for t in tools` iterates CHARS → empty <tools> block
    lines = []
    for t in (tools or []):
        if isinstance(t, str):
            try: t = json.loads(t)
            except Exception: continue
        if isinstance(t, dict) and t.get("type") == "function" and "function" in t:
            lines.append(_dump(t))
        elif isinstance(t, dict) and t.get("name"):
            lines.append(_dump({"type": "function", "function": t}))
    return "\n".join(lines)

def h_system_tools(tools, base=None):
    blk = h_tools_block(tools)
    if blk:
        return h_sys(_TC_INSTR.format(tools=blk) + (("\n\n" + base) if base else ""))
    return h_sys(base or "You are a helpful assistant.")

def to_calls(raw):
    """Coerce ANY vendor tool-call form → [{"name", "arguments":<dict>}] (the ONE shape)."""
    if isinstance(raw, str):
        raw = _loads(raw)
        if raw is None: return []
    if isinstance(raw, dict): raw = [raw]
    out = []
    for c in (raw or []):
        if not isinstance(c, dict): continue
        fn = c.get("function") if isinstance(c.get("function"), dict) else {}
        name = c.get("name") or c.get("tool") or fn.get("name")
        if not name: continue
        args = c.get("arguments")
        if args is None: args = c.get("args")
        if args is None: args = fn.get("arguments")
        if isinstance(args, str):
            parsed = _loads(args); args = parsed if isinstance(parsed, dict) else {"_raw": args}
        if not isinstance(args, dict): args = {} if args is None else {"value": args}
        out.append({"name": name, "arguments": args})
    return out

def h_tool_calls(calls):     # assistant turn: stacked <tool_call> blocks
    body = "\n".join(f"<tool_call>\n{_dump(c)}\n</tool_call>" for c in calls)
    return h_asst(body)

def h_tool_responses(results):  # tool turn: stacked <tool_response> blocks
    body = "\n".join(f"<tool_response>\n{_dump(r)}\n</tool_response>" for r in results)
    return h_tool(body)

# ── pretrain (raw text, no markers) + ChatML instruction/chat formatters ──
PERMISSIVE = {"mit", "apache-2.0", "apache2.0", "bsd-3-clause", "bsd-2-clause", "isc",
              "bsd", "unlicense", "cc0-1.0", "cc-by-4.0", "0bsd"}

def mk_plain(field="text", minlen=200):
    def f(rec):
        t = rec.get(field) or ""
        return t if isinstance(t, str) and len(t) >= minlen else None
    return f

def mk_plain_licensed(field="code", lic_field="license", minlen=80):
    def f(rec):
        lic = (rec.get(lic_field) or "").lower()
        if lic and lic not in PERMISSIVE:
            return None
        t = rec.get(field) or ""
        return t if isinstance(t, str) and len(t) >= minlen else None
    return f

def mk_qa(qf, af, sys=None, qfb=(), afb=()):
    def f(rec):
        q = rec.get(qf) or next((rec.get(k) for k in qfb if rec.get(k)), None)
        a = rec.get(af) or next((rec.get(k) for k in afb if rec.get(k)), None)
        if not q or not a:
            return None
        head = h_sys(sys) if sys else (h_sys(rec["system_prompt"]) if rec.get("system_prompt") else "")
        return head + h_user(str(q)) + h_asst(str(a))
    return f

# Embedded tool calls inside a chat turn's text (Hermes <tool_call> or bare JSON list/obj)
_EMB_TC = re.compile(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", re.DOTALL)

def _asst_turn(content):
    """Assistant content → normalize any embedded tool calls to canonical <tool_call>."""
    calls = [m.group(1) for m in _EMB_TC.finditer(content)]
    if calls:
        norm = []
        for c in calls: norm += to_calls(c)
        if norm: return h_tool_calls(norm)
    s = content.strip()
    if s.startswith("[") or s.startswith("{"):   # bare JSON tool-call payload
        norm = to_calls(s)
        if norm: return h_tool_calls(norm)
    return h_asst(content)

def mk_chat(fields=("messages", "conversations", "conversation"), tools_field="tools"):
    def f(rec):
        msgs = next((rec.get(k) for k in fields if rec.get(k)), None)
        if isinstance(msgs, str):                          # some rows ship messages as a JSON string
            try: msgs = json.loads(msgs)
            except Exception: return None
        if not isinstance(msgs, list) or not msgs:
            return None
        out = []
        tools = rec.get(tools_field)
        sys_done = False
        for m in msgs:
            if not isinstance(m, dict): continue
            role = (m.get("role") or m.get("from") or "user").lower()
            content = m.get("content") or m.get("value") or ""
            if isinstance(content, list):
                content = "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
            content = str(content)
            tc = m.get("tool_calls")                        # explicit tool_calls field
            if role in ("system",):
                out.append(h_system_tools(tools, content) if tools else h_sys(content)); sys_done = True
            elif role in ("user", "human"):
                out.append(h_user(content))
            elif role in ("function_call", "tool_call", "tool_calls"):   # the turn IS a call (APIGen-style)
                out.append(h_tool_calls(to_calls(content)))
            elif role in ("assistant", "gpt", "ai"):
                out.append(h_tool_calls(to_calls(tc)) if tc else _asst_turn(content))
            elif role in ("tool", "function", "observation", "tool_response"):
                out.append(h_tool_responses([{"name": m.get("name", ""), "content": content}]))
            else:
                out.append(h_user(content))
        # if a tools schema exists but no system turn declared it, prepend one
        if tools and not sys_done:
            out.insert(0, h_system_tools(tools))
        return "".join(out) if out else None
    return f

# ── structured tool-call formatters → Hermes (reuse mmllm parsers, new emission) ──
def fmt_xlam_h(rec):
    q = rec.get("query"); ans = rec.get("answers")
    calls = to_calls(ans)
    if not q or not calls: return None
    return h_system_tools(rec.get("tools")) + h_user(str(q)) + h_tool_calls(calls)

def fmt_glaive_h(rec):
    chat = rec.get("chat"); sysf = rec.get("system")
    if not isinstance(chat, str) or not chat.strip(): return None
    chat = chat.replace("<|endoftext|>", "")          # real glaive uses <|endoftext|> turn terminators
    parts = re.compile(r"\b(USER|ASSISTANT|FUNCTION RESPONSE):\s*").split(chat)
    if len(parts) < 3: return None
    out = [h_sys(sysf.strip()) if isinstance(sysf, str) and sysf.strip() else h_sys("You are a tool-using assistant.")]
    saw = False; i = 1
    while i + 1 < len(parts):
        role, body = parts[i].strip(), parts[i + 1].strip(); i += 2
        if not body: continue
        if role == "USER": out.append(h_user(body))
        elif role == "ASSISTANT":
            mm = _GLAIVE_FC.search(body)               # <functioncall> {…}  (greedy → full dict, no closing tag)
            calls = to_calls(mm.group(1)) if mm else []
            out.append(h_tool_calls(calls) if calls else h_asst(body)); saw = True
        elif role == "FUNCTION RESPONSE": out.append(h_tool_responses([{"name": "", "content": body}]))
    return "".join(out) if saw else None

def _conv_h(rec):
    """Hermes-funcall / ToolACE: conversations [{from/role, value/content}] → ChatML+Hermes."""
    convs = rec.get("conversations") or rec.get("messages")
    if not isinstance(convs, list) or not convs: return None
    out = []; saw = False; tools = rec.get("tools"); sysd = False
    for t in convs:
        if not isinstance(t, dict): continue
        role = (t.get("from") or t.get("role") or "").lower()
        body = t.get("value") or t.get("content")
        if not isinstance(body, str) or not body.strip(): continue
        body = body.strip()
        if role in ("system",):
            out.append(h_system_tools(tools, body) if tools else h_sys(body)); sysd = True
        elif role in ("human", "user"): out.append(h_user(body))
        elif role in ("gpt", "assistant"): out.append(_asst_turn(body)); saw = True
        elif role in ("tool", "function", "observation"):
            out.append(h_tool_responses([{"name": "", "content": body}]))
    if tools and not sysd: out.insert(0, h_system_tools(tools))
    return "".join(out) if saw else None

fmt_hermes_h = _conv_h
fmt_toolace_h = _conv_h

# ── inject the MISSING sources (existing keys reused untouched) ──
def _reg(key, hf_name, fmt, hf_config=None, split="train", hf_data_dir=None):
    DATASET_REGISTRY[key] = {"hf_name": hf_name, "hf_config": hf_config, "split": split,
                             "formatter": fmt, "kind": "mix", "notes": "10g-build injected",
                             **({"hf_data_dir": hf_data_dir} if hf_data_dir else {})}

# text
_reg("wikipedia",          "wikimedia/wikipedia", mk_plain("text"), hf_config="20231101.en")
_reg("project-gutenberg",  "common-pile/project_gutenberg", mk_plain("text"))
# math
_reg("finemath",           "HuggingFaceTB/finemath", mk_plain("text"), hf_config="finemath-4plus")
_reg("openmathinstruct2",  "nvidia/OpenMathInstruct-2",
     mk_qa("problem", "generated_solution", afb=("solution", "output")))
_reg("numinamath-cot",     "AI-MO/NuminaMath-CoT", mk_qa("problem", "solution"))
_reg("openr1-math",        "open-r1/OpenR1-Math-220k",
     mk_qa("problem", "solution", afb=("answer", "generation")))
_reg("metamathqa",         "meta-math/MetaMathQA", mk_qa("query", "response"))
_reg("competition-math",   "hendrycks/competition_math", mk_qa("problem", "solution"))
# agentic  (Toucan SFT subset = the canonical chat/tool-trajectory config)
_reg("toucan",             "Agent-Ark/Toucan-1.5M", mk_chat(), hf_config="SFT")       # 119k recs (~0.77GB)
_reg("toucan-kimi",        "Agent-Ark/Toucan-1.5M", mk_chat(), hf_config="Kimi-K2")   # 519k recs — fills the agentic shortfall
_reg("toucan-qwen3",       "Agent-Ark/Toucan-1.5M", mk_chat(), hf_config="Qwen3")     # 552k recs
_reg("apigen-mt",          "Salesforce/APIGen-MT-5k", mk_chat())
for _osplit in ("creative_content", "rc", "mcq", "rag"):   # orca has NO 'train' split — split by category
    _reg(f"orca-{_osplit}", "microsoft/orca-agentinstruct-1M-v1", mk_chat(), split=_osplit)
_reg("ultrachat",          "HuggingFaceH4/ultrachat_200k", mk_chat(), split="train_sft")
_reg("openorca",           "Open-Orca/OpenOrca", mk_qa("question", "response"))
# code
_reg("starcoderdata-py",   "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir="python")
_reg("starcoderdata-js",   "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir="javascript")
_reg("starcoderdata-go",   "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir="go")
_reg("starcoderdata-rust", "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir="rust")
_reg("starcoderdata-java", "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir="java")
for _lang in ("c", "cpp", "typescript", "ruby", "php"):   # github-code-clean is script-based/dead → more starcoderdata langs (parquet, gated-ok, FIM)
    _reg(f"starcoderdata-{_lang}", "bigcode/starcoderdata", mk_plain("content", minlen=80), hf_data_dir=_lang)
_reg("opencodeinstruct",   "nvidia/OpenCodeInstruct", mk_qa("input", "output", qfb=("instruction", "question"), afb=("response", "solution")))
_reg("self-oss-instruct",  "bigcode/self-oss-instruct-sc2-exec-filter-50k",
     mk_qa("instruction", "response", afb=("output",)))

# ── OVERRIDE existing-registry formatters that emit the OLD <|sys|> markers →
#    point every formatted record at the ONE ChatML+Hermes format. (Leaves the shared
#    mmllm source untouched; the running cg5 line uses its prebuilt corpora.) ──
DATASET_REGISTRY["xlam"]["formatter"]           = fmt_xlam_h
DATASET_REGISTRY["glaive-funcall"]["formatter"] = fmt_glaive_h
DATASET_REGISTRY["hermes-funcall"]["formatter"] = fmt_hermes_h
DATASET_REGISTRY["toolace"]["formatter"]        = fmt_toolace_h
DATASET_REGISTRY["dolly-instruct"]["formatter"] = mk_qa("instruction", "response")
DATASET_REGISTRY["magicoder"]["formatter"]      = mk_qa("instruction", "response", qfb=("problem",), afb=("output", "solution"))
# algebraic-stack: hoskinson-center/proof-pile is script-based/delisted → parquet proof-pile-2
DATASET_REGISTRY["algebraic-stack"]["hf_name"]   = "EleutherAI/proof-pile-2"
DATASET_REGISTRY["algebraic-stack"]["hf_config"] = "algebraic-stack"

# ── bank baskets: (registry_key, GB) ── (existing keys + injected keys) ──
GB = 1_000_000_000
BANKS = {
    "text":    [("fineweb-edu", 4.0), ("project-gutenberg", 2.5), ("wikipedia", 2.0), ("cosmopedia", 1.5)],
    "math":    [("finemath", 4.0), ("open-web-math", 2.0), ("openmathinstruct2", 2.0),
                ("numinamath-cot", 1.6), ("openr1-math", 0.3), ("metamathqa", 0.1)],
    # dropped: competition_math + proof-pile/proof-pile-2 (all script-based, delisted from Hub);
    # formal-proof axis covered by openr1 reasoning + LaTeX in finemath/open-web-math.
    "agentic": [("toucan", 4.0), ("toucan-kimi", 3.0), ("toucan-qwen3", 2.5),   # 3 Toucan configs = the tool-trajectory bulk
                ("hermes-funcall", 0.3), ("glaive-funcall", 0.27), ("xlam", 0.5), ("apigen-mt", 0.1),
                ("orca-creative_content", 0.6), ("orca-rc", 0.6), ("orca-mcq", 0.6), ("orca-rag", 0.6),
                ("ultrachat", 1.5), ("openorca", 1.5), ("dolly-instruct", 0.013)],
    "code":    [("starcoderdata-py", 1.6), ("starcoderdata-js", 1.0), ("starcoderdata-go", 0.8),
                ("starcoderdata-rust", 0.8), ("starcoderdata-java", 0.8),
                ("starcoderdata-c", 0.4), ("starcoderdata-cpp", 0.4), ("starcoderdata-typescript", 0.5),
                ("starcoderdata-ruby", 0.35), ("starcoderdata-php", 0.35),   # replaces dead github-code (2.0GB across 5 langs)
                ("opencodeinstruct", 1.5), ("self-oss-instruct", 1.0), ("magicoder", 0.5)],
}

def probe_one(key, cap=5_000_000):
    spec = DATASET_REGISTRY[key]; fmt = spec["formatter"]
    n = nk = wb = 0; sample = ""
    t0 = time.time()
    try:
        for rec in _iter_hf(spec["hf_name"], spec["hf_config"], spec["split"],
                            hf_data_dir=spec.get("hf_data_dir")):
            try:
                s = fmt(rec)
            except Exception as e:
                nk += 1
                if nk <= 2: print(f"      fmt-err: {e}")
                continue
            if not s:
                nk += 1; continue
            if not sample:
                sample = s[:240].replace("\n", "\\n")
            n += 1; wb += len(s.encode("utf-8", "replace"))
            if wb >= cap:
                break
    except Exception as e:
        return f"  ✗ {key:<20} LOAD-FAIL: {type(e).__name__}: {str(e)[:120]}"
    rate = wb / max(time.time() - t0, 1e-3) / 1e6
    return (f"  ✓ {key:<20} {n:>5} recs / {wb/1e6:4.1f}MB ({nk} skip) {rate:5.1f}MB/s\n"
            f"      ⤷ {sample}")

def build_bank(bank):
    os.makedirs(TMP, exist_ok=True)
    parts = {"train": [], "val": [], "test": []}
    for key, gb in BANKS[bank]:
        mb = int(gb * GB); out = f"{TMP}/{bank}.{key}"
        print(f"\n@@@ {bank} ← {key}  (cap {gb}GB)", flush=True)
        prepare_hf_dataset(key, out, max_bytes=mb,
                           val_bytes=int(mb * 0.02), test_bytes=int(mb * 0.02))
        for s in parts:
            p = f"{out}.{s}.bin"
            if os.path.exists(p): parts[s].append(p)
    for s in parts:
        dst = f"{G}/{bank}-10g.bin.{s}.bin"
        with open(dst, "wb") as fo:
            for p in parts[s]:
                with open(p, "rb") as fi: shutil.copyfileobj(fi, fo)
        print(f"@@@ {bank}.{s} → {dst}  ({os.path.getsize(dst)/1e9:.2f}GB)", flush=True)
    shutil.rmtree(TMP, ignore_errors=True)   # janitor: drop per-source scratch

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "probe"
    which = sys.argv[2] if len(sys.argv) > 2 else "all"
    banks = list(BANKS) if which == "all" else [which]
    if mode == "probe":
        for b in banks:
            print(f"\n===== PROBE {b} =====", flush=True)
            for key, _ in BANKS[b]:
                print(probe_one(key), flush=True)
    elif mode == "build":
        for b in banks:
            print(f"\n===== BUILD {b} =====", flush=True)
            build_bank(b)
        print("@@@ BUILD DONE", flush=True)
