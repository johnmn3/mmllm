(ns mmllm.jvm.model
  "sym24 cpu-mini forward (eval mode, prefill, B=1) — hand-rolled port of
   attention_kernel.py block_forward + memory.py / netbank.py / gating.py.
   Python-path PKM semantics (goldens pin those; C++ kernel ties differ).

   Shapes: x is (T, 32) row-major float[]. Heads: 4 × head-dim 8; heads 0-1
   short, 2-3 long; per-tier 1 KV head GQA-expanded ×2. bank_q = the two
   long heads' q, which is the CONTIGUOUS tail 16 floats of each q row."
  (:require [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]))

(set! *warn-on-reflection* true)

(def ^:const eps
  "torch nn.RMSNorm(eps=None) resolves to finfo(float32).eps."
  1.1920928955078125E-7)

;; ── RoPE ──

(defn build-rope
  "-> {:cos ^floats :sin ^floats} of (max-pos, head-dim), matching
   core.lpy build-rope-cache (half-freqs duplicated across the two halves)."
  [^long max-pos ^long head-dim ^double theta]
  (let [half (quot head-dim 2)
        cos (float-array (* max-pos head-dim))
        sin (float-array (* max-pos head-dim))]
    (dotimes [pos max-pos]
      (dotimes [j half]
        ;; torch builds this cache in float32 end-to-end (core.lpy
        ;; build-rope-cache); round each intermediate to float or the
        ;; cache drifts ~4e-5 at large positions vs the reference.
        (let [inv (float (Math/exp (- (* (/ (double (* 2 j)) head-dim) (Math/log theta)))))
              f (float (* pos (double inv)))
              c (float (Math/cos f)) s (float (Math/sin f))
              off (* pos head-dim)]
          (aset cos (+ off j) c) (aset cos (+ off half j) c)
          (aset sin (+ off j) s) (aset sin (+ off half j) s))))
    {:cos cos :sin sin}))

(defn rope-at!
  "Apply RoPE in place to an 8-float head vector at x[off..off+8) for
   position pos. y = x·cos + rotate_half(x)·sin, rotate_half = [-x2, x1]."
  [^floats x off {:keys [^floats cos ^floats sin]} pos head-dim]
  (let [off (long off) pos (long pos) head-dim (long head-dim)
        half (quot head-dim 2)
        roff (* pos head-dim)
        tmp (float-array head-dim)]
    (System/arraycopy x off tmp 0 head-dim)
    (dotimes [j half]
      (aset x (+ off j)
            (float (+ (* (aget tmp j) (aget cos (+ roff j)))
                      (* (- (aget tmp (+ half j))) (aget sin (+ roff j))))))
      (aset x (+ off half j)
            (float (+ (* (aget tmp (+ half j)) (aget cos (+ roff half j)))
                      (* (aget tmp j) (aget sin (+ roff half j)))))))))

;; ── causal SDPA (prefill, one query head vs one kv head) ──

(defn sdpa-causal
  "q (T,d) strided in Q at q-off/q-stride; k,v (T,d) contiguous float[][].
   Writes out (T,d) into OUT at out-off/out-stride. Math backend semantics."
  [^floats Q q-off q-stride
   ^floats K ^floats V T d
   ^floats OUT out-off out-stride]
  (let [q-off (long q-off) q-stride (long q-stride) T (long T) d (long d)
        out-off (long out-off) out-stride (long out-stride)
        scale (/ 1.0 (Math/sqrt (double d)))
        scores (float-array T)]
    (dotimes [i T]
      (let [qoff (+ q-off (* i q-stride))
            n (inc i)]
        (dotimes [j n]
          (let [koff (* j d)]
            (loop [c 0 acc 0.0]
              (if (< c d)
                (recur (inc c) (+ acc (* (double (aget Q (+ qoff c)))
                                         (double (aget K (+ koff c))))))
                (aset scores j (float (* acc scale)))))))
        ;; softmax over scores[0..n)
        (let [mx (loop [j 0 m Float/NEGATIVE_INFINITY]
                   (if (< j n) (recur (inc j) (max m (aget scores j))) m))
              sum (loop [j 0 s 0.0]
                    (if (< j n)
                      (let [e (Math/exp (- (aget scores j) (double mx)))]
                        (aset scores j (float e))
                        (recur (inc j) (+ s e)))
                      s))
              ooff (+ out-off (* i out-stride))]
          (dotimes [c d] (aset OUT (+ ooff c) (float 0.0)))
          (dotimes [j n]
            (let [w (/ (aget scores j) sum)
                  voff (* j d)]
              (dotimes [c d]
                (aset OUT (+ ooff c)
                      (float (+ (aget OUT (+ ooff c))
                                (* w (aget V (+ voff c))))))))))))))

