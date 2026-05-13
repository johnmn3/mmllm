// _pkm_kernels.cpp — PKM forward kernels F2 (row gather) and F3 (fused
// outer-sum + top-K) for the mmllm CPU training path.
//
// Build (in-tree, via setup.py):
//     python setup.py build_ext --inplace
// or lazy load (no setup.py change):
//     torch.utils.cpp_extension.load(..., extra_cflags=["-fopenmp","-O3",...])
//
// Both functions:
//   * accept contiguous CPU fp32 tensors (V) / int64 tensors (indices)
//   * release the GIL (ATen ops do this; we use at::parallel_for which
//     respects the global thread pool and is GIL-safe)
//   * are read-only on V — mmap-backed V is safe across worker processes
//     via the OS page cache (MAP_SHARED + read-only access pattern)
//
// Gradient strategy (F2):
//   The C++ kernel returns the gathered tensor; backward is implemented
//   in Python (PKMGather.backward) by constructing a sparse_coo_tensor
//   keyed on idx — exactly the format CPUSparseSGD / CPUOffloadSparseAdam
//   already consume via index_add_. No new optimizer plumbing needed.

#include <torch/extension.h>
#include <ATen/Parallel.h>
#include <cstring>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <limits>

// --------------------------------------------------------------------------
// F2 — pkm_gather_rows
//
// V:   (N, D)     contiguous fp32
// idx: (...)      contiguous int64, arbitrary leading shape (B,T,K) etc.
// out: (..., D)   contiguous fp32, allocated if not provided
//
// For each flat index i in idx.numel():
//   row = idx[i]
//   memcpy(out + i*D, V + row*D, D*sizeof(float))
// --------------------------------------------------------------------------
at::Tensor pkm_gather_rows(
    const at::Tensor& V,
    const at::Tensor& idx,
    c10::optional<at::Tensor> out_opt
) {
    TORCH_CHECK(V.is_cpu(),            "V must be CPU");
    TORCH_CHECK(V.dtype() == at::kFloat,"V must be fp32");
    TORCH_CHECK(V.dim() == 2,           "V must be 2D (N, D)");
    TORCH_CHECK(V.is_contiguous(),      "V must be contiguous");
    TORCH_CHECK(idx.is_cpu(),           "idx must be CPU");
    TORCH_CHECK(idx.dtype() == at::kLong,"idx must be int64");
    TORCH_CHECK(idx.is_contiguous(),    "idx must be contiguous");

    const int64_t N = V.size(0);
    const int64_t D = V.size(1);
    const int64_t M = idx.numel();

    // Build output shape: idx.shape + (D,)
    std::vector<int64_t> out_shape(idx.sizes().begin(), idx.sizes().end());
    out_shape.push_back(D);

    at::Tensor out;
    if (out_opt.has_value()) {
        out = out_opt.value();
        TORCH_CHECK(out.is_cpu() && out.dtype() == at::kFloat && out.is_contiguous(),
                    "out must be contiguous CPU fp32");
        TORCH_CHECK(out.numel() == M * D, "out has wrong numel");
    } else {
        out = at::empty(out_shape, V.options());
    }

    if (M == 0) return out;   // empty top_global edge case

    const float*   V_ptr   = V.data_ptr<float>();
    const int64_t* idx_ptr = idx.data_ptr<int64_t>();
    float*         out_ptr = out.data_ptr<float>();
    const size_t row_bytes = static_cast<size_t>(D) * sizeof(float);

    // at::parallel_for plays nice with OMP_NUM_THREADS / TORCH_NUM_THREADS
    // and the autograd engine's own intraop pool. The body is GIL-free.
    constexpr int64_t GRAIN = 64;   // ~64 rows per chunk: row_bytes (~q_dim*4)
                                    // × 64 ≈ a few KB, fits in L1.
    at::parallel_for(0, M, GRAIN, [&](int64_t begin, int64_t end) {
        for (int64_t i = begin; i < end; ++i) {
            int64_t row = idx_ptr[i];
            // Defense-in-depth: out-of-range index would otherwise read
            // arbitrary memory. Cheap on the hot path; branch-predicted.
            TORCH_CHECK(row >= 0 && row < N, "idx out of range: ", row,
                        " not in [0, ", N, ")");
            std::memcpy(out_ptr + i * D,
                        V_ptr   + row * D,
                        row_bytes);
        }
    });
    return out;
}

