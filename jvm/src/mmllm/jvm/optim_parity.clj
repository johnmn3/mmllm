(ns mmllm.jvm.optim-parity
  "M5a parity (the optimizer-delta half of gate G4, docs/jvm-port-spec.md):

   - schedule.npz : per-step (base, dense, kab, bank, net) lr table vs
     core.lpy lr-at-step + pick-lr-*-mult, rel tol 1e-9 (f64 both sides),
     prod recipe AND the ROUND_BASE/RAMP_FLOOR chain-resume variant;
   - adamw.npz : 5-step param trajectory vs torch.optim.AdamW exactly as
     make-opt-dense builds it, abs tol 1e-6 after every step;
   - sparse_adam.npz : 5-step trajectories vs optim.py CPUOffloadSparseAdam
     (touched-row buffers, per-param step counter, coalesce, LOCAL_MULT +
     LAYER_MULTS tiling incl. the grad-less-param counter skip), abs 1e-6.

   Goldens regenerate with: .venv/bin/python scripts/dump_goldens.py --optim
   Exits nonzero on any failure. Run: jvm/run.sh -m mmllm.jvm.optim-parity"
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.optim :as o]
            [mmllm.jvm.schedule :as sched]))

(set! *warn-on-reflection* true)

(def ^:private fails (atom 0))

(defn- check [name ^double err ^double tol]
  (println (format "%-26s err %.3e  tol %.0e  %s"
                   name err tol (if (<= err tol) "OK" "FAIL")))
  (when (> err tol) (swap! fails inc)))

(defn- f64 ^doubles [z k] (:data (get z k)))
(defn- f32 ^floats [z k] (:data (get z k)))
(defn- d0 ^double [z k] (aget ^doubles (:data (get z k)) 0))
(defn- l0 ^long [z k] (aget ^longs (:data (get z k)) 0))

(defn- rel-err-f64
  "elementwise |got-want| / max(|want|, 1e-12), max over the array."
  ^double [^doubles got ^doubles want]
  (assert (= (alength got) (alength want)))
  (loop [i 0 mv 0.0]
    (if (< i (alength got))
      (let [w (aget want i)
            d (Math/abs (- (aget got i) w))]
        (recur (inc i) (max mv (/ d (max 1e-12 (Math/abs w))))))
      mv)))

(defn- abs-err-f32 ^double [^floats got ^floats want]
  (assert (= (alength got) (alength want)))
  (loop [i 0 mv 0.0]
    (if (< i (alength got))
      (recur (inc i) (max mv (Math/abs (- (double (aget got i))
                                          (double (aget want i))))))
      mv)))

(defn- slice ^floats [^floats a ^long off ^long n]
  (java.util.Arrays/copyOfRange a off (+ off n)))

;; ── schedule ──

(defn- check-schedule [z prefix cfg]
  (let [total (long (:total cfg))
        base  (double-array total)]
    (dotimes [s total] (aset base s (sched/lr-at-step cfg s)))
    (check (str prefix "base") (rel-err-f64 base (f64 z (str prefix "base"))) 1e-9)
    (doseq [g [:dense :kab :bank :net]]
      (let [got (double-array total)]
        (dotimes [s total]
          (aset got s (* (aget base s) (sched/group-mult cfg g s))))
        (check (str prefix (name g))
               (rel-err-f64 got (f64 z (str prefix (name g)))) 1e-9)))))

;; ── sparse adam ──

