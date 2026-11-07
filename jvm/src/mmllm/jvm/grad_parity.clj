(ns mmllm.jvm.grad-parity
  "Backward parity (gate G2 of docs/jvm-port-spec.md §12): every backward
   in mmllm.jvm.grad is checked TWO ways —

   1. against torch autograd goldens (jvm/goldens/grads_*.npz, regenerate
      with `.venv/bin/python scripts/dump_goldens.py --grads`), rel tol 1e-4;
   2. against central finite differences computed on the JVM side alone
      (perturb ±1e-3, rel tol ~1e-2 on the largest-|grad| coordinates —
      float32 forwards put a noise floor under smaller ones).

   Two places where naive FD is structurally wrong (not gradient bugs):

   - SwitchGate ST-Bernoulli: golden-checked in :st mode (the replayed-R
     hard decision), FD-checked in :smooth mode — the ST estimator is
     deliberately NOT the a.e.-zero true derivative of the hard draw, so
     FD can only validate the differentiable branch.
   - PKM/NetBank score path (dq/dK_a/dK_b/dq_norm): at prod dims a ±1e-3
     nudge flips which of the sub_top_k² candidates survive the top-k, and
     the loss JUMPS by more than the true-gradient signal (selection is
     piecewise-constant; torch defines the grad on the fixed selection).
     So the score path is FD-checked on a small FULLY-SELECTED config
     (sub_top_k = sqrt_n, top_k = sub_top_k² — same code, nothing to
     flip, loss genuinely differentiable), while the linear paths (dV,
     d_expander) are FD-checked at prod dims where selection cancels in
     the central difference.

   Exits nonzero on any failure. Run: jvm/run.sh -m mmllm.jvm.grad-parity"
  (:require [clojure.java.io :as io]
            [mmllm.jvm.grad :as g]
            [mmllm.jvm.model :as m]
            [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]))

(set! *warn-on-reflection* true)

(def ^:private fails (atom 0))

(defn- check [name ^double err ^double tol]
  (println (format "%-22s err %.3e  tol %.0e  %s"
                   name err tol (if (<= err tol) "OK" "FAIL")))
  (when (> err tol) (swap! fails inc)))

(defn- f32 ^floats [z k] (t/data (t/from-npy (get z k))))

(defn- max-abs ^double [^floats a]
  (loop [i 0 mv 0.0]
    (if (< i (alength a))
      (recur (inc i) (max mv (Math/abs (double (aget a i)))))
      mv)))

(defn- rel-err
  "max-abs-err normalized by the golden's max-abs."
  ^double [^floats got ^floats want]
  (assert (= (alength got) (alength want)))
  (loop [i 0 mv 0.0]
    (if (< i (alength got))
      (recur (inc i) (max mv (Math/abs (- (double (aget got i))
                                          (double (aget want i))))))
      (/ mv (max 1e-8 (max-abs want))))))

;; ── finite differences ──

(defn- fd-coords!
  "Central difference on explicit coords of arr; expected aligned doubles.
   Uses the ACTUAL float32-rounded step (fl(x+h) − fl(x−h)) as denominator."
  [name loss-fn ^floats arr coords expected h tol]
  (let [h (double h)
        worst
        (loop [cs (seq coords) es (seq expected) mv 0.0]
          (if cs
            (let [i (int (long (first cs)))
                  a (double (first es))
                  orig (aget arr i)
                  vp (float (+ orig h))
                  vm (float (- orig h))]
              (aset arr i vp)
              (let [lp (double (loss-fn))]
                (aset arr i vm)
                (let [lm (double (loss-fn))]
                  (aset arr i orig)
                  (let [fd (/ (- lp lm) (- (double vp) (double vm)))
                        denom (max (Math/abs a) (Math/abs fd))
                        e (double (if (< denom 1e-4)
                                    0.0
                                    (/ (Math/abs (- a fd)) denom)))]
                    (recur (next cs) (next es) (max mv e))))))
            mv))]
    (check name worst tol)))

(defn- top-coords [^floats a ^long n]
  (take n (sort-by #(- (Math/abs (double (aget a (int %)))))
                   (range (alength a)))))

