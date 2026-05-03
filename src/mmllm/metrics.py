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
    """Background thread that polls pynvml for GPU power every second
    and integrates Joules under the curve. Stops on close()."""

    def __init__(self, sample_hz: float = 1.0):
        self.sample_hz = sample_hz
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self.joules = 0.0
        self.samples = 0
        self.peak_w = 0.0
        self._handles = []
        self._pynvml = None

    def start(self) -> bool:
        try:
            import pynvml  # type: ignore
            pynvml.nvmlInit()
            n = pynvml.nvmlDeviceGetCount()
            self._handles = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(n)]
            self._pynvml = pynvml
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
            now = time.time()
            dt = now - last
            self.joules += w_total * dt
            self.peak_w = max(self.peak_w, w_total)
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
            from codecarbon import EmissionsTracker  # type: ignore
            self._cc_tracker = EmissionsTracker(
                project_name=self.label,
                save_to_file=False,                  # we don't want emissions.csv
                logging_logger=None,
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
        if self._backend == "codecarbon" and self._cc_tracker is not None:
            try:
                kwh = float(self._cc_tracker.final_emissions_data.energy_consumed)
            except Exception:
                kwh = 0.0
        elif self._backend == "pynvml" and self._poller is not None:
            kwh = self._poller.joules / 3.6e6
            peak_w = self._poller.peak_w
        else:
            # Wall+TDP fallback.
            kwh = self._wall_kwh_estimate
            peak_w = TDP_FALLBACK.get(self.device, 100.0)
        # Carbon estimate
        gco2eq = kwh * _pue() * _grid_intensity()
        joules = kwh * 3.6e6
        j_per_tok = joules / self._n_tokens if self._n_tokens > 0 else 0.0
        tok_per_s = self._n_tokens / elapsed_s if self._n_tokens > 0 else 0.0
        return {
            "label":       self.label,
            "backend":     self._backend,
            "wall_s":      round(elapsed_s, 3),
            "kwh":         round(kwh, 6),
            "joules":      round(joules, 1),
            "gco2eq":      round(gco2eq, 3),
            "n_tokens":    self._n_tokens,
            "j_per_tok":   round(j_per_tok, 6),
            "tok_per_s":   round(tok_per_s, 2),
            "peak_w":      round(peak_w, 1),
            "pue":         _pue(),
            "grid_g_per_kwh": _grid_intensity(),
            "warning":     self.start_warning,
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
