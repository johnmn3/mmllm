(ns mmllm.jvm.grad
  "Hand-derived backward passes for the sym24 modules (M4 of
   docs/jvm-port-spec.md, §7) + CE-from-logits. No tape: each bwd fn
   recomputes the cheap forward intermediates it needs from the saved
   inputs. Verified two ways in mmllm.jvm.grad-parity — torch autograd
   goldens (grads_*.npz) and JVM-side central finite differences.

   Layout conventions match model.clj: row-major float[] with explicit
   dims; module goldens' loss is (out · r) so dL/dout = r."
  (:require [mmllm.jvm.model :as m]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]))

(set! *warn-on-reflection* true)

(defn dot-at
  "Σ a[ao+i]·b[bo+i], double accumulation. (>4 args — no primitive hints;
   cast inside, per the repo's Clojure gotcha note.)"
  [^floats a ao ^floats b bo n]
  (let [ao (long ao) bo (long bo) n (long n)]
    (loop [i 0 acc 0.0]
      (if (< i n)
        (recur (inc i) (+ acc (* (double (aget a (+ ao i)))
                                 (double (aget b (+ bo i))))))
        acc))))

(defn loss-dot
  "Σ a·b — the (out * r).sum() loss every module golden uses."
  ^double [^floats a ^floats b]
  (double (dot-at a 0 b 0 (alength a))))

;; ── RMSNorm ──

(defn rmsnorm-bwd
  "y = w ⊙ x/rms, rms = sqrt(mean(x²)+eps).
   dx = (w⊙dy)/rms − x · mean(dy⊙w⊙x)/rms³ ; dw = Σ_rows dy ⊙ x/rms.
   x,dy (rows,d); w (d) -> {:dx (rows,d) :dw (d)}."
  [^floats x ^floats w ^floats dy rows d eps]
  (let [rows (long rows) d (long d) eps (double eps)
        dx (float-array (* rows d))
        dw (float-array d)]
    (dotimes [r rows]
      (let [off (* r d)
            ss (loop [i 0 s 0.0]
                 (if (< i d)
                   (let [v (double (aget x (+ off i)))] (recur (inc i) (+ s (* v v))))
                   s))
            inv (/ 1.0 (Math/sqrt (+ (/ ss d) eps)))
            s1 (loop [i 0 s 0.0]                     ; Σ dy_i w_i x_i
                 (if (< i d)
                   (recur (inc i) (+ s (* (double (aget dy (+ off i)))
                                          (double (aget w i))
                                          (double (aget x (+ off i))))))
                   s))
            c (/ (* s1 inv inv inv) d)]
        (dotimes [i d]
          (aset dx (+ off i)
                (float (- (* inv (aget w i) (aget dy (+ off i)))
                          (* (aget x (+ off i)) c))))
          (aset dw i (float (+ (aget dw i)
                               (* (aget dy (+ off i)) (aget x (+ off i)) inv)))))))
    {:dx dx :dw dw}))

;; ── Linear (torch F.linear, y = x·Wᵀ, no bias anywhere in sym24) ──

(defn linear-bwd
  "x (rows,in), W (out,in), dy (rows,out) -> {:dx = dy·W :dW += dyᵀ·x}."
  [^floats x ^floats W ^floats dy rows in out]
  (let [rows (long rows) in (long in) out (long out)
        dx (float-array (* rows in))
        dW (float-array (* out in))]
    (dotimes [r rows]
      (let [xoff (* r in) yoff (* r out)]
        (dotimes [o out]
          (let [dyv (aget dy (+ yoff o)) woff (* o in)]
            (when-not (zero? dyv)
              (dotimes [i in]
                (aset dx (+ xoff i)
                      (float (+ (aget dx (+ xoff i)) (* dyv (aget W (+ woff i))))))
                (aset dW (+ woff i)
                      (float (+ (aget dW (+ woff i)) (* dyv (aget x (+ xoff i))))))))))))
    {:dx dx :dW dW}))

