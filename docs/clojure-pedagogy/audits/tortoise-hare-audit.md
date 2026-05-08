# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2 1/2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"42"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:tortoise` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:winner` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'STRING_AS_CHAR_MISCLAIM': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\space` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK': 1}
    - [SMALL_INT_LEAK] form=`(+ 2 3)` — small-int answer 5 leaks via resolution-slot phrasing
    - [CLAUSE_STACK_OVERFLOW] form=`(* (+ 1 2) 3)` — sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(* (+ 1 2) 3)` — sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'REPEATED_OPENER_FRAGMENT': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPEATED_OPENER_FRAGMENT] form=`(* 4 5)` — opener fragment 'at the edge of the hilltop,' also appears later in user_msg
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 7 8)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(- 20 7)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2 3 4)` — sentence with 6 commas reads as AI-output cadence: 'You can split a heap." To add 2, 4, 6, and 2, she\ncomposed the multi-arg sum, su'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'The answer is\nprecise." To add 7, 9, 7, and 5, he composed the multi-arg sum,\nsu'
    - [CLAUSE_STACK_OVERFLOW] form=`(- 100 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You can split a heap." To subtract 5, 9, and 9 from 576, she\ncomposed the multi-'
    - [CLAUSE_STACK_OVERFLOW] form=`(- 100 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You can split a heap." To subtract 9, 0, and 1 from 401, he\ncomposed the multi-a'

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 6}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 2, 1, 6, 3, and 0, she with eyes always on the path compo'
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 8, 2, 3, 5, and 6, she with eyes always on the path compo'
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 7 commas reads as AI-output cadence: 'You can split a heap." To find the maximum of 5, 3, 5, 9, and 6, he\ncomposed the'

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(inc 5)` — answer 6 in narrative

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 8 commas reads as AI-output cadence: 'Concat strings together,\nand the threads are spliced; cut a substring out, and y'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 8 commas reads as AI-output cadence: 'Concat strings together,\nand the threads are spliced; cut a substring out, and y'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 6 commas reads as AI-output cadence: 'To use str to join the integer 1, the plus sign, the integer 0, the equals sign,'

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 213 words

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To count '
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 232 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To define x, shadow it '
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To define x, shadow it '

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — sentence with 6 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To bind a to 7, b to a+'
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 224 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 205 words

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1 :b 2} :a)` — sentence with 7 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'currant'): 18, ('__kw__', 'pear'): 20, "
    - [ANSWER_LEAK_STRING] form=`(get {:a 1} :missing :default)` — answer string ':default' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1} :missing :default)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'blackberry'): 16, ('__kw__', 'mango'): "

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(assoc {:a 1} :a 99)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'strawberry'): 3, ('__kw__', 'lychee'): "

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 6 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he with steady, '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '14', ':nectarine'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '17', ':orange'), resolution doesn't close the loop)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 9}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Firm the tortoise shook\nher head and went on with the work: to\nconvert a list co'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count