// --------------------------------------------------------------------------
// F3 — pkm_fused_outer_topk
//
// top_a_s: (B, T, S)   fp32     S = sub_top_k
// top_a_i: (B, T, S)   int64
// top_b_s: (B, T, S)   fp32
// top_b_i: (B, T, S)   int64
// sqrt_n:  int64       — flat index is ia * sqrt_n + ib (matches the
//                        current Python: combined_idx = idx_a * sqrt_n + idx_b)
// top_k:   int64
//
// returns:
//   top_scores: (B, T, top_k) fp32
//   top_global: (B, T, top_k) int64
//
// Per (b,t): scan S*S pairs (S=32 → 1024 candidates), keep top_k by
// score with a binary min-heap of size top_k. Heap holds (score, ia, ib);
// when a candidate beats the current min, replace and sift-down.
//
// We DO NOT sort the output (the current Python topk doesn't either —
// torch.topk returns unsorted by default when sorted=True is the
// default but order among equals is implementation-defined; we match
// "sorted=True descending" because downstream softmax is order-invariant
// and the gather index is per-position). Tie-break: stable on (ia, ib)
// ascending — see test_fused_topk_eq comment.
// --------------------------------------------------------------------------
namespace {

struct HeapEntry {
    float   score;
    int64_t ia;
    int64_t ib;
};

inline bool heap_lt(const HeapEntry& x, const HeapEntry& y) {
    // Min-heap: parent <= children. Tie-break by (ia, ib) ascending so
    // identical-score candidates produce deterministic flat indices.
    if (x.score != y.score) return x.score < y.score;
    if (x.ia    != y.ia)    return x.ia    < y.ia;
    return x.ib < y.ib;
}

inline void sift_down(HeapEntry* h, int64_t n, int64_t i) {
    while (true) {
        int64_t l = 2 * i + 1;
        int64_t r = 2 * i + 2;
        int64_t smallest = i;
        if (l < n && heap_lt(h[l], h[smallest])) smallest = l;
        if (r < n && heap_lt(h[r], h[smallest])) smallest = r;
        if (smallest == i) return;
        std::swap(h[i], h[smallest]);
        i = smallest;
    }
}

inline void heapify(HeapEntry* h, int64_t n) {
    for (int64_t i = n / 2 - 1; i >= 0; --i) sift_down(h, n, i);
}

}  // namespace