;; ── top-k (descending, torch semantics on distinct floats) ──

(defn topk
  "Return long-array of the k indices with largest vals, descending."
  ^longs [^floats vals ^long n ^long k]
  (let [idx (long-array n)]
    (dotimes [i n] (aset idx i i))
    ;; simple selection via boxed sort — n ≤ 1024 here, parity > speed
    (let [order (sort-by #(- (double (aget vals (int %)))) (vec idx))]
      (long-array (take k order)))))

;; ── product-key retrieval core (shared by Local PKM and NetBank) ──

(defn rms-row!
  "RMSNorm a d-float row in place against weight w. (Public: grad.clj
   reuses it for the q_norm recompute in the backward passes.)"
  [^floats x ^long off ^floats w ^long d]
  (let [ss (loop [i 0 s 0.0]
             (if (< i d)
               (let [v (double (aget x (+ off i)))] (recur (inc i) (+ s (* v v))))
               s))
        inv (/ 1.0 (Math/sqrt (+ (/ ss d) eps)))]
    (dotimes [i d]
      (aset x (+ off i) (float (* (aget x (+ off i)) inv (aget w i)))))))

(defn- sub-scores
  "q-half (8) · Kᵀ (sqrt-n, 8) -> float[sqrt-n]."
  ^floats [^floats q q-off ^floats K sqrt-n sub-dim]
  (let [q-off (long q-off) sqrt-n (long sqrt-n) sub-dim (long sub-dim)
        out (float-array sqrt-n)]
    (dotimes [r sqrt-n]
      (let [koff (* r sub-dim)]
        (loop [c 0 acc 0.0]
          (if (< c sub-dim)
            (recur (inc c) (+ acc (* (double (aget q (+ q-off c)))
                                     (double (aget K (+ koff c))))))
            (aset out r (float acc))))))
    out))

(defn pk-retrieve
  "One query row -> {:idx long[top-k] (global rows, descending score)
                     :w float[top-k] (softmax weights)}.
   q must ALREADY be q_norm'd and split at sub-dim."
  [^floats q ^long q-off
   {:keys [^floats Ka ^floats Kb ^long sqrt-n ^long sub-dim
           ^long sub-top-k ^long top-k]}]
  (let [sa (sub-scores q q-off Ka sqrt-n sub-dim)
        sb (sub-scores q (+ q-off sub-dim) Kb sqrt-n sub-dim)
        ia (topk sa sqrt-n sub-top-k)
        ib (topk sb sqrt-n sub-top-k)
        ncand (* sub-top-k sub-top-k)
        cs (float-array ncand)
        ci (long-array ncand)]
    (dotimes [a sub-top-k]
      (dotimes [b sub-top-k]
        (let [p (+ (* a sub-top-k) b)]
          (aset cs p (float (+ (aget sa (int (aget ia a)))
                               (aget sb (int (aget ib b))))))
          (aset ci p (+ (* (aget ia a) sqrt-n) (aget ib b))))))
    (let [sel (topk cs ncand top-k)
          idx (long-array top-k)
          w (float-array top-k)]
      (dotimes [k top-k]
        (aset idx k (aget ci (int (aget sel k))))
        (aset w k (aget cs (int (aget sel k)))))
      ;; softmax over the selected scores
      (let [mx (loop [k 0 m Float/NEGATIVE_INFINITY]
                 (if (< k top-k) (recur (inc k) (max m (aget w k))) m))
            sum (loop [k 0 s 0.0]
                  (if (< k top-k)
                    (let [e (Math/exp (- (aget w k) (double mx)))]
                      (aset w k (float e)) (recur (inc k) (+ s e)))
                    s))]
        (dotimes [k top-k] (aset w k (float (/ (aget w k) sum)))))
      {:idx idx :w w})))