## Grade 5

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The trail is the trail; whatever\nthe condition evaluates to, that decides which '

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '20'), resolution doesn't close the loop)

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6}
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 10 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To walk t'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce * [1 2 3 4 5])` — sentence with 12 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To fold *'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce * [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To fold * over the vector containing 1, 2, 3, 4, and 5, computing their product,'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence with 7 commas reads as AI-output cadence: 'What Clojure form computes the largest pebble found by walking 3, 1, 4, 1, 5, 9,'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence with 7 commas reads as AI-output cadence: 'Question: write a Clojure expression for the largest pebble found by walking 3, '
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence with 7 commas reads as AI-output cadence: 'Question: write a Clojure expression for the largest pebble found by walking 3, '

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 202 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(some even? [1 3 5 8 7])` — user_msg 220 words
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, he w'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(some neg? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Fen the tortoise shook\nher head and went on with the work: to\ncheck if any eleme'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '19'), resolution doesn't close the loop)

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 7 commas reads as AI-output cadence: 'Tor the tortoise shook\nher head and went on with the work: to\ntake the first 3 e'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'To take the first 3 elements from the vector containing 10, 20, 30, 40, and 50, '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a Clojure expression that computes the sequence produced by passing 1, 1, '

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'With one, the\nrunner knows when the laps are done and the tally is the\nanswer." '

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(= 'a.b 'a.b)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(count ["src" "test" "resources"])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(count ["src" "test" "resources"])` — sentence with 6 commas reads as AI-output cadence: 'Slumber the tortoise, stepping deliberately, simply walked to the slate, wrote\nc'

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '\{:doc "steady wins"\} race))` — answer string 'steady wins' appears in user_msg

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try 7 (finally (prn :cleanup)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real race is not." To throw an ex-info wit'

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real race is not." To assert that 5 equals'

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Scrolls are how the two meet — a value\ncrosses out and becomes letters on parchm'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(:cmd {:cmd "ls" :args ["-l"]})` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were cool and {('__kw__', 'papaya'): 17, ('__kw__', 'mang"

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 212 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 207 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 5 commas reads as AI-output cadence: 'Faster, more\nfocused, less convenient." To define a Runner case with two named c'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — sentence with 5 commas reads as AI-output cadence: 'Faster, more\nfocused, less convenient." To define a record type named Runner wit'

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 203 words
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — answer string ':number' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg 207 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Tortoise that imple'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 209 words

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To define a mu'
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To define a pr'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To define a pr'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Tagged with method tag-of, define a record Stone that imple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Tagged with method tag-of, define a record Stone that imple'

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 227 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 5 commas reads as AI-output cadence: 'Any animal that can sign the book may claim\nmembership." To define two protocols'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [HIGH_LENGTH] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg 213 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 6 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '3', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '12', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '9', '14'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 6 to a new vector, then return the unchange'

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'to write atomically, no matter\nwho else is watching." To construct an atom holdi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 8 commas reads as AI-output cadence: 'to write atomically, no matter\nwho else is watching." To construct an atom holdi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 211 words

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 9, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, she composed\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 219 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 9 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.98
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (* 6 7))` — concept_phrase 'future, multiply, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (* 6 7))` — sentence with 5 commas reads as AI-output cadence: 'To\nconstruct a future that multiplies 6 and 7, and dereference it, he composed f'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (* 6 7))` — concept_phrase 'future, multiply, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'ANSWER_LEAK_STRING': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 6 commas reads as AI-output cadence: 'To\nconstruct a promise, deliver a completion keyword to it, and dereference to g'
    - [ANSWER_LEAK_STRING] form=`(do (def p (promise)) (deliver p :done) @p)` — answer string ':done' appears in user_msg
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To define'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 208 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 208 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 6 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'THE_FORM_OVERUSE': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [xs [1 2 3]] `(list ~@xs))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 205 words

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A rule takes a *form* and makes a different *form* — only\nthen does the runtime '

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when false 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when false 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 203 words
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she with e'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 6 commas reads as AI-output cadence: 'To\nthread a vector through filter, map, and reduce using thread-last, she compos'
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 203 words

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 217 words
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — answer string ':slow' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 11

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "import is a top-of-file ns clause" :studied)` — sentence with 6 commas reads as AI-output cadence: 'Sepia the tortoise, with eyes always on the path, simply walked to the slate, wr'

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 212 words
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "cljs runs in browsers and Node, with JS inter` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "cljs runs in browsers and Node, with JS inter` — sentence with 6 commas reads as AI-output cadence: 'Vine the tortoise, saying very little, simply walked to the slate, wrote\nwhere C'

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 6 commas reads as AI-output cadence: 'Meander the tortoise, saying very little, simply walked to the slate, wrote\nthe '
    - [HEDGING_NEAR_FORM] form=`(do "basilisp interops with Python via the same do` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp interops with Python via the same do` — sentence with 7 commas reads as AI-output cadence: 'Quietkin the tortoise, with steady, careful steps, simply walked to the slate, w'

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (filter even?) [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'Bedrock the tortoise shook\nhis head and went on with the work: to\nuse the filter'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sum accumulated via transduce using the '
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 221 words
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 9 commas reads as AI-output cadence: 'To compose map-inc and filter-even, then use transduce to sum the kept elements '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Deepen the tortoise shook\nher head and went on with the work: to\nuse the map-inc'

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — sentence with 6 commas reads as AI-output cadence: 'Sage the tortoise, with eyes always on the path, simply walked to the slate, wro'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "pipelines transform streams of values channel` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipelines transform streams of values channel` — sentence with 6 commas reads as AI-output cadence: 'Sepia the tortoise, with eyes always on the path, simply walked to the slate, wr'

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'Knoll the tortoise, saying very little, simply walked to the slate, wrote\nthe sa'
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "spec generators turn specs into property-base` — sentence with 6 commas reads as AI-output cadence: 'Bide the tortoise, stepping deliberately, simply walked to the slate, wrote\nthe '

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "test.check generates inputs and checks proper` — sentence with 6 commas reads as AI-output cadence: 'Taupe the tortoise, saying very little, simply walked to the slate, wrote\nthe pr'

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 6 commas reads as AI-output cadence: 'Meander the tortoise, saying very little, simply walked to the slate, wrote\nthe '
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn is read by the official `clj`/`cloju` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn is read by the official `clj`/`cloju` — sentence with 7 commas reads as AI-output cadence: 'Quietkin the tortoise, with steady, careful steps, simply walked to the slate, w'

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "queries are written in datalog over EDN-shape` — opener fragment 'at the edge of the garden,' also appears later in user_msg

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "good libraries expose data, then functions, t` — sentence with 5 commas reads as AI-output cadence: 'Halfway through the race, Lightfoot the hare, boasting at every turn, stopped on'

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "prefer pure functions, name predicates with ?` — opener fragment 'at the edge of the meadow' also appears later in user_msg

