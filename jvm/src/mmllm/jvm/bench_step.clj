(ns mmllm.jvm.bench-step
  "M6 benchmark (docs/jvm-port-spec.md §10): steps/s of the full
   16-router sym24 train step vs thread count, on the golden model.

   Usage:
     _JAVA_OPTIONS=-Xmx10g jvm/run.sh -m mmllm.jvm.bench-step \\
        [T] [n-steps] [thread-count ...]
   Defaults: T=256, n-steps=4, threads = seq 1 2 4 ... up to nproc
   (\"seq\" as a thread-count benches the sequential ts/train-step!
   reference path instead of the 1-thread pool).

   Per config: FRESH env (dense + overlays reload — every config does
   identical work), steps alternate KD on/off (KD_EVERY=2, like prod:
   even step index fires KD = 2 extra forwards + 1 extra backward).
   Reported per config: per-step walls, kd / non-kd medians, and overall
   steps/s (n-steps / total wall). Results are written as a table to
   stdout; docs/jvm-port-bench.md holds the curated numbers + caveats."
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]
            [mmllm.jvm.model :as m]
            [mmllm.jvm.train-step :as ts]
            [mmllm.jvm.parallel-step :as ps])
  (:import [java.util HashMap Random]))

(set! *warn-on-reflection* true)

(defn- d0 ^double [z k] (let [d (:data (get z k))]
                          (if (instance? (Class/forName "[D") d)
                            (aget ^doubles d 0)
                            (double (aget ^floats d 0)))))

(defn- l0 ^long [z k] (aget ^longs (:data (get z k)) 0))

(defn- fresh-env [manifest rope zmeta]
  (let [dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks0 (p/load-banks manifest "jvm/goldens/banks")
        banks (into {} (for [[k v] banks0] [k (assoc v :overlay (HashMap.))]))
        model (m/build-model manifest dense banks {:rope rope})
        sp-of (fn [kind layer]
                (some #(when (and (= (:kind %) kind) (= (:layer %) layer)) %)
                      (:sparse manifest)))
        mk-param (fn [s] {:bank (get banks (:name s))
                          :rows (first (:shape s)) :dim (second (:shape s))})]
    {:model model :manifest manifest :dense dense
     :local-params (mapv #(mk-param (sp-of "local" %)) (range 24))
     :net-params (mapv #(mk-param (sp-of "net" %)) (range 32))
     :opt-states (ts/make-opt-states 24 32)
     :z-coef (d0 zmeta "z_coef") :kd-temp (d0 zmeta "kd_temp")
     :kd-coef (d0 zmeta "kd_coef")
     :sqrt-local (l0 zmeta "sqrt_local") :local-mult (d0 zmeta "local_mult")}))

(defn- synth-batch [B T seed]
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
     :trunk-ids (vec (map #(rem (long %) 16) (range B))) :R-rows r-rows}))

(defn- median ^double [xs]
  (let [v (vec (sort xs)) n (count v)]
    (cond (zero? n) Double/NaN
          (odd? n) (double (nth v (quot n 2)))
          :else (/ (+ (double (nth v (dec (quot n 2))))
                      (double (nth v (quot n 2)))) 2.0))))

(defn- run-config
  "Run n-steps on a fresh env; step-fn: (fn [cfg]) -> result. Returns
   {:times [[secs kd?] ...] :total secs}."
  [label env batch lrs n-steps step-fn]
  (println (format "── %s ──" label))
  (let [times
        (vec
         (for [i (range n-steps)]
           (let [kd? (even? (long i))
                 cfg (assoc batch :kd? kd? :lrs lrs)
                 t0 (System/nanoTime)
                 _ (step-fn env cfg)
                 dt (/ (- (System/nanoTime) t0) 1e9)]
             (println (format "   step %d kd=%-5s %.2fs" i kd? dt))
             [dt kd?])))
        total (reduce + (map first times))]
    (println (format "   %s: total %.1fs, %.4f steps/s, median kd %.2fs / non-kd %.2fs"
                     label total (/ (double n-steps) total)
                     (median (map first (filter second times)))
                     (median (map first (remove second times)))))
    {:times times :total total}))

(defn -main [& args]
  (let [T (if (seq args) (Long/parseLong (first args)) 256)
        n-steps (if (second args) (Long/parseLong (second args)) 4)
        nproc (.availableProcessors (Runtime/getRuntime))
        configs (if (seq (drop 2 args))
                  (vec (drop 2 args))
                  (mapv str (concat ["seq"] (take-while #(<= (long %) nproc)
                                                        (iterate #(* 2 (long %)) 1)))))
        manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        rope {:cos (:data (t/from-npy (get rope-z "cos")))
              :sin (:data (t/from-npy (get rope-z "sin")))}
        zmeta (npy/read-npz "jvm/goldens/step.npz")
        lrs {:dense (d0 zmeta "s0_lr_dense") :kab (d0 zmeta "s0_lr_kab")
             :bank (d0 zmeta "s0_lr_bank") :net (d0 zmeta "s0_lr_net")}
        batch (synth-batch 16 T 20260704)]
    (println (format "bench: B=16 routers, T=%d, %d steps/config (KD every 2), %d cores, Xmx=%dM"
                     T n-steps nproc
                     (quot (.maxMemory (Runtime/getRuntime)) (* 1024 1024))))
    ;; JIT warmup — small T, untimed, exercises parallel + sequential paths
    (println "── JIT warmup (T=32, untimed) ──")
    (let [wb (synth-batch 16 32 1)
          wenv (fresh-env manifest rope zmeta)]
      (ps/with-pool [pool nproc]
        (ps/parallel-train-step! wenv (assoc wb :kd? true :lrs lrs) pool))
      (ts/train-step! wenv (assoc wb :kd? true :lrs lrs)))
    (let [results
          (vec
           (for [c configs]
             (let [env (fresh-env manifest rope zmeta)]
               [c (if (= c "seq")
                    (run-config "sequential ts/train-step!" env batch lrs n-steps
                                (fn [env cfg] (ts/train-step! env cfg)))
                    (let [n (Long/parseLong c)]
                      (ps/with-pool [pool n]
                        (run-config (str "parallel, " n " thread(s)") env batch lrs n-steps
                                    (fn [env cfg] (ps/parallel-train-step! env cfg pool))))))])))
          base (some (fn [[c r]] (when (= c "1") (:total r))) results)]
      (println "\n== summary ==")
      (println (format "%-14s %10s %10s %10s" "config" "total(s)" "steps/s" "speedup"))
      (doseq [[c r] results]
        (println (format "%-14s %10.1f %10.4f %10s"
                         c (:total r) (/ (double n-steps) (:total r))
                         (if base (format "%.2fx" (/ (double base) (:total r))) "-")))))))
