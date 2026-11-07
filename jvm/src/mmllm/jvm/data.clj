(ns mmllm.jvm.data
  "Native corpus staging + byte-level batcher (M7, spec §11).

   Corpora are the release-tarball staging used by the torch reference
   (scripts/fetch_static_assets.sh corpora → workers/dispatcher/corpora,
   .part-NN chunks reassembled exactly like scripts/train.sh does).
   Byte-level 'tokenization' is unsigned byte → long, straight off a
   read-only mmap.

   Batch semantics mirror core.lpy's mix-batch-multi-trunk:
   - ONE corpus per batch, drawn from the 9-corpus FIM-heavy prod mix
     ('chunky mixing' — proportions hold across many batches);
   - that corpus is content-sharded into n-trunks contiguous byte
     ranges; trunk t samples its window from range t only;
   - the held-out eval stream is pick-mix-val: the LAST 4096 bytes of
     each mix corpus concatenated in mix order (never sampled by the
     training windows above, which run on range starts < tail for any
     corpus much larger than 4096·n-trunks... strictly: the torch
     sampler has the same property and the same caveat).

   DELIBERATE SAMPLER DEVIATION (spec §11 'document, don't hide'):
   randomness comes from a seeded java.util.Random per step —
   multinomial draw via cumulative weights + one nextInt per trunk —
   NOT torch's RNG. Loss curves are therefore not point-by-point
   comparable with a torch run; distributionally the sampler is the
   same. Deterministic given (seed, step)."
  (:require [clojure.java.io :as io])
  (:import [java.io File]
           [java.nio ByteBuffer ByteOrder]
           [java.nio.channels FileChannel FileChannel$MapMode]
           [java.nio.file Files Paths StandardOpenOption StandardCopyOption]
           [java.util Random]))

(set! *warn-on-reflection* true)

(def nine-mix
  "The prod 9-corpus FIM-heavy mix (scripts/train.sh fim-json-v3 branch):
   [relative-corpus-path weight]."
  [["fim-json-v3.train.bin"                25.0]
   ["battery/cosmopedia.train.bin"         10.0]
   ["battery/fineweb-edu.train.bin"        10.0]
   ["battery/magicoder.train.bin"          10.0]
   ["battery/hermes-funcall.train.bin"     10.0]
   ["battery/toolace.train.bin"            10.0]
   ["battery/aesop-fables.bin.train.bin"   10.0]
   ["battery/open-web-math.train.bin"      10.0]
   ["battery/tiny-stories.train.bin"        5.0]])

(defn- reassemble!
  "Ensure `dst` holds corpus `rel` from corpora root `src-root`:
   copy the single file, or cat the .part-?? chunks (train.sh's loop).
   Idempotent on size match."
  [^File src-root ^String rel ^File dst]
  (let [single (io/file src-root rel)
        parts (when-not (.exists single)
                (let [dir (.getParentFile (io/file src-root rel))
                      base (.getName (io/file rel))]
                  (->> (.listFiles dir)
                       (filter #(re-matches (re-pattern (str (java.util.regex.Pattern/quote base)
                                                             "\\.part-\\d+"))
                                            (.getName ^File %)))
                       (sort-by #(.getName ^File %)))))
        want (if (.exists single)
               (.length single)
               (reduce + 0 (map #(.length ^File %) parts)))]
    (assert (pos? (long want)) (str "corpus not found: " rel " under " src-root))
    (when-not (and (.exists dst) (= (.length dst) (long want)))
      (io/make-parents dst)
      (if (.exists single)
        (Files/copy (.toPath single) (.toPath dst)
                    ^"[Ljava.nio.file.CopyOption;"
                    (into-array java.nio.file.CopyOption
                                [StandardCopyOption/REPLACE_EXISTING]))
        (with-open [out (io/output-stream dst)]
          (doseq [^File p parts]
            (io/copy p out)))))
    dst))

(defn- mmap-ro ^ByteBuffer [^File f]
  (with-open [ch (FileChannel/open (Paths/get (.getPath f) (make-array String 0))
                                   (into-array StandardOpenOption
                                               [StandardOpenOption/READ]))]
    (let [b (.map ch FileChannel$MapMode/READ_ONLY 0 (.size ch))]
      (.order b ByteOrder/LITTLE_ENDIAN)
      b)))

(defn stage!
  "Stage the nine-mix corpora from `corpora-root` into `scratch-dir`
   (reassembling .part chunks) and mmap them read-only.
   → {:corpora [{:name :buf :n}] :weights [w...] :cum ^doubles}"
  [corpora-root scratch-dir]
  (let [src (io/file corpora-root)
        corpora (mapv (fn [[rel w]]
                        (let [dst (reassemble! src rel
                                               (io/file scratch-dir
                                                        (.getName (io/file rel))))
                              buf (mmap-ro dst)]
                          {:name (.getName (io/file rel))
                           :buf buf :n (long (.capacity buf)) :weight w}))
                      nine-mix)
        ws (mapv :weight corpora)
        tot (reduce + ws)
        cum (double-array (count ws))]
    (loop [i 0 acc 0.0]
      (when (< i (count ws))
        (let [acc' (+ acc (/ (double (nth ws i)) tot))]
          (aset cum i acc')
          (recur (inc i) acc'))))
    {:corpora corpora :weights ws :cum cum}))

(defn- draw-corpus ^long [{:keys [^doubles cum]} ^Random rnd]
  (let [u (.nextDouble rnd)
        n (alength cum)]
    (loop [i 0]
      (if (or (= i (dec n)) (< u (aget cum i)))
        i
        (recur (inc i))))))

(defn- window
  "T+1-byte window starting at off → {:x [T longs] :y [T longs]}."
  [^ByteBuffer buf ^long off ^long T]
  (let [x (long-array T) y (long-array T)
        b0 (long (bit-and (.get buf (int off)) 0xFF))]
    (loop [t 0 prev b0]
      (if (= t T)
        {:x (vec x) :y (vec y)}
        (let [nxt (long (bit-and (.get buf (int (+ off t 1))) 0xFF))]
          (aset x t prev)
          (aset y t nxt)
          (recur (inc t) nxt))))))

(defn mix-batch-multi-trunk
  "One training batch: draw a corpus by weight, content-shard it into
   n-trunks contiguous ranges, one T+1 window per trunk (B-per-trunk=1,
   the prod recipe). Deterministic given rnd's state.
   → {:x-rows :y-rows :trunk-ids :corpus-idx}"
  [mix ^Random rnd n-trunks T]
  (let [n-trunks (long n-trunks) T (long T)
        ci (draw-corpus mix rnd)
        {:keys [^ByteBuffer buf ^long n]} (nth (:corpora mix) ci)
        per (quot n n-trunks)
        rows (mapv (fn [t]
                     (let [t-start (* (long t) per)
                           t-len (- per T 1)
                           off (+ t-start (.nextInt rnd (int t-len)))]
                       (window buf off T)))
                   (range n-trunks))]
    {:x-rows (mapv :x rows)
     :y-rows (mapv :y rows)
     :trunk-ids (vec (range n-trunks))
     :corpus-idx ci}))

(defn val-tail
  "pick-mix-val: last `per` bytes of each mix corpus, concatenated in
   mix order → byte-array. Deterministic, held-out (training windows
   sample uniformly; the exact tail windows are ~never drawn)."
  ^bytes [mix ^long per]
  (let [chunks (mapv (fn [{:keys [^ByteBuffer buf ^long n]}]
                       (let [k (min n per)
                             a (byte-array k)
                             b (.duplicate buf)]
                         (.position b (int (- n k)))
                         (.get b a)
                         a))
                     (:corpora mix))
        tot (reduce + (map alength chunks))
        out (byte-array tot)]
    (loop [cs chunks off 0]
      (when (seq cs)
        (let [^bytes c (first cs)]
          (System/arraycopy c 0 out off (alength c))
          (recur (rest cs) (+ off (alength c))))))
    out))

(defn r-rows
  "Replay-style ST-Bernoulli uniform draws for one step: per batch row,
   24 local layers × flat (H=2, T) floats. Seeded per (seed, step, row)
   so results are independent of thread scheduling (spec §10.4)."
  [^long seed ^long step ^long B ^long T]
  (let [H 2]
    (mapv (fn [b]
            (let [r (Random. (unchecked-add (unchecked-multiply (+ seed step) 1000003)
                                            (* 7919 (long b))))]
              (mapv (fn [_]
                      (let [a (float-array (* H T))]
                        (dotimes [i (* H T)] (aset a i (.nextFloat r)))
                        a))
                    (range 24))))
          (range B))))