;; ── SiLU / SwiGLU ──

(defn silu-bwd
  "y = x·σ(x): dx = dy · σ(x)·(1 + x·(1−σ(x)))."
  ^floats [^floats x ^floats dy]
  (let [n (alength x) dx (float-array n)]
    (dotimes [i n]
      (let [v (double (aget x i))
            s (/ 1.0 (+ 1.0 (Math/exp (- v))))]
        (aset dx i (float (* (aget dy i) s (+ 1.0 (* v (- 1.0 s))))))))
    dx))

(defn swiglu-fwd
  "y = (silu(x·Wgᵀ) ⊙ (x·Wuᵀ))·Wdᵀ. Returns intermediates for the bwd."
  [^floats x ^floats Wg ^floats Wu ^floats Wd rows d dff]
  (let [rows (long rows) d (long d) dff (long dff)
        g (t/data (t/linear (t/tensor [rows d] x) (t/tensor [dff d] Wg)))
        u (t/data (t/linear (t/tensor [rows d] x) (t/tensor [dff d] Wu)))
        s (t/data (t/silu! (t/copy (t/tensor [rows dff] g))))
        h (float-array (* rows dff))]
    (dotimes [i (* rows dff)]
      (aset h i (float (* (aget ^floats s i) (aget ^floats u i)))))
    {:y (t/data (t/linear (t/tensor [rows dff] h) (t/tensor [d dff] Wd)))
     :g g :u u :s s :h h}))

(defn swiglu-bwd
  [^floats x ^floats Wg ^floats Wu ^floats Wd ^floats dy rows d dff]
  (let [rows (long rows) d (long d) dff (long dff)
        {:keys [^floats g ^floats u ^floats s ^floats h]}
        (swiglu-fwd x Wg Wu Wd rows d dff)
        {^floats dh :dx dWd :dW} (linear-bwd h Wd dy rows dff d)
        n (* rows dff)
        ds (float-array n)
        du (float-array n)]
    (dotimes [i n]
      (aset ds i (float (* (aget dh i) (aget u i))))
      (aset du i (float (* (aget dh i) (aget s i)))))
    (let [dg (silu-bwd g ds)
          {^floats dx1 :dx dWu :dW} (linear-bwd x Wu du rows d dff)
          {^floats dx2 :dx dWg :dW} (linear-bwd x Wg dg rows d dff)
          dx (float-array (* rows d))]
      (dotimes [i (* rows d)]
        (aset dx i (float (+ (aget dx1 i) (aget dx2 i)))))
      {:dx dx :dWg dWg :dWu dWu :dWd dWd})))

;; ── causal SDPA (recompute-backward, per §9 no (T,T) is kept) ──

(defn sdpa-causal-bwd
  "Single head, q/k/v/dout (T,d) contiguous. Recomputes each softmax row.
   ds = softmax-bwd; dq += scale·Σ ds_j k_j; dk_j += scale·ds_j q;
   dv_j += p_j·dout."
  [^floats q ^floats k ^floats v ^floats dout T d]
  (let [T (long T) d (long d)
        scale (/ 1.0 (Math/sqrt (double d)))
        dq (float-array (* T d)) dk (float-array (* T d)) dv (float-array (* T d))
        pr (float-array T) dp (float-array T)]
    (dotimes [i T]
      (let [n (inc i) qoff (* i d) ooff (* i d)]
        (dotimes [j n] (aset pr j (float (* scale (dot-at q qoff k (* j d) d)))))
        (let [mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
                   (if (< j n) (recur (inc j) (max mv (double (aget pr j)))) mv))
              sum (loop [j 0 s 0.0]
                    (if (< j n)
                      (let [e (Math/exp (- (aget pr j) mx))]
                        (aset pr j (float e)) (recur (inc j) (+ s e)))
                      s))]
          (dotimes [j n] (aset pr j (float (/ (aget pr j) sum)))))
        (dotimes [j n]
          (aset dp j (float (dot-at dout ooff v (* j d) d)))
          (let [pj (aget pr j) voff (* j d)]
            (dotimes [c d]
              (aset dv (+ voff c)
                    (float (+ (aget dv (+ voff c)) (* pj (aget dout (+ ooff c)))))))))
        (let [sd (loop [j 0 s 0.0]
                   (if (< j n)
                     (recur (inc j) (+ s (* (double (aget pr j)) (double (aget dp j)))))
                     s))]
          (dotimes [j n]
            (let [ds (* (aget pr j) (- (aget dp j) sd)) koff (* j d)]
              (dotimes [c d]
                (aset dq (+ qoff c)
                      (float (+ (aget dq (+ qoff c)) (* scale ds (aget k (+ koff c))))))
                (aset dk (+ koff c)
                      (float (+ (aget dk (+ koff c)) (* scale ds (aget q (+ qoff c))))))))))))
    {:dq dq :dk dk :dv dv}))

