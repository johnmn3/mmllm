(ns mmllm.jvm.optim
  "Optimizers (M5a): torch-exact AdamW + a port of optim.py's
   CPUOffloadSparseAdam (touched-row sparse Adam). All arithmetic is
   f32-rounded op-for-op like the torch CPU kernels (each binary op
   wrapped in (float ...)), so 5-step param trajectories match the
   goldens to ~1e-7.

   Faithfulness notes — replicate the REFERENCE, not textbook Adam:
   - AdamW (torch _single_tensor_adam, decoupled_weight_decay=true):
       step += 1
       p *= 1 - lr*wd                    ; weight decay FIRST, on the param
       m += (1-b1) * (g - m)             ; lerp_
       v  = b2*v + (1-b2)*g*g
       denom = sqrt(v)/sqrt(1-b2^step) + eps
       p += -(lr/(1-b1^step)) * m/denom
   - Sparse Adam keeps ONE state step counter PER PARAM, incremented on
     every step() in which that param has a grad — NOT a per-row
     first-touch counter. A row first touched at param-step k gets bias
     correction for k with zero moments, exactly like optim.py:263-331.
   - _is_v_local (optim.py:98): rows divide into >= 2 trunks of
     sqrt-local². Matching params get lr × local-mult (MMLLM_LR_LOCAL_MULT,
     default 0.05) × layer-mults[i mod n] (MMLLM_LR_LAYER_MULTS tiling),
     where i counts v-local params WITH grads in param order within one
     step — optim.py `continue`s on grad-less params BEFORE bumping the
     counter, so a grad-less v-local param shifts later tile indices.
     That quirk is replicated, not fixed."
  (:require [mmllm.jvm.rowstore :as rs])
  (:import [mmllm.jvm.rowstore IRowStore]))

(set! *warn-on-reflection* true)

;; ── AdamW ──

(defn adamw-init
  "Mutable AdamW state for a param of n elements."
  [^long n]
  {:step (long-array 1) :m (float-array n) :v (float-array n)})

