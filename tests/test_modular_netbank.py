"""Unit tests for ModularNetBank — the skill-module partition of NetBank.

Runs in the torch training env (CI bird / Modal / local torch venv); this
box has no torch. Validates the drop-in forward, out-of-band routing,
composition, per-module param groups, and the freeze/cooling guarantee
(a cooled module's params get requires_grad=False so its V_net cannot move).

    pytest tests/test_modular_netbank.py        # or: python tests/test_modular_netbank.py
"""
import torch
from mmllm.netbank import ModularNetBank, NetBank


def _mk(names=("lang", "math", "talk")):
    # tiny, mmap-free (unit-test path: plain nn.Embedding), no sim-delay
    return ModularNetBank(
        q_dim=8, module_names=names,
        sqrt_n=16, c_net=4, top_k=4, sub_top_k=4,
        mmap_prefix=None, delay_ms_min=0.0, delay_ms_max=0.0,
    )


def test_is_dropin_for_netbank_forward():
    mb = _mk()
    q = torch.randn(2, 3, 8)
    out = mb(q)                       # same call shape as NetBank(bank_q)
    assert out.shape == (2, 3, 8)
    assert all(isinstance(b, NetBank) for b in mb.banks.values())


def test_single_module_routing():
    mb = _mk()
    mb.set_active("math")
    assert mb.active_names() == ["math"]
    assert mb(torch.randn(2, 3, 8)).shape == (2, 3, 8)


def test_composition_sums_active_modules():
    mb = _mk()
    mb.set_active(["lang", "math"])
    assert mb.active_names() == ["lang", "math"]
    assert mb(torch.randn(1, 4, 8)).shape == (1, 4, 8)
    mb.set_active(None)               # None → all modules
    assert mb.active_names() == ["lang", "math", "talk"]


def test_unknown_module_rejected():
    mb = _mk()
    try:
        mb.set_active("nope")
        assert False, "expected KeyError for unknown module"
    except KeyError:
        pass


def test_per_module_param_groups_are_disjoint():
    mb = _mk()
    sp_math = mb.module_sparse_parameters("math")
    sp_lang = mb.module_sparse_parameters("lang")
    assert len(sp_math) == 1 and sp_math[0] is mb.banks["math"].V.weight
    # disjoint tensors across modules (no shared V) — required for per-module LR
    assert sp_math[0] is not sp_lang[0]
    # aggregate = union of all modules
    assert len(mb.sparse_parameters()) == len(mb.module_names)


def test_freeze_is_structural_isolation():
    """A cooled module's params must be requires_grad=False (so optimizer
    steps are no-ops → moved% 0), while other modules stay plastic."""
    mb = _mk()
    mb.freeze_module("lang")
    assert mb.is_frozen("lang")
    assert all(not p.requires_grad
               for p in mb.module_dense_parameters("lang") + mb.module_sparse_parameters("lang"))
    # math/talk untouched — still trainable
    assert not mb.is_frozen("math")
    assert all(p.requires_grad for p in mb.module_dense_parameters("math"))
    # thaw restores
    mb.freeze_module("lang", frozen=False)
    assert not mb.is_frozen("lang")


def test_frozen_module_gets_no_grad():
    mb = _mk()
    mb.freeze_module("talk")
    mb.set_active(None)
    out = mb(torch.randn(2, 3, 8))
    out.sum().backward()
    for p in mb.module_sparse_parameters("talk") + mb.module_dense_parameters("talk"):
        assert p.grad is None, "frozen module must receive no gradient"
    # an active, non-frozen module should have grads
    assert any(p.grad is not None for p in mb.module_dense_parameters("math"))


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"all {len(fns)} ModularNetBank tests passed")
