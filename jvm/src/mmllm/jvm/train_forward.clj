(ns mmllm.jvm.train-forward
  "Train-mode forward + block backward for the sym24 step replay (M5b,
   gate G4). One batch row at a time — (T, d) row-major float[], same
   layout as mmllm.jvm.model, whose eval API is untouched (this ns only
   REUSES model.clj pieces: rope, sdpa, pk-retrieve, rms, sub-scores).

   Differences from the eval forward, mirroring the torch train path:
   - Local PKM z-loss: per-token logsumexp² of the sub-key scores
     (memory.py:957-960). Only Local carries grad — NetBank's z is
     detached telemetry (netbank.py:332-342) and is not computed here.
   - SwitchGate net-default takes the ST-Bernoulli TRAIN branch
     (gating.py:218-226) consuming a REPLAYED uniform stream R (the
     torch.rand_like dump) — grad.clj's gate-train-bwd, mode :st.
   - modes: :main (all tiers), :teacher (local-only: netbank nil'd,
     2-way sdpa/mem sigmoid gate on local layers, plain SDPA on
     net-only layers), :student (net-only: memory nil'd, 2-way
     sdpa/net gate with alpha_net everywhere) — core.lpy block-forward
     kd routing. :student pairs with freeze-trunk (KD_FREEZE=trunk):
     dense trunk params (norm1/2, q/k/v/o, FFN, tok-emb) propagate dx
     but accumulate NO weight grad (attention_kernel._flin/_fnorm).

   Each block-train-fwd returns [x-out ctx]; block-train-bwd consumes
   the ctx and accumulates into a `grads` container (see make-grads)."
  (:require [mmllm.jvm.model :as m]
            [mmllm.jvm.grad :as g]
            [mmllm.jvm.params :as p]
            [mmllm.jvm.tensor :as t])
  (:import [java.util HashMap]))

(set! *warn-on-reflection* true)

;; ── grads container ──

(defn make-grads
  "Accumulator for one train-step's backward(s).
   :dense    name → float[] (manifest names, torch .grad equivalents)
   :dv-local layer → HashMap<row, float[16]>  (sparse V_local grads)
   :dv-net   layer → HashMap<row, float[8]>   (sparse V_net grads)"
  []
  {:dense (HashMap.) :dv-local (HashMap.) :dv-net (HashMap.)})

(defn gacc
  "Get-or-create the dense grad buffer for `name` (n floats)."
  ^floats [grads ^String name ^long n]
  (let [^HashMap h (:dense grads)]
    (or (.get h name)
        (let [a (float-array n)] (.put h name a) a))))

(defn dv-map
  "Get-or-create the sparse dV HashMap for (:dv-local|:dv-net, layer)."
  ^HashMap [grads kind ^long layer]
  (let [^HashMap h (kind grads)]
    (or (.get h layer)
        (let [mm (HashMap.)] (.put h layer mm) mm))))

(defn add-into!
  "dst[i] += src[i] elementwise (f32)."
  [^floats dst ^floats src]
  (dotimes [i (alength dst)]
    (aset dst i (float (+ (aget dst i) (aget src i))))))

(defn merge-dv!
  "Merge a per-call dV HashMap (row → float[dim]) into the layer's."
  [^HashMap dst ^HashMap src]
  (doseq [e src]
    (let [^java.util.Map$Entry e e
          row (.getKey e)
          ^floats v (.getValue e)]
      (if-let [^floats acc (.get dst row)]
        (add-into! acc v)
        (.put dst row (java.util.Arrays/copyOf v (alength v)))))))

;; ── layout helpers: (T, H*8) column-major-by-head ↔ head-major (H, T, 8) ──

(defn t->h
  "(T,16) with head h at col h*8 → flat (2,T,8)."
  ^floats [^floats a ^long T]
  (let [o (float-array (* T 16))]
    (dotimes [h 2]
      (dotimes [ti T]
        (System/arraycopy a (+ (* ti 16) (* h 8)) o (+ (* h T 8) (* ti 8)) 8)))
    o))