---

## Summary

### Issue counts (across all examples × 3 records)

- **CLAUSE_STACK_OVERFLOW**: 177
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **STORY_RESOLUTION_NO_DRAWN**: 62
- **NARRATIVE_NUMERAL_HARDCODE**: 42
- **HIGH_LENGTH**: 37
- **FORM_DISPLAY_AND_FORM_NOUN**: 29
- **LOW_GROUNDING**: 23
- **HEDGING_NEAR_FORM**: 12
- **PARAGRAPH_FRAGMENTATION**: 9
- **ANSWER_LEAK_STRING**: 7
- **STRING_AS_CHAR_MISCLAIM**: 6
- **THE_FORM_OVERUSE**: 6
- **ANSWER_LEAK**: 3
- **REPEATED_OPENER_FRAGMENT**: 3
- **DOUBLE_NAME_INTRO**: 2
- **SMALL_INT_LEAK**: 1
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 25 | — |
| 2 | 22 | 88 | 30 | — |
| 3 | 18 | 31 | 14 | — |
| 4 | 20 | 39 | 30 | — |
| 5 | 22 | 39 | 46 | — |
| 6 | 16 | 33 | 6 | — |
| 7 | 18 | 36 | 16 | — |
| 8 | 16 | 31 | 50 | — |
| 9 | 18 | 34 | 188 | — |
| 10 | 16 | 36 | 50 | — |
| 11 | 14 | 29 | 13 | — |
| 12 | 18 | 37 | 27 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

A small audience of forest creatures had gathered on the road to watch
Rush the hare attempt to outwit Plodder the tortoise at reading the REPL.
Plodder, saying very little, pointed to the integer 1...
    ```
- `G1-03` (form `(* 2 1/2)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It happened in the orchard, on a morning when the air was kind to swift feet and steady ones alike.

A small audience of forest creatures had gathered at the edge of the orchard to watch
Kit the hare attempt to outwit Tendril the tortoise at reading the REPL.
Tendril, stepping deliberately, pointed ...
    ```
- `G1-04` (form `"42"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    All this took place at the edge of the meadow, where the dust still keeps the shape of the runners' feet.

A small audience of forest creatures had gathered at the edge of the meadow to watch
Chipmunk the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback, stepping deliberate...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Beaver the hare chalked a wager on a flat stone along the road: whoever
predicted the result of `true` would set the next race's
distance. Plod the tortoise, without complaint, said it wou...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

A small audience of forest creatures had gathered near the meadow to watch
Speedwell the hare attempt to outwit Sandstone the tortoise at reading the REPL.
Sandstone, with steady, careful step...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Halfway through the race, Dell the hare, as if the race were already won, stopped atop the hilltop
and refused to continue until someone could prove what the form
`"harbor"` eva...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Polecat announced the race in a voice loud enough to wake the owls, and Stoneheart accepted with a nod.