(defn pkm-forward
  "Local PKM: q (T,16) -> out (T,16). trunk-id offsets the V gather."
  [^floats q ^long T mem ^long trunk-id]
  (let [{:keys [^floats qnorm-w bank ^long q-dim ^long n-per-trunk]} mem
        out (float-array (* T q-dim))
        row (float-array q-dim)
        qn (java.util.Arrays/copyOf q (alength q))
        off (* trunk-id n-per-trunk)]
    (dotimes [ti T]
      (rms-row! qn (* ti q-dim) qnorm-w q-dim))
    (dotimes [ti T]
      (let [{:keys [^longs idx ^floats w]} (pk-retrieve qn (* ti q-dim) mem)
            ooff (* ti q-dim)]
        (dotimes [k (alength idx)]
          (p/bank-row! bank (+ off (aget idx k)) row 0)
          (let [wk (aget w k)]
            (dotimes [c q-dim]
              (aset out (+ ooff c)
                    (float (+ (aget out (+ ooff c)) (* wk (aget row c))))))))))
    out))

(defn netbank-forward
  "NetBank: q (T,16) -> out (T,16) via c_net latents + expander."
  [^floats q ^long T nb]
  (let [{:keys [^floats qnorm-w bank ^long q-dim ^long c-net ^floats expander-w]} nb
        lat (float-array c-net)
        row (float-array c-net)
        out (float-array (* T q-dim))
        qn (java.util.Arrays/copyOf q (alength q))]
    (dotimes [ti T]
      (rms-row! qn (* ti q-dim) qnorm-w q-dim))
    (dotimes [ti T]
      (java.util.Arrays/fill lat (float 0.0))
      (let [{:keys [^longs idx ^floats w]} (pk-retrieve qn (* ti q-dim) nb)]
        (dotimes [k (alength idx)]
          (p/bank-row! bank (aget idx k) row 0)
          (let [wk (aget w k)]
            (dotimes [c c-net]
              (aset lat c (float (+ (aget lat c) (* wk (aget row c)))))))))
      ;; expander: (q-dim, c-net) weight, no bias
      (let [ooff (* ti q-dim)]
        (dotimes [o q-dim]
          (loop [c 0 acc 0.0]
            (if (< c c-net)
              (recur (inc c) (+ acc (* (double (aget lat c))
                                       (double (aget expander-w (+ (* o c-net) c))))))
              (aset out (+ ooff o) (float acc)))))))
    out))

;; ── SwitchGate (eval path: smooth Bernoulli expectation) ──

(defn- dot8 ^double [^floats a ^long ao ^floats b ^long bo]
  (loop [i 0 acc 0.0]
    (if (< i 8)
      (recur (inc i) (+ acc (* (double (aget a (+ ao i))) (double (aget b (+ bo i))))))
      acc)))

