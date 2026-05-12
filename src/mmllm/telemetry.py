"""Per-layer NetBank-vs-Local diagnostic telemetry.

Designed to answer one question: *is NetBank actually being adopted as
a function tier, or is the gate / V / routing collapsing it regardless
of how V was initialized?*

The numbers captured per layer per ablation event:

  local_out_norm     — mean L2 norm of Local Bank's residual contribution
  net_out_norm       — mean L2 norm of NetBank's residual contribution
                       (compare to local — if ~0 while local is ~5,
                       the gate is silencing NetBank)
  net_v_grad_norm    — gradient norm on NetBank V.weight (sparse-aware).
                       Near-zero ⇒ V is not getting trained at all.
  net_ka_grad_norm   — gradient norm on NetBank K_a (routing keys)
  net_kb_grad_norm   — gradient norm on NetBank K_b
  alpha_net_mean     — mean of the per-head learnable residual scale
                       on the Net path (when SwitchGate has it). If
                       collapsing toward 0 the gate is killing NetBank
                       by scaling its contribution to zero.
  gate_w_sdpa/local/net — per-tier mean softmax weight from the 3-way
                       SwitchGate. The headline "is the gate even
                       routing to Net?" — if w_net is near 0 we know
                       why NetBank can't learn (no gradient flow).

Emit cadence: once per ablation event (every MMLLM_ABLATE_EVERY steps).
Adds ~5 extra fields per block to the structured log; cheap."""
from __future__ import annotations

import json
from typing import Any


def _grad_norm(p) -> "float | None":
    """L2 norm of a parameter's current gradient. Handles sparse grads
    (SparseAdam emits coalesced sparse tensors) and the None case
    (no backward yet, or grad cleared)."""
    if p is None:
        return None
    g = p.grad
    if g is None:
        return None
    if g.is_sparse:
        v = g.coalesce().values()
        return float(v.norm().item())
    return float(g.norm().item())


def _safe_float(x) -> "float | None":
    if x is None:
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def layer_telemetry(layer_idx: int, netbank, memory, gate) -> dict:
    """Return one layer's diagnostic dict. Any field that doesn't apply
    (e.g. alpha_net when SwitchGate doesn't have it) is omitted, so
    consumers can pattern-match on presence."""
    entry: dict[str, Any] = {
        "layer":          int(layer_idx),
        "local_out_norm": _safe_float(getattr(memory, "last_output_norm", 0.0)),
    }
    # Feature-count proxy: unique pages touched in each bank's mmap storage
    # since model init. Each page covers `page_rows` V rows (default 1024).
    # A rough lower bound on accumulated "feature units" — informs adaptive
    # bank sizing across runs (start small, grow to fit observed feature
    # count). Only present when the bank uses a PagedMmapStorage; otherwise
    # the field is omitted.
    mem_storage = getattr(memory, "_storage", None)
    if mem_storage is not None and hasattr(mem_storage, "n_dirty_pages"):
        entry["local_touched_pages"] = int(mem_storage.n_dirty_pages())
    if netbank is not None:
        net_storage = getattr(netbank, "_storage", None)
        if net_storage is not None and hasattr(net_storage, "n_dirty_pages"):
            entry["net_touched_pages"] = int(net_storage.n_dirty_pages())
        entry["net_out_norm"]      = _safe_float(getattr(netbank, "last_output_norm", 0.0))
        entry["net_v_grad_norm"]   = _grad_norm(netbank.V.weight)
        entry["net_ka_grad_norm"]  = _grad_norm(netbank.K_a)
        entry["net_kb_grad_norm"]  = _grad_norm(netbank.K_b)
    if gate is not None:
        ld = getattr(gate, "last_gate_dist", None)
        if ld is not None and len(ld) >= 3:
            entry["gate_w_sdpa"]  = _safe_float(ld[0])
            entry["gate_w_local"] = _safe_float(ld[1])
            entry["gate_w_net"]   = _safe_float(ld[2])
        a = getattr(gate, "alpha_net", None)
        if a is not None:
            entry["alpha_net_mean"] = float(a.detach().mean().item())
        # local_firing_rate: mean Bernoulli decision per (B, H, T) forward,
        # present only when MMLLM_GATE_NET_DEFAULT=true. Diagnoses whether
        # the gate invokes Local on most queries (saturated near 1),
        # rarely (collapsed near 0), or selectively (target: rises with
        # corpus complexity, drops as Net consolidates patterns).
        fr = getattr(gate, "last_local_firing_rate", None)
        if fr is not None:
            entry["local_firing_rate"] = _safe_float(fr)
    return entry


def to_event_json(step: int, layers: list, event: str = "netbank_telemetry") -> str:
    """Wrap a list of layer dicts into a single-line JSONL event."""
    return json.dumps({
        "step":       int(step),
        "event":      event,
        "per_layer":  layers,
    }, separators=(",", ":"))
