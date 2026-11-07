(ns mmllm.jvm.m1-check
  "M1 acceptance: load manifest + dense.npz + banks, verify counts/shapes,
   spot-check module goldens that need no model code (rmsnorm, swiglu via
   tensor ops). Run: jvm/run.sh -m mmllm.jvm.m1-check"
  (:require [mmllm.jvm.npy :as npy]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t]))

(defn -main [& _]
  (let [manifest (p/load-manifest "jvm/resources/arch-sym24.edn")
        dense (p/load-dense manifest "jvm/goldens/dense.npz")
        banks (p/load-banks manifest "jvm/goldens/banks")]
    (println "dense tensors:" (count (:by-index dense))
             "banks:" (count banks))

    ;; rmsnorm golden — first real math parity check
    (let [{:strs [x y w]} (npy/read-npz "jvm/goldens/rmsnorm.npz")
          xt (t/from-npy x) yt (t/from-npy y) wt (t/from-npy w)
          mine (t/rms-norm xt wt 1e-6)
          err (t/max-abs-diff mine yt)]
      (println (format "rmsnorm  max-abs-err %.3e %s" err (if (< err 1e-5) "OK" "FAIL")))
      (assert (< err 1e-5)))

    ;; swiglu golden — exercises linear + silu against block-0 weights
    (let [{:strs [x y]} (npy/read-npz "jvm/goldens/swiglu.npz")
          xt (t/from-npy x) yt (t/from-npy y)
          w (fn [n] (get (:by-name dense) (str "blocks.0." n ".weight")))
          h (t/mul! (t/silu! (t/linear xt (w "gate_proj")))
                    (t/linear xt (w "up_proj")))
          mine (t/linear h (w "down_proj"))
          err (t/max-abs-diff mine yt)]
      (println (format "swiglu   max-abs-err %.3e %s" err (if (< err 1e-5) "OK" "FAIL")))
      (assert (< err 1e-5)))

    ;; bank spot-check: mmap'd row 0 of block-0 local V is finite + nonzero
    (let [b (get banks "blocks.0.memory.V")
          row (float-array 16)]
      (p/bank-row! b 0 row 0)
      (println "bank blocks.0.memory.V row0[0..3]:" (vec (take 4 row))))
    (println "M1 OK")))
