(ns mmllm.jvm.spoon
  "M7 + gate G5: a real multi-step training round (a 'spoon') standalone
   on the JVM — parallel per-router train steps (M6) + prod LR schedule
   (M5a) + native byte batcher (data.clj) + end-of-round eval battery
   (evals.clj), with the G5 acceptance checks:

     (a) train loss fell materially from step 0
     (b) Δ_local > 0            (ablate Local V → eval bpc rises)
     (c) V_local moved% > 1% AND cos(V_cur, V_init) < 1
         — the 2026-05-13 CLAUDE.md lesson: Δ alone is a FALSE POSITIVE
           (gaussian-init V + trained K_a/K_b + trained gates give Δ>0
           with V untouched); the moved check is mandatory.

     Δ_net is reported but NOT gated: at 100 steps the wake phase
     (bank-lr-dominant, net-lr ≈ 0 until step ~70) dominates, so V_net
     consolidation is expected to be small (CLAUDE.md 'What to watch').

   The golden dense/banks are never mutated: dense params are a fresh
   in-RAM copy; banks are COPIED to a scratch dir and mmap'd there with
   direct writes (:writable? — no overlay, so bank state lives in file
   pages, not heap). V_init for the moved check = the pristine
   jvm/goldens/banks files.

   Model init = the goldens' seed-0 model (a fresh init, not a trained
   chain head): full-forward golden bpc is ~36 — i.e. step 0 starts from
   an untrained model, exactly what a genesis spoon trains from.

   Recipe: the sym24 prod recipe at 100 steps (§2 of the spec):
   LR 3e-3 (min 3e-3), warmup 70%, group mults dense .05→.005,
   kab .15→.001, bank 3.0→.001, net .001→5.0, KD logitkd temp 2 coef 1
   every 2, z 1e-5, LOCAL_MULT .05, 16 routers × B=1.

   Run: _JAVA_OPTIONS=-Xmx10g jvm/run.sh -m mmllm.jvm.spoon \\
          [steps=100] [T=256] [threads=4] [seed=20260704] [eval-cap=36864]"
  (:require [clojure.java.io :as io]
            [mmllm.jvm.data :as data]
            [mmllm.jvm.evals :as ev]
            [mmllm.jvm.model :as m]
            [mmllm.jvm.npy :as npy]
            [mmllm.jvm.parallel-step :as ps]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.schedule :as sched]
            [mmllm.jvm.tensor :as t]
            [mmllm.jvm.train-step :as ts])
  (:import [java.io File]
           [java.nio.file Files StandardCopyOption]
           [java.util Random]))

(set! *warn-on-reflection* true)

(defn- vm-kb
  "VmHWM / VmRSS from /proc/self/status, in kB (nil off-Linux).
   NB: plain slurp errors on procfs in some sandboxes (available0
   EINVAL) — readAllBytes doesn't."
  [k]
  (try
    (some->> (String. (Files/readAllBytes
                       (.toPath (io/file "/proc/self/status"))))
             (re-find (re-pattern (str k ":\\s+(\\d+) kB")))
             second
             Long/parseLong)
    (catch Exception _ nil)))

(defn- gb ^double [kb] (if kb (/ (double kb) 1048576.0) Double/NaN))

(defn- copy-banks!
  "Fresh scratch copies of every manifest bank (training mutates them)."
  [manifest src-dir dst-dir]
  (.mkdirs (io/file dst-dir))
  (doseq [{:keys [file]} (:sparse manifest)]
    (Files/copy (.toPath (io/file src-dir ^String file))
                (.toPath (io/file dst-dir ^String file))
                ^"[Ljava.nio.file.CopyOption;"
                (into-array java.nio.file.CopyOption
                            [StandardCopyOption/REPLACE_EXISTING]))))