(defn- fd!
  "FD-check analytic grads on the n largest-|analytic| coords of arr."
  ([name loss-fn arr analytic] (fd! name loss-fn arr analytic 12 1e-3 1e-2))
  ([name loss-fn ^floats arr ^floats analytic n h tol]
   (let [coords (top-coords analytic (long n))]
     (fd-coords! name loss-fn arr coords
                 (map #(double (aget analytic (int (long %)))) coords)
                 h tol))))

;; ── sparse dV compare ──

(defn- check-dv [name ^java.util.HashMap dV ^longs gidx ^floats gval dim tol]
  (let [dim (long dim) tol (double tol) nnz (alength gidx)]
    (if (not= nnz (.size dV))
      (do (println (format "%-22s nnz %d != golden %d  FAIL"
                           name (.size dV) nnz))
          (swap! fails inc))
      (let [ma (max-abs gval)
            worst
            (loop [k 0 mv 0.0]
              (if (< k nnz)
                (let [^floats got (.get dV (aget gidx k))]
                  (if (nil? got)
                    Double/POSITIVE_INFINITY
                    (recur (inc k)
                           (loop [c 0 mv2 mv]
                             (if (< c dim)
                               (recur (inc c)
                                      (max mv2 (Math/abs
                                                (- (double (aget got c))
                                                   (double (aget gval (+ (* k dim) c)))))))
                               mv2)))))
                mv))]
        (check name (/ (double worst) (max 1e-8 ma)) tol)))))

(defn- dv-flat
  "Flatten a dV HashMap into ([bank-flat-idx grad] ...) pairs."
  [^java.util.HashMap dV dim]
  (let [dim (long dim)]
    (for [^java.util.Map$Entry e (.entrySet dV)
          c (range dim)]
      [(+ (* (long (.getKey e)) dim) c)
       (double (aget ^floats (.getValue e) (int (long c))))])))

(defn- fd-dv!
  "FD the 12 largest dV coords against the bank's backing array."
  [name loss-fn ^floats bank-arr pairs]
  (let [picked (take 12 (sort-by #(- (Math/abs (double (second %)))) pairs))]
    (fd-coords! name loss-fn bank-arr
                (map first picked) (map second picked) 1e-3 1e-2)))

(defn- randn-arr
  "Deterministic Gaussian float[] for the JVM-only FD fixtures."
  ^floats [^java.util.Random rng n scale]
  (let [n (long n) scale (double scale) a (float-array n)]
    (dotimes [i n] (aset a i (float (* scale (.nextGaussian rng)))))
    a))

;; ── in-memory bank (FD must not scribble on the mmap'd golden files) ──

(defn- load-bank-mem
  "Read a raw bank .bin fully into a heap float[] and wrap it as the
   {:fb :dim} map p/bank-row! expects. -> {:arr float[] :bank map}"
  [file ^long rows ^long dim]
  (let [^bytes bs (java.nio.file.Files/readAllBytes (.toPath (io/file file)))
        _ (assert (= (alength bs) (* 4 rows dim)) (str file " size mismatch"))
        fb (.asFloatBuffer (.order (java.nio.ByteBuffer/wrap bs)
                                   java.nio.ByteOrder/LITTLE_ENDIAN))
        arr (float-array (* rows dim))]
    (.get fb arr)
    {:arr arr :bank {:rows rows :dim dim :fb (java.nio.FloatBuffer/wrap arr)}}))

(defn -main [& _]
  (let [manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        sp0 (fn [kind] (some #(when (and (= (:kind %) kind) (= (:layer %) 0)) %)
                             (:sparse manifest)))
        lmem (sp0 "local") lnet (sp0 "net")
        {lbank :bank lbank-arr :arr}
        (load-bank-mem (str "jvm/goldens/banks/" (:file lmem))
                       (first (:shape lmem)) (second (:shape lmem)))
        {nbank :bank nbank-arr :arr}
        (load-bank-mem (str "jvm/goldens/banks/" (:file lnet))
                       (first (:shape lnet)) (second (:shape lnet)))
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        rope {:cos (f32 rope-z "cos") :sin (f32 rope-z "sin")}]

    ;; ── rmsnorm ──
    (let [z (npy/read-npz "jvm/goldens/grads_rmsnorm.npz")
          x (f32 z "x") w (f32 z "w") r (f32 z "r")
          rows (quot (alength x) 32)
          {:keys [dx dw]} (g/rmsnorm-bwd x w r rows 32 m/eps)
          loss #(g/loss-dot (t/data (t/rms-norm (t/tensor [rows 32] x)
                                                (t/tensor [32] w) m/eps)) r)]
      (check "rmsnorm/dx" (rel-err dx (f32 z "dx")) 1e-4)
      (check "rmsnorm/dw" (rel-err dw (f32 z "dw")) 1e-4)
      (fd! "rmsnorm/dx fd" loss x dx)
      (fd! "rmsnorm/dw fd" loss w dw))

    ;; ── linear ──
    (let [z (npy/read-npz "jvm/goldens/grads_linear.npz")
          x (f32 z "x") W (f32 z "W") r (f32 z "r")
          rows (quot (alength x) 32)
          {:keys [dx dW]} (g/linear-bwd x W r rows 32 32)
          loss #(g/loss-dot (t/data (t/linear (t/tensor [rows 32] x)
                                              (t/tensor [32 32] W))) r)]
      (check "linear/dx" (rel-err dx (f32 z "dx")) 1e-4)
      (check "linear/dW" (rel-err dW (f32 z "dW")) 1e-4)
      (fd! "linear/dx fd" loss x dx)
      (fd! "linear/dW fd" loss W dW))

    ;; ── silu ──
    (let [z (npy/read-npz "jvm/goldens/grads_silu.npz")
          x (f32 z "x") r (f32 z "r")
          dx (g/silu-bwd x r)
          n (alength x)
          loss #(g/loss-dot (t/data (t/silu! (t/copy (t/tensor [n] x)))) r)]
      (check "silu/dx" (rel-err dx (f32 z "dx")) 1e-4)
      (fd! "silu/dx fd" loss x dx))

    ;; ── swiglu ──
    (let [z (npy/read-npz "jvm/goldens/grads_swiglu.npz")
          x (f32 z "x") r (f32 z "r")
          Wg (f32 z "Wg") Wu (f32 z "Wu") Wd (f32 z "Wd")
          rows (quot (alength x) 32)
          {:keys [dx dWg dWu dWd]} (g/swiglu-bwd x Wg Wu Wd r rows 32 128)
          loss #(g/loss-dot (:y (g/swiglu-fwd x Wg Wu Wd rows 32 128)) r)]
      (check "swiglu/dx" (rel-err dx (f32 z "dx")) 1e-4)
      (check "swiglu/dWg" (rel-err dWg (f32 z "dWg")) 1e-4)
      (check "swiglu/dWu" (rel-err dWu (f32 z "dWu")) 1e-4)
      (check "swiglu/dWd" (rel-err dWd (f32 z "dWd")) 1e-4)
      (fd! "swiglu/dx fd" loss x dx)
      (fd! "swiglu/dWg fd" loss Wg dWg)
      (fd! "swiglu/dWu fd" loss Wu dWu)
      (fd! "swiglu/dWd fd" loss Wd dWd))

    ;; ── causal SDPA (2 heads, contiguous (16,8) slices) ──
    (let [z (npy/read-npz "jvm/goldens/grads_sdpa.npz")
          q (f32 z "q") k (f32 z "k") v (f32 z "v") r (f32 z "r")
          slice (fn [^floats a ^long h]
                  (java.util.Arrays/copyOfRange a (* h 128) (* (inc h) 128)))
          dq (float-array 256) dk (float-array 256) dv (float-array 256)
          _ (dotimes [h 2]
              (let [{hq :dq hk :dk hv :dv}
                    (g/sdpa-causal-bwd (slice q h) (slice k h) (slice v h)
                                       (slice r h) 16 8)]
                (System/arraycopy ^floats hq 0 dq (* h 128) 128)
                (System/arraycopy ^floats hk 0 dk (* h 128) 128)
                (System/arraycopy ^floats hv 0 dv (* h 128) 128)))
          loss (fn []
                 (let [out (float-array 256)]
                   (dotimes [h 2]
                     (m/sdpa-causal q (* h 128) 8 (slice k h) (slice v h)
                                    16 8 out (* h 128) 8))
                   (g/loss-dot out r)))]
      (check "sdpa/dq" (rel-err dq (f32 z "dq")) 1e-4)
      (check "sdpa/dk" (rel-err dk (f32 z "dk")) 1e-4)
      (check "sdpa/dv" (rel-err dv (f32 z "dv")) 1e-4)
      (fd! "sdpa/dq fd" loss q dq)
      (fd! "sdpa/dk fd" loss k dk)
      (fd! "sdpa/dv fd" loss v dv))

    ;; ── rope (linear; pos offset 3, (1,2,5,8) head stride 40) ──
    (let [z (npy/read-npz "jvm/goldens/grads_rope.npz")
          q (f32 z "q") r (f32 z "r")
          dq (java.util.Arrays/copyOf ^floats r (alength ^floats r))
          _ (dotimes [h 2]
              (dotimes [ti 5]
                (g/rope-bwd-at! dq (+ (* h 40) (* ti 8)) rope (+ ti 3) 8)))
          loss (fn []
                 (let [y (java.util.Arrays/copyOf ^floats q (alength ^floats q))]
                   (dotimes [h 2]
                     (dotimes [ti 5]
                       (m/rope-at! y (+ (* h 40) (* ti 8)) rope (+ ti 3) 8)))
                   (g/loss-dot y r)))]
      (check "rope/dq" (rel-err dq (f32 z "dq")) 1e-4)
      (fd! "rope/dq fd" loss q dq))

    ;; ── Local PKM (block-0 params from the golden; routers 0 and 3) ──
    (let [z (npy/read-npz "jvm/goldens/grads_pkm.npz")
          q (f32 z "q") r (f32 z "r")
          Ka (f32 z "Ka") Kb (f32 z "Kb") qnw (f32 z "qnorm_w")
          mem {:Ka Ka :Kb Kb :qnorm-w qnw :bank lbank
               :sqrt-n (:sqrt_n lmem) :sub-dim 8
               :sub-top-k (:sub_top_k lmem) :top-k (:top_k lmem)
               :q-dim 16
               :n-per-trunk (* (long (:sqrt_n lmem)) (long (:sqrt_n lmem)))}
          ^longs tids (:data (get z "trunk_ids"))
          seg (fn [^floats a ^long b] (java.util.Arrays/copyOfRange a (* b 64) (* (inc b) 64)))
          acc {:dKa (float-array (alength Ka)) :dKb (float-array (alength Kb))
               :dqnorm-w (float-array 16) :dV (java.util.HashMap.)}
          dq (float-array 128)
          _ (dotimes [b 2]
              (let [res (g/pkm-bwd (seg q b) 4 mem (aget tids b) (seg r b) acc)]
                (System/arraycopy ^floats (:dq res) 0 dq (* b 64) 64)))
          loss (fn []
                 (+ (g/loss-dot (m/pkm-forward (seg q 0) 4 mem (aget tids 0)) (seg r 0))
                    (g/loss-dot (m/pkm-forward (seg q 1) 4 mem (aget tids 1)) (seg r 1))))]
      (check "pkm/dq" (rel-err dq (f32 z "dq")) 1e-4)
      (check "pkm/dKa" (rel-err (:dKa acc) (f32 z "dKa")) 1e-4)
      (check "pkm/dKb" (rel-err (:dKb acc) (f32 z "dKb")) 1e-4)
      (check "pkm/dqnorm" (rel-err (:dqnorm-w acc) (f32 z "dqnorm_w")) 1e-4)
      (check-dv "pkm/dV" (:dV acc) (:data (get z "dV_idx")) (f32 z "dV_val") 16 1e-4)
      ;; dV is linear in V — FD-able at prod dims (selection can't flip)
      (fd-dv! "pkm/dV fd" loss lbank-arr (dv-flat (:dV acc) 16)))

    ;; ── Local PKM score path, FULLY-SELECTED small config (see ns doc) ──
    (let [rng (java.util.Random. 20260703)
          Ka (randn-arr rng 64 1.0) Kb (randn-arr rng 64 1.0)
          qnw (randn-arr rng 16 0.1)
          _ (dotimes [i 16] (aset qnw i (float (+ 1.0 (aget qnw i)))))
          bank-arr (randn-arr rng (* 2 64 16) 0.05)   ; 2 trunks × 8² rows
          mem {:Ka Ka :Kb Kb :qnorm-w qnw
               :bank {:rows 128 :dim 16 :fb (java.nio.FloatBuffer/wrap bank-arr)}
               :sqrt-n 8 :sub-dim 8 :sub-top-k 8 :top-k 64
               :q-dim 16 :n-per-trunk 64}
          q (randn-arr rng 48 0.5) r (randn-arr rng 48 1.0)
          {:keys [dq dKa dKb dqnorm-w dV]} (g/pkm-bwd q 3 mem 1 r)
          loss #(g/loss-dot (m/pkm-forward q 3 mem 1) r)]
      (fd! "pkm-full/dq fd" loss q dq)
      (fd! "pkm-full/dKa fd" loss Ka dKa)
      (fd! "pkm-full/dKb fd" loss Kb dKb)
      (fd! "pkm-full/dqnorm fd" loss qnw dqnorm-w)
      (fd-dv! "pkm-full/dV fd" loss bank-arr (dv-flat dV 16)))

    ;; ── NetBank (block-0) ──
    (let [z (npy/read-npz "jvm/goldens/grads_netbank.npz")
          q (f32 z "q") r (f32 z "r")
          Ka (f32 z "Ka") Kb (f32 z "Kb") qnw (f32 z "qnorm_w")
          exp-w (f32 z "expander_w")
          nb {:Ka Ka :Kb Kb :qnorm-w qnw :expander-w exp-w :bank nbank
              :sqrt-n (:sqrt_n lnet) :sub-dim 8
              :sub-top-k (:sub_top_k lnet) :top-k (:top_k lnet)
              :q-dim 16 :c-net (:c_net lnet)}
          {:keys [dq dKa dKb dqnorm-w dexp dV]} (g/netbank-bwd q 4 nb r)
          loss #(g/loss-dot (m/netbank-forward q 4 nb) r)]
      (check "netbank/dq" (rel-err dq (f32 z "dq")) 1e-4)
      (check "netbank/dKa" (rel-err dKa (f32 z "dKa")) 1e-4)
      (check "netbank/dKb" (rel-err dKb (f32 z "dKb")) 1e-4)
      (check "netbank/dqnorm" (rel-err dqnorm-w (f32 z "dqnorm_w")) 1e-4)
      (check "netbank/dexp" (rel-err dexp (f32 z "dexpander")) 1e-4)
      (check-dv "netbank/dV" dV (:data (get z "dV_idx")) (f32 z "dV_val") 8 1e-4)
      ;; expander + dV are post-/pre-selection linear — FD-able at prod dims
      (fd! "netbank/dexp fd" loss exp-w dexp)
      (fd-dv! "netbank/dV fd" loss nbank-arr (dv-flat dV 8)))

    ;; ── NetBank score path, FULLY-SELECTED small config (see ns doc) ──
    (let [rng (java.util.Random. 7030626)
          Ka (randn-arr rng 64 1.0) Kb (randn-arr rng 64 1.0)
          qnw (randn-arr rng 16 0.1)
          _ (dotimes [i 16] (aset qnw i (float (+ 1.0 (aget qnw i)))))
          exp-w (randn-arr rng (* 16 8) 0.3)
          bank-arr (randn-arr rng (* 64 8) 0.05)
          nb {:Ka Ka :Kb Kb :qnorm-w qnw :expander-w exp-w
              :bank {:rows 64 :dim 8 :fb (java.nio.FloatBuffer/wrap bank-arr)}
              :sqrt-n 8 :sub-dim 8 :sub-top-k 8 :top-k 64
              :q-dim 16 :c-net 8}
          q (randn-arr rng 48 0.5) r (randn-arr rng 48 1.0)
          {:keys [dq dKa dKb dqnorm-w dexp dV]} (g/netbank-bwd q 3 nb r)
          loss #(g/loss-dot (m/netbank-forward q 3 nb) r)]
      (fd! "netbank-full/dq fd" loss q dq)
      (fd! "netbank-full/dKa fd" loss Ka dKa)
      (fd! "netbank-full/dKb fd" loss Kb dKb)
      (fd! "netbank-full/dqnorm fd" loss qnw dqnorm-w)
      (fd! "netbank-full/dexp fd" loss exp-w dexp)
      (fd-dv! "netbank-full/dV fd" loss bank-arr (dv-flat dV 8)))

    ;; ── SwitchGate: golden-check the ST branch, FD-check the smooth one ──
    (let [z (npy/read-npz "jvm/goldens/grads_gate.npz")
          gate {:gate-proj-3 (f32 z "p_gate_proj_3")
                :alpha-net (f32 z "p_alpha_net")
                :lap (f32 z "p_local_active_proj")
                :lab (f32 z "p_local_active_bias")}
          q (f32 z "q") sd (f32 z "sdpa") me (f32 z "mem") ne (f32 z "net")
          R (f32 z "R") r (f32 z "r")
          st (g/gate-train-bwd gate q sd me ne R 2 6 :st r)]
      (check "gate/y (ST replay)" (rel-err (:y st) (f32 z "y")) 1e-5)
      (check "gate/dq" (rel-err (:dq st) (f32 z "dq")) 1e-4)
      (check "gate/dsdpa" (rel-err (:dsdpa st) (f32 z "dsdpa")) 1e-4)
      (check "gate/dmem" (rel-err (:dmem st) (f32 z "dmem")) 1e-4)
      (check "gate/dnet" (rel-err (:dnet st) (f32 z "dnet")) 1e-4)
      (check "gate/dg3" (rel-err (:dg3 st) (f32 z "dgate_proj_3")) 1e-4)
      (check "gate/dalpha" (rel-err (:dalpha st) (f32 z "dalpha_net")) 1e-4)
      (check "gate/dlap" (rel-err (:dlap st) (f32 z "dlap")) 1e-4)
      (check "gate/dlab" (rel-err (:dlab st) (f32 z "dlab")) 1e-4)
      (let [sm (g/gate-train-bwd gate q sd me ne R 2 6 :smooth r)
            loss #(g/loss-dot (:y (g/gate-train-bwd gate q sd me ne R 2 6
                                                    :smooth nil)) r)]
        (fd! "gate/dq fd" loss q (:dq sm))
        (fd! "gate/dsdpa fd" loss sd (:dsdpa sm))
        (fd! "gate/dmem fd" loss me (:dmem sm))
        (fd! "gate/dnet fd" loss ne (:dnet sm))
        (fd! "gate/dg3 fd" loss (:gate-proj-3 gate) (:dg3 sm))
        (fd! "gate/dalpha fd" loss (:alpha-net gate) (:dalpha sm) 2 1e-3 1e-2)
        (fd! "gate/dlap fd" loss (:lap gate) (:dlap sm))
        (fd! "gate/dlab fd" loss (:lab gate) (:dlab sm) 2 1e-3 1e-2)))

    ;; ── tied head ──
    (let [z (npy/read-npz "jvm/goldens/grads_tiedhead.npz")
          W (f32 z "W") r (f32 z "r")
          toks (vec (:data (get z "tokens")))
          {:keys [logits demb]} (g/tied-head-bwd W toks r 8 32 256)
          loss (fn []
                 (let [x (float-array (* 8 32))]
                   (dotimes [ti 8]
                     (System/arraycopy W (* (long (nth toks ti)) 32) x (* ti 32) 32))
                   (g/loss-dot (t/data (t/linear (t/tensor [8 32] x)
                                                 (t/tensor [256 32] W))) r)))]
      (check "tiedhead/logits" (rel-err logits (f32 z "logits")) 1e-5)
      (check "tiedhead/demb" (rel-err demb (f32 z "dW")) 1e-4)
      (fd! "tiedhead/demb fd" loss W demb))

    ;; ── CE from logits ──
    (let [z (npy/read-npz "jvm/goldens/grads_ce.npz")
          logits (f32 z "logits")
          toks (vec (:data (get z "tokens")))
          want-loss (double (aget ^doubles (:data (get z "loss")) 0))
          {:keys [loss dlogits]} (g/ce-from-logits logits toks 64 256)
          loss-fn #(double (:loss (g/ce-from-logits logits toks 64 256)))]
      (check "ce/loss" (/ (Math/abs (- (double loss) want-loss))
                          (Math/abs want-loss)) 1e-5)
      (check "ce/dlogits" (rel-err dlogits (f32 z "dlogits")) 1e-4)
      (fd! "ce/dlogits fd" loss-fn logits dlogits))

    (if (pos? @fails)
      (do (println @fails "FAILURES") (System/exit 1))
      (println "ALL GRAD PARITY CHECKS PASSED"))))
