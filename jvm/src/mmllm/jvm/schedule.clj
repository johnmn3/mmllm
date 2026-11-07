(ns mmllm.jvm.schedule
  "LR schedule (M5a) — port of core.lpy's lr-at-step + the per-group
   cosine mult interpolation (pick-lr-{dense,kab,bank,net}-mult arity-2).
   Driven by a config map, not env vars:

     {:lr 3e-3 :lr-min 3e-3 :warmup 70 :total 100
      :round-base 0 :ramp-floor 0.0            ; optional, default 0
      :dense-mult 0.05 :dense-mult-end 0.005
      :kab-mult   0.15 :kab-mult-end   0.001   ; prod since c0449a3 (unset
      :bank-mult  3.0  :bank-mult-end  0.001   ;  kab defaults to dense's
      :net-mult   0.001 :net-mult-end  5.0}    ;  START, constant)

   Reference quirks kept ON PURPOSE (parity over cleanliness):
   - lr-at-step's linear ramp uses round-base-relative s-eff/warmup-eff
     (MMLLM_LR_ROUND_BASE semantics: each chain round gets a fresh ramp),
     but the cosine phase uses ABSOLUTE s and warmup.
   - the ramp's minimum is ramp-floor × max-lr (MMLLM_LR_RAMP_FLOOR),
     applied as (max floor progress) — NOT interpolated.
   - mult-cosine-interp returns start when start == end, when total == 0,
     or inside the warmup window; end at/after total."
  (:refer-clojure :exclude []))

(set! *warn-on-reflection* true)

(defn mult-cosine-interp
  "core.lpy mult-cosine-interp: cosine from `start` to `end` over
   (warmup, total]. 5 args — no primitive hints (Clojure caps primitive
   fn interfaces at 4 args); cast inside."
  [start end step total warmup]
  (let [start  (double start)
        end    (double end)
        step   (long step)
        total  (long total)
        warmup (long warmup)]
    (cond
      (== start end)   start
      (zero? total)    start
      (< step warmup)  start
      (>= step total)  end
      :else (let [progress (/ (double (- step warmup))
                              (double (- total warmup)))
                  cos-half (* 0.5 (+ 1.0 (Math/cos (* Math/PI progress))))]
              (+ end (* (- start end) cos-half))))))

(defn lr-at-step
  "core.lpy lr-at-step: linear warmup (from ramp-floor × max-lr) + cosine
   decay to lr-min. warmup == 0 (after round-base subtraction) means
   constant max-lr."
  ^double [cfg ^long s]
  (let [max-lr     (double (:lr cfg))
        min-lr     (double (:lr-min cfg))
        total      (long (:total cfg))
        warmup     (long (:warmup cfg))
        round-base (long (:round-base cfg 0))
        floor      (double (:ramp-floor cfg 0.0))
        s-eff      (max 0 (- s round-base))
        warmup-eff (max 0 (- warmup round-base))]
    (cond
      (zero? warmup-eff)   max-lr
      (< s-eff warmup-eff) (let [progress (/ (double s-eff)
                                             (double warmup-eff))]
                             (* max-lr (max floor progress)))
      (>= s total)         min-lr
      ;; NOTE absolute s/warmup here (not s-eff/warmup-eff) — reference
      ;; behavior, do not "fix".
      :else (let [progress (/ (double (- s warmup))
                              (double (- total warmup)))
                  cos-half (* 0.5 (+ 1.0 (Math/cos (* Math/PI progress))))]
              (+ min-lr (* (- max-lr min-lr) cos-half))))))

(defn group-mult
  "Cosine-scheduled multiplier for `group` (:dense :kab :bank :net) at
   `step` — pick-lr-<group>-mult arity-2. The -end key defaults to the
   start (constant), mirroring MMLLM_LR_*_MULT_END's env default."
  ^double [cfg group ^long step]
  (let [start (double (get cfg (keyword (str (name group) "-mult"))))
        end   (double (get cfg (keyword (str (name group) "-mult-end")) start))]
    (double (mult-cosine-interp start end step (:total cfg) (:warmup cfg)))))

(defn lrs-at-step
  "Per-group lrs at `step`, composed exactly like the train loop
   (core.lpy:4888-4904): cur-lr × pick-lr-*-mult(step, total)."
  [cfg ^long step]
  (let [base (lr-at-step cfg step)]
    {:base  base
     :dense (* base (group-mult cfg :dense step))
     :kab   (* base (group-mult cfg :kab step))
     :bank  (* base (group-mult cfg :bank step))
     :net   (* base (group-mult cfg :net step))}))
