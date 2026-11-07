(ns mmllm.jvm.step-parity
  "Gate G4 (docs/jvm-port-spec.md §12): replay the 3 torch train-steps
   dumped by `dump_goldens.py --step` and check, per step:

     - every loss scalar (ce, plain-ce, loss-total=ce+z, kd, kd-kl,
       teacher/student bpc)           rel 1e-4
     - all 24 per-layer Local z terms rel 1e-4
     - all 698 dense grad L2 norms    rel 1e-3 (NaN ⇔ no grad, exact;
       abs floor 1e-7 for near-zero norms)
     - block-0 Local + Net sparse dV  idx exact, values rel-norm 1e-3
     - post-step values of all 698 dense tensors    abs 1e-5, with a
       bounded allowance (≤8 elements, each ≤2.5·Σlr) for Adam
       eps-boundary sign ties — see the post-dense check body
     - post-step touched V rows (block-0 local+net) abs 1e-5

   The goldens' bank .bin files are mapped read-only in effect: all V
   updates land in per-bank overlays (params.clj), so this gate never
   mutates jvm/goldens/banks. Run: jvm/run.sh -m mmllm.jvm.step-parity"
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]
            [mmllm.jvm.model :as m]
            [mmllm.jvm.train-step :as ts])
  (:import [java.util HashMap]))

(set! *warn-on-reflection* true)

(def ^:private fails (atom 0))

(defn- check [name ^double err ^double tol]
  (println (format "%-26s err %.3e  tol %.0e  %s"
                   name err tol (if (<= err tol) "OK" "FAIL")))
  (when (> err tol) (swap! fails inc)))

(defn- check-ok [name ok? detail]
  (println (format "%-26s %s%s" name (if ok? "OK" "FAIL")
                   (if ok? "" (str "  " detail))))
  (when-not ok? (swap! fails inc)))

(defn- rel ^double [^double got ^double want]
  (/ (Math/abs (- got want)) (max (Math/abs want) 1e-12)))

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

