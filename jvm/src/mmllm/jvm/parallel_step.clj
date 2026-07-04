(ns mmllm.jvm.parallel-step
  "M6 (docs/jvm-port-spec.md §10, gate G6): per-router thread parallelism
   for the sym24 train step.

   The sequential step (mmllm.jvm.train-step) processes the B batch rows
   one after another. But every per-row pipeline — main forward, CE
   dlogits, main backward, and (on KD steps) teacher forward, student
   forward, KD dlogits, student backward — is independent of every other
   row: CE / KD / z gradients scale by the GLOBAL 1/(B·T), which is known
   up front, and all cross-row coupling lives in (a) scalar loss
   reductions and (b) gradient accumulation. So the unit of parallelism
   is the (row=router, pass) pair, exactly the spec §10 design:

   - one task per row for [main forward + backward] into a PER-TASK
     grads container over the shared read-only dense params + banks;
   - on KD steps, one task per row for the no-grad TEACHER forward and
     one for [student forward + KD backward]. Tasks are submitted in
     main → teacher → student order to a FIFO fixed pool, so teacher
     forwards weave onto spare threads and a student task's blocking
     .get on its teacher future can never deadlock (its teacher task is
     already running or done by the time the student task is dequeued).

   Gradient landing zones:
   - dense grads: per-task buffers, reduced once per step in FIXED task
     order (main b=0..B-1, then student b=0..B-1 — the same order the
     sequential step accumulates rows). ~1.1 M floats/task: µs–ms, noise
     next to the step itself.
   - Local-bank V: each router's rows live in its own trunk slice
     (trunk_id·sqrt_n² offset), so when the batch's trunk-ids are
     pairwise distinct (the production 16-router step) the scatter
     writes are DISJOINT by construction and go hogwild-style straight
     into one shared per-layer rowstore, sharded per trunk slice (each
     shard has exactly one writer thread) — no locks, no merge phase.
     Rows written by exactly one task are a pure function of that
     task's inputs, so this stays bit-deterministic at any thread count.
     If trunk-ids repeat (a row pair CAN share rows) the code falls back
     to per-task stores + fixed-order merge.
   - V_net: rows CAN collide across routers, so always per-task stores +
     fixed-order merge.

   Determinism: the result is bit-identical for any thread count by
   construction — task outputs don't depend on scheduling, reductions
   run in fixed order, and stochastic inputs (the ST-Bernoulli uniforms)
   are per-router replayed stream slices supplied in :R-rows. The
   MMLLM_JVM_DETERMINISTIC env (default true) is honored trivially: a
   free-order reduction would only save the µs-scale reduce, so no
   non-deterministic fast path exists to switch to.

   Optimizer application is single-threaded (cheap), byte-identical to
   the sequential step's (AdamW two-group + the two bank sparse Adams).

   NOTE on parallel-vs-sequential numerics: N-thread ≡ 1-thread is
   BIT-exact (gate G6), and every scalar loss is also bit-exact vs the
   sequential step (identical reduction order). Dense/V_net grads differ
   from the sequential step at fp-reassociation level only (per-task
   partial sums are added as blocks instead of element-interleaved), so
   thread-parity checks those against the sequential path with a small
   relative tolerance instead of bit equality."
  (:require [mmllm.jvm.optim :as o]
            [mmllm.jvm.rowstore :as rs]
            [mmllm.jvm.train-forward :as tf]
            [mmllm.jvm.train-step :as ts])
  (:import [java.util HashMap]
           [java.util.concurrent Callable ExecutorService
            Executors Future]))

(set! *warn-on-reflection* true)

;; ── pool ──

(defn make-pool
  "Fixed FIFO platform-thread pool of n threads. Platform (not virtual)
   threads: the tasks are pure compute (spec §3). Caller owns shutdown
   (see with-pool)."
  ^ExecutorService [^long n]
  (Executors/newFixedThreadPool n))

