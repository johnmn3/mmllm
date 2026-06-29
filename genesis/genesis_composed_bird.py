import os, glob, shutil, time
import mlx.core as mx
mx.set_cache_limit(int(os.environ.get("MLX_CACHE_MB", "512")) << 20)   # cap the MLX buffer cache (was unbounded → 8GB hoard)
# HETEROGENEOUS COMPUTE (CPU/GPU split, PER-PROCESS): MMLLM_MLX_DEVICE=cpu routes THIS
# bird's MLX compute to the CPU; the GPU is left for the sibling GPU-bird. Each bird is
# its OWN process → its OWN Metal context (no shared-context buffer limit) → same memory
# as today's PAR=2, but CPU and GPU births run on SEPARATE units in PARALLEL. Default gpu.
if os.environ.get("MMLLM_MLX_DEVICE", "gpu").strip().lower() == "cpu":
    mx.set_default_device(mx.cpu)
    print("  [bird] MLX device = CPU (heterogeneous per-process cohort)", flush=True)
_T0 = time.monotonic()
G = os.path.expanduser("~/models/genesis")
W = int(os.environ["WB_W"]); MODULE = os.environ["WB_MODULE"]; K = int(os.environ["WB_K"])
TOTAL = int(os.environ["WB_TOTAL"]); STEPS = int(os.environ["WB_STEPS"])
ALLMODS = os.environ["WB_ALLMODS"]
TAG = os.environ.get("WAVE_TAG", "cm")
# GB-scale corpora (scaled up from the 13-19MB toys to fill the 10GB banks):
# tiny-stories→1GB tiny-stories, amps-math→1GB open-web-math, dolly-instruct→1GB
# cosmopedia, code→186MB magicoder. Module names unchanged (m4 netbank identities).
CORP = {"tiny-stories":"tiny-stories-big","amps-math":"open-web-math","dolly-instruct":"cosmopedia",
        "text":"text-10g","math":"math-10g","agentic":"agentic-10g","code":"code-10g"}   # matured 10GB banks (Hermes/ChatML)
CORPUS = CORP[MODULE]
RB = lambda w: f"{G}/{TAG}round{w}-bank"
RC = lambda w: f"{G}/{TAG}round{w}.ckpts"
pfx, ck = f"{G}/{TAG}b{W}-{MODULE}-{K}-bank", f"{G}/{TAG}b{W}-{MODULE}-{K}.ckpts"
for p in (pfx, ck):
    for f in glob.glob(p + "*"): (shutil.rmtree if os.path.isdir(f) else os.remove)(f)
# COMPOSED regime: seed ALL module slices (router needs them present) + trunk/router ckpt.
# NOT V_local (re-init = sleep reset). Cold modules are frozen (cool) AND stop-grad'd (HOT_MODULE).
rb = RB(W-1); rbn = os.path.basename(rb)
# COLD-SHARE (MMLLM_NET_COLD_SHARE, default off): clone ONLY the hot module this
# bird trains; cold modules are read in-place from the SHARED round-bank inode (no
# clone), so PAR=N births share ONE cold copy via the OS page cache (4 hot + 4
# shared-cold = 8) instead of N×4 = 16. Off → clone ALL modules (byte-identical).
_COLD_SHARE = os.environ.get("MMLLM_NET_COLD_SHARE", "").lower() in ("1", "true", "yes")
_clone_glob = f"{rb}-net.{MODULE}.*.bin" if _COLD_SHARE else f"{rb}-net.*.bin"
for f in glob.glob(_clone_glob):
    # APFS clone (cp -c): copy-on-write so cloning a 10GB SPARSE bank is instant +
    # uses ~no extra disk (shutil.copy would de-sparse → 10GB/module/bird blowup).
    os.system(f"cp -c {f!r} {pfx}{os.path.basename(f)[len(rbn):]!r}")
