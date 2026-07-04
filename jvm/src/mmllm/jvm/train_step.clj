(ns mmllm.jvm.train-step
  "The full sym24 train step on the JVM (M5b, gate G4) — core.lpy
   train-step at the prod logitkd recipe:

     loss  = CE(logits, y) + z_coef · Σ_layers z_local
     [step % KD_EVERY == 0] extra backward on
     kd    = KD_COEF · T² · KL(teacher_T ‖ student_T)
             teacher = local-only forward (no grad)
             student = net-only forward, freeze-trunk

   Backward runs through all 32 blocks via mmllm.jvm.train-forward /
   grad.clj; grads for the 698 dense tensors flow to AdamW (TWO groups
   since c0449a3's prod make-opt-dense: group 0 = core dense at
   lr-dense, group 1 = every block's memory.K_a/K_b at lr-kab; when
   (:kab lrs) is absent or equal it degenerates to the single-group
   back-compat path exactly like the reference's kab==dense branch;
   torch defaults incl. wd=1e-2, params without grads skipped), Local
   V and V_net sparse grads to two
   touched-row sparse-Adam instances (optim.py semantics — the Adam
   arithmetic below mirrors mmllm.jvm.optim/sparse-param-step! f32
   op-for-op, re-stated here against bank OVERLAYS because bank V lives
   in mmap'd goldens that must never be written; see params.clj).

   NOTE (reference quirk, replicated on purpose): at the sym24 sizes
   optim.py's _is_v_local matches V_net TOO — 1024² rows divide into 64
   trunks of sqrt_local²=128² — so opt-sparse-net's updates also carry
   MMLLM_LR_LOCAL_MULT (0.05). The docstring in optim.py claims V_net
   falls through; that's only true for configs where NET_SQRT_N² isn't
   a multiple of SQRT_N². Parity pins the actual behavior."
  (:require [mmllm.jvm.model :as m]
            [mmllm.jvm.grad :as g]
            [mmllm.jvm.optim :as o]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.train-forward :as tf])
  (:import [java.util HashMap]))

(set! *warn-on-reflection* true)

;; ── losses ──

(defn ce-all-positions
  "F.cross_entropy(logits.reshape(-1,V), y.reshape(-1)) over B rows —
   ALL T positions (y is already the shifted target window).
   logits-rows: vector of (T,V) float[]; y-rows: vector of T longs.
   -> {:loss double :dlogits [B × float[T*V]]} with dlogits scaled by
   1/(B*T) (mean reduction)."
  [logits-rows y-rows T V]
  (let [T (long T) V (long V)
        B (count logits-rows)
        n (* B T)
        pr (double-array V)]
    (loop [b 0 acc 0.0 douts (transient [])]
      (if (= b B)
        {:loss (/ acc n) :dlogits (persistent! douts)}
        (let [^floats logits (nth logits-rows b)
              y (nth y-rows b)
              dl (float-array (* T V))
              row-acc
              (loop [ti 0 racc 0.0]
                (if (= ti T)
                  racc
                  (let [off (* ti V)
                        tgt (long (nth y ti))
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
                           (+ racc (- (+ mx (Math/log sum)) (aget logits (+ off tgt))))))))]
          (recur (inc b) (+ acc row-acc) (conj! douts dl)))))))

(defn- log-softmax-row!
  "logits[off..off+V)/temp → out (double[V]) log-probs; returns nothing."
  [^floats logits off temp ^doubles out V]
  (let [off (long off) V (long V) temp (double temp)]
    (dotimes [j V] (aset out j (/ (double (aget logits (+ off j))) temp)))
    (let [mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
               (if (< j V) (recur (inc j) (max mv (aget out j))) mv))
          sm (loop [j 0 s 0.0]
               (if (< j V) (recur (inc j) (+ s (Math/exp (- (aget out j) mx)))) s))
          lse (+ mx (Math/log sm))]
      (dotimes [j V] (aset out j (- (aget out j) lse))))))

