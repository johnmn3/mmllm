(ns mmllm.jvm.evals
  "eval-bpc + ablation Δs + the V-moved check (M7, spec evals.clj).

   eval-bpc mirrors core.lpy eval-bpc: consecutive non-overlapping
   T-windows from the start of the held-out stream (x = data[iT..iT+T),
   y = data[iT+1..iT+T+1)), window i routed to trunk (i mod n-trunks)
   — deterministic, so control and ablated passes see identical
   routing and the Δ is the bank-tier signal. NLL is summed per window
   and reduced in window order (double accumulation), so the result is
   bit-identical at any thread count.

   Ablation NEVER touches the bank files: it re-wires the model's bank
   maps with :zero? true (params/bank-row! then reads all-zero rows —
   the exact effect of the reference's zero-the-V-in-place, without the
   save/restore round-trip), evals, and throws the wired model away.

   V-moved (CLAUDE.md 2026-05-13, MANDATORY): Δ-ablation alone is NOT
   proof the bank V trained. moved% = ‖V_cur − V_init‖/‖V_init‖ and
   cos(V_cur, V_init), computed per tier by streaming the trained
   scratch .bin files against the pristine originals."
  (:require [clojure.java.io :as io]
            [mmllm.jvm.model :as m])
  (:import [java.io File RandomAccessFile]
           [java.nio ByteBuffer ByteOrder]
           [java.util.concurrent Callable ExecutorService Future]))

(set! *warn-on-reflection* true)

(def ^:const LN2 (Math/log 2.0))

(defn- window-nll
  "Σ over T positions of -(log softmax(logits[t]))[y[t]] — double acc,
   same max-subtracted logsumexp as the train-side CE."
  ^double [^floats logits ^longs y ^long T ^long V]
  (loop [ti 0 acc 0.0]
    (if (= ti T)
      acc
      (let [off (* ti V)
            tgt (aget y ti)
            mx (loop [j 0 mv Double/NEGATIVE_INFINITY]
                 (if (< j V) (recur (inc j) (max mv (double (aget logits (+ off j))))) mv))
            sum (loop [j 0 s 0.0]
                  (if (< j V)
                    (recur (inc j) (+ s (Math/exp (- (aget logits (+ off j)) mx))))
                    s))]
        (recur (inc ti)
               (+ acc (- (+ mx (Math/log sum)) (aget logits (+ off tgt)))))))))

(defn eval-bpc
  "bpc of `model` over held-out byte stream `data` (byte[]), windows of
   T, capped at max-tokens, trunk round-robin over n-trunks. Windows are
   evaluated on `pool` when given (order-independent: fixed-order
   reduction). → {:bpc :n-tokens :n-windows}"
  [model ^bytes data T n-trunks max-tokens ^ExecutorService pool]
  (let [T (long T) V 256
        N (alength data)
        n-wins (min (quot (dec N) T) (quot (long max-tokens) T))
        eval-win (fn [^long i]
                   (let [off (* i T)
                         x (mapv #(long (bit-and (aget data (int (+ off (long %)))) 0xFF))
                                 (range T))
                         y (long-array T)
                         _ (dotimes [t T]
                             (aset y t (long (bit-and (aget data (int (+ off t 1))) 0xFF))))
                         logits (m/forward model x (rem i (long n-trunks)))]
                     (window-nll logits y T V)))
        nlls (if pool
               (let [futs (mapv (fn [i] (.submit pool ^Callable (fn [] (eval-win i))))
                                (range n-wins))]
                 (mapv (fn [^Future f] (.get f)) futs))
               (mapv eval-win (range n-wins)))
        total (loop [i 0 s 0.0]
                (if (< i n-wins) (recur (inc i) (+ s (double (nth nlls i)))) s))
        n-toks (* n-wins T)]
    {:bpc (/ (/ total n-toks) LN2) :n-tokens n-toks :n-windows n-wins}))

(defn ablate
  "Model with tier(s) zeroed: every matching bank map gets :zero? true
   (reads become zero rows; files untouched). tier ∈ :local :net :both."
  [model tier]
  (let [local? (contains? #{:local :both} tier)
        net? (contains? #{:net :both} tier)]
    (update model :blocks
            (fn [blocks]
              (mapv (fn [blk]
                      (cond-> blk
                        (and local? (:memory blk))
                        (update-in [:memory :bank] assoc :zero? true)
                        (and net? (:netbank blk))
                        (update-in [:netbank :bank] assoc :zero? true)))
                    blocks)))))

(defn- file-stats
  "Stream two equally-sized fp32 .bin files; accumulate the moved%/cos
   sufficient statistics in doubles."
  [^File cur ^File init]
  (assert (= (.length cur) (.length init))
          (str cur " and " init " sizes differ"))
  (with-open [rc (RandomAccessFile. cur "r")
              ri (RandomAccessFile. init "r")]
    (let [chunk (* 1024 1024)
          bc (byte-array chunk)
          bi (byte-array chunk)
          total (.length cur)]
      (loop [off 0 sii 0.0 scc 0.0 sci 0.0 sdd 0.0]
        (if (>= off total)
          {:sii sii :scc scc :sci sci :sdd sdd}
          (let [n (min chunk (- total off))
                _ (.readFully rc bc 0 (int n))
                _ (.readFully ri bi 0 (int n))
                fbc (.asFloatBuffer (.order (ByteBuffer/wrap bc 0 (int n))
                                            ByteOrder/LITTLE_ENDIAN))
                fbi (.asFloatBuffer (.order (ByteBuffer/wrap bi 0 (int n))
                                            ByteOrder/LITTLE_ENDIAN))
                nf (quot (long n) 4)
                sums (loop [j 0 a sii b scc c sci d sdd]
                       (if (= j nf)
                         [a b c d]
                         (let [vi (double (.get fbi (int j)))
                               vc (double (.get fbc (int j)))
                               dv (- vc vi)]
                           (recur (inc j) (+ a (* vi vi)) (+ b (* vc vc))
                                  (+ c (* vc vi)) (+ d (* dv dv))))))]
            (recur (+ off (long n)) (double (nth sums 0)) (double (nth sums 1))
                   (double (nth sums 2)) (double (nth sums 3)))))))))

(defn v-moved
  "moved% + cos for one tier across all its layers.
   files: seq of [cur-file init-file] pairs.
   → {:moved-pct :cos :l2-init :l2-delta}"
  [file-pairs]
  (let [{:keys [sii scc sci sdd]}
        (reduce (fn [acc [c i]]
                  (merge-with + acc (file-stats (io/file c) (io/file i))))
                {:sii 0.0 :scc 0.0 :sci 0.0 :sdd 0.0}
                file-pairs)
        l2i (Math/sqrt sii)
        l2c (Math/sqrt scc)
        l2d (Math/sqrt sdd)]
    {:moved-pct (* 100.0 (/ l2d (max l2i 1e-30)))
     :cos (/ sci (max (* l2i l2c) 1e-30))
     :l2-init l2i :l2-delta l2d}))