(defn gate-mix
  "3-way SwitchGate + alpha_net + net-default (EVAL branch, gating.py:227).
   All of q/sdpa/mem/net are (T, n-long-heads*8) with head h at h*8.
   mem may be nil -> 2-way sigmoid path. Returns (T, n-long-heads*8)."
  [{:keys [^floats gate-proj ^floats gate-proj-3 ^floats alpha-net
           ^floats lap ^floats lab ^long n-long-heads]}
   ^floats q ^floats sdpa ^floats mem ^floats net T]
  (let [T (long T) hd 8
        width (* n-long-heads hd)
        out (float-array (* T width))]
    (dotimes [ti T]
      (dotimes [h n-long-heads]
        (let [qoff (+ (* ti width) (* h hd))
              alpha (double (aget alpha-net h))]
          (if (nil? mem)
            ;; 2-way: g=σ(q·gate_proj[h]); out = g·sdpa + (1-g)·(α·net)
            (let [g (/ 1.0 (+ 1.0 (Math/exp (- (dot8 q qoff gate-proj (* h hd))))))]
              (dotimes [c hd]
                (aset out (+ qoff c)
                      (float (+ (* g (aget sdpa (+ qoff c)))
                                (* (- 1.0 g) alpha (aget net (+ qoff c))))))))
            ;; 3-way softmax + α on net + smooth local firing + renorm
            (let [l0 (dot8 q qoff gate-proj-3 (* h 3 hd))
                  l1 (dot8 q qoff gate-proj-3 (+ (* h 3 hd) hd))
                  l2 (dot8 q qoff gate-proj-3 (+ (* h 3 hd) (* 2 hd)))
                  mx (max l0 (max l1 l2))
                  e0 (Math/exp (- l0 mx)) e1 (Math/exp (- l1 mx)) e2 (Math/exp (- l2 mx))
                  z (+ e0 e1 e2)
                  w0 (/ e0 z) w1 (/ e1 z) w2 (/ e2 z)
                  lp (/ 1.0 (+ 1.0 (Math/exp (- (+ (dot8 q qoff lap (* h hd))
                                                   (double (aget lab h)))))))
                  w1 (* w1 lp)
                  tot (+ w0 w1 w2 1e-6)
                  w0 (/ w0 tot) w1 (/ w1 tot) w2 (/ w2 tot)]
              (dotimes [c hd]
                (aset out (+ qoff c)
                      (float (+ (* w0 (aget sdpa (+ qoff c)))
                                (* w1 (aget mem (+ qoff c)))
                                (* w2 alpha (aget net (+ qoff c))))))))))))
    out))

;; ── model assembly ──

(defn- named ^floats [dense n] (t/data (get (:by-name dense) n)))

(defn build-model
  "Assemble the runnable model from loaded dense params + banks + manifest.
   opts :rope — {:cos :sin} float[] override. The reference cache is torch
   float32 data; build-rope recomputes it to ~3e-5 (libm ulp drift at large
   positions), so exact-parity runs load the exported cache instead."
  ([manifest dense banks] (build-model manifest dense banks {}))
  ([manifest dense banks opts]
  (let [nb-of (fn [i] (some #(when (and (= (:kind %) "net") (= (:layer %) i)) %)
                            (:sparse manifest)))
        mem-of (fn [i] (some #(when (and (= (:kind %) "local") (= (:layer %) i)) %)
                             (:sparse manifest)))]
    {:tok-emb (named dense "tok_emb.weight")
     :norm-final (named dense "norm_final.weight")
     :rope (or (:rope opts) (build-rope 8192 8 500000.0))
     :blocks
     (vec
      (for [i (range 32)]
        (let [g #(named dense (str "blocks." i "." % ".weight"))
              gp #(named dense (str "blocks." i "." %))
              mem (mem-of i) nb (nb-of i)]
          (cond->
            {:norm1 (g "norm1") :norm2 (g "norm2")
             :q-proj (g "q_proj")
             :k-proj-s (g "k_proj_s") :v-proj-s (g "v_proj_s")
             :k-proj-l (g "k_proj_l") :v-proj-l (g "v_proj_l")
             :o-proj (g "o_proj")
             :gate-proj (g "gate_proj") :up-proj (g "up_proj")
             :down-proj (g "down_proj")
             :gate {:gate-proj (gp "long_gate.gate_proj")
                    :gate-proj-3 (gp "long_gate.gate_proj_3")
                    :alpha-net (gp "long_gate.alpha_net")
                    :lap (gp "long_gate.local_active_proj")
                    :lab (gp "long_gate.local_active_bias")
                    :n-long-heads 2}
             :netbank {:Ka (gp "netbank.K_a") :Kb (gp "netbank.K_b")
                       :qnorm-w (gp "netbank.q_norm.weight")
                       :expander-w (gp "netbank.expander.weight")
                       :bank (get banks (str "blocks." i ".netbank.V"))
                       :sqrt-n (:sqrt_n nb) :sub-dim 8
                       :sub-top-k (:sub_top_k nb) :top-k (:top_k nb)
                       :q-dim 16 :c-net (:c_net nb)}}
            mem (assoc :memory
                       {:Ka (gp "memory.K_a") :Kb (gp "memory.K_b")
                        :qnorm-w (gp "memory.q_norm.weight")
                        :bank (get banks (str "blocks." i ".memory.V"))
                        :sqrt-n (:sqrt_n mem) :sub-dim 8
                        :sub-top-k (:sub_top_k mem) :top-k (:top_k mem)
                        :q-dim 16
                        :n-per-trunk (* (long (:sqrt_n mem)) (long (:sqrt_n mem)))})))))})))