(defn kd-loss
  "logitkd KD: KL(teacher_T ‖ student_T) at temp, mean over B·T positions.
   -> {:kl double :dlogits [B × float[T*V]]} where dlogits is wrt the
   STUDENT logits, already scaled by kd-coef·temp/(B·T) (i.e. the grad of
   kd-coef·T²·kl wrt student logits)."
  [t-rows s-rows T V temp kd-coef]
  (let [T (long T) V (long V) temp (double temp) kd-coef (double kd-coef)
        B (count t-rows)
        n (* B T)
        tlp (double-array V)
        slp (double-array V)
        scale (/ (* kd-coef temp) n)]
    (loop [b 0 acc 0.0 douts (transient [])]
      (if (= b B)
        {:kl (/ acc n) :dlogits (persistent! douts)}
        (let [^floats tl (nth t-rows b)
              ^floats sl (nth s-rows b)
              dl (float-array (* T V))
              racc
              (loop [ti 0 racc 0.0]
                (if (= ti T)
                  racc
                  (let [off (* ti V)
                        _ (log-softmax-row! tl off temp tlp V)
                        _ (log-softmax-row! sl off temp slp V)
                        kacc (loop [j 0 kacc 0.0]
                               (if (< j V)
                                 (let [pt (Math/exp (aget tlp j))
                                       ps (Math/exp (aget slp j))]
                                   (aset dl (+ off j) (float (* scale (- ps pt))))
                                   (recur (inc j) (+ kacc (* pt (- (aget tlp j) (aget slp j))))))
                                 kacc))]
                    (recur (inc ti) (+ racc kacc)))))]
          (recur (inc b) (+ acc racc) (conj! douts dl)))))))

(defn mean-ce
  "Plain mean CE of logits-rows vs y-rows (for teacher/student bpc)."
  ^double [logits-rows y-rows T V]
  (:loss (ce-all-positions logits-rows y-rows T V)))

;; ── touched-row sparse Adam against bank overlays ──

(defn dv->sorted
  "Map<row → float[dim]> (already coalesced by construction) →
   {:idx ^longs (ascending) :val ^floats (nnz×dim)} — torch
   grad.coalesce() order. Public + Map-hinted: the M6 parallel step
   (parallel_step.clj) reuses it, incl. on ConcurrentHashMaps."
  [^java.util.Map dv ^long dim]
  (let [rows (long-array (map long (keys dv)))]
    (java.util.Arrays/sort rows)
    (let [nnz (alength rows)
          val (float-array (* nnz dim))]
      (dotimes [i nnz]
        (System/arraycopy ^floats (.get dv (aget rows i)) 0 val (* i dim) dim))
      {:idx rows :val val})))