;; ── RoPE (linear: bwd = fwd with negated sin) ──

(defn rope-bwd-at!
  "In-place RoPE transpose on an 8-float head vector at x[off..off+hd):
   dx = dy·cos + rotate_half(dy)·(−sin) — i.e. m/rope-at! with sin negated."
  [^floats x off {:keys [^floats cos ^floats sin]} pos head-dim]
  (let [off (long off) pos (long pos) head-dim (long head-dim)
        half (quot head-dim 2)
        roff (* pos head-dim)
        tmp (float-array head-dim)]
    (System/arraycopy x off tmp 0 head-dim)
    (dotimes [j half]
      (aset x (+ off j)
            (float (+ (* (aget tmp j) (aget cos (+ roff j)))
                      (* (aget tmp (+ half j)) (aget sin (+ roff j))))))
      (aset x (+ off half j)
            (float (- (* (aget tmp (+ half j)) (aget cos (+ roff half j)))
                      (* (aget tmp j) (aget sin (+ roff half j)))))))))

;; ── product-key retrieval backward (shared: Local PKM + NetBank) ──

;; dV maps are hinted java.util.Map (not HashMap): the sequential step
;; passes HashMaps; the M6 parallel step (parallel_step.clj) passes a
;; shared ConcurrentHashMap for V_local, whose row keys are disjoint
;; across router threads (per-trunk slices), so lock-free get/put is safe.
(defn- dv-acc ^floats [^java.util.Map dV ^long row ^long dim]
  (or (.get dV row)
      (let [a (float-array dim)] (.put dV row a) a)))