if _COLD_SHARE:
    # Point the netbank (torch V mmap + MLX StreamV) at the shared round-bank
    # prefix for the cold modules. Same inode across births → page-cache shared.
    os.environ["MMLLM_NET_COLD_SHARE_RB_PREFIX"] = f"{rb}-net"
latest = max(glob.glob(f"{RC(W-1)}/step-*"), key=lambda d:int(d.split('-')[-1]))
os.makedirs(ck, exist_ok=True); shutil.copytree(latest, f"{ck}/{os.path.basename(latest)}")
cool = ",".join(m for m in ALLMODS.split(",") if m != MODULE)
os.environ.update({
    "MMLLM_DEVICE":"cpu","MMLLM_NETBANK_ENABLED":"true","MMLLM_NET_MODULES":ALLMODS,  # all present
    "MMLLM_NET_SQRT_N":"256","MMLLM_NET_C_NET":"8",
    # TOP_K = rows WRITTEN per query per layer (only these fill). Was 8 (cg5-w256) → 97% of
    # the 10GB bank never touched. Design intent is 512 (core.lpy:1074). sub_top_k=32 feeds
    # it (32²=1024 ≥ top_k). THIS is the fill fix. Env-tunable.
    "MMLLM_NET_TOP_K":os.environ.get("WB_TOP_K","128"),"MMLLM_NET_SUB_TOP_K":os.environ.get("WB_SUB_TOP_K","16"),
    "MMLLM_NET_CACHE_ROWS":os.environ.get("WB_CACHE_ROWS","262144"),   # must hold TOP_K×B×T touched rows or StreamV thrashes → KeyError
    # LOCAL-bank topk: cpu-mini config defaults these to 128/128 → a 128²=16,384-wide
    # re-rank grid per layer = ~2.8GB of autograd graph. Netbank uses 8. 16 keeps a
    # healthy re-rank pool at negligible memory (16²=256). THE memory hog fix.
    "MMLLM_MEMORY_SUB_TOP_K":os.environ.get("WB_MEM_SUB_TOP_K","16"),
    "MMLLM_MEMORY_TOP_K":os.environ.get("WB_MEM_TOP_K","16"),
    # 10GB netbanks via DISK STREAMING (the only change from the working composed bird):
    # n_blocks×256²×8×4×32layers ≈ 10GB/module on disk, but only the bounded StreamV
    # row-cache is resident. NET_N_BLOCKS=160 → ~10.2GB/module.
    "MMLLM_NET_N_BLOCKS":os.environ.get("WB_N_BLOCKS","160"),"MMLLM_NET_VSTREAM":"true","MMLLM_NET_STREAM_LR":"0.003",
    "MMLLM_NET_VQ":"true","MMLLM_NET_Z_COEF":"0.1",   # learned VQ block-routing (+ commitment loss on net_z)
    "MMLLM_EVAL_BATCH":"4",                            # eval at B=4 (Δ_net does 2 passes; B=16 default spikes mem)
    "MMLLM_NET_DELAY_MIN":"0","MMLLM_NET_DELAY_MAX":"0","MMLLM_BANK_ON_GPU":"false","MMLLM_NET_BANK_ON_GPU":"false",
    "MMLLM_DISTILL_OBJECTIVE":os.environ.get("MMLLM_DISTILL_OBJECTIVE","logitkd"),"MMLLM_KD_TEMP":"2.0","MMLLM_KD_COEF":"1.0","MMLLM_KD_FREEZE":"trunk",
    "MMLLM_NET_ROUTER":"true","MMLLM_NET_ROUTER_AUX_COEF":"0.3","MMLLM_NET_ROUTER_K_LOAD":"4","MMLLM_NET_ROUTER_K_TOK":"2",
    # DE-BIAS the code monopoly: train each specialist tag-driven at FULL gradient
    # (router can't starve it), router still learns via aux, eval/inference router-driven.
    # K_LOAD=4 → all modules live at inference (was 2). See router-monopoly memory.
    "MMLLM_NET_ROUTER_DRIVE":"true",         # eval/inference: router drives (composed_bpc router-weighted)
    "MMLLM_NET_ROUTER_TRAIN_DRIVE":"false",  # TRAIN: tag-driven, specialist full gradient
    "MMLLM_NET_HOT_MODULE":MODULE,          # stop-grad all but this → composed bird ≈ single-module memory
    # Trunk SLOW-EVOLVE (was hard-frozen at 0.0): a small LR lets the trunk co-adapt,
    # and DENSE_WD is the shedding force that migrates module-absorbed skills (e.g.
    # math) OUT of the trunk and INTO the modules. Guarded by the composed retention
    # probe + drift monitor at harvest. Tunable via WB_DENSE_MULT / WB_DENSE_WD.
    "MMLLM_LR_DENSE_MULT":os.environ.get("WB_DENSE_MULT","0.03"),
    "MMLLM_LR_DENSE_WD":os.environ.get("WB_DENSE_WD","1e-4"),
    "MMLLM_NET_COOL_MODULES":cool,          # cold modules: no optimizer update
    "MMLLM_NET_CORE_MODULES":"","MMLLM_NET_EVAL_ACTIVE":"",   # eval composed (router decides)
    "MMLLM_LR_ROUND_BASE":str(TOTAL-STEPS),"MMLLM_MLX_MAX_STEPS":str(STEPS),
    "MMLLM_MIX":f"{G}/{CORPUS}.bin.train.bin:10","MMLLM_PROBE":f"{G}/{CORPUS}.bin.val.bin",
    "MEMCAP_PRESSURE_KILL":"5","MMLLM_CKPT_KEEP":"2",
    "MMLLM_LR_LOCAL_MULT":os.environ.get("WB_LOCAL_MULT","0.05"),"MMLLM_LR_LAYER_MULTS":"2.0,1.0,0.5,1.0,2.0",
    "MMLLM_LOCAL_NOISE_FRAC":"0.5","MMLLM_LOCAL_LR_WAKE":"20.0","MMLLM_LOCAL_LR_SLEEP":"1.0",
})
import basilisp.main; basilisp.main.init()
import mmllm.core as C, mmllm.mlx as mlxbk
import basilisp.lang.keyword as kw
cfg = C.default_config_cpu_mini.assoc(kw.keyword("memory-mmap-path"), pfx)
if os.environ.get("WB_SEQ_LEN"):                 # seq-len drives backward-graph memory (∝ T)
    cfg = cfg.assoc(kw.keyword("seq-len"), int(os.environ["WB_SEQ_LEN"]))