(defn block-forward
  "One pre-norm block, prefill T tokens. x (T,32) mutated by residual adds."
  [blk rope ^floats x T trunk-id]
  (let [T (long T) trunk-id (long trunk-id) d 32 hd 8
        xn (t/data (t/rms-norm (t/tensor [T d] x) (t/tensor [d] (:norm1 blk)) eps))
        q (t/data (t/linear (t/tensor [T d] xn) (t/tensor [d d] (:q-proj blk))))
        ks (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:k-proj-s blk))))
        vs (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:v-proj-s blk))))
        kl (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:k-proj-l blk))))
        vl (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:v-proj-l blk))))
        attn (float-array (* T d))]
    ;; RoPE on short q heads (0,1) and k_s
    (dotimes [ti T]
      (rope-at! q (* ti d) rope ti hd)              ; head 0
      (rope-at! q (+ (* ti d) hd) rope ti hd)       ; head 1
      (rope-at! ks (* ti hd) rope ti hd))
    ;; short heads 0,1 (GQA share ks/vs); write into attn cols 0..16
    (sdpa-causal q 0 d ks vs T hd attn 0 d)
    (sdpa-causal q hd d ks vs T hd attn hd d)
    ;; long-tier SDPA heads 2,3 -> separate buffer (gate needs it)
    (let [sdpa-l (float-array (* T 16))]
      (sdpa-causal q (* 2 hd) d kl vl T hd sdpa-l 0 16)
      (sdpa-causal q (* 3 hd) d kl vl T hd sdpa-l hd 16)
      ;; bank_q = contiguous long-head slice of q rows
      (let [bank-q (float-array (* T 16))]
        (dotimes [ti T]
          (System/arraycopy q (+ (* ti d) 16) bank-q (* ti 16) 16))
        (let [mem-out (when (:memory blk)
                        (pkm-forward bank-q T (:memory blk) trunk-id))
              net-out (netbank-forward bank-q T (:netbank blk))
              mixed (gate-mix (:gate blk) bank-q sdpa-l mem-out net-out T)]
          (dotimes [ti T]
            (System/arraycopy mixed (* ti 16) attn (+ (* ti d) 16) 16)))))
    ;; o-proj + residual
    (let [o (t/data (t/linear (t/tensor [T d] attn) (t/tensor [d d] (:o-proj blk))))]
      (dotimes [i (* T d)] (aset x i (float (+ (aget x i) (aget o i))))))
    ;; FFN + residual
    (let [xn2 (t/rms-norm (t/tensor [T d] x) (t/tensor [d] (:norm2 blk)) eps)
          h (t/mul! (t/silu! (t/linear xn2 (t/tensor [128 d] (:gate-proj blk))))
                    (t/linear xn2 (t/tensor [128 d] (:up-proj blk))))
          f (t/data (t/linear h (t/tensor [d 128] (:down-proj blk))))]
      (dotimes [i (* T d)] (aset x i (float (+ (aget x i) (aget f i))))))
    x))

(defn forward
  "tokens (long-seq, length T) -> logits (T, 256) float[]. Eval prefill."
  [model tokens ^long trunk-id]
  (let [d 32 T (count tokens)
        ^floats emb (:tok-emb model)
        x (float-array (* T d))]
    (dotimes [ti T]
      (System/arraycopy emb (* (long (nth tokens ti)) d) x (* ti d) d))
    (doseq [blk (:blocks model)]
      (block-forward blk (:rope model) x T trunk-id))
    (let [xf (t/rms-norm (t/tensor [T d] x) (t/tensor [d] (:norm-final model)) eps)]
      (t/data (t/linear xf (t/tensor [256 d] (:tok-emb model)))))))