(defn pk-bwd-token!
  "Backward through pk-retrieve + softmax-weighted V-row sum for ONE token.
   qn is the q_norm'd query (row at qn-off, 16 wide); dval (vdim) is the
   grad wrt the weighted V sum. Scatters dscores to the selected sub-key
   indices only (top-k choice itself is piecewise-constant — no grad).
   Accumulates dKa/dKb (dense), dV (HashMap global-row → float[vdim]) and
   the query grad into dqn at qn-off."
  [^floats qn qn-off mem trunk-off ^floats dval vdim
   ^floats dKa ^floats dKb ^java.util.Map dV ^floats dqn]
  (let [qn-off (long qn-off) trunk-off (long trunk-off) vdim (long vdim)
        {:keys [^floats Ka ^floats Kb bank]} mem
        sqrt-n (long (:sqrt-n mem)) sub-dim (long (:sub-dim mem))
        top-k (long (:top-k mem))
        {:keys [^longs idx ^floats w]} (m/pk-retrieve qn qn-off mem)
        row (float-array vdim)
        dw (float-array top-k)]
    ;; dV[row] += w_k·dval ; dw_k = dval·V_row
    (dotimes [k top-k]
      (let [grow (+ trunk-off (aget idx k))]
        (p/bank-row! bank grow row 0)
        (aset dw k (float (dot-at dval 0 row 0 vdim)))
        ;; ^floats at the call site: dv-acc's primitive-long args drop the
        ;; return tag (the repo's >4-args/primitive-hint gotcha), and this
        ;; aset loop is the hottest scatter in the backward.
        (let [^floats acc (dv-acc dV grow vdim)]
          (dotimes [c vdim]
            (aset acc c (float (+ (aget acc c) (* (aget w k) (aget dval c)))))))))
    ;; softmax bwd over the selected scores, scatter into ds_a / ds_b
    (let [sd (loop [k 0 s 0.0]
               (if (< k top-k)
                 (recur (inc k) (+ s (* (double (aget w k)) (double (aget dw k)))))
                 s))
          dsa (float-array sqrt-n) dsb (float-array sqrt-n)
          ta (java.util.HashSet.) tb (java.util.HashSet.)]
      (dotimes [k top-k]
        (let [ds (* (aget w k) (- (aget dw k) sd))
              ia (quot (aget idx k) sqrt-n)
              ib (rem (aget idx k) sqrt-n)]
          (aset dsa (int ia) (float (+ (aget dsa (int ia)) ds)))
          (aset dsb (int ib) (float (+ (aget dsb (int ib)) ds)))
          (.add ta ia) (.add tb ib)))
      ;; dK_a[r] += ds_a[r]·q_a ; dq_a += ds_a[r]·K_a[r]  (idem b-half)
      (doseq [r ta]
        (let [r (long r) ds (double (aget dsa (int r))) koff (* r sub-dim)]
          (dotimes [c sub-dim]
            (aset dKa (+ koff c)
                  (float (+ (aget dKa (+ koff c)) (* ds (aget qn (+ qn-off c))))))
            (aset dqn (+ qn-off c)
                  (float (+ (aget dqn (+ qn-off c)) (* ds (aget Ka (+ koff c)))))))))
      (doseq [r tb]
        (let [r (long r) ds (double (aget dsb (int r))) koff (* r sub-dim)]
          (dotimes [c sub-dim]
            (aset dKb (+ koff c)
                  (float (+ (aget dKb (+ koff c)) (* ds (aget qn (+ qn-off sub-dim c))))))
            (aset dqn (+ qn-off sub-dim c)
                  (float (+ (aget dqn (+ qn-off sub-dim c)) (* ds (aget Kb (+ koff c))))))))))
    nil))

(defn pkm-bwd
  "Local PKM backward for one batch row: q (T,16), dout (T,16).
   Pass `acc` ({:dKa :dKb :dqnorm-w :dV}) to accumulate param grads across
   batch rows (torch sums them). Returns
   {:dq :dKa :dKb :dqnorm-w :dV HashMap<long,float[16]>}."
  ([^floats q T mem trunk-id ^floats dout]
   (pkm-bwd q T mem trunk-id dout nil))
  ([^floats q T mem trunk-id ^floats dout acc]
   (let [T (long T) trunk-id (long trunk-id)
         {:keys [^floats qnorm-w]} mem
         q-dim (long (:q-dim mem)) n-per-trunk (long (:n-per-trunk mem))
         sqrt-n (long (:sqrt-n mem)) sub-dim (long (:sub-dim mem))
         ^floats dKa (or (:dKa acc) (float-array (* sqrt-n sub-dim)))
         ^floats dKb (or (:dKb acc) (float-array (* sqrt-n sub-dim)))
         ^java.util.Map dV (or (:dV acc) (java.util.HashMap.))
         ^floats dqnw (or (:dqnorm-w acc) (float-array q-dim))
         qn (java.util.Arrays/copyOf q (alength q))
         dqn (float-array (* T q-dim))
         off (* trunk-id n-per-trunk)]
     (dotimes [ti T] (m/rms-row! qn (* ti q-dim) qnorm-w q-dim))
     (dotimes [ti T]
       (pk-bwd-token! qn (* ti q-dim) mem off
                      (java.util.Arrays/copyOfRange dout (* ti q-dim) (* (inc ti) q-dim))
                      q-dim dKa dKb dV dqn))
     (let [{:keys [dx ^floats dw]} (rmsnorm-bwd q qnorm-w dqn T q-dim m/eps)]
       (dotimes [i q-dim] (aset dqnw i (float (+ (aget dqnw i) (aget dw i)))))
       {:dq dx :dKa dKa :dKb dKb :dqnorm-w dqnw :dV dV}))))

(defn netbank-bwd
  "NetBank backward: q (T,16), dout (T,16). Adds the expander backward
   (out = expander(Σ w_k·latent_k), latents fp32 c_net-dim) before the
   shared pk scatter. Returns {:dq :dKa :dKb :dqnorm-w :dexp :dV}."
  [^floats q T nb ^floats dout]
  (let [T (long T)
        {:keys [^floats qnorm-w ^floats expander-w bank]} nb
        q-dim (long (:q-dim nb)) c-net (long (:c-net nb))
        sqrt-n (long (:sqrt-n nb)) sub-dim (long (:sub-dim nb))
        top-k (long (:top-k nb))
        dKa (float-array (* sqrt-n sub-dim))
        dKb (float-array (* sqrt-n sub-dim))
        dV (java.util.HashMap.)
        dexp (float-array (* q-dim c-net))
        qn (java.util.Arrays/copyOf q (alength q))
        dqn (float-array (* T q-dim))
        lat (float-array c-net)
        row (float-array c-net)
        dlat (float-array c-net)]
    (dotimes [ti T] (m/rms-row! qn (* ti q-dim) qnorm-w q-dim))
    (dotimes [ti T]
      ;; recompute the weighted latent (needed for d_expander)
      (java.util.Arrays/fill lat (float 0.0))
      (let [{:keys [^longs idx ^floats w]} (m/pk-retrieve qn (* ti q-dim) nb)]
        (dotimes [k top-k]
          (p/bank-row! bank (aget idx k) row 0)
          (dotimes [c c-net]
            (aset lat c (float (+ (aget lat c) (* (aget w k) (aget row c))))))))
      ;; expander bwd: dexp[o,c] += dout_o·lat_c ; dlat_c = Σ_o dout_o·W[o,c]
      (let [doff (* ti q-dim)]
        (dotimes [c c-net]
          (loop [o 0 acc 0.0]
            (if (< o q-dim)
              (do (aset dexp (+ (* o c-net) c)
                        (float (+ (aget dexp (+ (* o c-net) c))
                                  (* (aget dout (+ doff o)) (aget lat c)))))
                  (recur (inc o) (+ acc (* (double (aget dout (+ doff o)))
                                           (double (aget expander-w (+ (* o c-net) c)))))))
              (aset dlat c (float acc)))))
        (pk-bwd-token! qn (* ti q-dim) nb 0 dlat c-net dKa dKb dV dqn)))
    (let [{:keys [dx dw]} (rmsnorm-bwd q qnorm-w dqn T q-dim m/eps)]
      {:dq dx :dKa dKa :dKb dKb :dqnorm-w dw :dexp dexp :dV dV})))

;; ── SwitchGate 3-way + alpha_net + net-default, TRAIN branch ──

(defn gate-train-bwd
  "gating.py:239+ (net-default Bernoulli path), head-major (H,T,8) flat
   arrays; R (H,T) replayed uniform draws (the torch.rand_like dump).

   mode :st     — forward value uses the hard decision (p > R); backward
                  routes the decision grad through the smooth σ (that IS
                  the straight-through trick). Torch-golden parity.
   mode :smooth — decision = p in value AND grad (the differentiable eval
                  branch); what the finite-difference check runs against,
                  since the ST estimator is deliberately ≠ the true
                  (a.e. zero) derivative of the hard draw.

   Renormalization (w_sdpa + w_local·dec + w_net + 1e-6) is a quotient
   rule over the stabilized sum. dout nil → forward only.
   Returns {:y :dq :dsdpa :dmem :dnet :dg3 :dalpha :dlap :dlab}."
  [{:keys [^floats gate-proj-3 ^floats alpha-net ^floats lap ^floats lab]}
   ^floats q ^floats sdpa ^floats mem ^floats net ^floats R
   H T mode ^floats dout]
  (let [H (long H) T (long T) hd 8
        n (* H T hd)
        y (float-array n)
        dq (float-array n) dsdpa (float-array n)
        dmem (float-array n) dnet (float-array n)
        dg3 (float-array (* H 3 hd)) dalpha (float-array H)
        dlap (float-array (* H hd)) dlab (float-array H)]
    (dotimes [h H]
      (let [alpha (double (aget alpha-net h))
            g3off (* h 3 hd)]
        (dotimes [ti T]
          (let [off (+ (* h T hd) (* ti hd))
                l0 (dot-at q off gate-proj-3 g3off hd)
                l1 (dot-at q off gate-proj-3 (+ g3off hd) hd)
                l2 (dot-at q off gate-proj-3 (+ g3off (* 2 hd)) hd)
                mx (max l0 (max l1 l2))
                e0 (Math/exp (- l0 mx)) e1 (Math/exp (- l1 mx)) e2 (Math/exp (- l2 mx))
                z (+ e0 e1 e2)
                w0 (/ e0 z) w1 (/ e1 z) w2 (/ e2 z)
                ll (+ (dot-at q off lap (* h hd) hd) (double (aget lab h)))
                pp (/ 1.0 (+ 1.0 (Math/exp (- ll))))
                dec (if (= mode :st)
                      (if (> pp (double (aget R (+ (* h T) ti)))) 1.0 0.0)
                      pp)
                b (* w1 dec)
                tot (+ w0 b w2 1e-6)]
            (dotimes [c hd]
              (aset y (+ off c)
                    (float (/ (+ (* w0 (aget sdpa (+ off c)))
                                 (* b (aget mem (+ off c)))
                                 (* w2 alpha (aget net (+ off c))))
                              tot))))
            (when dout
              (let [gS (dot-at dout off sdpa off hd)
                    gM (dot-at dout off mem off hd)
                    gN (dot-at dout off net off hd)
                    gO (dot-at dout off y off hd)   ; dout·out (already /tot)
                    dw0 (/ (- gS gO) tot)
                    db (/ (- gM gO) tot)
                    dw2 (/ (- (* alpha gN) gO) tot)]
                (dotimes [c hd]
                  (aset dsdpa (+ off c) (float (* (/ w0 tot) (aget dout (+ off c)))))
                  (aset dmem (+ off c) (float (* (/ b tot) (aget dout (+ off c)))))
                  (aset dnet (+ off c) (float (* (/ w2 tot) alpha (aget dout (+ off c))))))
                (aset dalpha h (float (+ (aget dalpha h) (* (/ w2 tot) gN))))
                ;; decision: dw1 uses the forward VALUE of dec; dp is the
                ;; ST/smooth grad — identical formula either way.
                (let [dw1 (* db dec)
                      dp (* db w1)
                      dll (* dp pp (- 1.0 pp))]
                  (aset dlab h (float (+ (aget dlab h) dll)))
                  (dotimes [c hd]
                    (aset dlap (+ (* h hd) c)
                          (float (+ (aget dlap (+ (* h hd) c)) (* dll (aget q (+ off c))))))
                    (aset dq (+ off c)
                          (float (+ (aget dq (+ off c)) (* dll (aget lap (+ (* h hd) c)))))))
                  ;; softmax bwd on the 3 gate logits
                  (let [sd (+ (* w0 dw0) (* w1 dw1) (* w2 dw2))
                        dl0 (* w0 (- dw0 sd)) dl1 (* w1 (- dw1 sd)) dl2 (* w2 (- dw2 sd))]
                    (dotimes [c hd]
                      (let [qc (double (aget q (+ off c)))]
                        (aset dg3 (+ g3off c)
                              (float (+ (aget dg3 (+ g3off c)) (* dl0 qc))))
                        (aset dg3 (+ g3off hd c)
                              (float (+ (aget dg3 (+ g3off hd c)) (* dl1 qc))))
                        (aset dg3 (+ g3off (* 2 hd) c)
                              (float (+ (aget dg3 (+ g3off (* 2 hd) c)) (* dl2 qc))))
                        (aset dq (+ off c)
                              (float (+ (aget dq (+ off c))
                                        (* dl0 (aget gate-proj-3 (+ g3off c)))
                                        (* dl1 (aget gate-proj-3 (+ g3off hd c)))
                                        (* dl2 (aget gate-proj-3 (+ g3off (* 2 hd) c))))))))))))))))
    {:y y :dq dq :dsdpa dsdpa :dmem dmem :dnet dnet
     :dg3 dg3 :dalpha dalpha :dlap dlap :dlab dlab}))

;; ── tied head / embedding ──

(defn tied-head-bwd
  "logits = gather(emb, tokens)·embᵀ (weight-tied head). demb accumulates
   from BOTH the output matmul and the input gather. tokens: seq of longs.
   Returns {:logits (T,V) :demb (V,d)}."
  [^floats emb tokens ^floats dlogits T d V]
  (let [T (long T) d (long d) V (long V)
        x (float-array (* T d))]
    (dotimes [ti T]
      (System/arraycopy emb (* (long (nth tokens ti)) d) x (* ti d) d))
    (let [logits (t/data (t/linear (t/tensor [T d] x) (t/tensor [V d] emb)))
          demb (float-array (* V d))
          dx (float-array (* T d))]
      ;; output matmul: dx = dlogits·emb ; demb += dlogitsᵀ·x
      (dotimes [ti T]
        (dotimes [v V]
          (let [dl (aget dlogits (+ (* ti V) v))]
            (when-not (zero? dl)
              (let [voff (* v d) xoff (* ti d)]
                (dotimes [c d]
                  (aset dx (+ xoff c)
                        (float (+ (aget dx (+ xoff c)) (* dl (aget emb (+ voff c))))))
                  (aset demb (+ voff c)
                        (float (+ (aget demb (+ voff c)) (* dl (aget x (+ xoff c))))))))))))
      ;; input gather: scatter dx back onto the gathered rows
      (dotimes [ti T]
        (let [voff (* (long (nth tokens ti)) d) xoff (* ti d)]
          (dotimes [c d]
            (aset demb (+ voff c)
                  (float (+ (aget demb (+ voff c)) (aget dx (+ xoff c))))))))
      {:logits logits :demb demb})))

;; ── CE from logits ──

(defn ce-from-logits
  "Positions 0..T-2 predict tokens[t+1]; mean reduction — matches
   F.cross_entropy(logits[:, :-1].reshape(-1,V), tokens[:, 1:]).
   dlogits[t] = (softmax(logits[t]) − onehot(y_t)) / (T−1), zero at T−1.
   Double-precision softmax/logsumexp. -> {:loss :dlogits (T,V)}."
  [^floats logits tokens ^long T ^long V]
  (let [n (dec T)
        dl (float-array (* T V))
        pr (double-array V)]
    (loop [ti 0 acc 0.0]
      (if (< ti n)
        (let [off (* ti V)
              tgt (long (nth tokens (inc ti)))
              mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
                   (if (< j V) (recur (inc j) (max mv (double (aget logits (+ off j))))) mv))
              sum (loop [j 0 s 0.0]
                    (if (< j V)
                      (do (aset pr j (Math/exp (- (aget logits (+ off j)) mx)))
                          (recur (inc j) (+ s (aget pr j))))
                      s))]
          (dotimes [j V]
            (aset dl (+ off j)
                  (float (/ (- (/ (aget pr j) sum) (if (= j tgt) 1.0 0.0)) n))))
          (recur (inc ti)
                 (+ acc (- (+ mx (Math/log sum)) (aget logits (+ off tgt))))))
        {:loss (/ acc n) :dlogits dl}))))
