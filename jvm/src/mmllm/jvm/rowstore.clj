(ns mmllm.jvm.rowstore
  "Packed primitive sparse-row stores (M7 prerequisite — the follow-up
   stamped in docs/jvm-port-bench.md): replaces the boxed
   HashMap<Long, float[]> rows used for sparse V grads, sparse-Adam
   moments and bank overlays. Per touched row the boxed layout costs
   ~115 B (HashMap.Node + boxed Long + small float[] object headers);
   this layout costs width·4 B payload + ~26 B of index (open-addressing
   long key + int slot at ≤0.5 load, plus a slot→row long for
   iteration) — 2-3× denser, and the payload lives in a few large chunk
   arrays instead of millions of tiny objects (GC scan cost drops
   accordingly). That is what lets a T=256 B=16 step fit the 15 GB box
   (see the bench doc's 'Why T=64' section).

   Semantics are IDENTICAL to the boxed maps — a pure data-structure
   swap, pinned by the five parity gates:
   - rows are get-or-created zero-filled on first touch;
   - per-row accumulation (rsAxpyRow / rsAddRow) does the exact f32
     arithmetic of the old per-row float[] loops:
     v' = (float)(v + (double)a · (double)src[c]);
   - dv->sorted output sorts row keys ascending exactly like the old
     (sort (keys dv)) path;
   - iteration (rsRowOfSlot over 0..size) is insertion-ordered, which
     is deterministic; cross-row order never affects values (each row
     accumulates independently).

   Two implementations of IRowStore:
   - PackedRowMap  — single-writer open-addressing map (linear probe,
     fibonacci hash, power-of-two capacity, grow at 0.5 load). Values
     live in 4096-row float[] chunks.
   - ShardedRowMap — N contiguous-row-range shards of PackedRowMap.
     The hogwild shared V_local grad container in the parallel step:
     each router writes only rows in its own trunk slice
     [t·rows-per-shard, (t+1)·rows-per-shard), so each shard has
     exactly one writer thread — lock-free AND bit-deterministic, same
     argument as the previous shared ConcurrentHashMap but without the
     boxed nodes. Shard ranges ascend with row index, so concatenating
     per-shard sorted keys is globally sorted.")

(set! *warn-on-reflection* true)

(definterface IRowStore
  (^long rsWidth [])
  (^long rsSize [])
  (^long rsSlot [^long row])            ;; -1 when absent
  (^long rsEnsureSlot [^long row])      ;; get-or-create (zero row)
  (^floats rsChunkOf [^long slot])
  (^long rsOffsetOf [^long slot])       ;; float offset of the row in its chunk
  (^long rsRowOfSlot [^long slot])
  (^void rsGrow [])
  (^void rsAxpyRow [^long row ^double a ^floats src ^long srcOff])
  (^void rsAddRow [^long row ^floats src ^long srcOff])
  (^void rsPutRow [^long row ^floats src ^long srcOff])
  (^boolean rsCopyRow [^long row ^floats dst ^long dstOff])
  (^longs rsSortedRows []))

(def ^:const ^long CHUNK-SHIFT 12)                    ;; 4096 rows / chunk
(def ^:const ^long CHUNK-ROWS (bit-shift-left 1 CHUNK-SHIFT))
(def ^:const ^long CHUNK-MASK (dec CHUNK-ROWS))

(defn- mix ^long [^long row]
  ;; fibonacci-ish 64-bit mix; keys are bank row indices (always >= 0)
  (let [h (unchecked-multiply row -7046029254386353131)]
    (bit-xor h (unsigned-bit-shift-right h 32))))

(deftype PackedRowMap
  [^long width
   ^:unsynchronized-mutable ^longs keyt   ;; open-addressing keys, -1 empty
   ^:unsynchronized-mutable ^ints slott   ;; parallel: slot of that key
   ^:unsynchronized-mutable ^long mask
   ^:unsynchronized-mutable ^long n
   ^:unsynchronized-mutable ^objects vchunks   ;; float[CHUNK-ROWS·width] each
   ^:unsynchronized-mutable ^objects rchunks]  ;; long[CHUNK-ROWS] each (slot → row)

  IRowStore
  (rsWidth [_] width)
  (rsSize [_] n)

  (rsGrow [_]
    (let [^longs oldk keyt
          ^ints olds slott
          ncap (* 2 (inc mask))
          nk (long-array ncap)
          ns' (int-array ncap)
          nm (dec ncap)]
      (java.util.Arrays/fill nk -1)
      (dotimes [i (alength oldk)]
        (let [k (aget oldk i)]
          (when-not (= k -1)
            (loop [j (bit-and (mix k) nm)]
              (if (= -1 (aget nk j))
                (do (aset nk j k)
                    (aset ns' j (aget olds i)))
                (recur (bit-and (inc j) nm)))))))
      (set! keyt nk)
      (set! slott ns')
      (set! mask (long nm))))

  (rsSlot [_ row]
    (let [^longs ks keyt ^ints sl slott m mask]
      (loop [i (bit-and (mix row) m)]
        (let [k (aget ks i)]
          (cond (= k -1) -1
                (= k row) (long (aget sl i))
                :else (recur (bit-and (inc i) m)))))))

  (rsEnsureSlot [this row]
    ;; grow eagerly so the probe-insert loop below stays in tail
    ;; position (set! on mutable fields is illegal inside an
    ;; expression-position loop, which the compiler lifts to a fn).
    ;; Capacity never affects values or iteration order, so growing on
    ;; an ensure of an EXISTING row is harmless.
    (when (>= (* 2 (inc n)) (inc mask)) (.rsGrow this))
    (when (>= (bit-shift-right n CHUNK-SHIFT) (alength vchunks))
      (let [cap (alength vchunks)
            nv (object-array (* 2 cap))
            nr (object-array (* 2 cap))]
        (System/arraycopy vchunks 0 nv 0 cap)
        (System/arraycopy rchunks 0 nr 0 cap)
        (set! vchunks nv)
        (set! rchunks nr)))
    (let [ci (bit-shift-right n CHUNK-SHIFT)]
      (when (nil? (aget vchunks ci))
        (aset vchunks ci (float-array (* CHUNK-ROWS width)))
        (aset rchunks ci (long-array CHUNK-ROWS))))
    (let [^longs ks keyt ^ints sl slott m mask nn n
          ^objects rcs rchunks
          found
          (loop [i (bit-and (mix row) m)]
            (let [k (aget ks i)]
              (cond
                (= k row) (long (aget sl i))
                (= k -1) (let [slot nn]
                           (aset ks i row)
                           (aset sl i (int slot))
                           (aset ^longs (aget rcs (bit-shift-right slot CHUNK-SHIFT))
                                 (bit-and slot CHUNK-MASK) row)
                           (- (- slot) 1))              ;; flag: inserted
                :else (recur (bit-and (inc i) m)))))]
      (if (neg? found)
        (let [slot (- (- found) 1)]
          (set! n (inc n))
          slot)
        found)))

  (rsChunkOf [_ slot] (aget vchunks (bit-shift-right slot CHUNK-SHIFT)))
  (rsOffsetOf [_ slot] (* (bit-and slot CHUNK-MASK) width))
  (rsRowOfSlot [_ slot]
    (aget ^longs (aget rchunks (bit-shift-right slot CHUNK-SHIFT))
          (bit-and slot CHUNK-MASK)))

  (rsAxpyRow [this row a src srcOff]
    (let [slot (.rsEnsureSlot this row)
          ^floats ch (.rsChunkOf this slot)
          off (.rsOffsetOf this slot)]
      (dotimes [c width]
        (aset ch (+ off c)
              (float (+ (aget ch (+ off c)) (* a (aget src (+ srcOff c)))))))))

  (rsAddRow [this row src srcOff]
    (let [slot (.rsEnsureSlot this row)
          ^floats ch (.rsChunkOf this slot)
          off (.rsOffsetOf this slot)]
      (dotimes [c width]
        (aset ch (+ off c)
              (float (+ (aget ch (+ off c)) (aget src (+ srcOff c))))))))

  (rsPutRow [this row src srcOff]
    (let [slot (.rsEnsureSlot this row)
          ^floats ch (.rsChunkOf this slot)
          off (.rsOffsetOf this slot)]
      (System/arraycopy src (int srcOff) ch (int off) (int width))))

  (rsCopyRow [this row dst dstOff]
    (let [slot (.rsSlot this row)]
      (if (neg? slot)
        false
        (do (System/arraycopy ^floats (.rsChunkOf this slot)
                              (int (.rsOffsetOf this slot))
                              dst (int dstOff) (int width))
            true))))

  (rsSortedRows [this]
    (let [out (long-array n)]
      (dotimes [s n] (aset out s (.rsRowOfSlot this s)))
      (java.util.Arrays/sort out)
      out))

  Object
  (toString [_] (str "PackedRowMap[width=" width " n=" n "]")))

(defn packed-row-map
  "New single-writer packed row map of `width` floats per row."
  (^mmllm.jvm.rowstore.IRowStore [width] (packed-row-map width 1024))
  (^mmllm.jvm.rowstore.IRowStore [width init-cap]
   (let [cap (loop [c 16] (if (>= c (long init-cap)) c (recur (* 2 c))))
         kt (long-array cap)]
     (java.util.Arrays/fill kt -1)
     (PackedRowMap. (long width) kt (int-array cap) (dec cap) 0
                    (object-array 4) (object-array 4)))))

(def ^:const ^long SHARD-SHIFT 40)

(deftype ShardedRowMap [^long width ^long rows-per-shard ^objects shards]
  IRowStore
  (rsWidth [_] width)
  (rsSize [_]
    (loop [i 0 s 0]
      (if (< i (alength shards))
        (recur (inc i) (+ s (.rsSize ^IRowStore (aget shards i))))
        s)))
  (rsGrow [_] nil)
  (rsSlot [_ row]
    (let [sh (quot row rows-per-shard)
          inner (.rsSlot ^IRowStore (aget shards sh) row)]
      (if (neg? inner) -1 (bit-or (bit-shift-left sh SHARD-SHIFT) inner))))
  (rsEnsureSlot [_ row]
    (let [sh (quot row rows-per-shard)]
      (bit-or (bit-shift-left sh SHARD-SHIFT)
              (.rsEnsureSlot ^IRowStore (aget shards sh) row))))
  (rsChunkOf [_ slot]
    (.rsChunkOf ^IRowStore (aget shards (bit-shift-right slot SHARD-SHIFT))
                (bit-and slot (dec (bit-shift-left 1 SHARD-SHIFT)))))
  (rsOffsetOf [_ slot]
    (.rsOffsetOf ^IRowStore (aget shards (bit-shift-right slot SHARD-SHIFT))
                 (bit-and slot (dec (bit-shift-left 1 SHARD-SHIFT)))))
  (rsRowOfSlot [_ slot]
    (.rsRowOfSlot ^IRowStore (aget shards (bit-shift-right slot SHARD-SHIFT))
                  (bit-and slot (dec (bit-shift-left 1 SHARD-SHIFT)))))
  (rsAxpyRow [_ row a src srcOff]
    (.rsAxpyRow ^IRowStore (aget shards (quot row rows-per-shard)) row a src srcOff))
  (rsAddRow [_ row src srcOff]
    (.rsAddRow ^IRowStore (aget shards (quot row rows-per-shard)) row src srcOff))
  (rsPutRow [_ row src srcOff]
    (.rsPutRow ^IRowStore (aget shards (quot row rows-per-shard)) row src srcOff))
  (rsCopyRow [_ row dst dstOff]
    (.rsCopyRow ^IRowStore (aget shards (quot row rows-per-shard)) row dst dstOff))
  (rsSortedRows [this]
    ;; shard s covers rows [s·rps, (s+1)·rps) — concat of per-shard
    ;; sorted keys is globally sorted
    (let [tot (.rsSize this)
          out (long-array tot)]
      (loop [i 0 off 0]
        (when (< i (alength shards))
          (let [^longs sr (.rsSortedRows ^IRowStore (aget shards i))]
            (System/arraycopy sr 0 out off (alength sr))
            (recur (inc i) (+ off (alength sr))))))
      out))
  Object
  (toString [_] (str "ShardedRowMap[width=" width " shards=" (alength shards) "]")))

(defn sharded-row-map
  "Row map sharded into n-shards contiguous row ranges of rows-per-shard
   rows each. Safe for concurrent writers when every writer's rows fall
   in its own shard range (the parallel step's per-trunk V_local slices)."
  ^mmllm.jvm.rowstore.IRowStore [n-shards rows-per-shard width]
  (let [shards (object-array (long n-shards))]
    (dotimes [i (long n-shards)]
      (aset shards i (packed-row-map width)))
    (ShardedRowMap. (long width) (long rows-per-shard) shards)))

(defn row-store? [x] (instance? IRowStore x))

(defn store-size
  "Row count of either store flavor or a java.util.Map."
  ^long [dv]
  (if (instance? IRowStore dv)
    (.rsSize ^IRowStore dv)
    (long (.size ^java.util.Map dv))))

(defn merge-into!
  "dst[row] += src[row] for every row of src (get-or-create zero rows in
   dst). src iterates in insertion order (PackedRowMap slots 0..n);
   dst may be packed or sharded. Per-row f32 add order matches the old
   boxed merge-dv! exactly (cross-row order never affects values)."
  [^IRowStore dst ^IRowStore src]
  (let [n (.rsSize src)]
    (loop [s 0]
      (when (< s n)
        (.rsAddRow dst (.rsRowOfSlot src s) (.rsChunkOf src s) (.rsOffsetOf src s))
        (recur (inc s))))))
