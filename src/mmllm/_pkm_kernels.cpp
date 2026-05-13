// _pkm_kernels.cpp — PKM forward kernels F2 (row gather), F3 (fused
// outer-sum + top-K), and F-FULL (fused full forward, inference-only)
// for the mmllm CPU path.
//
// Build (in-tree, via setup.py):
//     python setup.py build_ext --inplace
// or lazy load (no setup.py change):
//     torch.utils.cpp_extension.load(..., extra_cflags=["-fopenmp","-O3",...])
//
// All functions:
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
//
// F-FULL (pkm_full_forward) NO-AUTOGRAD CONTRACT:
//   pkm_full_forward fuses score → sub-topk → outer-sum-topk → gather →
//   softmax → weighted-sum into ONE C++ entry point. It is the
//   inference-only fast path. The function does NOT register any autograd
//   nodes. Callers MUST ensure they're under torch.no_grad() / not
//   self.training. Behavior under autograd is undefined (the operation
//   silently produces an output with no grad_fn linking back to inputs).
//   At training time, the slow per-op path in memory.py:forward is the
//   only correct path because it routes sparse gradients to V via
//   PKMGather and dense gradients to K_a/K_b via PKMFusedTopK.

#include <torch/extension.h>
#include <ATen/Parallel.h>
#include <cstring>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <limits>
#include <tuple>

// --------------------------------------------------------------------------
// Internal helpers — refactored bodies of pkm_gather_rows and
// pkm_fused_outer_topk so they can be reused from pkm_full_forward without
// going back through the public ATen-binding overhead. These take fully
// validated, contiguous CPU fp32/int64 inputs and write into pre-allocated
// outputs. The public functions wrap these with validation + alloc.
// --------------------------------------------------------------------------

// Min-heap entry for the fused outer-sum top-K kernel.
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

// _gather_rows_into — F2 body, no allocation, no validation.
// V is (N, D) fp32 contiguous, idx is int64 contiguous with M = idx.numel(),
// out is (M, D) fp32 contiguous (the caller is responsible for the leading
// shape interpretation). Parallel over M.
void _gather_rows_into(
    const float*   V_ptr,
    int64_t        N,
    int64_t        D,
    const int64_t* idx_ptr,
    int64_t        M,
    float*         out_ptr
) {
    if (M == 0) return;
    const size_t row_bytes = static_cast<size_t>(D) * sizeof(float);
    constexpr int64_t GRAIN = 64;
    at::parallel_for(0, M, GRAIN, [&](int64_t begin, int64_t end) {
        for (int64_t i = begin; i < end; ++i) {
            int64_t row = idx_ptr[i];
            TORCH_CHECK(row >= 0 && row < N, "idx out of range: ", row,
                        " not in [0, ", N, ")");
            std::memcpy(out_ptr + i * D,
                        V_ptr   + row * D,
                        row_bytes);
        }
    });
}

// _fused_outer_topk_into — F3 body, no allocation, no validation.
// Inputs: top_a_s/top_a_i/top_b_s/top_b_i all shape (B,T,S) contiguous.
// Outputs: out_scores (B,T,top_k) fp32, out_idx (B,T,top_k) int64 where
//   out_idx[b,t,k] = top_a_i[b,t,ia_local] * sqrt_n + top_b_i[b,t,ib_local]
// Parallel over BT = B*T.
void _fused_outer_topk_into(
    const float*   pas,
    const int64_t* pai,
    const float*   pbs,
    const int64_t* pbi,
    int64_t        B,
    int64_t        T,
    int64_t        S,
    int64_t        sqrt_n,
    int64_t        top_k,
    float*         pos,
    int64_t*       pog
) {
    const int64_t BT = B * T;
    constexpr int64_t GRAIN = 8;
    at::parallel_for(0, BT, GRAIN, [&](int64_t begin, int64_t end) {
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

            int64_t scanned = 0;
            for (int64_t ia = 0; ia < S; ++ia) {
                const float a_s = as[ia];
                const int64_t a_i = ai[ia];
                for (int64_t ib = 0; ib < S; ++ib) {
                    if (scanned++ < top_k) continue;
                    const float cand_score = a_s + bs[ib];
                    HeapEntry& root = heap[0];
                    if (cand_score > root.score) {
                        root.score = cand_score;
                        root.ia    = a_i;
                        root.ib    = bi[ib];
                        sift_down(heap.data(), top_k, 0);
                    }
                }
            }

            float*   out_s = pos + bt * top_k;
            int64_t* out_g = pog + bt * top_k;
            for (int64_t k = 0; k < top_k; ++k) {
                out_s[k] = heap[k].score;
                out_g[k] = heap[k].ia * sqrt_n + heap[k].ib;
            }
        }
    });
}

}  // namespace