if os.environ.get("WB_D_MODEL"):                 # WIDE trunk (d_model 32→256 = ~101MB); n_heads stays 4 so attention mem unchanged
    cfg = cfg.assoc(kw.keyword("d-model"), int(os.environ["WB_D_MODEL"]))
if os.environ.get("WB_D_FF"):
    cfg = cfg.assoc(kw.keyword("d-ff"), int(os.environ["WB_D_FF"]))
base = f"{G}/{CORPUS}.bin"
_EVAL_EVERY = int(os.environ.get("MMLLM_EVAL_EVERY", "50"))   # print step/bpc this often (was STEPS → only at end)
r = mlxbk.run_round(cfg, f"{base}.train.bin", f"{base}.val.bin", ck,
                    f"{G}/{TAG}b{W}-{MODULE}-{K}.log.jsonl", TOTAL, _EVAL_EVERY, 1000000)
print(f"@@@BIRD w{W} {MODULE}.k{K}: composed_bpc={r.get('ctrl_bpc'):.4f}  "
      f"active={mx.get_active_memory()/2**30:.2f}GB cache={mx.get_cache_memory()/2**30:.2f}GB "
      f"PEAK={mx.get_peak_memory()/2**30:.2f}GB  (eval_cap={os.environ.get('MMLLM_ABLATION_EVAL_CAP','default')})", flush=True)