(defn h->t
  "flat (2,T,8) → (T,16) with head h at col h*8."
  ^floats [^floats a ^long T]
  (let [o (float-array (* T 16))]
    (dotimes [h 2]
      (dotimes [ti T]
        (System/arraycopy a (+ (* h T 8) (* ti 8)) o (+ (* ti 16) (* h 8)) 8)))
    o))

(defn col-slice
  "Contiguous (T, w) copy of columns [off, off+w) from a (T, stride) array."
  [^floats a T stride off w]
  (let [T (long T) stride (long stride) off (long off) w (long w)
        o (float-array (* T w))]
    (dotimes [ti T]
      (System/arraycopy a (+ (* ti stride) off) o (* ti w) w))
    o))

(defn col-add!
  "dst (T, stride) columns [off, off+w) += src (T, w)."
  [^floats dst T stride off w ^floats src]
  (let [T (long T) stride (long stride) off (long off) w (long w)]
    (dotimes [ti T]
      (dotimes [c w]
        (let [di (+ (* ti stride) off c)]
          (aset dst di (float (+ (aget dst di) (aget src (+ (* ti w) c))))))))))

;; ── Local PKM: train fwd (out + z-lse) and bwd (retrieval + z branch) ──

(defn pkm-train-forward
  "Local PKM forward with the training z-loss side-product.
   q (T,16) → {:out (T,16) :lse float[2T] (lse_a, lse_b per token) or nil}.
   want-z? false (teacher pass) skips the logsumexp."
  [^floats q T mem trunk-id want-z?]
  (let [T (long T) trunk-id (long trunk-id)
        {:keys [^floats qnorm-w ^floats Ka ^floats Kb bank]} mem
        q-dim (long (:q-dim mem)) n-per-trunk (long (:n-per-trunk mem))
        sqrt-n (long (:sqrt-n mem)) sub-dim (long (:sub-dim mem))
        out (float-array (* T q-dim))
        row (float-array q-dim)
        qn (java.util.Arrays/copyOf q (alength q))
        lse (when want-z? (float-array (* 2 T)))
        off (* trunk-id n-per-trunk)
        lse-of (fn [^floats s]
                 (let [n (alength s)
                       mx (loop [i 0 mv Double/NEGATIVE_INFINITY]
                            (if (< i n) (recur (inc i) (max mv (double (aget s i)))) mv))
                       sm (loop [i 0 acc 0.0]
                            (if (< i n) (recur (inc i) (+ acc (Math/exp (- (aget s i) mx)))) acc))]
                   (+ mx (Math/log sm))))]
    (dotimes [ti T]
      (m/rms-row! qn (* ti q-dim) qnorm-w q-dim))
    (dotimes [ti T]
      (when want-z?
        (let [sa (m/sub-scores qn (* ti q-dim) Ka sqrt-n sub-dim)
              sb (m/sub-scores qn (+ (* ti q-dim) sub-dim) Kb sqrt-n sub-dim)]
          (aset ^floats lse (* 2 ti) (float (lse-of sa)))
          (aset ^floats lse (inc (* 2 ti)) (float (lse-of sb)))))
      (let [{:keys [^longs idx ^floats w]} (m/pk-retrieve qn (* ti q-dim) mem)
            ooff (* ti q-dim)]
        (dotimes [k (alength idx)]
          (p/bank-row! bank (+ off (aget idx k)) row 0)
          (let [wk (aget w k)]
            (dotimes [c q-dim]
              (aset out (+ ooff c)
                    (float (+ (aget out (+ ooff c)) (* wk (aget row c))))))))))
    {:out out :lse lse}))