(defmacro with-pool
  "Run body with `sym` bound to a fresh n-thread pool; always shuts it down."
  [[sym n] & body]
  (let [sym (vary-meta sym assoc :tag 'java.util.concurrent.ExecutorService)]
    `(let [~sym (make-pool ~n)]
       (try ~@body
            (finally (.shutdown ~sym))))))

;; ── per-row loss pieces (bit-identical to train-step's batch loops) ──

(defn ce-row
  "One row of ts/ce-all-positions: CE racc (UNscaled Σ over positions)
   plus dlogits scaled by the global 1/n (n = B·T). Same arithmetic,
   same accumulation order as the sequential row loop."
  [^floats logits y T V n]
  (let [T (long T) V (long V) n (long n)
        dl (float-array (* T V))
        pr (double-array V)
        racc
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
    {:racc racc :dl dl}))

(defn ce-racc
  "Row CE racc only (teacher/student bpc terms) — no dlogits allocation.
   Same per-position arithmetic as ce-row / ts/ce-all-positions."
  ^double [^floats logits y T V]
  (let [T (long T) V (long V)]
    (loop [ti 0 racc 0.0]
      (if (= ti T)
        racc
        (let [off (* ti V)
              tgt (long (nth y ti))
              mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
                   (if (< j V) (recur (inc j) (max mv (double (aget logits (+ off j))))) mv))
              sum (loop [j 0 s 0.0]
                    (if (< j V)
                      (recur (inc j) (+ s (Math/exp (- (aget logits (+ off j)) mx))))
                      s))]
          (recur (inc ti)
                 (+ racc (- (+ mx (Math/log sum)) (aget logits (+ off tgt))))))))))

(defn- log-softmax-row!
  "= ts's private helper: logits[off..off+V)/temp → out log-probs."
  [^floats logits off temp ^doubles out V]
  (let [off (long off) V (long V) temp (double temp)]
    (dotimes [j V] (aset out j (/ (double (aget logits (+ off j))) temp)))
    (let [mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
               (if (< j V) (recur (inc j) (max mv (aget out j))) mv))
          sm (loop [j 0 s 0.0]
               (if (< j V) (recur (inc j) (+ s (Math/exp (- (aget out j) mx)))) s))
          lse (+ mx (Math/log sm))]
      (dotimes [j V] (aset out j (- (aget out j) lse))))))

(defn kd-row
  "One row of ts/kd-loss: KL racc (UNscaled Σ over positions) + student
   dlogits scaled by the global kd-coef·temp/n."
  [^floats tl ^floats sl T V temp kd-coef n]
  (let [T (long T) V (long V) temp (double temp)
        kd-coef (double kd-coef) n (long n)
        tlp (double-array V)
        slp (double-array V)
        dl (float-array (* T V))
        scale (/ (* kd-coef temp) n)
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
    {:racc racc :dl dl}))

(defn- row-z-sum
  "Σ lse² over one row's per-token (lse_a, lse_b) — the per-row share of
   one layer's z term, double accumulation like the sequential loop."
  ^double [^floats lse]
  (loop [i 0 s 0.0]
    (if (< i (alength lse))
      (let [v (double (aget lse i))] (recur (inc i) (+ s (* v v))))
      s)))

;; ── grads plumbing ──

(defn- task-grads
  "Per-task grads container. shared-local non-nil (hogwild mode) makes
   :dv-local the SHARED layer→ShardedRowMap outer map — safe because
   each task's V_local rows live in its own trunk slice = its own shard
   (single writer per shard)."
  [shared-local]
  (cond-> (tf/make-grads)
    shared-local (assoc :dv-local shared-local)))

(defn- merge-task-grads!
  "Fixed-order reduction of one task's grads into the step accumulator.
   dense: whole-buffer adds; :dv-net (and :dv-local when NOT hogwild):
   merge-dv!. Caller iterates tasks in fixed order."
  [grads tgrads hogwild?]
  (let [^HashMap td (:dense tgrads)]
    (doseq [^java.util.Map$Entry e td]
      (let [^String nm (.getKey e)
            ^floats src (.getValue e)]
        (tf/add-into! (tf/gacc grads nm (alength src)) src))))
  (let [^HashMap tn (:dv-net tgrads)]
    (doseq [^java.util.Map$Entry e tn]
      (tf/merge-dv! (tf/dv-map grads :dv-net (long (.getKey e))) (.getValue e))))
  (when-not hogwild?
    (let [^HashMap tl (:dv-local tgrads)]
      (doseq [^java.util.Map$Entry e tl]
        (tf/merge-dv! (tf/dv-map grads :dv-local (long (.getKey e))) (.getValue e))))))

(defn- submit ^Future [^ExecutorService pool f]
  (.submit pool ^Callable f))

;; ── the parallel step driver ──

(defn parallel-train-step!
  "Thread-parallel train step: same env / step-cfg / result contract as
   ts/train-step!, same in-place mutation of dense params + bank
   overlays, computed by per-router tasks on `pool` (see ns doc).

   Extra env key: :hogwild-local? (default true) — allow the shared
   lock-free V_local grad map when trunk-ids are pairwise distinct."
  [env step-cfg ^ExecutorService pool]
  (let [{:keys [model manifest dense local-params net-params opt-states]} env
        z-coef (double (:z-coef env))
        {:keys [x-rows y-rows trunk-ids R-rows kd? lrs]} step-cfg
        B (count x-rows)
        T (long (count (first x-rows)))
        V 256
        n-bt (* (long B) T)
        z-scale (/ z-coef n-bt)
        n-local (count local-params)
        hogwild? (boolean (and (:hogwild-local? env true)
                               (apply distinct? trunk-ids)))
        ;; hogwild shard geometry: one shard per trunk slice, so each
        ;; task writes only its own shard (rows-per-shard = sqrt_n²)
        n-per-trunk (long (:n-per-trunk (some :memory (:blocks model))))
        n-shards (quot (long (:rows (first local-params))) n-per-trunk)
        shared-local (when hogwild?
                       (let [h (HashMap.)]
                         (dotimes [l n-local]
                           (.put h (long l) (rs/sharded-row-map n-shards n-per-trunk 16)))
                         h))
        ;; ── tasks (submission order: main → teacher → student; FIFO) ──
        main-task
        (fn [b]
          (fn []
            (let [fwd (tf/forward-train model (nth x-rows b) (nth trunk-ids b)
                                        :main (nth R-rows b))
                  z-row (double-array 24)
                  _ (dotimes [l 24]
                      (aset z-row l (row-z-sum (nth (:z-lses fwd) l))))
                  {:keys [racc dl]} (ce-row (:logits fwd) (nth y-rows b) T V n-bt)
                  grads (task-grads shared-local)]
              (tf/backward-train model fwd (nth x-rows b) dl T grads
                                 {:mode :main :z-scale z-scale
                                  :trunk-id (nth trunk-ids b)})
              {:grads grads :z-row z-row :ce-racc racc})))
        teacher-task
        (fn [b]
          (fn []
            (let [fwd (tf/forward-train model (nth x-rows b) (nth trunk-ids b)
                                        :teacher nil)]
              {:logits (:logits fwd)
               :racc (ce-racc (:logits fwd) (nth y-rows b) T V)})))
        student-task
        (fn [b ^Future teacher-fut]
          (fn []
            (let [s-fwd (tf/forward-train model (nth x-rows b) (nth trunk-ids b)
                                          :student nil)
                  t (.get teacher-fut)
                  {:keys [racc dl]} (kd-row (:logits t) (:logits s-fwd) T V
                                            (:kd-temp env) (:kd-coef env) n-bt)
                  s-racc (ce-racc (:logits s-fwd) (nth y-rows b) T V)
                  grads (task-grads nil)]
              (tf/backward-train model s-fwd (nth x-rows b) dl T grads
                                 {:mode :student :z-scale 0.0
                                  :trunk-id (nth trunk-ids b)})
              {:grads grads :kd-racc racc :s-racc s-racc})))
        submit-all (fn [task-of]
                     (let [al (java.util.ArrayList.)]
                       (dotimes [b B] (.add al (submit pool (task-of b))))
                       al))
        ^java.util.ArrayList main-futs (submit-all main-task)
        teach-futs (when kd? (mapv #(submit pool (teacher-task %)) (range B)))
        ^java.util.ArrayList stud-futs
        (when kd? (submit-all #(student-task % (nth teach-futs %))))
        ;; ── fixed-order STREAMING grad reduction (main rows, then student
        ;; rows — the same order the sequential step accumulates). Each
        ;; task's grads merge as soon as its turn comes and the future slot
        ;; is nulled, so completed-but-unmerged results don't pile up: a
        ;; B=16 V_net-heavy step would otherwise retain ~2 GB of per-task
        ;; sparse maps. Order is by row index, never completion order —
        ;; bit-deterministic at any thread count. ──
        grads {:dense (HashMap.)
               :dv-local (or shared-local (HashMap.))
               :dv-net (HashMap.)}
        consume! (fn [^java.util.ArrayList futs]
                   (mapv (fn [i]
                           (let [^Future f (.get futs (int i))
                                 r (.get f)]
                             (.set futs (int i) nil)
                             (merge-task-grads! grads (:grads r) hogwild?)
                             (dissoc r :grads)))
                         (range (.size futs))))
        mains (consume! main-futs)
        studs (when kd? (consume! stud-futs))
        teachs (when kd? (mapv (fn [^Future f] (.get f)) teach-futs))
        ;; ── fixed-order scalar reductions (≡ sequential arithmetic) ──
        sum-over (fn ^double [rows k]
                   (loop [b 0 acc 0.0]
                     (if (< b B)
                       (recur (inc b) (+ acc (double (k (nth rows b)))))
                       acc)))
        ce (/ (sum-over mains :ce-racc) n-bt)
        z-layers (double-array 24)
        _ (dotimes [l 24]
            (let [zs (loop [b 0 acc 0.0]
                       (if (< b B)
                         (recur (inc b) (+ acc (aget ^doubles (:z-row (nth mains b)) l)))
                         acc))]
              (aset z-layers l (double (/ (double zs) n-bt)))))
        z-total (loop [l 0 s 0.0] (if (< l 24) (recur (inc l) (+ s (aget z-layers l))) s))
        loss-total (+ ce (* z-coef z-total))
        kd-kl (when kd? (/ (sum-over studs :kd-racc) n-bt))
        kd-val (when kd? (* (double (:kd-coef env)) (double kd-kl)
                            (double (:kd-temp env)) (double (:kd-temp env))))
        teacher-bpc (when kd? (/ (/ (sum-over teachs :racc) n-bt) (Math/log 2.0)))
        student-bpc (when kd? (/ (/ (sum-over studs :s-racc) n-bt) (Math/log 2.0)))]
    ;; (grads were already reduced by consume!, in fixed task order)
    ;; ── optimizers: single-threaded, ≡ ts/train-step!'s application ──
    (let [^HashMap gdense (:dense grads)
          ^HashMap adamw-states (:adamw opt-states)
          lr-dense (double (:dense lrs))
          lr-kab (double (:kab lrs lr-dense))]
      (doseq [{:keys [name]} (:dense manifest)]
        (when-let [^floats gr (.get gdense name)]
          (let [^floats pd (:data (get (:by-name dense) name))
                st (or (.get adamw-states name)
                       (let [s (o/adamw-init (alength pd))]
                         (.put adamw-states name s) s))
                kab? (or (.endsWith ^String name ".memory.K_a")
                         (.endsWith ^String name ".memory.K_b"))]
            (o/adamw-step! st pd gr {:lr (if kab? lr-kab lr-dense)})))))
    (let [^HashMap outer-l (:dv-local grads)
          ^HashMap outer-n (:dv-net grads)
          ;; sort each layer's merged store then DROP it from the outer
          ;; map — the sorted {:idx :val} copy is all the optimizer (and
          ;; the parity checks) need, and releasing the store here keeps
          ;; the step's peak from holding both representations of every
          ;; layer at once.
          sorted-of (fn [^HashMap outer l dim]
                      (let [dv (.get outer l)]
                        (when (and dv (pos? (rs/store-size dv)))
                          (let [r (ts/dv->sorted dv (long dim))]
                            (.remove outer l)
                            r))))
          sl-grads (mapv #(sorted-of outer-l % 16) (range (count local-params)))
          sn-grads (mapv #(sorted-of outer-n % 8) (range (count net-params)))
          sopts {:sqrt-local (:sqrt-local env) :local-mult (:local-mult env)}]
      (ts/bank-sparse-adam-step! (:sparse-local opt-states) local-params sl-grads
                                 (assoc sopts :lr (:bank lrs)))
      (ts/bank-sparse-adam-step! (:sparse-net opt-states) net-params sn-grads
                                 (assoc sopts :lr (:net lrs)))
      (merge {:plain-ce ce :ce ce :z-layers z-layers :loss-total loss-total
              :kd (if kd? kd-val 0.0)
              :grads grads :sparse-local sl-grads :sparse-net sn-grads
              :hogwild? hogwild?}
             (when kd? {:kd-kl kd-kl
                        :teacher-bpc teacher-bpc
                        :student-bpc student-bpc})))))