(defn bank-sparse-adam-step!
  "One CPUOffloadSparseAdam step over bank-backed params, writing the
   updates to the banks' overlays. Same semantics as
   mmllm.jvm.optim/sparse-adam-step! (per-param step counter bumped only
   when the param has a grad; _is_v_local × local-mult; layer-mults
   tiling counter) and byte-identical f32 arithmetic.
   states: vector of o/sparse-adam-init, one per param;
   params: vector of {:bank mapped-bank :rows n :dim d};
   grads:  vector of nil or {:idx ^longs :val ^floats} (coalesced);
   opts:   {:lr :sqrt-local :local-mult :layer-mults}."
  [states params grads opts]
  (let [lm (:layer-mults opts)
        local-mult (double (:local-mult opts 0.05))
        sqrt-local (long (:sqrt-local opts))
        beta1 (double (:beta1 opts 0.9))
        beta2 (double (:beta2 opts 0.999))
        n (count params)]
    (loop [i 0 vc 0]
      (when (< i n)
        (let [gr (nth grads i)]
          (if (nil? gr)
            (recur (inc i) vc)
            (let [{:keys [bank rows dim]} (nth params i)
                  dim (long dim)
                  vloc? (o/is-v-local? (long rows) sqrt-local)
                  per-layer (if (and vloc? (seq lm))
                              (double (nth lm (rem vc (count lm))))
                              1.0)
                  layer-mult (if vloc? (* local-mult per-layer) 1.0)
                  state (nth states i)
                  ^longs stepa (:step state)
                  ^HashMap mm (:m state)
                  ^HashMap vv (:v state)
                  _ (aset stepa 0 (inc (aget stepa 0)))
                  step (aget stepa 0)
                  b1f (float beta1)
                  a1f (float (- 1.0 beta1))
                  b2f (float beta2)
                  c2f (float (- 1.0 beta2))
                  bc1f (float (- 1.0 (Math/pow beta1 (double step))))
                  bc2f (float (- 1.0 (Math/pow beta2 (double step))))
                  negf (float (- (* (double (:lr opts)) layer-mult)))
                  epsf (float (:eps opts 1e-8))
                  ^longs cidx (:idx gr)
                  ^floats cval (:val gr)
                  prow (float-array dim)]
              (dotimes [k (alength cidx)]
                (let [row (aget cidx k)
                      ^floats mrow (or (.get mm row)
                                       (let [a (float-array dim)] (.put mm row a) a))
                      ^floats vrow (or (.get vv row)
                                       (let [a (float-array dim)] (.put vv row a) a))]
                  (p/bank-row! bank row prow 0)
                  (dotimes [j dim]
                    (let [gj (aget cval (+ (* k dim) j))
                          mj' (float (+ (float (* (aget mrow j) b1f))
                                        (float (* a1f gj))))
                          vj' (float (+ (float (* (aget vrow j) b2f))
                                        (float (* (float (* c2f gj)) gj))))
                          mh (float (/ mj' bc1f))
                          vh (float (/ vj' bc2f))
                          den (float (+ (float (Math/sqrt (double vh))) epsf))
                          dlt (float (/ (float (* negf mh)) den))]
                      (aset mrow j mj')
                      (aset vrow j vj')
                      (aset prow j (float (+ (aget prow j) dlt)))))
                  (p/bank-put-row! bank row prow)))
              (recur (inc i) (if vloc? (inc vc) vc)))))))
    states))

;; ── the step driver ──

(defn make-opt-states
  "Fresh optimizer states for the three optimizers.
   local-params/net-params: vectors of {:bank :rows :dim} in block order."
  [n-local n-net]
  {:adamw (HashMap.)
   :sparse-local (vec (repeatedly n-local o/sparse-adam-init))
   :sparse-net (vec (repeatedly n-net o/sparse-adam-init))})

(defn train-step!
  "One replayed train step, mutating the model's dense param arrays
   (AdamW) and bank overlays (sparse Adam) in place.

   env: {:model :manifest :dense (p/load-dense result) :local-params
         :net-params :opt-states :z-coef :kd-temp :kd-coef
         :sqrt-local :local-mult}
   step-cfg: {:kd? bool :lrs {:dense :kab :bank :net} :x-rows [B × [T longs]]
              :y-rows :trunk-ids [B longs] :R-rows [B × [24 × float[H*T]]]}

   Returns {:plain-ce :ce :z-layers double[24] :loss-total :kd :kd-kl
            :teacher-bpc :student-bpc :grads :sparse-local [per-param
            {:idx :val}] :sparse-net ...} — everything step-parity checks."
  [env step-cfg]
  (let [{:keys [model manifest dense local-params net-params opt-states]} env
        z-coef (double (:z-coef env))
        {:keys [x-rows y-rows trunk-ids R-rows kd? lrs]} step-cfg
        B (count x-rows)
        T (count (first x-rows))
        V 256
        n-bt (* (long B) (long T))
        ;; ── main forward (row-major, matching torch batch semantics) ──
        fwds (mapv (fn [b]
                     (tf/forward-train model (nth x-rows b) (nth trunk-ids b)
                                       :main (nth R-rows b)))
                   (range B))
        ;; z per layer: mean over (B,T) of lse² for both halves
        z-layers (double-array 24)
        _ (dotimes [l 24]
            (let [zs (loop [b 0 acc 0.0]
                       (if (= b B)
                         acc
                         (let [^floats lse (nth (:z-lses (nth fwds b)) l)]
                           (recur (inc b)
                                  (+ acc (loop [i 0 s 0.0]
                                           (if (< i (alength lse))
                                             (let [v (double (aget lse i))]
                                               (recur (inc i) (+ s (* v v))))
                                             s)))))))]
              (aset z-layers l (/ zs n-bt))))
        z-total (loop [l 0 s 0.0] (if (< l 24) (recur (inc l) (+ s (aget z-layers l))) s))
        {ce :loss ce-dl :dlogits} (ce-all-positions (mapv :logits fwds) y-rows T V)
        loss-total (+ ce (* z-coef z-total))
        ;; ── KD forwards (teacher no-grad local-only; student net-only) ──
        kd-res
        (when kd?
          (let [t-fwds (mapv (fn [b] (tf/forward-train model (nth x-rows b)
                                                       (nth trunk-ids b) :teacher nil))
                             (range B))
                s-fwds (mapv (fn [b] (tf/forward-train model (nth x-rows b)
                                                       (nth trunk-ids b) :student nil))
                             (range B))
                {:keys [kl dlogits]} (kd-loss (mapv :logits t-fwds)
                                              (mapv :logits s-fwds)
                                              T V (:kd-temp env) (:kd-coef env))]
            {:kl kl
             :kd (* (double (:kd-coef env)) kl (double (:kd-temp env)) (double (:kd-temp env)))
             :teacher-bpc (/ (mean-ce (mapv :logits t-fwds) y-rows T V) (Math/log 2.0))
             :student-bpc (/ (mean-ce (mapv :logits s-fwds) y-rows T V) (Math/log 2.0))
             :s-fwds s-fwds :dlogits dlogits}))
        ;; ── backward: main (CE + z), then student (KD) into same grads ──
        grads (tf/make-grads)
        z-scale (/ z-coef n-bt)]
    (dotimes [b B]
      (tf/backward-train model (nth fwds b) (nth x-rows b) (nth ce-dl b) T grads
                         {:mode :main :z-scale z-scale :trunk-id (nth trunk-ids b)}))
    (when kd?
      (dotimes [b B]
        (tf/backward-train model (nth (:s-fwds kd-res) b) (nth x-rows b)
                           (nth (:dlogits kd-res) b) T grads
                           {:mode :student :z-scale 0.0 :trunk-id (nth trunk-ids b)})))
    ;; ── optimizers ──
    (let [^HashMap gdense (:dense grads)
          ^HashMap adamw-states (:adamw opt-states)
          lr-dense (double (:dense lrs))
          ;; group 1 (make-opt-dense's kab-parameters: each block's
          ;; memory.K_a/K_b — NOT netbank.K_a/K_b) steps at lr-kab.
          ;; Defaulting :kab to :dense keeps the single-group back-compat
          ;; path (reference kab==dense branch) byte-identical.
          lr-kab (double (:kab lrs lr-dense))]
      ;; AdamW over the positional manifest order; params w/o grads skipped
      (doseq [{:keys [name]} (:dense manifest)]
        (when-let [^floats gr (.get gdense name)]
          (let [^floats pd (:data (get (:by-name dense) name))
                st (or (.get adamw-states name)
                       (let [s (o/adamw-init (alength pd))]
                         (.put adamw-states name s) s))
                kab? (or (.endsWith ^String name ".memory.K_a")
                         (.endsWith ^String name ".memory.K_b"))]
            (o/adamw-step! st pd gr {:lr (if kab? lr-kab lr-dense)})))))
    (let [sl-grads (mapv (fn [l] (when-let [^HashMap dv (.get ^HashMap (:dv-local grads) l)]
                                   (dv->sorted dv 16)))
                         (range (count local-params)))
          sn-grads (mapv (fn [l] (when-let [^HashMap dv (.get ^HashMap (:dv-net grads) l)]
                                   (dv->sorted dv 8)))
                         (range (count net-params)))
          sopts {:sqrt-local (:sqrt-local env) :local-mult (:local-mult env)}]
      (bank-sparse-adam-step! (:sparse-local opt-states) local-params sl-grads
                              (assoc sopts :lr (:bank lrs)))
      (bank-sparse-adam-step! (:sparse-net opt-states) net-params sn-grads
                              (assoc sopts :lr (:net lrs)))
      (merge {:plain-ce ce :ce ce :z-layers z-layers :loss-total loss-total
              :kd (if kd? (:kd kd-res) 0.0)
              :grads grads :sparse-local sl-grads :sparse-net sn-grads}
             (when kd? {:kd-kl (:kl kd-res)
                        :teacher-bpc (:teacher-bpc kd-res)
                        :student-bpc (:student-bpc kd-res)})))))