(defn pkm-train-bwd
  "Local PKM backward for one batch row: retrieval scatter (grad.clj's
   pk-bwd-token!) PLUS the z-loss branch. z-scale = z_coef / (B·T): the
   z term is z_coef · Σ_layers mean_{B,T}(lse_a² + lse_b²), so
   dL/dlse = z-scale · 2 · lse and dscores = dlse · softmax(scores)
   (dense — ALL sqrt-n sub-rows get a dK contribution). Accumulates
   dKa/dKb/dqnorm-w into caller-owned arrays and dV into `dV`
   (HashMap row → float[16], global rows incl. trunk offset).
   Returns dq (T,16)."
  [^floats q T mem trunk-id ^floats dout z-scale acc]
  (let [T (long T) trunk-id (long trunk-id) z-scale (double z-scale)
        {:keys [^floats qnorm-w ^floats Ka ^floats Kb]} mem
        q-dim (long (:q-dim mem)) n-per-trunk (long (:n-per-trunk mem))
        sqrt-n (long (:sqrt-n mem)) sub-dim (long (:sub-dim mem))
        ^floats dKa (:dKa acc) ^floats dKb (:dKb acc)
        ^floats dqnw (:dqnorm-w acc) ^HashMap dV (:dV acc)
        qn (java.util.Arrays/copyOf q (alength q))
        dqn (float-array (* T q-dim))
        off (* trunk-id n-per-trunk)]
    (dotimes [ti T] (m/rms-row! qn (* ti q-dim) qnorm-w q-dim))
    (dotimes [ti T]
      ;; retrieval branch (softmax-weighted V sum → scatter)
      (g/pk-bwd-token! qn (* ti q-dim) mem off
                       (java.util.Arrays/copyOfRange dout (* ti q-dim) (* (inc ti) q-dim))
                       q-dim dKa dKb dV dqn)
      ;; z branch: dscores = 2·z-scale·lse · softmax(scores), both halves
      (when (pos? z-scale)
        (dotimes [half 2]
          (let [qoff (+ (* ti q-dim) (* half sub-dim))
                ^floats K (if (zero? half) Ka Kb)
                ^floats dK (if (zero? half) dKa dKb)
                s (m/sub-scores qn qoff K sqrt-n sub-dim)
                mx (loop [i 0 mv Double/NEGATIVE_INFINITY]
                     (if (< i sqrt-n) (recur (inc i) (max mv (double (aget s i)))) mv))
                sm (loop [i 0 acc' 0.0]
                     (if (< i sqrt-n) (recur (inc i) (+ acc' (Math/exp (- (aget s i) mx)))) acc'))
                lse (+ mx (Math/log sm))
                dlse (* 2.0 z-scale lse)]
            (dotimes [r sqrt-n]
              (let [ds (* dlse (/ (Math/exp (- (aget s r) mx)) sm))
                    koff (* r sub-dim)]
                (dotimes [c sub-dim]
                  (aset dK (+ koff c)
                        (float (+ (aget dK (+ koff c)) (* ds (aget qn (+ qoff c))))))
                  (aset dqn (+ qoff c)
                        (float (+ (aget dqn (+ qoff c)) (* ds (aget K (+ koff c)))))))))))))
    (let [{:keys [dx ^floats dw]} (g/rmsnorm-bwd q qnorm-w dqn T q-dim m/eps)]
      (dotimes [i q-dim] (aset dqnw i (float (+ (aget dqnw i) (aget dw i)))))
      dx)))

;; ── 2-way SwitchGate branches (T-major (T,16) layout) ──

(defn gate2-net-fwd
  "gating.py:140-159 (mem_out=None, net_out present — student pass and
   net-only layers): g = σ(q·gate_proj[h]); y = g·sdpa + (1-g)·α_h·net."
  [{:keys [^floats gate-proj ^floats alpha-net]} ^floats q ^floats sdpa ^floats net T]
  (let [T (long T) hd 8
        y (float-array (* T 16))]
    (dotimes [ti T]
      (dotimes [h 2]
        (let [off (+ (* ti 16) (* h hd))
              gg (/ 1.0 (+ 1.0 (Math/exp (- (g/dot-at q off gate-proj (* h hd) hd)))))
              alpha (double (aget alpha-net h))]
          (dotimes [c hd]
            (aset y (+ off c)
                  (float (+ (* gg (aget sdpa (+ off c)))
                            (* (- 1.0 gg) alpha (aget net (+ off c))))))))))
    y))

(defn gate2-net-bwd
  "Backward of gate2-net-fwd. Accumulates dgate-proj (2,8) and dalpha (2)
   into caller arrays; returns {:dq :dsdpa :dnet} (T,16)."
  [{:keys [^floats gate-proj ^floats alpha-net]} ^floats q ^floats sdpa ^floats net
   T ^floats dout ^floats dgp ^floats dalpha]
  (let [T (long T) hd 8
        dq (float-array (* T 16))
        dsdpa (float-array (* T 16))
        dnet (float-array (* T 16))]
    (dotimes [ti T]
      (dotimes [h 2]
        (let [off (+ (* ti 16) (* h hd))
              logit (g/dot-at q off gate-proj (* h hd) hd)
              gg (/ 1.0 (+ 1.0 (Math/exp (- logit))))
              alpha (double (aget alpha-net h))
              gS (g/dot-at dout off sdpa off hd)
              gN (g/dot-at dout off net off hd)]
          (dotimes [c hd]
            (aset dsdpa (+ off c) (float (* gg (aget dout (+ off c)))))
            (aset dnet (+ off c) (float (* (- 1.0 gg) alpha (aget dout (+ off c))))))
          (aset dalpha h (float (+ (aget dalpha h) (* (- 1.0 gg) gN))))
          (let [dg (- gS (* alpha gN))
                dlogit (* dg gg (- 1.0 gg))]
            (dotimes [c hd]
              (aset dgp (+ (* h hd) c)
                    (float (+ (aget dgp (+ (* h hd) c)) (* dlogit (aget q (+ off c))))))
              (aset dq (+ off c)
                    (float (+ (aget dq (+ off c))
                              (* dlogit (aget gate-proj (+ (* h hd) c)))))))))))
    {:dq dq :dsdpa dsdpa :dnet dnet}))

(defn gate2-mem-fwd
  "gating.py:160-168 (net_out=None — the KD teacher's local layers):
   y = g·sdpa + (1-g)·mem, NO alpha. Forward only (teacher is no-grad)."
  [{:keys [^floats gate-proj]} ^floats q ^floats sdpa ^floats mem T]
  (let [T (long T) hd 8
        y (float-array (* T 16))]
    (dotimes [ti T]
      (dotimes [h 2]
        (let [off (+ (* ti 16) (* h hd))
              gg (/ 1.0 (+ 1.0 (Math/exp (- (g/dot-at q off gate-proj (* h hd) hd)))))]
          (dotimes [c hd]
            (aset y (+ off c)
                  (float (+ (* gg (aget sdpa (+ off c)))
                            (* (- 1.0 gg) (aget mem (+ off c))))))))))
    y))

;; ── block train forward ──

(defn block-train-fwd
  "One pre-norm block, train mode, prefill T tokens of ONE batch row.
   mode :main | :teacher | :student. Rl: replayed uniform draws for this
   (block, row) — flat (H,T) — required for :main on local-bank layers.
   Returns {:x-out (T,32) :ctx {...}} (x untouched; x-out fresh)."
  [blk rope ^floats x T trunk-id mode Rl]
  (let [T (long T) d 32 hd 8
        mem (when (not= mode :student) (:memory blk))
        net (when (not= mode :teacher) (:netbank blk))
        xn (t/data (t/rms-norm (t/tensor [T d] x) (t/tensor [d] (:norm1 blk)) m/eps))
        q (t/data (t/linear (t/tensor [T d] xn) (t/tensor [d d] (:q-proj blk))))
        ks (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:k-proj-s blk))))
        vs (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:v-proj-s blk))))
        kl (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:k-proj-l blk))))
        vl (t/data (t/linear (t/tensor [T d] xn) (t/tensor [hd d] (:v-proj-l blk))))
        attn (float-array (* T d))]
    (dotimes [ti T]
      (m/rope-at! q (* ti d) rope ti hd)
      (m/rope-at! q (+ (* ti d) hd) rope ti hd)
      (m/rope-at! ks (* ti hd) rope ti hd))
    (m/sdpa-causal q 0 d ks vs T hd attn 0 d)
    (m/sdpa-causal q hd d ks vs T hd attn hd d)
    (let [sdpa-l (float-array (* T 16))]
      (m/sdpa-causal q (* 2 hd) d kl vl T hd sdpa-l 0 16)
      (m/sdpa-causal q (* 3 hd) d kl vl T hd sdpa-l hd 16)
      (let [bank-q (col-slice q T d 16 16)
            mem-res (when mem (pkm-train-forward bank-q T mem trunk-id (= mode :main)))
            mem-out (:out mem-res)
            net-out (when net (m/netbank-forward bank-q T net))
            gate (:gate blk)
            mixed (cond
                    (and mem-out net-out)   ; 3-way ST-Bernoulli train branch
                    (h->t (:y (g/gate-train-bwd gate
                                                (t->h bank-q T) (t->h sdpa-l T)
                                                (t->h mem-out T) (t->h net-out T)
                                                Rl 2 T :st nil))
                          T)
                    net-out (gate2-net-fwd gate bank-q sdpa-l net-out T)
                    mem-out (gate2-mem-fwd gate bank-q sdpa-l mem-out T)
                    :else sdpa-l)]          ; teacher on a net-only layer
        (dotimes [ti T]
          (System/arraycopy mixed (* ti 16) attn (+ (* ti d) 16) 16))
        (let [o (t/data (t/linear (t/tensor [T d] attn) (t/tensor [d d] (:o-proj blk))))
              x-mid (float-array (* T d))]
          (dotimes [i (* T d)] (aset x-mid i (float (+ (aget x i) (aget o i)))))
          (let [xn2 (t/data (t/rms-norm (t/tensor [T d] x-mid)
                                        (t/tensor [d] (:norm2 blk)) m/eps))
                h2 (t/mul! (t/silu! (t/linear (t/tensor [T d] xn2)
                                              (t/tensor [128 d] (:gate-proj blk))))
                           (t/linear (t/tensor [T d] xn2) (t/tensor [128 d] (:up-proj blk))))
                f (t/data (t/linear h2 (t/tensor [d 128] (:down-proj blk))))
                x-out (float-array (* T d))]
            (dotimes [i (* T d)] (aset x-out i (float (+ (aget x-mid i) (aget f i)))))
            {:x-out x-out
             :ctx {:x-in x :xn xn :q q :ks ks :vs vs :kl kl :vl vl
                   :sdpa-l sdpa-l :bank-q bank-q
                   :mem-out mem-out :net-out net-out
                   :z-lse (:lse mem-res)
                   :attn attn :x-mid x-mid :xn2 xn2 :Rl Rl}}))))))