(defn adamw-step!
  "One AdamW step in-place on param array `p` with dense grad `g`.
   opts: {:lr .. :beta1 0.9 :beta2 0.999 :eps 1e-8 :weight-decay 1e-2}."
  [state ^floats p ^floats g opts]
  (let [lr    (double (:lr opts))
        wd    (double (:weight-decay opts 1e-2))
        beta1 (double (:beta1 opts 0.9))
        beta2 (double (:beta2 opts 0.999))
        ^longs stepa (:step state)
        ^floats m (:m state)
        ^floats v (:v state)
        _     (aset stepa 0 (inc (aget stepa 0)))
        step  (aget stepa 0)
        decayf (float (- 1.0 (* lr wd)))
        w1f   (float (- 1.0 beta1))         ; lerp weight
        b2f   (float beta2)
        c2f   (float (- 1.0 beta2))
        bc1   (- 1.0 (Math/pow beta1 (double step)))
        bc2   (- 1.0 (Math/pow beta2 (double step)))
        negssf (float (- (/ lr bc1)))       ; addcdiv value = -step_size
        bc2sf (float (Math/sqrt bc2))
        epsf  (float (:eps opts 1e-8))]
    (dotimes [i (alength p)]
      (let [pi  (float (* (aget p i) decayf))
            gi  (aget g i)
            mi  (aget m i)
            mi' (float (+ mi (float (* w1f (float (- gi mi))))))
            vi' (float (+ (float (* (aget v i) b2f))
                          (float (* (float (* c2f gi)) gi))))
            den (float (+ (float (/ (float (Math/sqrt (double vi'))) bc2sf))
                          epsf))]
        (aset m i mi')
        (aset v i vi')
        (aset p i (float (+ pi (float (* negssf (float (/ mi' den)))))))))
    state))

;; ── touched-row sparse Adam (CPUOffloadSparseAdam port) ──

(defn is-v-local?
  "optim.py _is_v_local: row count divides cleanly into >= 2 trunks of
   sqrt-local². V_net's sqrt_n² rows fall through (mult 1.0)."
  [^long rows ^long sqrt-local]
  (let [rpt (* sqrt-local sqrt-local)]
    (and (zero? (rem rows rpt))
         (>= (quot rows rpt) 2))))

(defn coalesce
  "torch sparse grad.coalesce(): unique ascending row indices, duplicate
   rows' values summed (f32, stable first-occurrence order within a row).
   idx (nnz) longs, val (nnz×dim) floats -> {:idx ^longs :val ^floats}."
  [^longs idx ^floats val ^long dim]
  (let [nnz   (alength idx)
        order (int-array nnz)]
    (dotimes [i nnz] (aset order i i))
    ;; stable sort positions by row index
    (let [^objects boxed (object-array nnz)]
      (dotimes [i nnz] (aset boxed i (Integer/valueOf i)))
      (java.util.Arrays/sort boxed
                             (reify java.util.Comparator
                               (compare [_ a b]
                                 (Long/compare (aget idx (int a))
                                               (aget idx (int b))))))
      (dotimes [i nnz] (aset order i (int (aget boxed i)))))
    (let [n-uniq (loop [i 0 n 0 prev Long/MIN_VALUE]
                   (if (< i nnz)
                     (let [r (aget idx (aget order i))]
                       (recur (inc i) (if (= r prev) n (inc n)) r))
                     n))
          out-idx (long-array n-uniq)
          out-val (float-array (* n-uniq dim))]
      (loop [i 0 o -1 prev Long/MIN_VALUE]
        (when (< i nnz)
          (let [pos (aget order i)
                r   (aget idx pos)
                o'  (if (= r prev) o (inc o))]
            (when-not (= r prev)
              (aset out-idx o' r))
            (dotimes [j dim]
              (let [oj (+ (* o' dim) j)]
                (aset out-val oj (float (+ (aget out-val oj)
                                           (aget val (+ (* pos dim) j)))))))
            (recur (inc i) o' r))))
      {:idx out-idx :val out-val})))

(defn sparse-adam-init
  "Mutable per-param state: one step counter + a lazily-created packed
   m+v moment store (one 2·dim-wide row per touched bank row; m at
   [0,dim), v at [dim,2·dim); rows start at zero moments on first
   touch — identical semantics to the old per-row float[] maps, packed
   per the M7 accumulator swap). The store is lazy because dim isn't
   known until the first grad arrives."
  []
  {:step (long-array 1) :mv (object-array 1)})

(defn state-mv
  "Get-or-create the packed m+v store of a sparse-adam state for rows of
   `width` (= 2·dim) floats."
  ^mmllm.jvm.rowstore.IRowStore [state ^long width]
  (let [^objects holder (:mv state)]
    (or (aget holder 0)
        (let [s (rs/packed-row-map width)]
          (aset holder 0 s)
          s))))

(defn- sparse-param-step!
  "Adam update on the coalesced touched rows of one param."
  [state ^floats pdata dim cidx cval opts layer-mult]
  (let [dim   (long dim)
        ^longs cidx cidx
        ^floats cval cval
        lr    (double (:lr opts))
        beta1 (double (:beta1 opts 0.9))
        beta2 (double (:beta2 opts 0.999))
        ^longs stepa (:step state)
        ^IRowStore mv (state-mv state (* 2 dim))
        _     (aset stepa 0 (inc (aget stepa 0)))
        step  (aget stepa 0)
        b1f   (float beta1)
        a1f   (float (- 1.0 beta1))         ; add_(values, alpha=1-beta1)
        b2f   (float beta2)
        c2f   (float (- 1.0 beta2))
        bc1f  (float (- 1.0 (Math/pow beta1 (double step))))
        bc2f  (float (- 1.0 (Math/pow beta2 (double step))))
        negf  (float (- (* lr (double layer-mult))))
        epsf  (float (:eps opts 1e-8))]
    (dotimes [i (alength cidx)]
      (let [row (aget cidx i)
            slot (.rsEnsureSlot mv row)
            ^floats mvch (.rsChunkOf mv slot)
            mvoff (.rsOffsetOf mv slot)]
        (dotimes [j dim]
          (let [gj  (aget cval (+ (* i dim) j))
                mj' (float (+ (float (* (aget mvch (+ mvoff j)) b1f))
                              (float (* a1f gj))))
                vj' (float (+ (float (* (aget mvch (+ mvoff dim j)) b2f))
                              (float (* (float (* c2f gj)) gj))))
                mh  (float (/ mj' bc1f))
                vh  (float (/ vj' bc2f))
                den (float (+ (float (Math/sqrt (double vh))) epsf))
                dlt (float (/ (float (* negf mh)) den))
                pj  (+ (* row dim) j)]
            (aset mvch (+ mvoff j) mj')
            (aset mvch (+ mvoff dim j) vj')
            (aset pdata pj (float (+ (aget pdata pj) dlt)))))))
    state))

(defn sparse-adam-step!
  "One CPUOffloadSparseAdam step over all params.
   states: vector from sparse-adam-init, one per param;
   params: vector of {:data ^floats :rows n :dim d};
   grads:  vector of nil or {:idx ^longs :val ^floats} (uncoalesced ok —
           duplicates summed, rows sorted here, like grad.coalesce());
   opts:   {:lr :beta1 :beta2 :eps :sqrt-local :local-mult :layer-mults}."
  [states params grads opts]
  (let [lm         (:layer-mults opts)
        local-mult (double (:local-mult opts 0.05))
        sqrt-local (long (:sqrt-local opts))
        n          (count params)]
    (loop [i 0 vc 0]
      (when (< i n)
        (let [gr (nth grads i)]
          (if (nil? gr)
            (recur (inc i) vc)              ; no grad: no step bump, no vc bump
            (let [{:keys [data rows dim]} (nth params i)
                  vloc?      (is-v-local? (long rows) sqrt-local)
                  per-layer  (if (and vloc? (seq lm))
                               (double (nth lm (rem vc (count lm))))
                               1.0)
                  layer-mult (if vloc? (* local-mult per-layer) 1.0)
                  {ci :idx cv :val} (coalesce (:idx gr) (:val gr) (long dim))]
              (sparse-param-step! (nth states i) data dim ci cv opts layer-mult)
              (recur (inc i) (if vloc? (inc vc) vc)))))))
    states))