"There is no need to evaluate that," Polecat the hare said, with a smug grin.
"Anyone can see what the character \space comes to." Stoneheart the tortoise, who
in the orchard had grown used to su...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    When Chitter declared the race already won, no one yet knew how long the afternoon would be.

A small audience of forest creatures had gathered in the forest to watch
Chitter the hare attempt to outwit Forest the tortoise at reading the REPL.
Forest, without complaint, pointed to the character \spac...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    atop the hilltop, where the path bends past the elm, Scurry taunted Marrow one too many times.

Scurry the hare chalked a wager on a flat stone near the hilltop: whoever
predicted the result of `"candle"` would set the next race's
distance. Marrow the tortoise, untroubled by what others thought, sai...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Halfway through the race, Mallow the hare, boasting at every turn, stopped at the edge of the meadow
and refused to continue until someone could prove what the form
`"pebble"` e...
    ```

#### SMALL_INT_LEAK

- `G1-12` (form `(+ 2 3)`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    It happened atop the hilltop, on a morning when the air was kind to swift feet and steady ones alike.

Mossback the tortoise chalked a small expression on the path: the plus-mark, then 9, then 9, all wrapped in a single set of parens. Pip the hare paused — was the answer 6 (parens means multiply, su...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-12` (form `(* (+ 1 2) 3)`): sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 2, and 6, and an outer fence holding the star-mark, the inner fence, and 8. Pip counted the parens and declared the resu...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 6, and 9, and an outer fence holding the star-mark, the inner fence, and 9. Pip counted the parens ...
    ```
- `G2-01` (form `(+ 1 2 3 4)`): sentence with 6 commas reads as AI-output cadence: 'You can split a heap." To add 2, 4, 6, and 2, she\ncomposed the multi-arg sum, su'
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Knoll the tortoise laid acorns out on a flat stone in the meadow, sorting
them with steady, careful steps. "Numbers in Clojure are like acorns in heaps,"
she said. "You can count them. ...
    ```
- `G2-01` (form `(+ 1 2 3 4)`): sentence with 5 commas reads as AI-output cadence: 'The answer is\nprecise." To add 7, 9, 7, and 5, he composed the multi-arg sum,\nsu'
    ```
    When Quick declared the race already won, no one yet knew how long the afternoon would be.

"The runtime gives the exact count," Spread the tortoise said,
saying very little. "Small or large. Fraction or whole. The answer is
precise." To add 7, 9, 7, and 5, he composed the multi-arg sum,
submitted t...
    ```
- `G2-01` (form `(- 100 1 2 3)`): sentence with 5 commas reads as AI-output cadence: 'You can split a heap." To subtract 5, 9, and 9 from 576, she\ncomposed the multi-'
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

Hummock the tortoise laid acorns out on a flat stone at the edge of the woods, sorting
them stepping deliberately. "Numbers in Clojure are like acorns in heaps,"
she said. "You can count them....
    ```

#### ANSWER_LEAK

- `G1-12` (form `(* (+ 1 2) 3)`): answer 9 in narrative
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 6, and 9, and an outer fence holding the star-mark, the inner fence, and 9. Pip counted the parens ...
    ```
- `G2-06` (form `(inc 5)`): answer 6 in narrative
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Bramble the hare eyed the heap boasting at every turn and called out a guess
without bothering to count. Sienna the tortoise simply began counting,
with steady, careful steps. To increment 6 b...
    ```
- `G2-19` (form `(+ 99999999999 1)`): answer 100000000000 in narrative
    ```
    near the garden, where the path bends past the elm, Heather taunted Stoneback one too many times.

Heather the hare eyed the heap with great whoops of laughter and called out a guess
without bothering to count. Stoneback the tortoise simply began counting,
stepping deliberately. To add 4 to 10000000...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G1-13` (form `(+ 1 2)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback had sorted this morning's acorns into two small heaps beside the trail — one heap of 7 and another of 7.

She needed the running total before deciding whether to carry them all or lea...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Lichen had nothing to prove, but Jumper had everything to lose, and the race was on.

