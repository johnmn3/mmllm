"""Permissive no-op stub. The original was lost from this scratch clone (corrupt git
blob, no cached .pyc); telemetry is non-essential to training. Module-level __getattr__
makes any `mmllm.telemetry.<anything>(...)` a harmless no-op so nothing can fail on it."""

def _noop(*args, **kwargs):
    return None

def __getattr__(name):          # any attribute access → no-op callable
    return _noop