(defn- build-env
  "Same env shape as the parity gates' fresh-env, but banks are the
   scratch copies opened :writable? (direct mmap writes, no overlay)."
  [manifest bank-dir]
  (let [dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks0 (p/load-banks manifest bank-dir)
        banks (into {} (for [[k v] banks0] [k (assoc v :writable? true)]))
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        model (m/build-model manifest dense banks
                             {:rope {:cos (:data (t/from-npy (get rope-z "cos")))
                                     :sin (:data (t/from-npy (get rope-z "sin")))}})
        sp-of (fn [kind layer]
                (some #(when (and (= (:kind %) kind) (= (:layer %) layer)) %)
                      (:sparse manifest)))
        mk-param (fn [s] {:bank (get banks (:name s))
                          :rows (first (:shape s)) :dim (second (:shape s))})]
    {:model model :manifest manifest :dense dense :banks banks
     :local-params (mapv #(mk-param (sp-of "local" %)) (range 24))
     :net-params (mapv #(mk-param (sp-of "net" %)) (range 32))
     :opt-states (ts/make-opt-states 24 32)
     :z-coef 1e-5 :kd-temp 2.0 :kd-coef 1.0
     :sqrt-local 128 :local-mult 0.05}))

(def ^:private recipe
  "sym24 prod recipe group mults (extend_chain.sh / spec §2), scaled to
   the round's step count by :total/:warmup at build time."
  {:lr 3e-3 :lr-min 3e-3
   :dense-mult 0.05 :dense-mult-end 0.005
   :kab-mult 0.15 :kab-mult-end 0.001
   :bank-mult 3.0 :bank-mult-end 0.001
   :net-mult 0.001 :net-mult-end 5.0})

(defn- run-evals
  "ctrl + ablated bpc over the held-out mix tail. Ablation zeroes the
   tier in the MODEL WIRING only (evals/ablate) — files untouched."
  [model val-data T eval-cap pool]
  (let [ctrl (ev/eval-bpc model val-data T 16 eval-cap pool)
        abl-l (ev/eval-bpc (ev/ablate model :local) val-data T 16 eval-cap pool)
        abl-n (ev/eval-bpc (ev/ablate model :net) val-data T 16 eval-cap pool)]
    {:ctrl (:bpc ctrl)
     :n-windows (:n-windows ctrl) :n-tokens (:n-tokens ctrl)
     :ablated-local (:bpc abl-l)
     :ablated-net (:bpc abl-n)
     :d-local (- (:bpc abl-l) (:bpc ctrl))
     :d-net (- (:bpc abl-n) (:bpc ctrl))}))

(defn- moved-pairs [manifest kind cur-dir init-dir]
  (for [s (:sparse manifest)
        :when (= (:kind s) kind)]
    [(io/file cur-dir ^String (:file s)) (io/file init-dir ^String (:file s))]))

(defn -main [& args]
  (let [[steps T threads seed eval-cap]
        (mapv (fn [d s] (if s (Long/parseLong s) d))
              [100 256 4 20260704 36864]
              (concat args (repeat nil)))
        scratch (or (System/getenv "MMLLM_JVM_SCRATCH") "/tmp/mmllm-jvm-spoon")
        bank-dir (str scratch "/banks")
        corpus-dir (str scratch "/corpora")
        init-dir "jvm/goldens/banks"
        t0 (System/nanoTime)
        _ (println (format "spoon: steps=%d T=%d threads=%d seed=%d eval-cap=%d B=16 (16 routers × 1)"
                           steps T threads seed eval-cap))
        manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        _ (println "▶ copying banks to scratch:" bank-dir)
        _ (copy-banks! manifest init-dir bank-dir)
        _ (println "▶ staging corpora:" corpus-dir)
        mix (data/stage! "workers/dispatcher/corpora" corpus-dir)
        _ (doseq [{:keys [name n]} (:corpora mix)]
            (println (format "    %-28s %11d bytes" name n)))
        ^bytes val-data (data/val-tail mix 4096)
        _ (println (format "  held-out mix tail: %d bytes (%d per corpus)"
                           (alength val-data) 4096))
        env (build-env manifest bank-dir)
        cfg (assoc recipe :total steps :warmup (long (* 0.7 steps)))
        losses (double-array steps)
        wall-train
        (ps/with-pool [pool threads]
          (let [tt0 (System/nanoTime)]
            (dotimes [step steps]
              (let [st0 (System/nanoTime)
                    rnd (Random. (unchecked-add (long seed)
                                                (unchecked-multiply (long step) 2654435761)))
                    batch (data/mix-batch-multi-trunk mix rnd 16 T)
                    rrows (data/r-rows seed step 16 T)
                    lrs (sched/lrs-at-step cfg step)
                    kd? (zero? (rem step 2))
                    res (ps/parallel-train-step!
                         env {:kd? kd?
                              :lrs {:dense (:dense lrs) :kab (:kab lrs)
                                    :bank (:bank lrs) :net (:net lrs)}
                              :x-rows (:x-rows batch) :y-rows (:y-rows batch)
                              :trunk-ids (:trunk-ids batch) :R-rows rrows}
                         pool)
                    dt (/ (- (System/nanoTime) st0) 1e9)]
                (when-not (Double/isFinite (double (:loss-total res)))
                  (println "FATAL: non-finite loss at step" step (:loss-total res))
                  (System/exit 2))
                (aset losses step (double (:plain-ce res)))
                (println
                 (format "step %3d/%d  loss %.4f  ce %.4f  kd %s  t/s_bpc %s  corpus %-14s lr_d %.2e lr_b %.2e lr_n %.2e  %5.1fs%s"
                         (inc step) steps
                         (:loss-total res) (:plain-ce res)
                         (if kd? (format "%.4f" (:kd res)) "  -  ")
                         (if kd? (format "%.3f/%.3f" (:teacher-bpc res) (:student-bpc res)) "  -  ")
                         (:name (nth (:corpora mix) (:corpus-idx batch)))
                         (:dense lrs) (:bank lrs) (:net lrs) dt
                         (if (zero? (rem (inc step) 10))
                           (format "  [rss %.1f GB]" (gb (vm-kb "VmRSS")))
                           "")))
                (flush)))
            (/ (- (System/nanoTime) tt0) 1e9)))
        ;; flush mapped bank writes before the file-vs-file moved check
        _ (doseq [[_ b] (:banks env)]
            (.force ^java.nio.MappedByteBuffer (:mbb b)))
        _ (println (format "▶ training done in %.1fs — running end-of-round evals" wall-train))
        ev0 (System/nanoTime)
        evals (ps/with-pool [pool threads]
                (run-evals (:model env) val-data T eval-cap pool))
        wall-eval (/ (- (System/nanoTime) ev0) 1e9)
        _ (println (format "  eval: %d windows × T=%d (%d tokens), trunk round-robin N=16, %.1fs/pass avg"
                           (:n-windows evals) T (:n-tokens evals) (/ wall-eval 3.0)))
        mv0 (System/nanoTime)
        moved-local (ev/v-moved (moved-pairs manifest "local" bank-dir init-dir))
        moved-net (ev/v-moved (moved-pairs manifest "net" bank-dir init-dir))
        wall-moved (/ (- (System/nanoTime) mv0) 1e9)
        wall-total (/ (- (System/nanoTime) t0) 1e9)
        hwm (gb (vm-kb "VmHWM"))
        ce0 (aget losses 0)
        ce-end (/ (reduce + (map #(aget losses (- steps 1 (long %))) (range (min 5 steps))))
                  (min 5 steps))
        ;; ── gate G5 ──
        a-ok? (< ce-end (* 0.7 ce0))
        b-ok? (pos? (double (:d-local evals)))
        c-ok? (and (> (double (:moved-pct moved-local)) 1.0)
                   (< (double (:cos moved-local)) 1.0))]
    (println)
    (println "── spoon summary ─────────────────────────────────────────")
    (println (format "  train CE        step0 %.4f → last-5-mean %.4f  (%.1f%% of step0)"
                     ce0 ce-end (* 100.0 (/ ce-end ce0))))
    (println (format "  ctrl bpc        %.4f   (over %d tokens held-out mix tail)"
                     (:ctrl evals) (:n-tokens evals)))
    (println (format "  Δ_local         %+.4f   (ablated %.4f)"
                     (:d-local evals) (:ablated-local evals)))
    (println (format "  Δ_net           %+.4f   (ablated %.4f)  [reported, not gated at 100 steps]"
                     (:d-net evals) (:ablated-net evals)))
    (println (format "  V_local moved%%  %.2f%%   cos %.6f" (:moved-pct moved-local) (:cos moved-local)))
    (println (format "  V_net   moved%%  %.2f%%   cos %.6f" (:moved-pct moved-net) (:cos moved-net)))
    (println (format "  wall            train %.1fs + eval %.1fs + moved %.1fs = %.1fs total"
                     wall-train wall-eval wall-moved wall-total))
    (println (format "  peak RSS        %.1f GB (VmHWM)" hwm))
    (println "── gate G5 ───────────────────────────────────────────────")
    (println (format "  (a) loss fell materially (last5 < 0.7·step0)  %s" (if a-ok? "OK" "FAIL")))
    (println (format "  (b) Δ_local > 0                               %s" (if b-ok? "OK" "FAIL")))
    (println (format "  (c) V_local moved%% > 1%% AND cos < 1           %s" (if c-ok? "OK" "FAIL")))
    (if (and a-ok? b-ok? c-ok?)
      (do (println "GATE G5 PASSED") (System/exit 0))
      (do (println "GATE G5 FAILED") (System/exit 1)))))
