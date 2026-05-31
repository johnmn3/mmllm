"""Verify delta-sparse-net encode/apply/fedavg matches naive full-V_net FedAvg.

Three properties we care about:

1. **Roundtrip exactness.** encode(ref, current) → apply(ref, delta) ≡ current.
   The delta path is a lossless re-encoding when no rows are pruned.

2. **Single-worker reconstruction.** apply(ref, encode(ref, current))
   reproduces `current` bit-equally on touched rows and reference-equally
   on untouched rows.

3. **Multi-worker FedAvg equivalence (full-touch case).** When every
   worker touches every row, naive mean of full V_net ≡
   apply(ref, fedavg(workers' deltas)). The delta path is just the naive
   mean shifted by a constant.

4. **Multi-worker row-aware semantic (sparse-touch case).** Each row is
   averaged only over the workers that touched it, not over N. This is
   the divergence from current naive V_net FedAvg and the whole point
   of the rewrite.

Test uses small dimensions (sqrt_n=4, c_net=2, 4 layers) so it runs in
under a second. Same logic scales to design banks.
"""
import sys, tempfile
from pathlib import Path
import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import _delta_sparse_net as dsn


def _write_v_net(out_dir: Path, layer_arrays):
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, a in enumerate(layer_arrays):
        a = a.astype(np.float32)
        m = np.memmap(out_dir / f"V_net.{i}.bin", dtype=np.float32,
                      mode="w+", shape=a.shape)
        m[:] = a
        m.flush()


def _read_v_net(in_dir: Path, n_layers, n_rows, c_net):
    return [np.array(np.memmap(in_dir / f"V_net.{i}.bin", dtype=np.float32,
                               mode="r", shape=(n_rows, c_net)))
            for i in range(n_layers)]


def test_roundtrip_and_fedavg():
    # Override module's design sizes to test sizes so chunks aren't huge.
    dsn.SQRT_NET = 4
    dsn.C_NET = 2
    dsn.N_LAYERS = 4
    N_ROWS = dsn.SQRT_NET ** 2  # = 16
    C = dsn.C_NET                # = 2
    N_LAYERS = dsn.N_LAYERS      # = 4

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        rng = np.random.default_rng(0)

        # Reference: random V_net.
        ref = [rng.standard_normal((N_ROWS, C)).astype(np.float32)
               for _ in range(N_LAYERS)]
        ref_dir = td / "ref"
        _write_v_net(ref_dir, ref)

        # Worker A: touches every row (full-state semantics).
        wA = [r + rng.standard_normal(r.shape).astype(np.float32) * 0.1
              for r in ref]
        wA_dir = td / "workerA"
        _write_v_net(wA_dir, wA)

        # Worker B: touches only rows 0, 3, 5 on each layer.
        wB = [r.copy() for r in ref]
        for layer in wB:
            for row in [0, 3, 5]:
                layer[row] += rng.standard_normal(C).astype(np.float32) * 0.2
        wB_dir = td / "workerB"
        _write_v_net(wB_dir, wB)

        # Worker C: touches only rows 5, 10 on each layer.
        wC = [r.copy() for r in ref]
        for layer in wC:
            for row in [5, 10]:
                layer[row] += rng.standard_normal(C).astype(np.float32) * 0.15
        wC_dir = td / "workerC"
        _write_v_net(wC_dir, wC)

        # ────────────────────────────────────────────────────────────
        # (1) + (2): encode + apply roundtrip is bit-exact for each
        # worker.
        # ────────────────────────────────────────────────────────────
        for label, current_dir, current_state in [
            ("A", wA_dir, wA), ("B", wB_dir, wB), ("C", wC_dir, wC),
        ]:
            dchunks = td / f"delta_{label}"
            dsn.encode(ref_dir, current_dir, dchunks)
            recon = td / f"recon_{label}"
            dsn.apply(ref_dir, dchunks, recon)
            for i in range(N_LAYERS):
                rec = np.array(np.memmap(recon / f"V_net.{i}.bin",
                                         dtype=np.float32, mode="r",
                                         shape=(N_ROWS, C)))
                np.testing.assert_array_equal(
                    rec, current_state[i],
                    err_msg=f"worker {label} layer {i} roundtrip mismatch")
        print("  ✓ encode/apply roundtrip bit-exact for all 3 workers")

        # ────────────────────────────────────────────────────────────
        # (3): Full-touch case (worker A alone): apply(ref, fedavg([A]))
        # ≡ worker A's state.
        # ────────────────────────────────────────────────────────────
        out_solo = td / "fedavg_A_alone"
        dsn.fedavg(out_solo, [td / "delta_A"])
        recon_solo = td / "recon_A_alone"
        dsn.apply(ref_dir, out_solo, recon_solo)
        for i in range(N_LAYERS):
            rec = np.array(np.memmap(recon_solo / f"V_net.{i}.bin",
                                     dtype=np.float32, mode="r",
                                     shape=(N_ROWS, C)))
            np.testing.assert_allclose(rec, wA[i], rtol=0, atol=1e-7,
                                       err_msg=f"solo fedavg layer {i}")
        print("  ✓ single-worker fedavg reproduces worker state exactly")

        # ────────────────────────────────────────────────────────────
        # (4): Row-aware semantic across (A, B, C).
        # For each row, expected_merged = ref + mean(delta_w for w that
        # touched this row). Untouched rows pass through ref unchanged.
        # ────────────────────────────────────────────────────────────
        out_abc = td / "fedavg_ABC"
        dsn.fedavg(out_abc, [td / "delta_A", td / "delta_B", td / "delta_C"])
        recon_abc = td / "recon_ABC"
        dsn.apply(ref_dir, out_abc, recon_abc)

        for i in range(N_LAYERS):
            rec = np.array(np.memmap(recon_abc / f"V_net.{i}.bin",
                                     dtype=np.float32, mode="r",
                                     shape=(N_ROWS, C)))
            # Compute expected per-row.
            expected = ref[i].copy()
            for row in range(N_ROWS):
                deltas = []
                # A touches every row.
                deltas.append(wA[i][row] - ref[i][row])
                # B touches 0, 3, 5.
                if row in (0, 3, 5):
                    deltas.append(wB[i][row] - ref[i][row])
                # C touches 5, 10.
                if row in (5, 10):
                    deltas.append(wC[i][row] - ref[i][row])
                expected[row] = ref[i][row] + np.mean(deltas, axis=0)
            np.testing.assert_allclose(rec, expected, rtol=0, atol=1e-6,
                                       err_msg=f"row-aware fedavg layer {i}")

        # Sanity: the row-aware result differs from naive mean(wA, wB, wC).
        naive_mean = (wA[0] + wB[0] + wC[0]) / 3
        row_aware_recon = np.array(np.memmap(recon_abc / "V_net.0.bin",
                                             dtype=np.float32, mode="r",
                                             shape=(N_ROWS, C)))
        # Row 0: only A and B touched → row-aware ≠ naive (A+B+C)/3 which
        # would average in C's unchanged ref value.
        diff_at_row_0 = float(np.max(np.abs(row_aware_recon[0] - naive_mean[0])))
        assert diff_at_row_0 > 0.001, (
            f"row-aware result identical to naive mean at row 0 — "
            f"expected divergence > 0.001, got {diff_at_row_0:.6f}. "
            f"FedAvg is silently still naive."
        )
        print(f"  ✓ row-aware fedavg matches expected per-row mean "
              f"(diff vs naive at row 0: {diff_at_row_0:.4f})")


if __name__ == "__main__":
    test_roundtrip_and_fedavg()
    print("\nall delta-sparse-net tests passed.")
