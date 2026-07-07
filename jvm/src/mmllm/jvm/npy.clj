(ns mmllm.jvm.npy
  "Minimal NPY / NPZ reader — enough for the goldens + dense.npz fixtures.
   Supports <f4 <f8 <i8 <i4 |u1 little-endian C-order arrays."
  (:require [clojure.string :as str])
  (:import [java.io DataInputStream BufferedInputStream InputStream EOFException]
           [java.nio ByteBuffer ByteOrder]
           [java.util.zip ZipFile]))

(set! *warn-on-reflection* true)

(defn- read-fully ^bytes [^InputStream in ^long n]
  (let [buf (byte-array n)]
    (loop [off 0]
      (if (< off n)
        (let [r (.read in buf off (- n off))]
          (when (neg? r) (throw (EOFException. "short read")))
          (recur (+ off r)))
        buf))))

(defn- parse-header [^String h]
  (let [descr (second (re-find #"'descr':\s*'([^']+)'" h))
        fortran (boolean (re-find #"'fortran_order':\s*True" h))
        shape-str (second (re-find #"'shape':\s*\(([^)]*)\)" h))
        shape (->> (str/split (or shape-str "") #",")
                   (map str/trim) (remove empty?)
                   (mapv #(Long/parseLong %)))]
    (when fortran
      (throw (ex-info "fortran_order npy not supported" {:header h})))
    {:descr descr :shape shape}))

(defn read-npy
  "InputStream -> {:dtype kw :shape [..] :data primitive-array}.
   f8/i8/i4/u1 are widened/kept as {:dtype :f8/:i8/...}; f4 -> float-array."
  [^InputStream in]
  (let [magic (read-fully in 6)]
    (when-not (and (= (bit-and (aget magic 0) 0xff) 0x93)
                   (= (String. ^bytes (java.util.Arrays/copyOfRange magic 1 6)) "NUMPY"))
      (throw (ex-info "bad npy magic" {})))
    (let [ver (read-fully in 2)
          major (aget ver 0)
          hlen (if (= major 1)
                 (let [b (read-fully in 2)]
                   (bit-or (bit-and (aget b 0) 0xff)
                           (bit-shift-left (bit-and (aget b 1) 0xff) 8)))
                 (let [b (read-fully in 4)]
                   (.getInt (.order (ByteBuffer/wrap b) ByteOrder/LITTLE_ENDIAN))))
          {:keys [descr shape]} (parse-header (String. (read-fully in hlen) "ASCII"))
          n (long (reduce * 1 shape))]
      (case descr
        "<f4" (let [bb (.order (ByteBuffer/wrap (read-fully in (* 4 n))) ByteOrder/LITTLE_ENDIAN)
                    fb (.asFloatBuffer bb)
                    a (float-array n)]
                (.get fb a)
                {:dtype :f4 :shape shape :data a})
        "<f8" (let [bb (.order (ByteBuffer/wrap (read-fully in (* 8 n))) ByteOrder/LITTLE_ENDIAN)
                    db (.asDoubleBuffer bb)
                    a (double-array n)]
                (.get db a)
                {:dtype :f8 :shape shape :data a})
        "<i8" (let [bb (.order (ByteBuffer/wrap (read-fully in (* 8 n))) ByteOrder/LITTLE_ENDIAN)
                    lb (.asLongBuffer bb)
                    a (long-array n)]
                (.get lb a)
                {:dtype :i8 :shape shape :data a})
        "<i4" (let [bb (.order (ByteBuffer/wrap (read-fully in (* 4 n))) ByteOrder/LITTLE_ENDIAN)
                    ib (.asIntBuffer bb)
                    a (int-array n)]
                (.get ib a)
                {:dtype :i4 :shape shape :data a})
        "|u1" {:dtype :u1 :shape shape :data (read-fully in n)}
        (throw (ex-info (str "unsupported npy dtype " descr) {:descr descr}))))))

(defn read-npz
  "Path -> {entry-name (sans .npy) -> npy map}."
  [path]
  (with-open [zf (ZipFile. (str path))]
    (into {}
          (for [^java.util.zip.ZipEntry e (enumeration-seq (.entries zf))]
            [(str/replace (.getName e) #"\.npy$" "")
             (with-open [in (BufferedInputStream. (.getInputStream zf e))]
               (read-npy in))]))))