// --------------------------------------------------------------------------
// F2 — pkm_gather_rows (public)
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

    if (M == 0) return out;

    _gather_rows_into(
        V.data_ptr<float>(), N, D,
        idx.data_ptr<int64_t>(), M,
        out.data_ptr<float>()
    );
    return out;
}

// --------------------------------------------------------------------------
// F3 — pkm_fused_outer_topk (public)
// --------------------------------------------------------------------------
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
    const int64_t S2 = S * S;
    TORCH_CHECK(top_k <= S2, "top_k must be <= sub_top_k**2");

    at::Tensor top_scores = at::empty({B, T, top_k}, top_a_s.options());
    at::Tensor top_global = at::empty({B, T, top_k}, top_a_i.options());

    _fused_outer_topk_into(
        top_a_s.data_ptr<float>(),
        top_a_i.data_ptr<int64_t>(),
        top_b_s.data_ptr<float>(),
        top_b_i.data_ptr<int64_t>(),
        B, T, S, sqrt_n, top_k,
        top_scores.data_ptr<float>(),
        top_global.data_ptr<int64_t>()
    );

    return std::make_tuple(top_scores, top_global);
}

// --------------------------------------------------------------------------
// F-FULL — pkm_full_forward (public, inference-only, NO AUTOGRAD)
//
// Fuses every step of PKM forward into one C++ entry point:
//   1. q_a, q_b   = q_normed split on sub_dim
//   2. scores_a   = q_a @ K_a.T          (B,T,sqrt_n)
//   3. scores_b   = q_b @ K_b.T          (B,T,sqrt_n)
//   4. top_a_s, top_a_i = scores_a.topk(sub_top_k, -1)
//   5. top_b_s, top_b_i = scores_b.topk(sub_top_k, -1)
//   6. (top_scores, top_global) = _fused_outer_topk_into(...)
//   7. if row_offsets is non-empty: top_global += offsets[b]  (per batch)
//   8. values = V[top_global]            (gather via _gather_rows_into)
//   9. weights = softmax(top_scores, -1)
//  10. out    = (weights[..., None] * values).sum(-2)         (B,T,v_dim)
//
// Inputs:
//   q_normed:    (B, T, q_dim)    fp32 — RMSNormed by caller
//   K_a:         (sqrt_n, sub_dim) fp32 — first half sub-keys
//   K_b:         (sqrt_n, sub_dim) fp32 — second half sub-keys
//   V:           (n_rows, v_dim)   fp32 — value bank (in-RAM or mmap-backed)
//                                  v_dim may differ from q_dim — for
//                                  ProductKeyMemory v_dim == q_dim; for
//                                  NetBank v_dim == c_net (bottleneck)
//                                  and the caller applies the expander
//                                  linear to project back to q_dim.
//   sub_top_k:   int64             — per-sub-key top-K
//   top_k:       int64             — final top-K over the outer sum
//   row_offsets: (B,) int64        — optional multi-trunk offset; pass an
//                                    empty tensor when n_trunks=1
//
// Returns:
//   out:        (B, T, v_dim)        fp32 softmax-weighted sum
//   top_global: (B, T, top_k)        int64 flat indices into V (with
//                                    row_offsets applied) — useful for
//                                    callers that need to track which rows
//                                    were touched (e.g. dirty-page marking).
//                                    Inference callers typically drop this.
//
// NOTE: The function detaches inputs internally via ATen ops that don't
// participate in autograd. We use at::matmul / at::topk / at::softmax —
// none of these record a backward when called with .data() pointers but
// when called on tensors they DO record. To guarantee no autograd
// recording we set ::at::AutoDispatchBelowAutograd inside the function.
// --------------------------------------------------------------------------
std::tuple<at::Tensor, at::Tensor> pkm_full_forward(
    const at::Tensor& q_normed,
    const at::Tensor& K_a,
    const at::Tensor& K_b,
    const at::Tensor& V,
    int64_t           sub_top_k,
    int64_t           top_k,
    const at::Tensor& row_offsets
) {
    // ---- validation ----
    TORCH_CHECK(q_normed.is_cpu() && K_a.is_cpu() && K_b.is_cpu() && V.is_cpu(),
                "all inputs must be CPU");
    TORCH_CHECK(q_normed.dtype() == at::kFloat &&
                K_a.dtype() == at::kFloat &&
                K_b.dtype() == at::kFloat &&
                V.dtype() == at::kFloat,
                "all inputs must be fp32");
    TORCH_CHECK(q_normed.dim() == 3, "q_normed must be 3D (B, T, q_dim)");
    TORCH_CHECK(K_a.dim() == 2 && K_b.dim() == 2,
                "K_a, K_b must be 2D (sqrt_n, sub_dim)");
    TORCH_CHECK(V.dim() == 2, "V must be 2D (n_rows, q_dim)");
    TORCH_CHECK(V.is_contiguous(), "V must be contiguous");
    TORCH_CHECK(K_a.is_contiguous() && K_b.is_contiguous(),
                "K_a, K_b must be contiguous");
    TORCH_CHECK(sub_top_k > 0 && top_k > 0,
                "sub_top_k and top_k must be > 0");

    const int64_t B       = q_normed.size(0);
    const int64_t T       = q_normed.size(1);
    const int64_t q_dim   = q_normed.size(2);
    const int64_t sqrt_n  = K_a.size(0);
    const int64_t sub_dim = K_a.size(1);

    TORCH_CHECK(K_b.size(0) == sqrt_n, "K_a and K_b must have same sqrt_n");
    TORCH_CHECK(K_b.size(1) == sub_dim, "K_a and K_b must have same sub_dim");
    TORCH_CHECK(sub_dim * 2 == q_dim,
                "K_a + K_b sub_dim must equal q_dim / 2");
    // V row width (v_dim) is independent of q_dim — used by NetBank where
    // V stores c_net-dim bottleneck latents that the caller expands back
    // up to q_dim with a learned linear after this kernel returns.
    const int64_t v_dim = V.size(1);
    TORCH_CHECK(v_dim > 0, "V row width must be > 0");
    TORCH_CHECK(sub_top_k <= sqrt_n, "sub_top_k must be <= sqrt_n");
    TORCH_CHECK(top_k <= sub_top_k * sub_top_k,
                "top_k must be <= sub_top_k**2");

    const int64_t n_rows = V.size(0);
    const bool has_offsets = row_offsets.defined() && row_offsets.numel() > 0;
    if (has_offsets) {
        TORCH_CHECK(row_offsets.is_cpu(),                 "row_offsets must be CPU");
        TORCH_CHECK(row_offsets.dtype() == at::kLong,     "row_offsets must be int64");
        TORCH_CHECK(row_offsets.dim() == 1,               "row_offsets must be 1D");
        TORCH_CHECK(row_offsets.size(0) == B,             "row_offsets must be (B,)");
        TORCH_CHECK(row_offsets.is_contiguous(),          "row_offsets must be contiguous");
    }

    // ---- Disable autograd recording for the whole kernel. ----
    // We're inference-only; we don't want any of the ATen ops below to
    // build a backward graph. NoGradGuard sets the global no-grad flag for
    // this thread, which is exactly the user-facing torch.no_grad() ctx.
    at::NoGradGuard no_grad_guard;

    // ---- Score computation (steps 1-3) ----
    // q_a = q_normed[..., :sub_dim], q_b = q_normed[..., sub_dim:]
    // We use at::matmul on q_a/q_b views vs K_a.T; PyTorch handles the
    // 3D-x-2D dispatch internally as a batched 2D matmul.
    //
    // Slicing (narrow on the last dim) produces a non-contiguous view,
    // but matmul on (B,T,sub_dim) @ (sub_dim,sqrt_n) is fine — ATen
    // internally flattens to (B*T, sub_dim) and calls GEMM.
    at::Tensor q_a = q_normed.narrow(2, 0,       sub_dim);
    at::Tensor q_b = q_normed.narrow(2, sub_dim, sub_dim);

    at::Tensor scores_a = at::matmul(q_a, K_a.t());  // (B,T,sqrt_n)
    at::Tensor scores_b = at::matmul(q_b, K_b.t());  // (B,T,sqrt_n)

    // ---- Sub-key top-K (steps 4-5) ----
    // at::topk returns (values, indices) with the default sorted=true,
    // dim=-1, largest=true.
    auto topk_a = at::topk(scores_a, sub_top_k, /*dim=*/-1,
                           /*largest=*/true, /*sorted=*/true);
    auto topk_b = at::topk(scores_b, sub_top_k, /*dim=*/-1,
                           /*largest=*/true, /*sorted=*/true);
    at::Tensor top_a_s = std::get<0>(topk_a).contiguous();
    at::Tensor top_a_i = std::get<1>(topk_a).contiguous();
    at::Tensor top_b_s = std::get<0>(topk_b).contiguous();
    at::Tensor top_b_i = std::get<1>(topk_b).contiguous();

    // ---- Fused outer-sum + top-K (step 6) ----
    at::Tensor top_scores = at::empty({B, T, top_k}, q_normed.options());
    at::Tensor top_global = at::empty({B, T, top_k}, top_a_i.options());

    _fused_outer_topk_into(
        top_a_s.data_ptr<float>(),
        top_a_i.data_ptr<int64_t>(),
        top_b_s.data_ptr<float>(),
        top_b_i.data_ptr<int64_t>(),
        B, T, sub_top_k, sqrt_n, top_k,
        top_scores.data_ptr<float>(),
        top_global.data_ptr<int64_t>()
    );

    // ---- Multi-trunk row offsets (step 7) ----
    // top_global[b, t, k] += row_offsets[b]   for each b
    //
    // Loop manually rather than allocating a (B,1,1) broadcast tensor —
    // saves an alloc and we already have raw pointer access.
    if (has_offsets) {
        const int64_t* off_ptr = row_offsets.data_ptr<int64_t>();
        int64_t* tg_ptr = top_global.data_ptr<int64_t>();
        const int64_t per_b = T * top_k;
        at::parallel_for(0, B, 1, [&](int64_t begin, int64_t end) {
            for (int64_t b = begin; b < end; ++b) {
                const int64_t off = off_ptr[b];
                int64_t* row = tg_ptr + b * per_b;
                for (int64_t i = 0; i < per_b; ++i) {
                    row[i] += off;
                }
            }
        });
    }

    // ---- Gather rows of V (step 8) ----
    // values has shape (B, T, top_k, v_dim) — but we treat the gather as
    // operating on a flat (B*T*top_k,) idx and emitting (B*T*top_k, v_dim)
    // and reshape on the way out. The fused softmax+sum step below needs
    // the v_dim trailing axis to be contiguous.
    at::Tensor values = at::empty({B, T, top_k, v_dim}, V.options());
    _gather_rows_into(
        V.data_ptr<float>(), n_rows, v_dim,
        top_global.data_ptr<int64_t>(), B * T * top_k,
        values.data_ptr<float>()
    );

    // ---- Softmax over top_k (step 9) ----
    // top_scores: (B, T, top_k) → weights: (B, T, top_k)
    // We use the ATen op (it's GIL-free + uses internal vectorized impl).
    at::Tensor weights = at::softmax(top_scores, /*dim=*/-1);

    // ---- Weighted sum reduce (step 10) ----
    // out[b,t,d] = sum_k weights[b,t,k] * values[b,t,k,d]
    //
    // Hand-roll the reduce: a single fused loop over (B*T) outer rows,
    // each touching top_k * v_dim contiguous floats. With v_dim=16,
    // top_k=16 (local) or v_dim=8, top_k=64 (net), this is 256-512 floats
    // per row, well inside L1.
    at::Tensor out = at::empty({B, T, v_dim}, q_normed.options());

    const int64_t BT = B * T;
    const float* w_ptr = weights.data_ptr<float>();
    const float* v_ptr = values.data_ptr<float>();
    float* out_ptr = out.data_ptr<float>();

    constexpr int64_t GRAIN = 16;
    at::parallel_for(0, BT, GRAIN, [&](int64_t begin, int64_t end) {
        // Per-thread accumulator: v_dim floats.
        std::vector<float> acc(static_cast<size_t>(v_dim));

        for (int64_t bt = begin; bt < end; ++bt) {
            const float* wp = w_ptr + bt * top_k;
            const float* vp = v_ptr + bt * top_k * v_dim;
            float* op = out_ptr + bt * v_dim;

            // Zero accumulator
            std::memset(acc.data(), 0, v_dim * sizeof(float));

            for (int64_t k = 0; k < top_k; ++k) {
                const float w = wp[k];
                const float* row = vp + k * v_dim;
                // Vectorizable inner loop. -O3 -march=native should auto-
                // vectorize this; v_dim=16 fits nicely in 2x AVX2 lanes
                // or 1x AVX-512 lane.
                for (int64_t d = 0; d < v_dim; ++d) {
                    acc[d] += w * row[d];
                }
            }

            std::memcpy(op, acc.data(), v_dim * sizeof(float));
        }
    });

    return std::make_tuple(out, top_global);
}

