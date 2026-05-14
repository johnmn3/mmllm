"""End-to-end test of harvest_chain.py stream pipeline in delta mode.

Three things verified:

1. **Delta-mode discovery.** stream_update detects worker_dir has
   delta-sparse-net.meta.pt and folds via the row-aware delta path,
   not the full-V_net.bin path.

2. **Stream + finalize ≡ standalone delta fedavg.**
   `stream_update(A); stream_update(B); stream_update(C); stream_finalize`
   produces the same per-row V_net as
   `apply(ref, fedavg([dA, dB, dC]))`.

3. **Backward-compatibility with full-V_net workers.** A worker that
   only pushes V_net.{i}.bin (legacy) still folds via the naive sum-mean
   path. Stream-finalize works in pure-legacy mode without needing
   --reference-dir.

Test runs against the production harvest_chain.py functions directly,
not via the CLI, so the path bindings (SQRT_NET=1024, C_NET=8) need to
hold. We override them to test sizes and restore at the end.
"""
import sys, tempfile
from pathlib import Path
import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import _delta_sparse_net as dsn
import harvest_chain as hc


def _write_v_net(out_dir: Path, layer_arrays, c_net):
    out_dir.mkdir(parents=True, exist_ok=True)
    n_rows = layer_arrays[0].shape[0]
    for i, a in enumerate(layer_arrays):
        m = np.memmap(out_dir / f"V_net.{i}.bin", dtype=np.float32,
                      mode="w+", shape=(n_rows, c_net))
        m[:] = a.astype(np.float32); m.flush()


def _stage_worker_delta(stage_dir: Path, handle, reference_dir, current_dir):
    """Encode worker delta from current vs reference into stage_dir/handle."""
    wd = stage_dir / handle
    wd.mkdir(parents=True, exist_ok=True)
    dsn.encode(reference_dir, current_dir, wd,
               reference_descriptor=str(reference_dir))
    # Stub dense.pt and skip opt-state (not what this test exercises).
    torch.save([torch.zeros(2, dtype=torch.float32)], wd / "dense.pt")
    return wd


def _stage_worker_full(stage_dir: Path, handle, current_dir, c_net, n_layers):
    """Copy worker's full V_net.{i}.bin into stage_dir/handle (legacy mode)."""
    import shutil
    wd = stage_dir / handle
    wd.mkdir(parents=True, exist_ok=True)
    for i in range(n_layers):
        shutil.copy(current_dir / f"V_net.{i}.bin", wd / f"V_net.{i}.bin")
    torch.save([torch.zeros(2, dtype=torch.float32)], wd / "dense.pt")
    return wd


