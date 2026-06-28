"""Phase B — torch parameter container for the Mamba-2 byte enc/dec + cosine
chunker (the H-Net spine).  The LIVE training/eval path is MLX
(`mmllm/mlx/mamba.py` + `mmllm/mlx/chunker.py`); this module exists so the spine
is built as torch `nn.Module`s in `core.lpy build-model` (its weights flow
through the MLX trainer's `_extract`/`_write_back` and into `(parameters m)` at
END, for ckpt/optimizer compat).  A torch forward mirrors the MLX scan so CPU
birds / parity have a reference, but it is NOT wired into `core.lpy forward`
(default-OFF: nothing is built unless `MMLLM_HNET` is set).

Param tensors are oriented exactly like the MLX `mamba_block` param dict
(Linear-style `(out, in)`) so `_mxa(weight)` transfers them unchanged.
"""
from __future__ import annotations

import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class MambaBlock(nn.Module):
    """One minimal selective-SSM (Mamba-2 style) block.  d_inner defaults to
    d_model.  Holds exactly the tensors the MLX forward consumes."""

    def __init__(self, d_model, d_state=16, dt_rank=None, d_conv=4, expand=1, norm_eps=1e-5):
        super().__init__()
        d_inner = expand * d_model
        dt_rank = dt_rank or max(1, d_model // 16)
        self.d_state, self.dt_rank, self.d_conv, self.norm_eps = d_state, dt_rank, d_conv, norm_eps
        self.in_proj_w = nn.Parameter(torch.empty(2 * d_inner, d_model))
        self.conv_w = nn.Parameter(torch.empty(d_inner, d_conv))
        self.conv_b = nn.Parameter(torch.zeros(d_inner))
        self.x_proj_w = nn.Parameter(torch.empty(dt_rank + 2 * d_state, d_inner))
        self.dt_proj_w = nn.Parameter(torch.empty(d_inner, dt_rank))
        self.dt_proj_b = nn.Parameter(torch.zeros(d_inner))
        # S4D-real init: A = -[1..d_state] broadcast over channels (stable, standard)
        A = torch.arange(1, d_state + 1, dtype=torch.float32).repeat(d_inner, 1)
        self.A_log = nn.Parameter(torch.log(A))
        self.D = nn.Parameter(torch.ones(d_inner))
        self.out_proj_w = nn.Parameter(torch.empty(d_model, d_inner))
        self.norm_w = nn.Parameter(torch.ones(d_model))
        for w in (self.in_proj_w, self.conv_w, self.x_proj_w, self.dt_proj_w, self.out_proj_w):
            nn.init.normal_(w, std=0.02)

    def forward(self, x):  # x: (B,L,d_model) -> (B,L,d_model)  (torch reference)
        d_inner = self.A_log.shape[0]
        h = x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.norm_eps) * self.norm_w
        xz = h @ self.in_proj_w.t()
        xs, z = xz[..., :d_inner], xz[..., d_inner:]
        k = self.d_conv
        xs_c = F.conv1d(F.pad(xs.transpose(1, 2), (k - 1, 0)),
                        self.conv_w.unsqueeze(1), self.conv_b, groups=d_inner).transpose(1, 2)
        xs = F.silu(xs_c)
        proj = xs @ self.x_proj_w.t()
        dt = proj[..., :self.dt_rank]
        Bm = proj[..., self.dt_rank:self.dt_rank + self.d_state]
        Cm = proj[..., self.dt_rank + self.d_state:]
        delta = F.softplus(dt @ self.dt_proj_w.t() + self.dt_proj_b)        # (B,L,d_inner)
        A = -torch.exp(self.A_log)
        dA = torch.exp(delta.unsqueeze(-1) * A.unsqueeze(0).unsqueeze(0))   # (B,L,di,ds)
        dBu = delta.unsqueeze(-1) * Bm.unsqueeze(2) * xs.unsqueeze(-1)
        hs = torch.zeros(x.shape[0], d_inner, self.d_state, device=x.device, dtype=x.dtype)
        ys = []
        for t in range(x.shape[1]):
            hs = dA[:, t] * hs + dBu[:, t]
            ys.append((Cm[:, t].unsqueeze(1) * hs).sum(-1))
        y = torch.stack(ys, 1) + self.D * xs
        y = y * F.silu(z)
        return x + y @ self.out_proj_w.t()


class HNet(nn.Module):
    """The 1-stage H-Net spine: Mamba byte encoder/decoder + cosine chunker
    router weights (W_q, W_k).  Carries the chunk-ratio config as plain attrs."""

    def __init__(self, d_model, enc_layers=2, dec_layers=2, d_state=16,
                 target_n=6, conf_gate=False, smooth=False):
        super().__init__()
        self.enc = nn.ModuleList([MambaBlock(d_model, d_state) for _ in range(enc_layers)])
        self.dec = nn.ModuleList([MambaBlock(d_model, d_state) for _ in range(dec_layers)])
        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        nn.init.normal_(self.W_q.weight, std=0.5 / math.sqrt(d_model) ** 0.5)
        nn.init.normal_(self.W_k.weight, std=0.5 / math.sqrt(d_model) ** 0.5)
        self.target_n, self.conf_gate, self.smooth = float(target_n), bool(conf_gate), bool(smooth)
