(ns mmllm.jvm.tensor
  "Row-major float32 tensors as {:shape [..] :data ^floats}. Pure JVM —
   deliberately boring so parity gates audit math, not a library. The hot
   ops move onto Neanderthal/MKL behind this same API at M6."
  (:refer-clojure :exclude [get]))

(set! *warn-on-reflection* true)
(set! *unchecked-math* :warn-on-boxed)

(defn tensor
  ([shape] {:shape (vec shape)
            :data (float-array (long (reduce * 1 shape)))})
  ([shape ^floats data]
   (let [n (long (reduce * 1 shape))]
     (assert (= n (alength data)) (str "shape " shape " != data len " (alength data)))
     {:shape (vec shape) :data data})))

(defn numel ^long [t] (long (reduce * 1 (:shape t))))

(defn data ^floats [t] (:data t))

(defn reshape [t shape]
  (assert (= (long (reduce * 1 shape)) (numel t)))
  (assoc t :shape (vec shape)))

(defn from-npy
  "npy map (from mmllm.jvm.npy) -> f32 tensor (f8 narrowed)."
  [{:keys [dtype shape data]}]
  (case dtype
    :f4 (tensor shape data)
    :f8 (let [^doubles d data
              n (alength d)
              f (float-array n)]
          (dotimes [i n] (aset f i (float (aget d i))))
          (tensor shape f))))

;; ── elementwise ──

(defn copy [t] (tensor (:shape t) (java.util.Arrays/copyOf ^floats (:data t) (numel t))))

(defn add! [a b]
  (let [^floats x (:data a) ^floats y (:data b)]
    (dotimes [i (alength x)] (aset x i (+ (aget x i) (aget y i)))) a))

(defn mul! [a b]
  (let [^floats x (:data a) ^floats y (:data b)]
    (dotimes [i (alength x)] (aset x i (* (aget x i) (aget y i)))) a))

(defn scale! [a ^double s]
  (let [^floats x (:data a) s (float s)]
    (dotimes [i (alength x)] (aset x i (* (aget x i) s))) a))

;; ── linear algebra ──

(defn matmul
  "(m,k)·(k,n) -> (m,n). ikj loop order."
  [a b]
  (let [[m k] (:shape a) [k2 n] (:shape b)
        m (long m) k (long k) n (long n)]
    (assert (= k (long k2)) (str "matmul " (:shape a) " x " (:shape b)))
    (let [^floats A (:data a) ^floats B (:data b)
          C (float-array (* m n))]
      (dotimes [i m]
        (dotimes [p k]
          (let [aip (aget A (+ (* i k) p))]
            (when-not (zero? aip)
              (let [boff (* p n) coff (* i n)]
                (dotimes [j n]
                  (aset C (+ coff j)
                        (+ (aget C (+ coff j)) (* aip (aget B (+ boff j)))))))))))
      (tensor [m n] C))))

(defn linear
  "torch F.linear: x (.., in) · Wᵀ, W stored (out, in). x flattened to 2D."
  [x w]
  (let [xs (:shape x)
        in (long (peek xs))
        rows (quot (numel x) in)
        [out in2] (:shape w)
        out (long out)]
    (assert (= in (long in2)) (str "linear " xs " w " (:shape w)))
    (let [^floats X (:data x) ^floats W (:data w)
          Y (float-array (* rows out))]
      (dotimes [r rows]
        (let [xoff (* r in) yoff (* r out)]
          (dotimes [o out]
            (let [woff (* o in)]
              (loop [i 0 acc 0.0]
                (if (< i in)
                  (recur (inc i)
                         (+ acc (* (double (aget X (+ xoff i)))
                                   (double (aget W (+ woff i))))))
                  (aset Y (+ yoff o) (float acc))))))))
      (tensor (conj (pop xs) out) Y))))

;; ── reductions / activations over last dim ──

(defn softmax!
  "In-place softmax over the last dim."
  [t]
  (let [d (long (peek (:shape t)))
        rows (quot (numel t) d)
        ^floats X (:data t)]
    (dotimes [r rows]
      (let [off (* r d)
            mx (loop [i 0 m Float/NEGATIVE_INFINITY]
                 (if (< i d) (recur (inc i) (max m (aget X (+ off i)))) m))
            sum (loop [i 0 s 0.0]
                  (if (< i d)
                    (let [e (Math/exp (- (aget X (+ off i)) (double mx)))]
                      (aset X (+ off i) (float e))
                      (recur (inc i) (+ s e)))
                    s))]
        (dotimes [i d] (aset X (+ off i) (float (/ (aget X (+ off i)) sum))))))
    t))

(defn rms-norm
  "y = w ⊙ x / sqrt(mean(x²)+eps) over the last dim. Fresh output."
  [x w ^double eps]
  (let [d (long (peek (:shape x)))
        rows (quot (numel x) d)
        ^floats X (:data x) ^floats W (:data w)
        Y (float-array (numel x))]
    (dotimes [r rows]
      (let [off (* r d)
            ss (loop [i 0 s 0.0]
                 (if (< i d)
                   (let [v (double (aget X (+ off i)))] (recur (inc i) (+ s (* v v))))
                   s))
            inv (/ 1.0 (Math/sqrt (+ (/ ss d) eps)))]
        (dotimes [i d]
          (aset Y (+ off i) (float (* (aget X (+ off i)) inv (aget W i)))))))
    (tensor (:shape x) Y)))

(defn silu!
  [t]
  (let [^floats X (:data t)]
    (dotimes [i (alength X)]
      (let [v (double (aget X i))]
        (aset X i (float (/ v (+ 1.0 (Math/exp (- v))))))))
    t))

;; ── comparison (parity) ──

(defn max-abs-diff ^double [a b]
  (let [^floats x (:data a) ^floats y (:data b)]
    (assert (= (alength x) (alength y)))
    (loop [i 0 m 0.0]
      (if (< i (alength x))
        (recur (inc i) (max m (Math/abs (- (double (aget x i)) (double (aget y i))))))
        m))))

(defn max-rel-diff ^double [a b]
  (let [^floats x (:data a) ^floats y (:data b)]
    (loop [i 0 m 0.0]
      (if (< i (alength x))
        (let [d (Math/abs (- (double (aget x i)) (double (aget y i))))
              s (max 1e-8 (Math/abs (double (aget y i))))]
          (recur (inc i) (max m (/ d s))))
        m))))
