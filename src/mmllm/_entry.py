"""Python entry point. The CLI body lives in core.lpy."""
from basilisp.main import bootstrap


def _patch_torch():
    """Polyfill torch.nn.RMSNorm for torch < 2.4 (e.g. Intel Mac max: 2.2.x)."""
    import torch
    import torch.nn as nn

    if hasattr(nn, "RMSNorm"):
        return

    class RMSNorm(nn.Module):
        def __init__(self, normalized_shape, eps=1e-6, elementwise_affine=True,
                     device=None, dtype=None):
            super().__init__()
            if isinstance(normalized_shape, int):
                normalized_shape = (normalized_shape,)
            self.normalized_shape = tuple(normalized_shape)
            self.eps = eps
            self.elementwise_affine = elementwise_affine
            if elementwise_affine:
                self.weight = nn.Parameter(
                    torch.ones(normalized_shape, device=device, dtype=dtype)
                )

        def forward(self, x):
            rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
            x = x / rms
            if self.elementwise_affine:
                x = x * self.weight
            return x

    nn.RMSNorm = RMSNorm


def main():
    """Bootstrap basilisp and invoke mmllm.core/cli-main."""
    _patch_torch()
    return bootstrap("mmllm.core:cli-main")
