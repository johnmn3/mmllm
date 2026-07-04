(ns mmllm.jvm.thread-parity
  "Gate G6 (docs/jvm-port-spec.md §12): the parallel per-router train
   step (mmllm.jvm.parallel-step) is BIT-IDENTICAL at 1 thread and at
   16 threads, on a deterministic 16-router step:

     B=16 rows, trunk-ids 0..15 (one per router), T=32, synthetic
     next-byte batch + per-router replayed uniform stream slices (each
     router's ST-Bernoulli draws come from its own seeded stream, so
     results can't depend on scheduling).

   Checks, all bit-exact (== / Arrays.equals) between the two runs:
     - every loss scalar + the 24 per-layer z terms
     - all 698 dense grads
     - all Local + Net sparse grads (idx AND values)
     - post-step values of all 698 dense tensors
     - post-step touched V rows (all 24 local + 32 net banks)

   Plus two sanity legs:
     - parallel(1 thread) vs the SEQUENTIAL ts/train-step! on the same
       batch: loss scalars bit-exact (identical reduction order);
       V_local grads bit-exact (single-writer rows); dense + V_net grads
       within rel 1e-5 (per-task partial sums reassociate fp adds).
     - a duplicate-trunk mini-step (B=4, trunk-ids [0 0 5 5], T=16) at
       1 vs 8 threads, bit-exact — covers the non-hogwild fallback where
       V_local rows CAN collide across rows and are merged per-task in
       fixed order.

   The sequential path stays the default everywhere; this gate is
   additive. Gate G6(b) — step-parity staying green — is the existing
   jvm/run.sh -m mmllm.jvm.step-parity run.

   Run: _JAVA_OPTIONS=-Xmx11g jvm/run.sh -m mmllm.jvm.thread-parity

   Heap: run.sh's default 4 GB is NOT enough here. A B=16 step touches
   ~230 k V_net rows per layer (16 rows × T=32 × top_k=512 draws into
   1024² rows), and the port's boxed HashMap sparse structures cost
   ~115 B/row across grads + Adam moments + overlays — several GB per
   run even after this gate trims optimizer state between runs. That is
   workload-inherent (the torch reference needs a 15 GB box for the same
   effective batch), not a leak; _JAVA_OPTIONS overrides run.sh's -Xmx."
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]
            [mmllm.jvm.model :as m]
            [mmllm.jvm.train-step :as ts]
            [mmllm.jvm.parallel-step :as ps])
  (:import [java.util HashMap Random]))

(set! *warn-on-reflection* true)

(def ^:private fails (atom 0))

(defn- check-ok [name ok? detail]
  (println (format "%-34s %s%s" name (if ok? "OK" "FAIL")
                   (if ok? "" (str "  " detail))))
  (when-not ok? (swap! fails inc)))

(defn- check [name ^double err ^double tol]
  (println (format "%-34s err %.3e  tol %.0e  %s"
                   name err tol (if (<= err tol) "OK" "FAIL")))
  (when (> err tol) (swap! fails inc)))

(defn- d0 ^double [z k] (let [d (:data (get z k))]
                          (if (instance? (Class/forName "[D") d)
                            (aget ^doubles d 0)
                            (double (aget ^floats d 0)))))

(defn- l0 ^long [z k] (aget ^longs (:data (get z k)) 0))

(defn- norm2 ^double [^floats a]
  (loop [i 0 s 0.0]
    (if (< i (alength a))
      (let [v (double (aget a i))] (recur (inc i) (+ s (* v v))))
      (Math/sqrt s))))

;; ── environment builders (fresh state per run: overlays + dense arrays
;;    reload from the golden files, so every run starts byte-identical) ──