// --------------------------------------------------------------------------
// Registration. We use pybind11 (TORCH_EXTENSION_NAME comes from setup.py).
// --------------------------------------------------------------------------
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.doc() = "PKM forward kernels: F2 row gather + F3 fused outer-sum top-K + F-FULL one-shot forward";
    m.def("pkm_gather_rows",       &pkm_gather_rows,
          py::arg("V"), py::arg("idx"), py::arg("out") = py::none(),
          "Gather rows of V at idx via memcpy; parallel over idx.numel().");
    m.def("pkm_fused_outer_topk",  &pkm_fused_outer_topk,
          py::arg("top_a_s"), py::arg("top_a_i"),
          py::arg("top_b_s"), py::arg("top_b_i"),
          py::arg("sqrt_n"),  py::arg("top_k"),
          "Fused outer-sum + top-K with per-row min-heap; parallel over B*T.");
    m.def("pkm_full_forward",      &pkm_full_forward,
          py::arg("q_normed"), py::arg("K_a"), py::arg("K_b"), py::arg("V"),
          py::arg("sub_top_k"), py::arg("top_k"),
          py::arg("row_offsets"),
          "INFERENCE-ONLY one-shot PKM forward (no autograd). Fuses "
          "score→sub-topk→outer-sum-topk→gather→softmax→weighted-sum into a "
          "single C++ call. Pass row_offsets as an empty int64 tensor when "
          "n_trunks=1.");
}