std::tuple<at::Tensor, at::Tensor> pkm_fused_outer_topk(
    const at::Tensor& top_a_s,
    const at::Tensor& top_a_i,
    const at::Tensor& top_b_s,
    const at::Tensor& top_b_i,
    int64_t sqrt_n,
    int64_t top_k
) {
    TORCH_CHECK(top_a_s.is_cpu() && top_b_s.is_cpu(),       "top_*_s must be CPU");
    TORCH_CHECK(top_a_i.is_cpu() && top_b_i.is_cpu(),       "top_*_i must be CPU");
    TORCH_CHECK(top_a_s.dtype() == at::kFloat,              "top_a_s must be fp32");
    TORCH_CHECK(top_b_s.dtype() == at::kFloat,              "top_b_s must be fp32");
    TORCH_CHECK(top_a_i.dtype() == at::kLong,               "top_a_i must be int64");
    TORCH_CHECK(top_b_i.dtype() == at::kLong,               "top_b_i must be int64");
    TORCH_CHECK(top_a_s.dim() == 3 && top_b_s.dim() == 3,   "scores must be 3D (B,T,S)");
    TORCH_CHECK(top_a_s.is_contiguous() && top_b_s.is_contiguous() &&
                top_a_i.is_contiguous() && top_b_i.is_contiguous(),
                "all inputs must be contiguous");
    TORCH_CHECK(top_a_s.sizes() == top_a_i.sizes() &&
                top_b_s.sizes() == top_b_i.sizes() &&
                top_a_s.sizes() == top_b_s.sizes(),
                "score/index shapes must match");
    TORCH_CHECK(top_k > 0,  "top_k must be > 0");
    TORCH_CHECK(sqrt_n > 0, "sqrt_n must be > 0");

    const int64_t B = top_a_s.size(0);
    const int64_t T = top_a_s.size(1);
    const int64_t S = top_a_s.size(2);
    const int64_t BT = B * T;
    const int64_t S2 = S * S;
    TORCH_CHECK(top_k <= S2, "top_k must be <= sub_top_k**2");

    at::Tensor top_scores = at::empty({B, T, top_k}, top_a_s.options());
    at::Tensor top_global = at::empty({B, T, top_k}, top_a_i.options());

    const float*   pas = top_a_s.data_ptr<float>();
    const int64_t* pai = top_a_i.data_ptr<int64_t>();
    const float*   pbs = top_b_s.data_ptr<float>();
    const int64_t* pbi = top_b_i.data_ptr<int64_t>();
    float*         pos = top_scores.data_ptr<float>();
    int64_t*       pog = top_global.data_ptr<int64_t>();

    // One (b,t) row per task; per-row heap of size top_k. S=32, top_k=16
    // → 1024 scans + 16-entry heap per row. Cache-hot per task.
    constexpr int64_t GRAIN = 8;
    at::parallel_for(0, BT, GRAIN, [&](int64_t begin, int64_t end) {
        // Thread-local heap buffer reused across rows in this chunk.
        std::vector<HeapEntry> heap(static_cast<size_t>(top_k));

        for (int64_t bt = begin; bt < end; ++bt) {
            const float*   as = pas + bt * S;
            const int64_t* ai = pai + bt * S;
            const float*   bs = pbs + bt * S;
            const int64_t* bi = pbi + bt * S;

            // Seed heap with the first top_k pairs (in row-major ia,ib).
            int64_t filled = 0;
            for (int64_t ia = 0; ia < S && filled < top_k; ++ia) {
                for (int64_t ib = 0; ib < S && filled < top_k; ++ib) {
                    heap[filled].score = as[ia] + bs[ib];
                    heap[filled].ia    = ai[ia];
                    heap[filled].ib    = bi[ib];
                    ++filled;
                }
            }
            heapify(heap.data(), top_k);

            // Scan the remaining S*S - top_k pairs. (For S=32,top_k=16 we
            // start at flat pair index 16; the seed loop above filled the
            // first row + first 16 entries of the second row, but we just
            // restart from scratch to keep the index math simple — the
            // extra ~16 compares are negligible.)
            int64_t scanned = 0;
            for (int64_t ia = 0; ia < S; ++ia) {
                const float a_s = as[ia];
                const int64_t a_i = ai[ia];
                for (int64_t ib = 0; ib < S; ++ib) {
                    if (scanned++ < top_k) continue;  // already in heap
                    const float cand_score = a_s + bs[ib];
                    // Min-heap root is current smallest among kept top_k.
                    // If cand is strictly greater → replace + sift.
                    HeapEntry& root = heap[0];
                    if (cand_score > root.score) {
                        root.score = cand_score;
                        root.ia    = a_i;
                        root.ib    = bi[ib];
                        sift_down(heap.data(), top_k, 0);
                    }
                }
            }

            // Emit unsorted (matches what downstream softmax expects).
            // If a sorted output were ever required, do an in-place
            // heap-sort here — O(top_k log top_k), trivial.
            float*   out_s = pos + bt * top_k;
            int64_t* out_g = pog + bt * top_k;
            for (int64_t k = 0; k < top_k; ++k) {
                out_s[k] = heap[k].score;
                out_g[k] = heap[k].ia * sqrt_n + heap[k].ib;
            }
        }
    });

    return std::make_tuple(top_scores, top_global);
}

// --------------------------------------------------------------------------
// Registration. We use pybind11 (TORCH_EXTENSION_NAME comes from setup.py).
// pkm_gather_rows is exposed both as a plain function (for the autograd
// wrapper) and could be registered via TORCH_LIBRARY if we wanted
// torch.compile to see it — not needed for the spike.
// --------------------------------------------------------------------------
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.doc() = "PKM forward kernels: F2 row gather + F3 fused outer-sum top-K";
    m.def("pkm_gather_rows",       &pkm_gather_rows,
          py::arg("V"), py::arg("idx"), py::arg("out") = py::none(),
          "Gather rows of V at idx via memcpy; parallel over idx.numel().");
    m.def("pkm_fused_outer_topk",  &pkm_fused_outer_topk,
          py::arg("top_a_s"), py::arg("top_a_i"),
          py::arg("top_b_s"), py::arg("top_b_i"),
          py::arg("sqrt_n"),  py::arg("top_k"),
          "Fused outer-sum + top-K with per-row min-heap; parallel over B*T.");
}