(defn- fresh-env [manifest rope zmeta]
  (let [dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks0 (p/load-banks manifest "jvm/goldens/banks")
        banks (into {} (for [[k v] banks0] [k (assoc v :overlay (HashMap.))]))
        model (m/build-model manifest dense banks {:rope rope})
        sp-of (fn [kind layer]
                (some #(when (and (= (:kind %) kind) (= (:layer %) layer)) %)
                      (:sparse manifest)))
        mk-param (fn [s] {:bank (get banks (:name s))
                          :rows (first (:shape s)) :dim (second (:shape s))})
        local-params (mapv #(mk-param (sp-of "local" %)) (range 24))
        net-params (mapv #(mk-param (sp-of "net" %)) (range 32))]
    {:model model :manifest manifest :dense dense
     :local-params local-params :net-params net-params
     :opt-states (ts/make-opt-states 24 32)
     :z-coef (d0 zmeta "z_coef") :kd-temp (d0 zmeta "kd_temp")
     :kd-coef (d0 zmeta "kd_coef")
     :sqrt-local (l0 zmeta "sqrt_local") :local-mult (d0 zmeta "local_mult")}))

;; ── synthetic deterministic batch: per-row seeded streams ──

(defn- synth-batch
  "B rows of T next-byte tokens + per-router replayed uniform slices.
   Every stream is seeded per ROW, so any thread interleaving replays
   the same draws (spec §10.4)."
  [B T trunk-ids seed]
  (let [B (long B) T (long T) H 2
        rows (mapv (fn [b]
                     (let [r (Random. (+ (long seed) (long b)))
                           win (vec (repeatedly (inc T) #(long (.nextInt r 256))))]
                       {:x (subvec win 0 T) :y (subvec win 1 (inc T))}))
                   (range B))
        r-rows (mapv (fn [b]
                       (let [r (Random. (+ (long seed) 7000 (long b)))]
                         (mapv (fn [_]
                                 (let [a (float-array (* H T))]
                                   (dotimes [i (* H T)] (aset a i (.nextFloat r)))
                                   a))
                               (range 24))))
                     (range B))]
    {:x-rows (mapv :x rows) :y-rows (mapv :y rows)
     :trunk-ids (vec trunk-ids) :R-rows r-rows}))

;; ── comparisons ──

(defn- grads-equal? [manifest resa resb]
  (let [^HashMap ga (:dense (:grads resa))
        ^HashMap gb (:dense (:grads resb))]
    (loop [i 0 bad nil]
      (if (or bad (= i 698))
        bad
        (let [nm (:name (nth (:dense manifest) i))
              ^floats a (.get ga nm)
              ^floats b (.get gb nm)]
          (recur (inc i)
                 (cond (and (nil? a) (nil? b)) nil
                       (or (nil? a) (nil? b)) (str nm " presence mismatch")
                       (java.util.Arrays/equals a b) nil
                       :else (str nm " grad bits differ"))))))))

(defn- sparse-equal? [label sa sb]
  (loop [i 0 bad nil]
    (if (or bad (= i (count sa)))
      bad
      (let [a (nth sa i) b (nth sb i)]
        (recur (inc i)
               (cond (and (nil? a) (nil? b)) nil
                     (or (nil? a) (nil? b)) (str label i " presence mismatch")
                     (not (java.util.Arrays/equals ^longs (:idx a) ^longs (:idx b)))
                     (str label i " idx differ")
                     (not (java.util.Arrays/equals ^floats (:val a) ^floats (:val b)))
                     (str label i " val bits differ")
                     :else nil))))))

(defn- post-dense-equal? [manifest densea denseb]
  (loop [i 0 bad nil]
    (if (or bad (= i 698))
      bad
      (let [nm (:name (nth (:dense manifest) i))
            ^floats a (:data (get (:by-name densea) nm))
            ^floats b (:data (get (:by-name denseb) nm))]
        (recur (inc i) (when-not (java.util.Arrays/equals a b)
                         (str nm " post-step bits differ")))))))

(defn- post-v-equal?
  "Read back every touched row (per the run's own sparse idx) through
   both runs' overlays; bit-compare."
  [label params-a params-b sgrads dim]
  (let [dim (long dim)
        ra (float-array dim) rb (float-array dim)]
    (loop [l 0 bad nil]
      (if (or bad (= l (count sgrads)))
        bad
        (recur (inc l)
               (when-let [g (nth sgrads l)]
                 (let [^longs idx (:idx g)
                       ba (:bank (nth params-a l))
                       bb (:bank (nth params-b l))]
                   (loop [k 0 bad2 nil]
                     (if (or bad2 (= k (alength idx)))
                       bad2
                       (do (p/bank-row! ba (aget idx k) ra 0)
                           (p/bank-row! bb (aget idx k) rb 0)
                           (recur (inc k)
                                  (when-not (java.util.Arrays/equals ra rb)
                                    (format "%s%d row %d bits differ"
                                            label l (aget idx k))))))))))))))

(defn- scalar-checks [tag resa resb]
  (doseq [k [:plain-ce :loss-total :kd :kd-kl :teacher-bpc :student-bpc]]
    (check-ok (str tag (name k))
              (= (k resa) (k resb))
              (format "%s vs %s" (k resa) (k resb))))
  (check-ok (str tag "z-layers")
            (java.util.Arrays/equals ^doubles (:z-layers resa)
                                     ^doubles (:z-layers resb))
            "per-layer z bits differ"))

;; ── grad tolerance leg (parallel vs sequential fp reassociation) ──

(defn- grad-rel-worst ^double [manifest resa resb]
  (let [^HashMap ga (:dense (:grads resa))
        ^HashMap gb (:dense (:grads resb))]
    (loop [i 0 mx 0.0]
      (if (= i 698)
        mx
        (let [nm (:name (nth (:dense manifest) i))
              ^floats a (.get ga nm)
              ^floats b (.get gb nm)]
          (recur (inc i)
                 (double
                  (cond (and (nil? a) (nil? b)) mx
                        (or (nil? a) (nil? b)) Double/POSITIVE_INFINITY
                        :else (let [na (norm2 a) nb (norm2 b)
                                    e (Math/abs (- na nb))]
                                (max mx (if (<= e 1e-9) 0.0
                                            (/ e (max nb 1e-12)))))))))))))

(defn- sparse-val-rel-worst ^double [sa sb dim]
  (let [dim (long dim)]
    (loop [i 0 mx 0.0]
      (if (= i (count sa))
        mx
        (let [a (nth sa i) b (nth sb i)]
          (if (or (nil? a) (nil? b)
                  (not (java.util.Arrays/equals ^longs (:idx a) ^longs (:idx b))))
            Double/POSITIVE_INFINITY
            (let [^floats va (:val a) ^floats vb (:val b)
                  nnz (quot (alength va) dim)
                  w (loop [r 0 m2 0.0]
                      (if (= r nnz)
                        m2
                        (let [na (double (loop [j 0 s 0.0]
                                           (if (< j dim)
                                             (let [v (double (aget va (+ (* r dim) j)))]
                                               (recur (inc j) (+ s (* v v))))
                                             (Math/sqrt s))))
                              nb (double (loop [j 0 s 0.0]
                                           (if (< j dim)
                                             (let [v (double (aget vb (+ (* r dim) j)))]
                                               (recur (inc j) (+ s (* v v))))
                                             (Math/sqrt s))))
                              e (Math/abs (- na nb))]
                          (recur (inc r) (double (max m2 (if (<= e 1e-10) 0.0
                                                             (/ e (max nb 1e-12)))))))))]
              (recur (inc i) (double (max mx (double w)))))))))))

(defn -main [& _]
  (let [manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        rope {:cos (:data (t/from-npy (get rope-z "cos")))
              :sin (:data (t/from-npy (get rope-z "sin")))}
        zmeta (npy/read-npz "jvm/goldens/step.npz")
        ;; mid-warmup prod lrs — the same ones step.npz pinned for s0
        lrs {:dense (d0 zmeta "s0_lr_dense") :kab (d0 zmeta "s0_lr_kab")
             :bank (d0 zmeta "s0_lr_bank") :net (d0 zmeta "s0_lr_net")}
        ;; ── (a) the 16-router deterministic step ──
        batch (synth-batch 16 32 (range 16) 20260704)
        cfg (assoc batch :kd? true :lrs lrs)
        ;; after each run, drop what no comparison needs (Adam moments;
        ;; the merged dv maps duplicated by :sparse-*) so three runs'
        ;; retained state fits the heap alongside the next run's peak
        trim (fn [env res]
               {:env (dissoc env :opt-states)
                :res (update res :grads select-keys [:dense])})
        run-par (fn [n-threads]
                  (let [env (fresh-env manifest rope zmeta)]
                    (ps/with-pool [pool n-threads]
                      (trim env (ps/parallel-train-step! env cfg pool)))))
        _ (println "── G6: 16-router step, 1 thread vs 16 threads (T=32, KD on) ──")
        t0 (System/nanoTime)
        {resa :res enva :env} (run-par 1)
        t1 (System/nanoTime)
        {resb :res envb :env} (run-par 16)
        t2 (System/nanoTime)]
    (println (format "   wall: 1-thread %.1fs, 16-thread %.1fs (box has %d cores)"
                     (/ (- t1 t0) 1e9) (/ (- t2 t1) 1e9)
                     (.availableProcessors (Runtime/getRuntime))))
    (check-ok "hogwild-local engaged" (and (:hogwild? resa) (:hogwild? resb))
              "expected distinct trunk-ids to take the lock-free V_local path")
    ;; guard against vacuous bit-equality (an empty-grads bug once passed
    ;; every ≡ check below because both sides compared nothing)
    (check-ok "parallel grads non-empty"
              (and (> (.size ^HashMap (:dense (:grads resa))) 600)
                   (every? some? (:sparse-local resa))
                   (every? some? (:sparse-net resa)))
              (format "dense=%d local-nil=%d net-nil=%d"
                      (.size ^HashMap (:dense (:grads resa)))
                      (count (remove some? (:sparse-local resa)))
                      (count (remove some? (:sparse-net resa)))))
    (scalar-checks "1t≡16t " resa resb)
    (check-ok "1t≡16t dense grads (698)" (nil? (grads-equal? manifest resa resb))
              (grads-equal? manifest resa resb))
    (check-ok "1t≡16t local sparse grads" (nil? (sparse-equal? "local" (:sparse-local resa) (:sparse-local resb)))
              (sparse-equal? "local" (:sparse-local resa) (:sparse-local resb)))
    (check-ok "1t≡16t net sparse grads" (nil? (sparse-equal? "net" (:sparse-net resa) (:sparse-net resb)))
              (sparse-equal? "net" (:sparse-net resa) (:sparse-net resb)))
    (check-ok "1t≡16t post-step dense (698)"
              (nil? (post-dense-equal? manifest (:dense enva) (:dense envb)))
              (post-dense-equal? manifest (:dense enva) (:dense envb)))
    (check-ok "1t≡16t post-step V_local rows"
              (nil? (post-v-equal? "local" (:local-params enva) (:local-params envb)
                                   (:sparse-local resa) 16))
              (post-v-equal? "local" (:local-params enva) (:local-params envb)
                             (:sparse-local resa) 16))
    (check-ok "1t≡16t post-step V_net rows"
              (nil? (post-v-equal? "net" (:net-params enva) (:net-params envb)
                                   (:sparse-net resa) 8))
              (post-v-equal? "net" (:net-params enva) (:net-params envb)
                             (:sparse-net resa) 8))
    ;; ── sanity leg: parallel vs the sequential reference path ──
    (println "── sanity: parallel(1t) vs sequential ts/train-step! ──")
    (let [{ress :res} (let [envs (fresh-env manifest rope zmeta)]
                        (trim envs (ts/train-step! envs cfg)))]
      (scalar-checks "par≡seq " resa ress)
      (check "par~seq dense grad norms" (grad-rel-worst manifest resa ress) 1e-5)
      (check-ok "par≡seq V_local grads (single-writer rows)"
                (nil? (sparse-equal? "local" (:sparse-local resa) (:sparse-local ress)))
                (sparse-equal? "local" (:sparse-local resa) (:sparse-local ress)))
      (check "par~seq V_net grad row norms"
             (sparse-val-rel-worst (:sparse-net resa) (:sparse-net ress) 8) 1e-5))
    ;; ── (a') duplicate-trunk fallback: per-task merge path ──
    (println "── duplicate-trunk fallback (B=4, trunk-ids [0 0 5 5], T=16) ──")
    (let [batch2 (synth-batch 4 16 [0 0 5 5] 20260705)
          cfg2 (assoc batch2 :kd? true :lrs lrs)
          run2 (fn [n-threads]
                 (let [env (fresh-env manifest rope zmeta)]
                   (ps/with-pool [pool n-threads]
                     (trim env (ps/parallel-train-step! env cfg2 pool)))))
          {r2a :res e2a :env} (run2 1)
          {r2b :res e2b :env} (run2 8)]
      (check-ok "fallback (non-hogwild) engaged"
                (and (not (:hogwild? r2a)) (not (:hogwild? r2b)))
                "expected duplicate trunk-ids to take the per-task merge path")
      (scalar-checks "dup 1t≡8t " r2a r2b)
      (check-ok "dup 1t≡8t dense grads" (nil? (grads-equal? manifest r2a r2b))
                (grads-equal? manifest r2a r2b))
      (check-ok "dup 1t≡8t local sparse grads"
                (nil? (sparse-equal? "local" (:sparse-local r2a) (:sparse-local r2b)))
                (sparse-equal? "local" (:sparse-local r2a) (:sparse-local r2b)))
      (check-ok "dup 1t≡8t net sparse grads"
                (nil? (sparse-equal? "net" (:sparse-net r2a) (:sparse-net r2b)))
                (sparse-equal? "net" (:sparse-net r2a) (:sparse-net r2b)))
      (check-ok "dup 1t≡8t post-step dense"
                (nil? (post-dense-equal? manifest (:dense e2a) (:dense e2b)))
                (post-dense-equal? manifest (:dense e2a) (:dense e2b))))
    (if (pos? @fails)
      (do (println @fails "FAILURES") (System/exit 1))
      (println "ALL THREAD PARITY CHECKS PASSED (gate G6)"))))