Bramble the hare had counted 1 acorns beneath the oak and 1 more under the elm. Both heaps sat in separate leaf-cups at the edge of the path.

Bramble needed the combined count to report back to Shelly, who was tal...
    ```
- `G1-13` (form `(- 20 7)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    There is a kind of pride that runs ahead of itself, and a kind of patience that arrives at its own pace.

Slowpoke the tortoise had stockpiled 15 acorns near the hollow log. During the night, squirrels had carried off 3 of them.

Slowpoke needed the remaining count before deciding whether the stockp...
    ```
- `G4-01` (form `[]`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The sun rose by the woods, and with it the question of who could outrun whom.

Before the morning's foraging began, Mossback the tortoise set her basket on the path with its pebble row still empty — no pebbles, no contents, ready for whatever the meadow would yield. The value drawn fresh was 1, 15, ...
    ```
- `G6-08` (form `(= 'a.b 'a.b)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

Mossback wrote two namespace-like symbols on her slate: 'a.b and 'a.b. They were spelled exactly the same.

She wondered: are they truly the same symbol, or could there be some invisible difference ...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-13` (form `(* 4 5)`): opener fragment 'at the edge of the hilltop,' also appears later in user_msg
    ```
    at the edge of the hilltop, a Hare and a Tortoise once made a wager that the meadow still talks about.

Knurl the tortoise laid acorns out on a flat stone at the edge of the hilltop, sorting
them with steady, careful steps. "Numbers in Clojure are like acorns in heaps,"
he said. "You can count them....
    ```
- `G12-15` (form `(do "queries are written in datalog over EDN-shaped data" :d`): opener fragment 'at the edge of the garden,' also appears later in user_msg
    ```
    at the edge of the garden, where the path bends past the elm, Jolt taunted Cairn one too many times.

At a moss-covered milestone at the edge of the garden, Jolt the hare sketched a small
wager into the path: whoever could produce a form whose evaluation
would learn how queries are written in b over...
    ```
- `G12-18` (form `(do "prefer pure functions, name predicates with ?, danger! `): opener fragment 'at the edge of the meadow' also appears later in user_msg
    ```
    A quiet wager passed between Bouncekin and Linger, and at the edge of the meadow the meadow folk gathered to see it answered.

"There is no challenge here," Bouncekin the hare said, with great whoops of laughter.
"Anyone could learn the Clojure naming conventions: pure function preference, question-...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

"Watch the basket," Sepia the tortoise said, gesturing with eyes always on the path
at a small heap of acorns. "Every operation adds, takes away, or
combines — the heap grows or shrinks by exactly what you ...
    ```
- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    When Heath declared the race already won, no one yet knew how long the afternoon would be.

Hazel the tortoise laid acorns out on a flat stone at the edge of the orchard, sorting
them without complaint. "Numbers in Clojure are like acorns in heaps,"
he said. "You can count them. You can add heaps
to...
    ```
- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

"The runtime gives the exact count," Boulderkin the tortoise said,
untroubled by what others thought. "Small or large. Fraction or whole. The answer is
precise." To test whether 7 is...
    ```
- `G2-04` (form `(min 1 2 3)`): parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Jolt the hare eyed the heap with great whoops of laughter and called out a guess
without bothering to count. Whorl the tortoise simply began counting,
saying very little. To find the minim...
    ```
- `G2-04` (form `(min 1 2 3)`): parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    ```
    All this took place at the edge of the orchard, where the dust still keeps the shape of the runners' feet.

Lavender the hare eyed the heap as if the race were already won and called out a guess
without bothering to count. Pine the tortoise simply began counting,
stepping deliberately. To find the m...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Whiskling liked to talk; Stoneheart liked to listen, and the rivalry between them had grown into a small legend along the road.

"The runtime gives the exact count," Stoneheart the tortoise said,
untroubled by what others thought. "Small or large. Fraction or whole. The answer is
precise." To add on...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise divided a berry into halves and quarters. She held one half in her paw and one quarter in a small leaf. Both pieces were parts of the same whole fruit. The value at the ...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    The morning was bright and the dust on the road was dry, the sort of weather that invites a contest.

Stoneback the tortoise arranged a small heap of acorns at the edge of the meadow with steady, careful steps.
"Numbers in Clojure don't fudge," he said.
"Whatever you do, the runtime gets it right." ...
    ```
- `G4-13` (form `(count {:a 1 :b 2})`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '14', ':nectarine'), resolution doesn't close the loop)
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Stoic the tortoise untroubled by what others thought pointed to a small basket on the path in the garden.
"Whatever I want to do with what's inside," he
said, "I read from the b...
    ```
- `G4-13` (form `(count {:a 1 :b 2})`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '17', ':orange'), resolution doesn't close the loop)
    ```
    All this took place by the orchard, where the dust still keeps the shape of the runners' feet.

"Watch carefully," Pith the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the f...
    ```

#### HIGH_LENGTH

- `G2-15` (form `(if 0 1 0)`): user_msg 213 words
    ```
    Anyone passing at the edge of the meadow that morning would have seen Tippet stretching for show while Heft simply began.

A wooden gate at the trail's fork had a verdict-stone carved with the number zero. Mossback the tortoise stood before it, confused — zero was nothing, yet the gate stood, not ab...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 232 words
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 7 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Ju...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): user_msg 204 words
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback posted x at 13 on the road sign, then walked a detour where her hip-pouch shadowed x with 21. When she returned to the main road, the pouch was empty; only the road sign stood.

Back ...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): user_msg 224 words
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Mossback prepared three pouches in order: a held 2 acorns, then b was filled with one more than a, and finally c was loaded with twice whatever b held. Each pouch drew from the ...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg 205 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback was in a hurry at the roadside and had no time to write a full recipe card. She scratched a quick shorthand mark — `#(+ % 1)` — on a stone and put 5 acorns in front of it immediately...
    ```

#### LOW_GROUNDING

- `G2-20` (form `(count [1 2 3])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

Sandstone the tortoise walked the row of pebbles by the forest, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," she said: "at each pebble, you combin...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A quiet wager passed between Leveret and Rhizome, and atop the hilltop the meadow folk gathered to see it answered.

Rhizome the tortoise walked the row of pebbles atop the hilltop, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," she said: "at each pebble, you ...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A quiet wager passed between Furrling and Rhizome, and at the edge of the woods the meadow folk gathered to see it answered.

Rhizome the tortoise walked the row of pebbles by the woods, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," he said: "at each pebble, ...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Bistre had nothing to prove, but Heath had everything to lose, and the race was on.

Bistre the tortoise walked the row of pebbles by the meadow, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," he said: "at each pebble, you combine
it into the tally; at the end...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Plod the tortoise patted the pouch at her hip.
"Whatever I tuck in here is in force only while the pouch is
worn," she said, "and only for the form that names
the binding. Step past the fo...
    ```

#### ANSWER_LEAK_STRING

- `G4-07` (form `(get {:a 1} :missing :default)`): answer string ':default' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise's basket had one pouch — labeled :a. Pip the hare asked for the contents of a pouch labeled :missing, which had never been stitched into the basket at all. The values dr...
    ```
- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

On the long road, there lay a library shelf holding scrolls. Each scroll had a name — foo.bar, tortoise.race — inscribed on its spine in the style of the land.

Mossback the tortoise needed to know...
    ```
- `G6-15` (form `(:doc (meta '\{:doc "steady wins"\} race))`): answer string 'steady wins' appears in user_msg
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

On a scroll lay a symbol race, marked with marginalia in the margin: ^{:doc "steady wins"}. The margin held a note — a docstring — explaining what the symbol was about.

Mossback wanted...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Lichen the tortoise with eyes always on the path stretched a small net beneath a high jump
at the edge of the woods. "If the runner falls, the net catches them; the run
doesn't end, only the ...
    ```
- `G8-05` (form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet`): answer string ':number' appears in user_msg
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

Pip the hare founded the Greet guild and then wondered: could a number ever sign the book? Mossback showed him that `extend-protocol` could enroll the Long type, giving it its own `hail...
    ```

#### DOUBLE_NAME_INTRO

- `G4-14` (form `(empty? [1])`): character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback the tortoise's pebble row had one stone in its first slot — placed earlier in the morning. The row was not bare, but Pip the hare was unsure. The value drawn fresh was 15, 10, ...
    ```
- `G4-14` (form `(empty? [1])`): character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    Streak liked to talk; Bulk liked to listen, and the rivalry between them had grown into a small legend near the hilltop.

Mossback the tortoise's pebble row had one stone in its first slot — placed earlier in the morning. The row was not bare, but Pip the hare was unsure. The value drawn fresh was 1...
    ```

#### COLLECTION_LEAK

- `G5-10` (form `(map inc [1 2 3])`): elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

A row of three small acorns lay on a flat stone — the morning's first gathering, with counts of 1, 2, and 3.

Each acorn was missing a single bud at the cap. Mossback the tortoise wanted to a...
    ```

#### HEDGING_NEAR_FORM

- `G6-11` (form `(count ["src" "test" "resources"])`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

The wager was set by the meadow: produce the value before the breeze had
turned the next leaf. Bounder the hare, with a smug grin, bolted into a flurry
of guesses, calling out numbers and second-guessing hi...
    ```
- `G11-05` (form `(do "import is a top-of-file ns clause" :studied)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Hedgehog announced the race in a voice loud enough to wake the owls, and Sepia accepted with a nod.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Hedgehog the hare, swaggering through the underbrush, bolted into a flurry
of guesses, calling out numb...
    ```
- `G11-10` (form `(do "cljs runs in browsers and Node, with JS interop syntax"`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

The wager was set on the road: produce the value before the breeze had
turned the next leaf. Bluebell the hare, swaggering through the underbrush, bolted into a flurry
of guesses, calling out numbers and se...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    All this took place at the edge of the meadow, where the dust still keeps the shape of the runners' feet.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. Whirlikin the hare, boasting at every turn, bolted into a flurry
of guesses, calling o...
    ```
- `G11-12` (form `(do "basilisp interops with Python via the same dot-syntax c`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Brook was the first to laugh and the first to boast, and Quietkin simply began to walk.

The wager was set near the hilltop: produce the value before the breeze had
turned the next leaf. Brook the hare, boasting at every turn, bolted into a flurry
of guesses, calling out numbers and second-guessing ...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

The forest's berry-tally lived on a notebook open on the tree stump in the middle of the meadow. Anyone returning from foraging walked up, read the running total, and added their own count.

Today's tally...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The sun rose in the forest, and with it the question of who could outrun whom.

Skitter the hare with a smug grin swiped at the notebook on the stump,
trying to scribble an answer over the page. Deepen the tortoise
caught him firmly: notebooks shared by all the meadow
need careful updates, not snatc...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

"The notebook stays put on the stump," Roam the tortoise stepping deliberately said,
"so any animal who comes by can read what's on the page right
now. The page changes only when someon...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Skimble was certain he could not lose; Muse was certain of nothing except the next step.

"Many animals can come and go past the stump," Muse the tortoise untroubled by what others thought said, "and each one's read or write must agree with the others.
The runtime sees to that — no two writers stomp...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The morning was bright and the dust on the road was dry, the sort of weather that invites a contest.

"When I want to update the notebook," Hummock the tortoise untroubled by what others thought said,
"I don't pick it up and walk away — I read the page, apply the
change, and write it back, all in a ...
    ```

#### THE_FORM_OVERUSE

- `G10-01` (form `(quote (+ 1 2))`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

Mossback the tortoise had chalked the form `(+ 1 2)` on a strip of bark and set it aside, wanting to hand the form itself to the Hare — not its computed value.

She needed a way to label the form s...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Brisk was certain she could not lose; Pillow was certain of nothing except the next step.

"To talk about the form itself rather than evaluating it,"
Pillow the tortoise saying very little said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, just hand
it ...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Chipmunk was certain he could not lose; Shale was certain of nothing except the next step.

"To talk about the form itself rather than evaluating it,"
Shale the tortoise with eyes always on the path said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, jus...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

"To talk about the form itself rather than evaluating it,"
Sepia the tortoise with eyes always on the path said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, j...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

"There's a difference between *labeling* the form and
*evaluating* it," Ravine the tortoise stepping deliberately said. "Quote in any of its
shapes is the labeling — the runtime hands y...
    ```