;; ── block train backward ──

(defn block-train-bwd
  "Backward through one block for one batch row. dx (T,32) is dL/dx-out.
   opts {:mode :main|:student :layer i :z-scale double :trunk-id t}.
   Accumulates param grads into `grads` (freeze-trunk in :student mode:
   trunk dW skipped, dx still propagated). Returns dx-in (T,32)."
  [blk ctx rope ^floats dx T grads opts]
  (let [T (long T) d 32 hd 8
        layer (long (:layer opts))
        mode (:mode opts)
        frz? (= mode :student)
        pre (str "blocks." layer ".")
        {:keys [^floats x-in ^floats xn ^floats q ^floats ks ^floats vs
                ^floats kl ^floats vl ^floats sdpa-l ^floats bank-q
                ^floats mem-out ^floats net-out ^floats attn
                ^floats x-mid ^floats xn2 Rl]} ctx
        gate (:gate blk)
        ;; FFN: x-out = x-mid + down(silu(gate(xn2))·up(xn2))
        sw (g/swiglu-bwd xn2 (:gate-proj blk) (:up-proj blk) (:down-proj blk)
                         dx T d 128)
        ^floats dx' (:dx sw)
        {:keys [dWg dWu dWd]} sw
        _ (when-not frz?
            (add-into! (gacc grads (str pre "gate_proj.weight") (* 128 d)) dWg)
            (add-into! (gacc grads (str pre "up_proj.weight") (* 128 d)) dWu)
            (add-into! (gacc grads (str pre "down_proj.weight") (* 128 d)) dWd))
        {^floats dxm1 :dx ^floats dn2 :dw} (g/rmsnorm-bwd x-mid (:norm2 blk) dx' T d m/eps)
        _ (when-not frz? (add-into! (gacc grads (str pre "norm2.weight") d) dn2))
        dx-mid (float-array (* T d))
        _ (dotimes [i (* T d)]
            (aset dx-mid i (float (+ (aget dx i) (aget dxm1 i)))))
        ;; o-proj
        {^floats dattn :dx dWo :dW} (g/linear-bwd attn (:o-proj blk) dx-mid T d d)
        _ (when-not frz? (add-into! (gacc grads (str pre "o_proj.weight") (* d d)) dWo))
        dmixed (col-slice dattn T d 16 16)
        ;; gate backward → dq-long, dsdpa-l, dmem, dnet
        gate-res
        (cond
          (and mem-out net-out)
          (let [r (g/gate-train-bwd gate (t->h bank-q T) (t->h sdpa-l T)
                                    (t->h mem-out T) (t->h net-out T)
                                    Rl 2 T :st (t->h dmixed T))]
            (add-into! (gacc grads (str pre "long_gate.gate_proj_3") (* 2 3 hd)) (:dg3 r))
            (add-into! (gacc grads (str pre "long_gate.alpha_net") 2) (:dalpha r))
            (add-into! (gacc grads (str pre "long_gate.local_active_proj") (* 2 hd)) (:dlap r))
            (add-into! (gacc grads (str pre "long_gate.local_active_bias") 2) (:dlab r))
            {:dq (h->t (:dq r) T) :dsdpa (h->t (:dsdpa r) T)
             :dmem (h->t (:dmem r) T) :dnet (h->t (:dnet r) T)})
          net-out
          (let [dgp (gacc grads (str pre "long_gate.gate_proj") (* 2 hd))
                dal (gacc grads (str pre "long_gate.alpha_net") 2)]
            (gate2-net-bwd gate bank-q sdpa-l net-out T dmixed dgp dal))
          :else (throw (ex-info "block-train-bwd on a bankless path" {:layer layer})))
        ^floats dq-long (:dq gate-res)
        ^floats dsdpa-l (:dsdpa gate-res)
        ;; Local PKM (+z) backward — :main only
        _ (when mem-out
            (let [mem (:memory blk)
                  sqrt-n (long (:sqrt-n mem)) sub-dim (long (:sub-dim mem))
                  acc {:dKa (gacc grads (str pre "memory.K_a") (* sqrt-n sub-dim))
                       :dKb (gacc grads (str pre "memory.K_b") (* sqrt-n sub-dim))
                       :dqnorm-w (gacc grads (str pre "memory.q_norm.weight") 16)
                       :dV (dv-map grads :dv-local layer)}
                  dq-mem (pkm-train-bwd bank-q T mem (:trunk-id opts)
                                        (:dmem gate-res) (:z-scale opts) acc)]
              (add-into! dq-long dq-mem)))
        ;; NetBank backward
        _ (when net-out
            (let [nb (:netbank blk)
                  sqrt-n (long (:sqrt-n nb)) sub-dim (long (:sub-dim nb))
                  c-net (long (:c-net nb))
                  r (g/netbank-bwd bank-q T nb (:dnet gate-res))]
              (add-into! (gacc grads (str pre "netbank.K_a") (* sqrt-n sub-dim)) (:dKa r))
              (add-into! (gacc grads (str pre "netbank.K_b") (* sqrt-n sub-dim)) (:dKb r))
              (add-into! (gacc grads (str pre "netbank.q_norm.weight") 16) (:dqnorm-w r))
              (add-into! (gacc grads (str pre "netbank.expander.weight") (* 16 c-net)) (:dexp r))
              (merge-dv! (dv-map grads :dv-net layer) (:dV r))
              (add-into! dq-long (:dq r))))
        ;; long-tier SDPA (heads 2,3): no RoPE
        dkl (float-array (* T hd))
        dvl (float-array (* T hd))
        dq-full (float-array (* T d))
        _ (dotimes [h 2]
            (let [qh (col-slice q T d (* (+ 2 h) hd) hd)
                  doh (col-slice dsdpa-l T 16 (* h hd) hd)
                  {:keys [^floats dq ^floats dk ^floats dv]} (g/sdpa-causal-bwd qh kl vl doh T hd)]
              (col-add! dq-full T d (* (+ 2 h) hd) hd dq)
              (add-into! dkl dk)
              (add-into! dvl dv)))
        ;; gate/bank dq lands on the long-head q columns
        _ (col-add! dq-full T d 16 16 dq-long)
        ;; short tier (heads 0,1): SDPA bwd then RoPE-transpose on dq, dks
        dks (float-array (* T hd))
        dvs (float-array (* T hd))
        _ (dotimes [h 2]
            (let [qh (col-slice q T d (* h hd) hd)
                  doh (col-slice dattn T d (* h hd) hd)
                  {:keys [^floats dq ^floats dk ^floats dv]} (g/sdpa-causal-bwd qh ks vs doh T hd)]
              (dotimes [ti T] (g/rope-bwd-at! dq (* ti hd) rope ti hd))
              (col-add! dq-full T d (* h hd) hd dq)
              (add-into! dks dk)
              (add-into! dvs dv)))
        _ (dotimes [ti T] (g/rope-bwd-at! dks (* ti hd) rope ti hd))
        ;; projections back to xn
        dxn (float-array (* T d))
        proj-bwd (fn [^floats W ^floats dy out-dim ^String nm]
                   (let [{:keys [^floats dx dW]} (g/linear-bwd xn W dy T d (long out-dim))]
                     (add-into! dxn dx)
                     (when-not frz?
                       (add-into! (gacc grads (str pre nm) (* (long out-dim) d)) dW))))
        _ (proj-bwd (:q-proj blk) dq-full d "q_proj.weight")
        _ (proj-bwd (:k-proj-s blk) dks hd "k_proj_s.weight")
        _ (proj-bwd (:v-proj-s blk) dvs hd "v_proj_s.weight")
        _ (proj-bwd (:k-proj-l blk) dkl hd "k_proj_l.weight")
        _ (proj-bwd (:v-proj-l blk) dvl hd "v_proj_l.weight")
        {^floats dx1 :dx ^floats dn1 :dw} (g/rmsnorm-bwd x-in (:norm1 blk) dxn T d m/eps)
        _ (when-not frz? (add-into! (gacc grads (str pre "norm1.weight") d) dn1))
        dx-in (float-array (* T d))]
    (dotimes [i (* T d)]
      (aset dx-in i (float (+ (aget dx-mid i) (aget dx1 i)))))
    dx-in))

;; ── full-model train forward (one batch row) ──

(defn forward-train
  "Train-mode forward of one batch row.
   tokens: seq of T longs; mode :main|:teacher|:student; R: for :main a
   vector of 24 flat (H,T) float[] draws (per local layer), else nil.
   Returns {:logits (T,256) :x-final :xf :ctxs [32] :z-lses [24 or nil]}."
  [model tokens trunk-id mode R]
  (let [d 32 T (count tokens)
        ^floats emb (:tok-emb model)
        x0 (float-array (* T d))]
    (dotimes [ti T]
      (System/arraycopy emb (* (long (nth tokens ti)) d) x0 (* ti d) d))
    (loop [i 0 x x0 ctxs (transient []) local-i 0]
      (if (= i 32)
        (let [ctxs (persistent! ctxs)
              xf (t/data (t/rms-norm (t/tensor [T d] x)
                                     (t/tensor [d] (:norm-final model)) m/eps))
              logits (t/data (t/linear (t/tensor [T d] xf)
                                       (t/tensor [256 d] (:tok-emb model))))]
          {:logits logits :x-final x :xf xf :ctxs ctxs
           :z-lses (when (= mode :main)
                     (mapv #(:z-lse (:ctx %)) (take 24 ctxs)))})
        (let [blk (nth (:blocks model) i)
              local? (some? (:memory blk))
              Rl (when (and (= mode :main) local?) (nth R local-i))
              {:keys [x-out ctx]} (block-train-fwd blk (:rope model) x T
                                                   trunk-id mode Rl)]
          (recur (inc i) ^floats x-out (conj! ctxs {:ctx ctx :blk blk})
                 (if local? (inc local-i) local-i)))))))

(defn backward-train
  "Backward of one batch row from dlogits (T,256). Accumulates all param
   grads into `grads`. opts {:mode :main|:student :z-scale :trunk-id}.
   freeze-trunk (:student): tok-emb gets NO grad (detached emb-w on both
   the gather and the tied head — core.lpy forward), norm-final DOES
   (applied as a module, not via _fnorm — reference behavior)."
  [model fwd tokens ^floats dlogits T grads opts]
  (let [T (long T) d 32 V 256
        frz? (= (:mode opts) :student)
        ^floats emb (:tok-emb model)
        ^floats xf (:xf fwd)
        ^floats x-final (:x-final fwd)
        demb (when-not frz? (gacc grads "tok_emb.weight" (* V d)))
        dxf (float-array (* T d))]
    ;; tied head: logits = xf · embᵀ
    (dotimes [ti T]
      (dotimes [v V]
        (let [dl (aget dlogits (+ (* ti V) v))]
          (when-not (zero? dl)
            (let [voff (* v d) xoff (* ti d)]
              (dotimes [c d]
                (aset dxf (+ xoff c)
                      (float (+ (aget dxf (+ xoff c)) (* dl (aget emb (+ voff c))))))
                (when demb
                  (aset ^floats demb (+ voff c)
                        (float (+ (aget ^floats demb (+ voff c))
                                  (* dl (aget xf (+ xoff c)))))))))))))
    ;; norm-final (module — never trunk-frozen in the reference)
    (let [{^floats dx :dx ^floats dwf :dw}
          (g/rmsnorm-bwd x-final (:norm-final model) dxf T d m/eps)]
      (add-into! (gacc grads "norm_final.weight" d) dwf)
      ;; blocks, reversed
      (loop [i 31 dx dx]
        (if (neg? i)
          ;; embedding gather scatter (skip when frozen)
          (when demb
            (dotimes [ti T]
              (let [voff (* (long (nth tokens ti)) d) xoff (* ti d)]
                (dotimes [c d]
                  (aset ^floats demb (+ voff c)
                        (float (+ (aget ^floats demb (+ voff c))
                                  (aget dx (+ xoff c)))))))))
          (let [{:keys [ctx blk]} (nth (:ctxs fwd) i)]
            (recur (dec i)
                   ^floats (block-train-bwd blk ctx (:rope model) dx T grads
                                            (assoc opts :layer i)))))))
    nil))
