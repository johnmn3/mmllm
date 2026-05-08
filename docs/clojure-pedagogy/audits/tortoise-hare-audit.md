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
- issues: {'CONCEPT_PHRASE_FORM_PREFIX': 9, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
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

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(+
  1
  2)` — user_msg 202 words

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

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(= "a" "a")` — user_msg has un-substituted `{drawn.topaz}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(= "a" "a")` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

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
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 219 words

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To count '

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
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To define x, shadow it '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To define x, shadow it '
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x) x)` — user_msg 210 words

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — sentence with 6 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To bind a to 7, b to a+'
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 230 words

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

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 206 words

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(* 5 5 5)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3}
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`["a" "b"]` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
    - [REPL_TRIPLE_VOICE] form=`'(1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`'(1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`{:hare 1 :tortoise 2}` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(get {:a 1 :b 2} :a)` — user_msg 204 words
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1 :b 2} :a)` — sentence with 7 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'currant'): 18, ('__kw__', 'pear'): 20, "
    - [ANSWER_LEAK_STRING] form=`(get {:a 1} :missing :default)` — answer string ':default' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1} :missing :default)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'blackberry'): 16, ('__kw__', 'mango'): "

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(assoc {:a 1} :a 99)` — user_msg 208 words
    - [CLAUSE_STACK_OVERFLOW] form=`(assoc {:a 1} :a 99)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'strawberry'): 3, ('__kw__', 'lychee'): "

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'NUMERAL_LIST_IN_GOAL': 3, 'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [REPL_TRIPLE_VOICE] form=`(count [1 2 3 4 5])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 6 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he with steady, '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'DOUBLE_NAME_INTRO': 2}
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
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

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 206 words
    - [REPL_TRIPLE_VOICE] form=`(= [1 2 3] '(1 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(first (range 1 100))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 2, 'DRAWN_PLACEHOLDER_LEAK': 2}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(if (> 5 3) :a :b)` — user_msg has un-substituted `{drawn.y}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(if (> 5 3) :a :b)` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(if (> 5 3) :a :b)` — user_msg has un-substituted `{drawn.soft}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(if (> 5 3) :a :b)` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The trail is the trail; whatever\nthe condition evaluates to, that decides which '

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'NUMERAL_LIST_IN_GOAL': 3}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 222 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6}
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'NUMERAL_LIST_IN_GOAL': 9, 'CLAUSE_STACK_OVERFLOW': 6}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 203 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 10 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To walk t'
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 207 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

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
- issues: {'HIGH_LENGTH': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 212 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [HIGH_LENGTH] form=`(some even? [1 3 5 8 7])` — user_msg 220 words
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, he w'
    - [CLAUSE_STACK_OVERFLOW] form=`(some neg? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Fen the tortoise shook\nher head and went on with the work: to\ncheck if any eleme'

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 206 words
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 201 words
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 7 commas reads as AI-output cadence: 'Tor the tortoise shook\nher head and went on with the work: to\ntake the first 3 e'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [HIGH_LENGTH] form=`(take 3 [10 20 30 40 50])` — user_msg 204 words

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
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

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(= 'race.tortoise 'race.tortoise)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(clojure.string/reverse "abc")` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(clojure.string/reverse "abc")` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'GENERIC_RESOLUTION_TAIL': 3}
    - [GENERIC_RESOLUTION_TAIL] form=`(boolean (:private (meta 'public)))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(boolean (:private (meta 'public)))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(boolean (:private (meta 'public)))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop

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

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'REPL_TRIPLE_VOICE': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '\{:doc "steady wins"\} race))` — answer string 'steady wins' appears in user_msg
    - [REPL_TRIPLE_VOICE] form=`(:author (meta '\{:author "Aesop"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try 7 (finally (prn :cleanup)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(try 7 (finally (prn :cleanup)))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(try 7 (finally (prn :cleanup)))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

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

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1, 'REPL_TRIPLE_VOICE': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(with-out-str (prn 42))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(with-out-str (prn 42))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (prn 42))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [REPL_TRIPLE_VOICE] form=`(tap> :hello)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(tap> 42)` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(tap> 42)` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(try (throw (Exception. "oops")) (catch Exception ` — answer string 'oops' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Scrolls are how the two meet — a value\ncrosses out and becomes letters on parchm'
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G7-14: with-open

- examples: 1
- variety @ n=50: 0.98
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(with-out-str (println "hare"))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(with-out-str (println "hare"))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1, 'REPL_TRIPLE_VOICE': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(with-out-str (print "x"))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(with-out-str (print "x"))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (println))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string "42")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'REPL_TRIPLE_VOICE': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg 203 words
    - [CLAUSE_STACK_OVERFLOW] form=`(:cmd {:cmd "ls" :args ["-l"]})` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were cool and {('__kw__', 'papaya'): 17, ('__kw__', 'mang"

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
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
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"

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
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 233 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 5 commas reads as AI-output cadence: 'Any animal that can sign the book may claim\nmembership." To define two protocols'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

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
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 6 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [HIGH_LENGTH] form=`(let [v [1 2 3]] (conj v 4) v)` — user_msg 204 words
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
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 5}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 201 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding a start keyword, atomically reset it to a done keyw'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding a start keyword, atomically reset it to a done keyw'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'

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
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [HIGH_LENGTH] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — user_msg 217 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 100, perform a transactional ref-set to 7 inside dosy'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 219 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 6 commas reads as AI-output cadence: 'to write atomically, no matter\nwho else is watching." To construct a ref holding'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 5, asynchronously send + with 10 to it, await its '

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 202 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 8 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.98
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [ANSWER_LEAK_STRING] form=`(do (def p (promise)) (deliver p :done) @p)` — answer string ':done' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p 42) @p)` — sentence with 5 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct a promise, deliver 4'

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — sentence with 6 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [HIGH_LENGTH] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — user_msg 217 words

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 215 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 5 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 6 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 5 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'GENERIC_RESOLUTION_TAIL': 3}
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 216 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 218 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [GENERIC_RESOLUTION_TAIL] form=`(do (def lock (Object.)) (locking lock 42))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 220 words

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'THE_FORM_OVERUSE': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [xs [1 2 3]] `(list ~@xs))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 211 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 213 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A rule takes a *form* and makes a different *form* — only\nthen does the runtime '

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 213 words
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she with e'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 6 commas reads as AI-output cadence: 'To\nthread a vector through filter, map, and reduce using thread-last, she compos'
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 203 words

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'UNFILLED_DRAWN_PLACEHOLDER': 2, 'DRAWN_PLACEHOLDER_LEAK': 2}
    - [HIGH_LENGTH] form=`(eval '(+ 1 2 3))` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(eval (list '+ 4 5))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(eval (list '+ 4 5))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(eval (list '+ 4 5))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 217 words
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — answer string ':slow' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 11

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(Math/abs -7)` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(Math/abs -7)` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "import is a top-of-file ns clause" :studied)` — sentence with 6 commas reads as AI-output cadence: 'Sepia the tortoise, with eyes always on the path, simply walked to the slate, wr'

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(let [a (int-array [1 2 3])] (alength a))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(let [a (int-array [1 2 3])] (alength a))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 212 words

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

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_DRAWN_PLACEHOLDER': 2, 'DRAWN_PLACEHOLDER_LEAK': 2}
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'DRAWN_PLACEHOLDER_LEAK': 1, 'NUMERAL_LIST_IN_GOAL': 3}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 211 words
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(into [] (map inc) [1 2 3])` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [DRAWN_PLACEHOLDER_LEAK] form=`(into [] (map inc) [1 2 3])` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — goal_text contains 6 numerals across 6 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sum accumulated via transduce using the '
    - [NUMERAL_LIST_IN_GOAL] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — goal_text contains 6 numerals across 6 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 211 words
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(into #{} (map inc) [1 2 3])` — user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [DRAWN_PLACEHOLDER_LEAK] form=`(into #{} (map inc) [1 2 3])` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
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

- **CLAUSE_STACK_OVERFLOW**: 148
- **HIGH_LENGTH**: 55
- **NUMERAL_LIST_IN_GOAL**: 48
- **NARRATIVE_NUMERAL_HARDCODE**: 42
- **FORM_DISPLAY_AND_FORM_NOUN**: 29
- **REPL_TRIPLE_VOICE**: 25
- **UNFILLED_DRAWN_PLACEHOLDER**: 21
- **DRAWN_PLACEHOLDER_LEAK**: 21
- **HEDGING_NEAR_FORM**: 12
- **CONCEPT_PHRASE_FORM_PREFIX**: 9
- **PARAGRAPH_FRAGMENTATION**: 8
- **ANSWER_LEAK_STRING**: 8
- **STRING_AS_CHAR_MISCLAIM**: 6
- **GENERIC_RESOLUTION_TAIL**: 6
- **THE_FORM_OVERUSE**: 6
- **ANSWER_LEAK**: 3
- **REPEATED_OPENER_FRAGMENT**: 3
- **ONLY_SHOOK_HEAD_TIC**: 2
- **DOUBLE_NAME_INTRO**: 2
- **SMALL_INT_LEAK**: 1
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 41 | — |
| 2 | 22 | 88 | 23 | — |
| 3 | 18 | 31 | 11 | — |
| 4 | 20 | 39 | 43 | — |
| 5 | 22 | 39 | 89 | — |
| 6 | 16 | 33 | 12 | — |
| 7 | 18 | 36 | 29 | — |
| 8 | 16 | 31 | 40 | — |
| 9 | 18 | 34 | 75 | — |
| 10 | 16 | 36 | 34 | — |
| 11 | 14 | 29 | 17 | — |
| 12 | 18 | 37 | 42 | — |

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

#### CONCEPT_PHRASE_FORM_PREFIX

- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

At a moss-covered milestone in the garden, Racer the hare sketched a small
wager into the path: whoever guessed the result of `(+ 1/2 1/4)`
first would win the right to set the next race. ...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Halfway through the race, Rosemary the hare, with great whoops of laughter, stopped on the road
and refused to continue until someone could prove what the form
`(+ 1/2 1/4)` evaluated to. Rosemary called it...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

"There is no need to evaluate that," Glen the hare said, swaggering through the underbrush.
"Anyone can see what the form (+ 1/2 1/4) comes to." Cushion the tortoise, who
near the orchard had g...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

Halfway through the race, Stoat the hare, boasting at every turn, stopped along the road
and refused to continue until someone could prove what the form
`(* 2 1/2)` evaluated to. Sto...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Anyone passing on the road that morning would have seen Heather stretching for show while Bark simply began.

With a twig, Heather the hare marked out a wager along the road: whoever
guessed the result of `(* 1 1/2)` first would win the right to
choose the next contest. Bark the tortoise, saying ver...
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

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Dormouse the hare swaggering through the underbrush mistook the name on the bark for the
acorn it pointed to. "It says hare, so the value must be the
hare!" Heavyback the tortoise only shook his head: the
m...
    ```
- `G10-01` (form `(let [x 5] `(a ~x b))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Bouncer the hare swaggering through the underbrush mistook the name on the bark for the
acorn it pointed to. "It says hare, so the value must be the
hare!" Snooze the tortoise o...
    ```

#### HIGH_LENGTH

- `G1-11` (form `(+
  1
  2)`): user_msg 202 words
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Shelly the tortoise had written a form across three lines on a broad leaf — the operator on the first, each argument indented on its own line below. Hopper the hare wondered whe...
    ```
- `G2-15` (form `(if 0 1 0)`): user_msg 219 words
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
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): user_msg 210 words
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback posted x at 13 on the road sign, then walked a detour where her hip-pouch shadowed x with 21. When she returned to the main road, the pouch was empty; only the road sign stood.

Back ...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): user_msg 230 words
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Mossback prepared three pouches in order: a held 2 acorns, then b was filled with one more than a, and finally c was loaded with twice whatever b held. Each pouch drew from the ...
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
- `G6-08` (form `(= 'a.b 'a.b)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

Mossback wrote two namespace-like symbols on her slate: 'a.b and 'a.b. They were spelled exactly the same.

She wondered: are they truly the same symbol, or could there be some invisible difference ...
    ```
- `G8-09` (form `(do (defmulti pace :species) (defmethod pace :hare [_] :swif`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    When Whish declared the race already won, no one yet knew how long the afternoon would be.

An owl arrived at Mossback's sorting-table. No arm existed for owls. Mossback had added a `:default` arm to catch any stamp without a dedicated route.

She needed to route the owl and confirm the `:default` a...
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

#### UNFILLED_DRAWN_PLACEHOLDER

- `G1-15` (form `(= "a" "a")`): user_msg has un-substituted `{drawn.topaz}` placeholder — slot mismatch or render-time gap
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Two bark-strips each bore the single letter "{drawn.topaz}" pressed in ink, one on each gatepost of the trail gate. Bramble the hare said one might be topaz different shade of ink.

Shelly needed to know wh...
    ```
- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg has un-substituted `{drawn.y}` placeholder — slot mismatch or render-time gap
    ```
    When Skitter declared the race already won, no one yet knew how long the afternoon would be.

The trail forked near a mossy boulder. The condition-stone at the split was carved `(> 2 1)` — a comparison between two pebble-counts left there by a previous traveller.

Before taking a step, Mossback need...
    ```
- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg has un-substituted `{drawn.soft}` placeholder — slot mismatch or render-time gap
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

The trail forked near a mossy boulder. The condition-stone at the split was carved `(> 9 0)` — a comparison between two pebble-counts left there by a previous traveller.

Before taki...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

The same scroll held another routine: reverse. It took the letters in a string and handed them back in the opposite order. Mossback had a string {drawn.a} and wanted to see what the rev...
    ```
- `G7-03` (form `(try 7 (finally (prn :cleanup)))`): user_msg has un-substituted `{drawn.a}` placeholder — slot mismatch or render-time gap
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise always folded her safety net after each practice jump, no matter how the leap went. She asked the runtime to do the same: carry out the cleanup step after the form, regardless of out...
    ```

#### DRAWN_PLACEHOLDER_LEAK

- `G1-15` (form `(= "a" "a")`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Two bark-strips each bore the single letter "{drawn.topaz}" pressed in ink, one on each gatepost of the trail gate. Bramble the hare said one might be topaz different shade of ink.

Shelly needed to know wh...
    ```
- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    When Skitter declared the race already won, no one yet knew how long the afternoon would be.

The trail forked near a mossy boulder. The condition-stone at the split was carved `(> 2 1)` — a comparison between two pebble-counts left there by a previous traveller.

Before taking a step, Mossback need...
    ```
- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

The trail forked near a mossy boulder. The condition-stone at the split was carved `(> 9 0)` — a comparison between two pebble-counts left there by a previous traveller.

Before taki...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

The same scroll held another routine: reverse. It took the letters in a string and handed them back in the opposite order. Mossback had a string {drawn.a} and wanted to see what the rev...
    ```
- `G7-03` (form `(try 7 (finally (prn :cleanup)))`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise always folded her safety net after each practice jump, no matter how the leap went. She asked the runtime to do the same: carry out the cleanup step after the form, regardless of out...
    ```

#### REPL_TRIPLE_VOICE

- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Heft had nothing to prove, but Mallow had everything to lose, and the race was on.

Mallow the hare as if the race were already won glanced at the form and called out
what she thought it would do without paying attention to
the conventions of how it was written. Heft the tortoise only
shook his head...
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

"There are conventions for how the runtime *reads* a form,"
Olive the tortoise without complaint said: "what counts as one token, what's just
spacing, what gets ignored, what gets grouped toge...
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

"A form is what's actually there on the page," Umber the tortoise with eyes always on the path said. "After the conventions of writing and reading have done their work, the runtime evaluates the cl...
    ```
- `G3-18` (form `(* 5 5 5)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    in the garden, where the path bends past the elm, Cornflower taunted Vine one too many times.

Mossback decided the count was simple enough to write out directly — no pouch, no name. She placed three fives side by side on the calculation stone and let the REPL multiply them at once.

For a one-time ...
    ```
- `G4-01` (form `[]`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The sun rose by the woods, and with it the question of who could outrun whom.

Before the morning's foraging began, Mossback the tortoise set her basket on the path with its pebble row still empty — no pebbles, no contents, ready for whatever the meadow would yield. The value drawn fresh was 1, 15, ...
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
- `G7-11` (form `(try (throw (Exception. "oops")) (catch Exception e (.getMes`): answer string 'oops' appears in user_msg
    ```
    There is a kind of pride that runs ahead of itself, and a kind of patience that arrives at its own pace.

Mossback's alarm horn had sounded during a run. Rather than ignoring the alarm and dashing on like Hare, she stopped to read the message written on the horn's label — the first line of the stack...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Lichen the tortoise with eyes always on the path stretched a small net beneath a high jump
at the edge of the woods. "If the runner falls, the net catches them; the run
doesn't end, only the ...
    ```

#### NUMERAL_LIST_IN_GOAL

- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback the tortoise's pebble row held five stones laid out in order. She had lost track of the total and needed the REPL to confirm the count without her counting by hand. The value drawn fr...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Word went around at the edge of the orchard that two creatures had agreed to settle an old question with their feet.

A line of animals had formed by the orchard, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this proce...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Rush was certain she could not lose; Stalk was certain of nothing except the next step.

"Watch carefully," Stalk the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first o...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    A quiet wager passed between Yarrow and Trundler, and in the garden the meadow folk gathered to see it answered.

Trundler the tortoise with steady, careful steps stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," she said, "has been ...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Knoll had nothing to prove, but Snuffle had everything to lose, and the race was on.

Knoll the tortoise without complaint stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," he said, "has been through both rules in
order — applied as ...
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

#### GENERIC_RESOLUTION_TAIL

- `G6-07` (form `(boolean (:private (meta 'public)))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    The judge was a fox of solemn ear, and the prize was nothing more than the quiet certainty of being right.

"The good thing about a sign," Burl the tortoise said untroubled by what others thought
"is that it stays where you posted it. The road is long but the
sign holds; the next runner reads what's...
    ```
- `G6-07` (form `(boolean (:private (meta 'public)))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Now she did the same with a plain symbol 'public — no markers, no ropes. She wanted to test it the same way: extract the :private flag and convert to a boolean.

Would the plain symbol's answ...
    ```
- `G6-07` (form `(boolean (:private (meta 'public)))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

Dart the hare as if the race were already won glanced at the sign near the meadow and
called out what he thought it said without slowing.
Stonefoot the tortoise stopped and read carefully....
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

"Many animals can come and go past the stump," Bog the tortoise without complaint said, "and each one's read or write must agree with the others.
The runtime sees to that — no two writers ...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    near the hilltop, a Hare and a Tortoise once made a wager that the meadow still talks about.

Pip the hare wanted to understand the locking fence by using the simplest possible body — a bare value that needed no computation. She grabbed the fence-key and stepped inside just long enough to read the v...
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