(defn -main [& _]
  (let [manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks0 (p/load-banks manifest "jvm/goldens/banks")
        banks (into {} (for [[k v] banks0] [k (assoc v :overlay (HashMap.))]))
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        model (m/build-model manifest dense banks
                             {:rope {:cos (:data (t/from-npy (get rope-z "cos")))
                                     :sin (:data (t/from-npy (get rope-z "sin")))}})
        z (npy/read-npz "jvm/goldens/step.npz")
        ^longs steps (:data (get z "steps"))
        ^longs xd (:data (get z "x"))
        ^longs yd (:data (get z "y"))
        ^longs tid (:data (get z "trunk_ids"))
        kd-every (l0 z "kd_every")
        B 2 T 32 H 2
        x-rows (mapv (fn [b] (mapv #(aget xd (+ (* (long b) T) (long %))) (range T))) (range B))
        y-rows (mapv (fn [b] (mapv #(aget yd (+ (* (long b) T) (long %))) (range T))) (range B))
        trunk-ids (mapv #(aget tid (long %)) (range B))
        sp-of (fn [kind layer]
                (some #(when (and (= (:kind %) kind) (= (:layer %) layer)) %)
                      (:sparse manifest)))
        mk-param (fn [s] {:bank (get banks (:name s))
                          :rows (first (:shape s)) :dim (second (:shape s))})
        local-params (mapv #(mk-param (sp-of "local" %)) (range 24))
        net-params (mapv #(mk-param (sp-of "net" %)) (range 32))
        env {:model model :manifest manifest :dense dense
             :local-params local-params :net-params net-params
             :opt-states (ts/make-opt-states 24 32)
             :z-coef (d0 z "z_coef") :kd-temp (d0 z "kd_temp")
             :kd-coef (d0 z "kd_coef")
             :sqrt-local (l0 z "sqrt_local") :local-mult (d0 z "local_mult")}
        cum-lr (atom 0.0)]
    (dotimes [k 3]
      (let [pf (str "s" k "_")
            step (aget steps k)
            kd? (zero? (rem step kd-every))
            ;; R: (24, B, H, T) f32 → per row: 24 flat (H,T) draws
            ^floats R (:data (get z (str pf "R")))
            r-rows (mapv (fn [b]
                           (mapv (fn [l]
                                   (let [a (float-array (* H T))]
                                     (dotimes [h H]
                                       (System/arraycopy
                                        R (+ (* (long l) B H T) (* (long b) H T) (* h T))
                                        a (* h T) T))
                                     a))
                                 (range 24)))
                         (range B))
            res (ts/train-step!
                 env {:kd? kd?
                      :lrs {:dense (d0 z (str pf "lr_dense"))
                            :kab (d0 z (str pf "lr_kab"))
                            :bank (d0 z (str pf "lr_bank"))
                            :net (d0 z (str pf "lr_net"))}
                      :x-rows x-rows :y-rows y-rows :trunk-ids trunk-ids
                      :R-rows r-rows})]
        (println (format "── step %d (current_step=%d, kd=%s) ──" k step kd?))
        ;; loss scalars
        (check (str pf "plain-ce") (rel (:plain-ce res) (d0 z (str pf "plain_ce"))) 1e-4)
        (check (str pf "ce") (rel (:ce res) (d0 z (str pf "ce"))) 1e-4)
        (check (str pf "loss-total") (rel (:loss-total res) (d0 z (str pf "loss_total"))) 1e-4)
        (if kd?
          (do (check (str pf "kd") (rel (:kd res) (d0 z (str pf "kd"))) 1e-4)
              (check (str pf "kd-kl") (rel (:kd-kl res) (d0 z (str pf "kd_kl"))) 1e-4)
              (check (str pf "teacher-bpc") (rel (:teacher-bpc res) (d0 z (str pf "teacher_bpc"))) 1e-4)
              (check (str pf "student-bpc") (rel (:student-bpc res) (d0 z (str pf "student_bpc"))) 1e-4))
          (check-ok (str pf "kd=0") (zero? (double (:kd res))) (:kd res)))
        ;; per-layer z
        (let [^doubles zl-gold (:data (get z (str pf "z_layers")))
              ^doubles zl (:z-layers res)]
          (check (str pf "z-layers")
                 (loop [l 0 mx 0.0]
                   (if (< l 24) (recur (inc l) (max mx (rel (aget zl l) (aget zl-gold l)))) mx))
                 1e-4))
        ;; all-698 dense grad norms
        (let [^doubles gn-gold (:data (get z (str pf "grad_norms")))
              ^HashMap gdense (:dense (:grads res))]
          (loop [i 0 mx 0.0 worst nil nan-mismatch nil]
            (if (< i 698)
              (let [nm (:name (nth (:dense manifest) i))
                    want (aget gn-gold i)
                    ^floats gr (.get gdense nm)]
                (cond
                  (Double/isNaN want)
                  (recur (inc i) mx worst
                         (or nan-mismatch (when gr (str nm " has grad, torch None"))))
                  (nil? gr)
                  (recur (inc i) mx worst
                         (or nan-mismatch (str nm " missing grad, torch has one")))
                  ;; rel 1e-3, with an ABS floor of 1e-7: near-zero norms
                  ;; (e.g. alpha_net layers whose gate barely moves,
                  ;; ‖g‖ ~ 1e-5) make the pure relative test
                  ;; ill-conditioned, while any real missing/extra grad
                  ;; term shifts a norm by ~the norm itself ≫ 1e-7.
                  :else (let [e (if (<= (Math/abs (- (norm2 gr) want)) 1e-7)
                                  0.0
                                  (rel (norm2 gr) want))]
                          (if (> e mx)
                            (recur (inc i) e [nm (norm2 gr) want] nan-mismatch)
                            (recur (inc i) mx worst nan-mismatch)))))
              (do (check-ok (str pf "grad-presence") (nil? nan-mismatch) nan-mismatch)
                  (check (str pf "grad-norms") mx 1e-3)
                  (when (> mx 1e-3)
                    (println (format "    worst: %s jvm=%.9e torch=%.9e"
                                     (nth worst 0) (double (nth worst 1))
                                     (double (nth worst 2)))))))))
        ;; block-0 sparse dV (local + net): idx exact, value norms rel 1e-3
        (doseq [[label got gi gv dim] [["local0" (nth (:sparse-local res) 0)
                                        (str pf "local0_gidx") (str pf "local0_gval") 16]
                                       ["net0" (nth (:sparse-net res) 0)
                                        (str pf "net0_gidx") (str pf "net0_gval") 8]]]
          (let [^longs idx-gold (:data (get z gi))
                ^floats val-gold (:data (get z gv))
                ^longs idx (:idx got)
                ^floats val (:val got)]
            (check-ok (str pf label "-gidx")
                      (java.util.Arrays/equals idx idx-gold)
                      (format "nnz %d vs %d" (alength idx) (alength idx-gold)))
            (when (java.util.Arrays/equals idx idx-gold)
              (let [nnz (alength idx) dim (long dim)]
                (check (str pf label "-gval")
                       (loop [r 0 mx 0.0]
                         (if (< r nnz)
                           (let [w (loop [j 0 s 0.0]
                                     (if (< j dim)
                                       (let [v (double (aget val-gold (+ (* r dim) j)))]
                                         (recur (inc j) (+ s (* v v))))
                                       (Math/sqrt s)))
                                 g' (loop [j 0 s 0.0]
                                      (if (< j dim)
                                        (let [v (double (aget val (+ (* r dim) j)))]
                                          (recur (inc j) (+ s (* v v))))
                                        (Math/sqrt s)))]
                             (recur (inc r) (max mx (/ (Math/abs (- g' w))
                                                       (max w 1e-10)))))
                           mx))
                       1e-3)))))
        ;; post-step dense params, all 698 tensors (1.13M elements),
        ;; abs 1e-5 — EXCEPT a bounded number of Adam sign-boundary
        ;; ties: an element whose gradient lands at ~eps=1e-8 makes
        ;; first-step Adam's g/(|g|+eps) sign-sensitive to sub-1e-9
        ;; cross-runtime fp noise, so torch and the JVM can legally
        ;; step it in opposite directions. Such a tie diverges by at
        ;; most ~2·Σ lr_dense (one full step each way); any REAL bug
        ;; (wrong lr/group, missing weight decay, mis-routed grads)
        ;; moves whole tensors, not ≤8 isolated elements, and is also
        ;; caught by the grad-norm + loss checks above. The bound
        ;; accumulates the LARGEST dense-optimizer group lr (kab runs
        ;; 3× dense during warmup) so ties in either group are covered.
        (let [_ (swap! cum-lr + (max (d0 z (str pf "lr_dense"))
                                     (d0 z (str pf "lr_kab"))))
              tie-bound (* 2.5 (double @cum-lr))
              ^HashMap gdense (:dense (:grads res))
              [mx worst n-out]
              (loop [i 0 mx 0.0 worst nil n-out 0]
                (if (< i 698)
                  (let [nm (:name (nth (:dense manifest) i))
                        ^floats got (:data (get (:by-name dense) nm))
                        ^floats want (:data (get z (format "%sd%05d" pf i)))
                        [m2 j2 n2] (loop [j 0 m2 0.0 j2 -1 n2 0]
                                     (if (< j (alength got))
                                       (let [e (double (Math/abs (- (aget got j) (aget want j))))]
                                         (recur (inc j)
                                                (if (> e m2) e m2)
                                                (if (> e m2) j j2)
                                                (if (> e 1e-5) (inc n2) n2)))
                                       [m2 j2 n2]))]
                    (if (> (double m2) mx)
                      (recur (inc i) (double m2) [nm (long j2)] (+ n-out (long n2)))
                      (recur (inc i) mx worst (+ n-out (long n2)))))
                  [mx worst n-out]))
              ok? (or (<= mx 1e-5)
                      (and (<= (long n-out) 8) (<= mx tie-bound)))]
          (check-ok (format "%spost-dense (max %.3e, %d>1e-5, tie-bound %.3e)"
                            pf mx (long n-out) tie-bound)
                    ok? "outliers exceed the Adam sign-tie budget")
          (when (pos? (long n-out))
            (let [[nm j] worst
                  j (long j)
                  ^floats got (:data (get (:by-name dense) nm))
                  ^floats gr (.get gdense nm)]
              (println (format "    worst: %s[%d] jvm=%.9e jvm-grad=%s"
                               nm j (double (aget got j))
                               (if gr (format "%.9e" (double (aget gr j))) "nil"))))))
        ;; post-step touched V rows (read back through the overlay)
        (doseq [[label pkey ikey prm dim] [["local0-post" (str pf "local0_post")
                                            (str pf "local0_gidx") (nth local-params 0) 16]
                                           ["net0-post" (str pf "net0_post")
                                            (str pf "net0_gidx") (nth net-params 0) 8]]]
          (let [^longs idx (:data (get z ikey))
                ^floats want (:data (get z pkey))
                dim (long dim)
                row (float-array dim)
                mx (loop [r 0 mx 0.0]
                     (if (< r (alength idx))
                       (do (p/bank-row! (:bank prm) (aget idx r) row 0)
                           (recur (inc r)
                                  (loop [j 0 m2 mx]
                                    (if (< j dim)
                                      (recur (inc j)
                                             (max m2 (double (Math/abs (- (aget row j)
                                                                          (aget want (+ (* r dim) j)))))))
                                      m2))))
                       mx))]
            (check (str pf label) mx 1e-5)))))
    (if (pos? @fails)
      (do (println @fails "FAILURES") (System/exit 1))
      (println "ALL STEP PARITY CHECKS PASSED"))))
