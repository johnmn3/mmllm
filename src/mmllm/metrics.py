"""Energy / power instrumentation for training and inference.

Tracks the standard "green AI" units (Schwartz 2020, Patterson 2021,
Lacoste 2019, MLPerf Power v5.1, TokenPowerBench 2025):

  - Wall time (seconds)
  - Energy consumed (kWh)
  - CO2 emissions (gCO2eq, given a grid intensity)
  - Joules per token (J/tok) for inference (= kWh × 3.6e6 / n_tokens)
  - Throughput (tok/s)

Graceful degradation: if CodeCarbon isn't installed or fails to start
(no NVML on this host, RAPL unavailable inside container, network
issues fetching grid data, etc.), falls back to pynvml-only polling.
If pynvml also fails, falls back to wall-time-only with a TDP-based
estimate. Training/inference never breaks because of missing
instrumentation; the worst case is a logged warning and a partial
or zeroed energy summary.

Use as a context manager:

    with EnergyTracker(label="train-1B-ctx-add") as tr:
        # ... training or inference ...
        tr.add_tokens(n)        # call when you know the token count
    summary = tr.summary()      # {kwh, gco2eq, j_per_tok, wall_s, ...}
"""
from __future__ import annotations

import os
import threading
import time
import warnings
from typing import Optional


# Default grid intensity if no region info available (gCO2eq / kWh).
# Source: ML CO2 Impact Calculator's global average; specific datacenter
# regions range from ~20 (Quebec) to ~736 (Iowa). Override via
# MMLLM_GRID_INTENSITY env var when known.
DEFAULT_GRID_INTENSITY = 475.0  # gCO2eq / kWh

# Power Usage Effectiveness — multiplier on IT power for facility-level
# energy. Hyperscale ~1.10-1.15; assume modest cloud DC default.
DEFAULT_PUE = 1.15

# Fallback TDP estimates (W). Used only when both CodeCarbon and pynvml
# fail to provide a live reading. Wildly approximate.
TDP_FALLBACK = {
    "cuda": 400.0,  # typical A100/H100 SXM
    "cpu":   65.0,  # typical server CPU
}


def _grid_intensity() -> float:
    val = os.environ.get("MMLLM_GRID_INTENSITY")
    if val is None:
        return DEFAULT_GRID_INTENSITY
    try:
        return float(val)
    except ValueError:
        return DEFAULT_GRID_INTENSITY


def _pue() -> float:
    val = os.environ.get("MMLLM_PUE")
    if val is None:
        return DEFAULT_PUE
    try:
        return float(val)
    except ValueError:
        return DEFAULT_PUE


class _PynvmlPoller:
    """Background thread that polls pynvml for GPU power + VRAM every
    second and integrates Joules under the curve. Stops on close()."""

    def __init__(self, sample_hz: float = 1.0):
        self.sample_hz = sample_hz
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self.joules = 0.0
        self.samples = 0
        self.peak_w = 0.0
        self.peak_vram_bytes = 0  # max VRAM resident across all GPUs at any sample
        self.total_vram_bytes = 0  # total VRAM capacity across all GPUs (static)
        self._handles = []
        self._pynvml = None

    def start(self) -> bool:
        try:
            import pynvml  # type: ignore
            pynvml.nvmlInit()
            n = pynvml.nvmlDeviceGetCount()
            self._handles = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(n)]
            self._pynvml = pynvml
            # Capture total VRAM once (static per host).
            try:
                self.total_vram_bytes = sum(
                    pynvml.nvmlDeviceGetMemoryInfo(h).total
                    for h in self._handles
                )
            except Exception:
                self.total_vram_bytes = 0
        except Exception:
            return False
        if not self._handles:
            return False
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        return True

    def _loop(self):
        period = 1.0 / max(self.sample_hz, 0.1)
        last = time.time()
        while not self._stop.is_set():
            try:
                # Sum across all GPUs; nvmlDeviceGetPowerUsage returns mW.
                w_total = sum(
                    self._pynvml.nvmlDeviceGetPowerUsage(h) / 1000.0
                    for h in self._handles
                )
            except Exception:
                w_total = 0.0
            try:
                # Sum used VRAM across all GPUs at this sample. Captures
                # bank V + dense + activations + KV cache + opt state.
                vram_used = sum(
                    self._pynvml.nvmlDeviceGetMemoryInfo(h).used
                    for h in self._handles
                )
            except Exception:
                vram_used = 0
            now = time.time()
            dt = now - last
            self.joules += w_total * dt
            self.peak_w = max(self.peak_w, w_total)
            self.peak_vram_bytes = max(self.peak_vram_bytes, vram_used)
            self.samples += 1
            last = now
            self._stop.wait(period)

    def close(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2.0)
        try:
            if self._pynvml is not None:
                self._pynvml.nvmlShutdown()
        except Exception:
            pass