def test_stream_delta_matches_standalone():
    # Test sizes.
    SAVED = (hc.SQRT_NET, hc.C_NET, dsn.SQRT_NET, dsn.C_NET, dsn.N_LAYERS)
    hc.SQRT_NET = 4; hc.C_NET = 2
    dsn.SQRT_NET = 4; dsn.C_NET = 2; dsn.N_LAYERS = 4
    N_ROWS = 16; C = 2; N_LAYERS = 4

    try:
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            rng = np.random.default_rng(7)

            # Build reference + 3 worker states.
            ref_arr = [rng.standard_normal((N_ROWS, C)).astype(np.float32)
                       for _ in range(N_LAYERS)]
            ref_dir = td / "ref"
            _write_v_net(ref_dir, ref_arr, C)

            # Worker A: touches rows 0, 2, 7.
            wA = [r.copy() for r in ref_arr]
            for L in wA:
                for row in [0, 2, 7]:
                    L[row] += rng.standard_normal(C).astype(np.float32) * 0.1
            wA_dir = td / "wA"; _write_v_net(wA_dir, wA, C)

            # Worker B: touches rows 2, 5.
            wB = [r.copy() for r in ref_arr]
            for L in wB:
                for row in [2, 5]:
                    L[row] += rng.standard_normal(C).astype(np.float32) * 0.2
            wB_dir = td / "wB"; _write_v_net(wB_dir, wB, C)

            # Worker C: touches rows 7, 9.
            wC = [r.copy() for r in ref_arr]
            for L in wC:
                for row in [7, 9]:
                    L[row] += rng.standard_normal(C).astype(np.float32) * 0.15
            wC_dir = td / "wC"; _write_v_net(wC_dir, wC, C)

            # ────────────────────────────────────────────────────────
            # (1) Stage as delta-mode workers; stream + finalize.
            # ────────────────────────────────────────────────────────
            stage = td / "stage"
            for h, src in [("a", wA_dir), ("b", wB_dir), ("c", wC_dir)]:
                _stage_worker_delta(stage, h, ref_dir, src)
            accum_dir = td / "accum"
            for h in ["a", "b", "c"]:
                hc.stream_update(str(accum_dir), str(stage / h), h,
                                 ctrl_bpc=1.0)

            # Verify mode counts.
            import json
            meta = json.loads((accum_dir / "meta.json").read_text())
            assert meta["v_net_mode_counts"]["delta"] == 3, meta
            assert meta["v_net_mode_counts"]["full"] == 0, meta

            harvested_prefix = str(td / "harvested.bank")
            harvested_dense  = str(td / "harvested.dense.pt")
            hc.stream_finalize(str(accum_dir), target=999,
                               harvested_prefix=harvested_prefix,
                               harvested_dense=harvested_dense,
                               publish=False, repo_root=ROOT,
                               reference_dir=str(ref_dir))

            stream_v_net = [np.array(np.memmap(f"{harvested_prefix}-net.{i}.bin",
                                               dtype=np.float32, mode="r",
                                               shape=(N_ROWS, C)))
                            for i in range(N_LAYERS)]

            # ────────────────────────────────────────────────────────
            # (2) Standalone delta fedavg + apply on the same workers.
            # ────────────────────────────────────────────────────────
            standalone_out = td / "standalone"
            dsn.fedavg(standalone_out,
                       [stage / "a", stage / "b", stage / "c"])
            standalone_recon = td / "standalone_recon"
            dsn.apply(ref_dir, standalone_out, standalone_recon)
            standalone_v_net = [np.array(np.memmap(standalone_recon / f"V_net.{i}.bin",
                                                   dtype=np.float32, mode="r",
                                                   shape=(N_ROWS, C)))
                                for i in range(N_LAYERS)]

            # Stream pipeline must match standalone delta fedavg exactly.
            for i in range(N_LAYERS):
                np.testing.assert_allclose(
                    stream_v_net[i], standalone_v_net[i], rtol=0, atol=1e-6,
                    err_msg=f"layer {i}: stream != standalone")
            print("  ✓ stream-delta pipeline ≡ standalone delta fedavg")

            # ────────────────────────────────────────────────────────
            # (3) Backward-compat: legacy full-V_net mode.
            # ────────────────────────────────────────────────────────
            stage2 = td / "stage_legacy"
            for h, src in [("a", wA_dir), ("b", wB_dir), ("c", wC_dir)]:
                _stage_worker_full(stage2, h, src, C, N_LAYERS)
            accum2 = td / "accum_legacy"
            for h in ["a", "b", "c"]:
                hc.stream_update(str(accum2), str(stage2 / h), h, ctrl_bpc=1.0)
            meta2 = json.loads((accum2 / "meta.json").read_text())
            assert meta2["v_net_mode_counts"]["delta"] == 0, meta2
            assert meta2["v_net_mode_counts"]["full"] == 3, meta2

            harvested_prefix2 = str(td / "harvested2.bank")
            harvested_dense2  = str(td / "harvested2.dense.pt")
            hc.stream_finalize(str(accum2), target=999,
                               harvested_prefix=harvested_prefix2,
                               harvested_dense=harvested_dense2,
                               publish=False, repo_root=ROOT,
                               reference_dir=None)  # not needed in legacy mode

            legacy_v_net = [np.array(np.memmap(f"{harvested_prefix2}-net.{i}.bin",
                                               dtype=np.float32, mode="r",
                                               shape=(N_ROWS, C)))
                            for i in range(N_LAYERS)]
            for i in range(N_LAYERS):
                expected = (wA[i] + wB[i] + wC[i]) / 3
                np.testing.assert_allclose(
                    legacy_v_net[i], expected, rtol=0, atol=1e-6,
                    err_msg=f"legacy layer {i}: naive mean mismatch")
            print("  ✓ legacy full-V_net pipeline still produces naive mean")

            # The two paths give *different* results at sparsely-touched rows,
            # which is the whole point of the rewrite. Confirm that.
            diff_at_row_0_layer_0 = float(np.max(np.abs(
                stream_v_net[0][0] - legacy_v_net[0][0])))
            assert diff_at_row_0_layer_0 > 0.001, (
                f"delta and legacy gave same answer at row 0 — "
                f"row-aware semantic isn't activating. diff={diff_at_row_0_layer_0:.6f}"
            )
            print(f"  ✓ delta vs legacy diverges at sparse rows "
                  f"(row 0 layer 0 diff: {diff_at_row_0_layer_0:.4f})")
    finally:
        hc.SQRT_NET, hc.C_NET, dsn.SQRT_NET, dsn.C_NET, dsn.N_LAYERS = SAVED


if __name__ == "__main__":
    test_stream_delta_matches_standalone()
    print("\nall harvest_chain delta-stream tests passed.")
