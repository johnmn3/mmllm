(ns mmllm.jvm.parity
  "Forward parity vs jvm/goldens (gates G1 module-fwd + G3 full-fwd of
   docs/jvm-port-spec.md §12). Run: jvm/run.sh -m mmllm.jvm.parity"
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]
            [mmllm.jvm.model :as m]))

(def ^:dynamic *fail* (atom 0))

(defn- check [name ^double err ^double tol]
  (println (format "%-14s max-abs-err %.3e  tol %.0e  %s"
                   name err tol (if (<= err tol) "OK" "FAIL")))
  (when (> err tol) (swap! *fail* inc)))

(defn -main [& _]
  (let [manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks (p/load-banks manifest "jvm/goldens/banks")
        rope-z (npy/read-npz "jvm/goldens/rope.npz")
        model (m/build-model manifest dense banks
                             {:rope {:cos (:data (t/from-npy (get rope-z "cos")))
                                     :sin (:data (t/from-npy (get rope-z "sin")))}})
        b0 (first (:blocks model))]

    ;; rope: recomputed cache vs torch's + apply_rope golden
    (let [{:strs [q y cos]} rope-z
          rope (:rope model)
          gold-cos (t/from-npy cos)
          recompute-err (t/max-abs-diff
                         (t/tensor [(* 8192 8)] (:cos (m/build-rope 8192 8 500000.0)))
                         (t/reshape gold-cos [(* 8192 8)]))
          qt (t/from-npy q)          ; (1,2,5,8), pos offset 3
          ^floats qd (t/data (t/copy qt))]
      ;; fallback recompute is allowed ~5e-5 (libm ulps at pos≈8k); exact
      ;; runs use the exported cache, which the model above loads.
      (check "rope-fallback" recompute-err 5e-5)
      (dotimes [h 2]
        (dotimes [ti 5]
          (m/rope-at! qd (+ (* h 40) (* ti 8)) rope (+ ti 3) 8)))
      (check "rope-apply" (t/max-abs-diff (t/tensor (:shape qt) qd) (t/from-npy y)) 1e-5))

    ;; sdpa causal (1,2,16,8)
    (let [{:strs [q k v y]} (npy/read-npz "jvm/goldens/sdpa.npz")
          ^floats qd (t/data (t/from-npy q))
          ^floats kd (t/data (t/from-npy k))
          ^floats vd (t/data (t/from-npy v))
          out (float-array (* 2 16 8))]
      (dotimes [h 2]
        (let [koff (java.util.Arrays/copyOfRange kd (* h 128) (* (inc h) 128))
              voff (java.util.Arrays/copyOfRange vd (* h 128) (* (inc h) 128))]
          (m/sdpa-causal qd (* h 128) 8 koff voff 16 8 out (* h 128) 8)))
      (check "sdpa" (t/max-abs-diff (t/tensor [(* 2 16 8)] out)
                                    (t/reshape (t/from-npy y) [(* 2 16 8)])) 1e-5))

    ;; pkm (block-0, routers 0 and 3; golden q is (2,4,16))
    (let [{:strs [q y trunk_ids]} (npy/read-npz "jvm/goldens/pkm.npz")
          ^floats qd (t/data (t/from-npy q))
          ^longs tids (:data trunk_ids)
          out (float-array (* 2 4 16))]
      (dotimes [b 2]
        (let [qb (java.util.Arrays/copyOfRange qd (* b 64) (* (inc b) 64))
              ob (m/pkm-forward qb 4 (:memory b0) (aget tids b))]
          (System/arraycopy ob 0 out (* b 64) 64)))
      (check "pkm" (t/max-abs-diff (t/tensor [(* 2 4 16)] out)
                                   (t/reshape (t/from-npy y) [(* 2 4 16)])) 1e-5))

    ;; netbank (block-0, q (1,4,16))
    (let [{:strs [q y]} (npy/read-npz "jvm/goldens/netbank.npz")
          ob (m/netbank-forward (t/data (t/from-npy q)) 4 (:netbank b0))]
      (check "netbank" (t/max-abs-diff (t/tensor [(* 4 16)] ob)
                                       (t/reshape (t/from-npy y) [(* 4 16)])) 1e-5))

    ;; switchgate 3-way eval (perturbed params come WITH the golden)
    (let [{:strs [q sdpa mem net y] :as z} (npy/read-npz "jvm/goldens/gate.npz")
          gp (fn [n] (:data (t/from-npy (get z (str "p_" n)))))
          gate {:gate-proj (gp "gate_proj") :gate-proj-3 (gp "gate_proj_3")
                :alpha-net (gp "alpha_net") :lap (gp "local_active_proj")
                :lab (gp "local_active_bias") :n-long-heads 2}
          ;; goldens are (1,2,6,8) head-major; gate-mix wants (T, H*8)
          to-thw (fn [nm] (let [^floats a (:data (t/from-npy (get z nm)))
                                o (float-array 96)]
                            (dotimes [h 2]
                              (dotimes [ti 6]
                                (System/arraycopy a (+ (* h 48) (* ti 8))
                                                  o (+ (* ti 16) (* h 8)) 8)))
                            o))
          out (m/gate-mix gate (to-thw "q") (to-thw "sdpa") (to-thw "mem") (to-thw "net") 6)
          gold (to-thw "y")]
      (check "switchgate" (t/max-abs-diff (t/tensor [96] out) (t/tensor [96] gold)) 1e-5))

    ;; full forward (B=1, T=64, trunk 0)
    (let [{:strs [tokens logits bpc]} (npy/read-npz "jvm/goldens/full_forward.npz")
          toks (vec (:data tokens))
          out (m/forward model toks 0)
          gold (t/reshape (t/from-npy logits) [(* 64 256)])
          err (t/max-abs-diff (t/tensor [(* 64 256)] out) gold)
          ;; bpc from our own logits
          ce (loop [ti 0 s 0.0]
               (if (< ti 63)
                 (let [off (* ti 256)
                       tgt (long (nth toks (inc ti)))
                       mx (loop [j 0 mv Float/NEGATIVE_INFINITY]
                            (if (< j 256) (recur (inc j) (max mv (aget ^floats out (+ off j)))) mv))
                       lse (loop [j 0 acc 0.0]
                             (if (< j 256)
                               (recur (inc j) (+ acc (Math/exp (- (aget ^floats out (+ off j)) (double mx)))))
                               (+ (double mx) (Math/log acc))))]
                   (recur (inc ti) (+ s (- lse (aget ^floats out (+ off tgt))))))
                 (/ s 63)))
          my-bpc (/ ce (Math/log 2.0))]
      (check "full-forward" err 1e-4)
      (println (format "full-forward bpc: jvm %.4f vs torch %.4f"
                       my-bpc (double (aget ^doubles (:data bpc) 0)))))

    (if (pos? @*fail*)
      (do (println @*fail* "FAILURES") (System/exit 1))
      (println "ALL PARITY CHECKS PASSED"))))