class EnergyTracker:
    """Context manager that records energy + carbon for a training or
    inference block. Auto-selects backend: CodeCarbon → pynvml → wall+TDP.

    Parameters
    ----------
    label : str
        Free-form tag for the block (e.g., "train-1B-ctx-add").
    device : str
        "cuda" or "cpu" — used only for the wall+TDP fallback estimate.
    """

    def __init__(self, label: str = "run", device: str = "cuda"):
        self.label = label
        self.device = device
        self._t0 = 0.0
        self._t1 = 0.0
        self._n_tokens = 0
        self._backend = "wall"  # one of: "codecarbon", "pynvml", "wall"
        self._cc_tracker = None
        self._poller: Optional[_PynvmlPoller] = None
        self._wall_kwh_estimate = 0.0
        self.start_warning: Optional[str] = None

    # ── plain API (preferred for basilisp callers — Python dunder
    #    method dispatch from the basilisp compiler is finicky) ──

    def start(self) -> "EnergyTracker":
        return self.__enter__()

    def stop(self) -> dict:
        self.__exit__(None, None, None)
        return self.summary()

    # ── context manager ──

    def __enter__(self):
        self._t0 = time.time()
        # Try CodeCarbon first.
        try:
            import logging as _logging
            from codecarbon import EmissionsTracker  # type: ignore
            # Silence codecarbon's per-15s INFO chatter — we only want
            # the start/stop summary lines, not the running power readings.
            # Affects every codecarbon.* logger globally for the process.
            _logging.getLogger("codecarbon").setLevel(_logging.WARNING)
            self._cc_tracker = EmissionsTracker(
                project_name=self.label,
                save_to_file=False,                  # we don't want emissions.csv
                logging_logger=None,
                log_level="warning",                 # also suppresses tracker's own info logs
                tracking_mode="process",
                allow_multiple_runs=True,
            )
            self._cc_tracker.start()
            self._backend = "codecarbon"
            return self
        except Exception as e:
            self.start_warning = f"codecarbon failed: {e!r}"
        # Fallback: pynvml polling thread.
        poller = _PynvmlPoller(sample_hz=1.0)
        if poller.start():
            self._poller = poller
            self._backend = "pynvml"
            return self
        # Fallback to wall+TDP only.
        self._backend = "wall"
        return self

    def __exit__(self, exc_type, exc, tb):
        self._t1 = time.time()
        if self._cc_tracker is not None:
            try:
                self._cc_tracker.stop()
            except Exception:
                pass
        if self._poller is not None:
            try:
                self._poller.close()
            except Exception:
                pass
        # Wall+TDP fallback estimate
        elapsed_s = max(self._t1 - self._t0, 1e-9)
        tdp_w = TDP_FALLBACK.get(self.device, 100.0)
        self._wall_kwh_estimate = tdp_w * elapsed_s / 3.6e6  # W·s → kWh
        return False  # don't swallow exceptions

    # ── usage ──

    def add_tokens(self, n: int) -> None:
        """Record N additional tokens processed in this block. Call
        once with the total, or accumulate via repeated calls."""
        self._n_tokens += int(n)

    # ── reporting ──

    def summary(self) -> dict:
        elapsed_s = max(self._t1 - self._t0, 1e-9)
        kwh = 0.0
        peak_w = 0.0
        peak_vram_gb = 0.0
        total_vram_gb = 0.0
        if self._backend == "codecarbon" and self._cc_tracker is not None:
            try:
                kwh = float(self._cc_tracker.final_emissions_data.energy_consumed)
            except Exception:
                kwh = 0.0
            # Try to also pull VRAM info via pynvml directly even when
            # CodeCarbon owns the energy track. CodeCarbon doesn't expose
            # peak VRAM, and we want it for the "memory hot" claim.
            try:
                import pynvml  # type: ignore
                pynvml.nvmlInit()
                n = pynvml.nvmlDeviceGetCount()
                cur_used = sum(
                    pynvml.nvmlDeviceGetMemoryInfo(
                        pynvml.nvmlDeviceGetHandleByIndex(i)
                    ).used
                    for i in range(n)
                )
                cur_total = sum(
                    pynvml.nvmlDeviceGetMemoryInfo(
                        pynvml.nvmlDeviceGetHandleByIndex(i)
                    ).total
                    for i in range(n)
                )
                pynvml.nvmlShutdown()
                # End-of-run snapshot only; not a true peak (CodeCarbon
                # doesn't poll at sample-rate). Still useful as a lower
                # bound. For peak, use pynvml backend instead.
                peak_vram_gb = cur_used / 1024**3
                total_vram_gb = cur_total / 1024**3
            except Exception:
                pass
        elif self._backend == "pynvml" and self._poller is not None:
            kwh = self._poller.joules / 3.6e6
            peak_w = self._poller.peak_w
            peak_vram_gb = self._poller.peak_vram_bytes / 1024**3
            total_vram_gb = self._poller.total_vram_bytes / 1024**3
        else:
            # Wall+TDP fallback.
            kwh = self._wall_kwh_estimate
            peak_w = TDP_FALLBACK.get(self.device, 100.0)
        # Carbon estimate
        gco2eq = kwh * _pue() * _grid_intensity()
        joules = kwh * 3.6e6
        j_per_tok = joules / self._n_tokens if self._n_tokens > 0 else 0.0
        tok_per_s = self._n_tokens / elapsed_s if self._n_tokens > 0 else 0.0
        # Estimated kWh attributable to keeping VRAM resident over wall
        # time. Uses a midpoint HBM idle figure of 0.5 W/GB; specific to
        # A100/H100-class HBM2e. NOT measured — derived from peak VRAM
        # and elapsed wall, useful only as an order-of-magnitude proxy
        # for the "what does it cost to keep this hot?" question.
        vram_idle_kwh = peak_vram_gb * 0.5 * elapsed_s / 3.6e6
        return {
            "label":            self.label,
            "backend":          self._backend,
            "wall_s":           round(elapsed_s, 3),
            "kwh":              round(kwh, 6),
            "joules":           round(joules, 1),
            "gco2eq":           round(gco2eq, 3),
            "n_tokens":         self._n_tokens,
            "j_per_tok":        round(j_per_tok, 6),
            "tok_per_s":        round(tok_per_s, 2),
            "peak_w":           round(peak_w, 1),
            "peak_vram_gb":     round(peak_vram_gb, 3),
            "total_vram_gb":    round(total_vram_gb, 3),
            "vram_idle_kwh_estimate": round(vram_idle_kwh, 6),
            "pue":              _pue(),
            "grid_g_per_kwh":   _grid_intensity(),
            "warning":          self.start_warning,
        }


def maybe_warn_no_instrumentation(summary: dict) -> None:
    """Emit a warning if the energy tracker fell back to wall+TDP
    (i.e., no live power readings)."""
    if summary.get("backend") == "wall":
        warnings.warn(
            f"EnergyTracker for '{summary.get('label')}' used wall+TDP "
            f"fallback (kWh and gCO2eq are TDP-based estimates, "
            f"not live measurements). Install codecarbon or pynvml for "
            f"real numbers."
        )