(defn- run-sparse-variant
  "Replay one sparse_adam.npz variant (prefix a/b/c, n-params params of
   n-rows×dim) through mmllm.jvm.optim and check the param after every
   step against the golden."
  [z prefix n-params dim opts]
  (let [params (mapv (fn [j]
                       (let [^floats init (f32 z (str prefix "_p" j "_init"))
                             data (java.util.Arrays/copyOf init (alength init))]
                         {:data data :rows (quot (alength init) (long dim)) :dim dim}))
                     (range n-params))
        states (mapv (fn [_] (o/sparse-adam-init)) (range n-params))]
    (dotimes [s 5]
      (let [grads (mapv (fn [j]
                          (when-let [idx (get z (str prefix "_g" s "_p" j "_idx"))]
                            {:idx (:data idx)
                             :val (f32 z (str prefix "_g" s "_p" j "_val"))}))
                        (range n-params))]
        (o/sparse-adam-step! states params grads opts)
        (dotimes [j n-params]
          (check (str prefix "/p" j " step" s)
                 (abs-err-f32 (:data (nth params j))
                              (f32 z (str prefix "_p" j "_step" s)))
                 1e-6))))))

(defn -main [& _]
  ;; ── schedule table, prod recipe (rel 1e-9) ──
  (let [z (npy/read-npz "jvm/goldens/schedule.npz")
        cfg {:lr (d0 z "lr") :lr-min (d0 z "lr_min")
             :total (l0 z "total") :warmup (l0 z "warmup")
             :dense-mult (d0 z "dense_start") :dense-mult-end (d0 z "dense_end")
             :kab-mult (d0 z "kab_start")     :kab-mult-end (d0 z "kab_end")
             :bank-mult (d0 z "bank_start")   :bank-mult-end (d0 z "bank_end")
             :net-mult (d0 z "net_start")     :net-mult-end (d0 z "net_end")}]
    (check-schedule z "" cfg)
    ;; chain-round resume: ROUND_BASE=40, RAMP_FLOOR=0.1, warmup=68
    (check-schedule z "rb_" (assoc cfg
                                   :warmup (l0 z "rb_warmup")
                                   :round-base (l0 z "rb_round_base")
                                   :ramp-floor (d0 z "rb_ramp_floor"))))

  ;; ── AdamW 5-step trajectory (abs 1e-6 per step) ──
  (let [z (npy/read-npz "jvm/goldens/adamw.npz")
        ^floats p (let [^floats init (f32 z "p_init")]
                    (java.util.Arrays/copyOf init (alength init)))
        ^floats grads (f32 z "grads")
        ^floats steps-gold (f32 z "p_steps")
        n (alength p)
        state (o/adamw-init n)
        opts {:lr (d0 z "lr") :beta1 (d0 z "beta1") :beta2 (d0 z "beta2")
              :eps (d0 z "eps") :weight-decay (d0 z "weight_decay")}]
    (dotimes [s 5]
      (o/adamw-step! state p (slice grads (* s n) n) opts)
      (check (str "adamw/step" s)
             (abs-err-f32 p (slice steps-gold (* s n) n)) 1e-6)))

  ;; ── CPUOffloadSparseAdam trajectories (abs 1e-6 per step) ──
  (let [z (npy/read-npz "jvm/goldens/sparse_adam.npz")
        base {:lr (d0 z "lr") :beta1 (d0 z "beta1") :beta2 (d0 z "beta2")
              :eps (d0 z "eps") :local-mult (d0 z "local_mult")}]
    ;; (a) non-V_local at prod sqrt_local=128 -> layer mult 1.0
    (run-sparse-variant z "a" 1 4 (assoc base :sqrt-local (l0 z "a_sqrt_local")))
    ;; (b) V_local-shaped (3 trunks of 4²) -> LOCAL_MULT 0.05
    (run-sparse-variant z "b" 1 4 (assoc base :sqrt-local (l0 z "b_sqrt_local")))
    ;; (c) 3 V_local params + LAYER_MULTS tiling + grad-less steps
    (run-sparse-variant z "c" 3 4 (assoc base
                                         :sqrt-local (l0 z "c_sqrt_local")
                                         :layer-mults (vec (f64 z "c_layer_mults")))))

  (if (pos? @fails)
    (do (println @fails "FAILURES") (System/exit 1))
    (println "ALL OPTIM PARITY CHECKS PASSED")))
