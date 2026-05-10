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
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 5}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead

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
- issues: {'AND_HANDED_BACK_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [AND_HANDED_BACK_CADENCE] form=`(+ 2 3)` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(* (+ 1 2) 3)` — sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
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

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 2, 1, 6, 3, and 0, she with eyes always on the path compo'
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 8, 2, 3, 5, and 6, she with eyes always on the path compo'
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the maximum of 4, 6, 4, 1, and 6, she saying very little composed the ma'
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the maximum of 6, 8, 9, 4, and 3, she with eyes always on the path compo'

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(+ 1/2 1/4)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 6 commas reads as AI-output cadence: 'To use str to join the integer 1, the plus sign, the integer 0, the equals sign,'

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 219 words

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:hare {:hare 1 :tortoise 2})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:missing {:hare 1})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 8}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', counting the steps —\nreturned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (',\nwalking the row — returned the final value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (',\nwalking the row — returned the final value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (',\nwalking the row — returned the final value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead

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
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x) x)` — user_msg 210 words

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 230 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 205 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'AND_HANDED_BACK_CADENCE': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words
    - [AND_HANDED_BACK_CADENCE] form=`((fn [x] x x x 99) 1)` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'HIGH_LENGTH': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 206 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead

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
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(nth [10 20 30] 2)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [] :hare)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'REPL_TRIPLE_VOICE': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`'(1 2 3)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`'(1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`'(1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(cons 0 '(1 2 3))` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`{:hare 1 :tortoise 2}` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [HIGH_LENGTH] form=`(get {:a 1 :b 2} :a)` — user_msg 204 words
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1 :b 2} :a)` — sentence with 7 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'currant'): 18, ('__kw__', 'pear'): 20, "
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1 :b 2} :a)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1} :missing :default)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'blackberry'): 16, ('__kw__', 'mango'): "
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1} :missing :default)` — sentence closes with a participial coda (', keeping the operation safe.') — LLM-cadence; close on the verb instead

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :b 2)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(assoc {:a 1} :a 99)` — user_msg 208 words
    - [CLAUSE_STACK_OVERFLOW] form=`(assoc {:a 1} :a 99)` — sentence with 5 commas reads as AI-output cadence: "The values drawn fresh were {('__kw__', 'strawberry'): 3, ('__kw__', 'lychee'): "
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', leaving the old one untouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(contains? #{1 2 3} 2)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(count [1 2 3 4 5])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3 4 5])` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count {:a 1 :b 2})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'REPL_TRIPLE_VOICE': 2, 'DOUBLE_NAME_INTRO': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pip the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? "")` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

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

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 206 words
    - [REPL_TRIPLE_VOICE] form=`(= [1 2 3] '(1 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [REPL_TRIPLE_VOICE] form=`(first (range 1 100))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first (range 1 100))` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first (range 1 100))` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

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

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 222 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'TRAILING_PARTICIPLE_CLOSER': 9}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 203 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + [1 2 3 4])` — sentence closes with a participial coda (', producing the new tally.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + [1 2 3 4])` — sentence closes with a participial coda (', counting the steps —\nreturned the count.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 207 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + [1 2 3 4])` — sentence closes with a participial coda (', producing the new tally.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce * [1 2 3 4 5])` — sentence closes with a participial coda (', counting the steps —\nreturned the count.') — LLM-cadence; close on the verb instead

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 5}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', producing the combined total of all four values.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (',\nwalking the row — returned the final value.') — LLM-cadence; close on the verb instead

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 210 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(apply max [3 1 4 1 5])` — user_msg 202 words

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`((comp str inc) 9)` — sentence closes with a participial coda (', producing the final signpost text.') — LLM-cadence; close on the verb instead

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(some even? [1 3 5 8 7])` — user_msg 218 words
    - [CLAUSE_STACK_OVERFLOW] form=`(some neg? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Fen the tortoise shook\nher head and went on with the work: to\ncheck if any eleme'
    - [CLAUSE_STACK_OVERFLOW] form=`(some neg? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Cushion the tortoise shook\nher head and went on with the work: to\ncheck if any e'

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
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(name 'foo.bar)` — sentence closes with a participial coda (', leaving the scroll itself alone.') — LLM-cadence; close on the verb instead

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(= 'race.tortoise 'race.tortoise)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

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

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(:author (meta '\{:author "Aesop"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try 7 (finally (prn :cleanup)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'ABSTRACT_RESULT_NARRATION': 3}
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (prn 42))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(tap> :hello)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
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
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 212 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — sentence closes with a participial coda (', confirming the bare case held it faithfully.') — LLM-cadence; close on the verb instead

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 207 words

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 203 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence closes with a participial coda (', confirming the dispatch worked.') — LLM-cadence; close on the verb instead

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg 207 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Tortoise that imple'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 209 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence closes with a participial coda (',\ndispatching the runner — returned the branch-specific valu') — LLM-cadence; close on the verb instead

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence closes with a participial coda (',\ndispatching the runner — returned the branch-specific valu') — LLM-cadence; close on the verb instead

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'HIGH_LENGTH': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence closes with a participial coda (',\ndispatching the runner — returned the branch-specific valu') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence closes with a participial coda (',\ndispatching the runner — returned the branch-specific valu') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

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
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 233 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence closes with a participial coda (',\ndispatching the runner — returned the branch-specific valu') — LLM-cadence; close on the verb instead

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg 213 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — sentence closes with a participial coda (", ignoring the Hare's arm entirely.") — LLM-cadence; close on the verb instead

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 2, 'DOUBLED_INPUT_VALUE_PARENS': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 6 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [HIGH_LENGTH] form=`(let [v [1 2 3]] (conj v 4) v)` — user_msg 207 words
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(let [v [1 2 3]] (conj v 4) v)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [HIGH_LENGTH] form=`(let [v [1 2 3]] (conj v 4) v)` — user_msg 216 words

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding an idle value as progress, atomically reset it to r'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 201 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding a start keyword, atomically reset it to a done keyw'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding a start keyword, atomically reset it to a done keyw'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [HIGH_LENGTH] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — user_msg 217 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 100, perform a transactional ref-set to 7 inside dosy'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 219 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 5, asynchronously send + with 10 to it, await its '

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 202 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, use send-off to asynchronously apply inc, await'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.98
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'AND_HANDED_BACK_CADENCE': 2}
    - [AND_HANDED_BACK_CADENCE] form=`@(future (* 6 7))` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    - [AND_HANDED_BACK_CADENCE] form=`@(future (* 6 7))` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — user_msg 217 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — sentence closes with a participial coda (', overwriting the old page entirely.') — LLM-cadence; close on the verb instead

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 215 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence closes with a participial coda (', overriding the default for the duration of her stretch.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 6 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'GENERIC_RESOLUTION_TAIL': 3, 'TRAILING_PARTICIPLE_CLOSER': 2}
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
- issues: {'HIGH_LENGTH': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 219 words
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 213 words
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she with e'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 6 commas reads as AI-output cadence: 'To\nthread a vector through filter, map, and reduce using thread-last, she compos'
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand '(-> x f g))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 203 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(if-let [x 7] (* x x) 0)` — sentence closes with a participial coda (', making the expansion readable and collision-free.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(if-let [x 7] (* x x) 0)` — sentence closes with a participial coda (', making the expansion readable and collision-free.') — LLM-cadence; close on the verb instead

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [HIGH_LENGTH] form=`(eval '(+ 1 2 3))` — user_msg 206 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 217 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 11

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hare")` — sentence closes with a participial coda (', returning the length regardless of the input.') — LLM-cadence; close on the verb instead

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 212 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [^String s "abc"] (.toUpperCase s))` — sentence closes with a participial coda (', helping the compiler choose the fastest path to the method') — LLM-cadence; close on the verb instead

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — sentence closes with a participial coda (', letting the form continue if things go wrong.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — sentence closes with a participial coda (', letting the form continue if things go wrong.') — LLM-cadence; close on the verb instead

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 225 words
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Deepen the tortoise shook\nher head and went on with the work: to\nuse the map-inc'

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

- **TRAILING_PARTICIPLE_CLOSER**: 72
- **CLAUSE_STACK_OVERFLOW**: 60
- **HIGH_LENGTH**: 55
- **NARRATIVE_NUMERAL_HARDCODE**: 33
- **FORM_DISPLAY_AND_FORM_NOUN**: 28
- **REPL_TRIPLE_VOICE**: 25
- **CONCEPT_PHRASE_FORM_PREFIX**: 9
- **PARAGRAPH_FRAGMENTATION**: 8
- **GENERIC_RESOLUTION_TAIL**: 6
- **THE_FORM_OVERUSE**: 6
- **AND_HANDED_BACK_CADENCE**: 4
- **DOUBLED_INPUT_VALUE_PARENS**: 4
- **REPEATED_OPENER_FRAGMENT**: 3
- **UNFILLED_DRAWN_PLACEHOLDER**: 3
- **DRAWN_PLACEHOLDER_LEAK**: 3
- **ABSTRACT_RESULT_NARRATION**: 3
- **ONLY_SHOOK_HEAD_TIC**: 2
- **DOUBLE_NAME_INTRO**: 2
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 38 | — |
| 2 | 22 | 88 | 17 | — |
| 3 | 18 | 31 | 12 | — |
| 4 | 20 | 39 | 57 | — |
| 5 | 22 | 39 | 47 | — |
| 6 | 16 | 33 | 7 | — |
| 7 | 18 | 36 | 15 | — |
| 8 | 16 | 31 | 33 | — |
| 9 | 18 | 34 | 56 | — |
| 10 | 16 | 36 | 29 | — |
| 11 | 14 | 29 | 5 | — |
| 12 | 18 | 37 | 11 | — |

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

#### TRAILING_PARTICIPLE_CLOSER

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Slowpoke the tortoise had scratched an addition on the trail-stone and, beside it, added a small note after a semicolon explaining what the form computed — a scribe's marginal gloss. The valu...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

Dell the tortoise without complaint unrolled a small slate at the edge of the meadow and wrote
slowly, paying attention to every mark. "The form has to be
written so the reader can read it...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    It happened at the edge of the forest, on a morning when the air was kind to swift feet and steady ones alike.

Slowpoke the tortoise had scratched an addition on the trail-stone and, beside it, added a small note after a semicolon explaining what the form computed — a scribe's marginal gloss. The v...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    Bulk had nothing to prove, but Leveret had everything to lose, and the race was on.

Bulk the tortoise untroubled by what others thought unrolled a small slate near the road and wrote
slowly, paying attention to every mark. "The form has to be
written so the reader can read it cleanly," she
said. "I...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    There is a kind of pride that runs ahead of itself, and a kind of patience that arrives at its own pace.

"A form is what the reader sees," Marble the tortoise without complaint said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime ...
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

#### AND_HANDED_BACK_CADENCE

- `G1-12` (form `(+ 2 3)`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    It happened atop the hilltop, on a morning when the air was kind to swift feet and steady ones alike.

Mossback the tortoise chalked a small expression on the path: the plus-mark, then 9, then 9, all wrapped in a single set of parens. Pip the hare paused — was the answer 6 (parens means multiply, su...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback's recipe card for this stretch listed several intermediate steps, but the cook only served the final dish — everything before it was preparation, not what got plated.

The kitchen nee...
    ```
- `G9-13` (form `@(future (* 6 7))`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    When Fern declared the race already won, no one yet knew how long the afternoon would be.

Fern the hare as if the race were already won reached for the runner's pouch before
the runner had even returned. Hushwise the tortoise held him
back: a runner sent ahead must be allowed to finish. To
construc...
    ```
- `G9-13` (form `@(future (* 6 7))`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    atop the hilltop, where the path bends past the elm, Hedgepig taunted Whorl one too many times.

Hedgepig the hare with great whoops of laughter reached for the runner's pouch before
the runner had even returned. Whorl the tortoise held him
back: a runner sent ahead must be allowed to finish. To
con...
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
- `G2-04` (form `(min 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 2, 1, 6, 3, and 0, she with eyes always on the path compo'
    ```
    by the garden, where the path bends past the elm, Dappling taunted Tor one too many times.

To find the minimum of 2, 1, 6, 3, and 0, she with eyes always on the path composed the minimum of five numbers and submitted the form. The REPL counted out the answer:

Write a Clojure expression that comput...
    ```
- `G2-04` (form `(min 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'To find the minimum of 8, 2, 3, 5, and 6, she with eyes always on the path compo'
    ```
    Pipsqueak was the first to laugh and the first to boast, and Steady simply began to walk.

To find the minimum of 8, 2, 3, 5, and 6, she with eyes always on the path composed the minimum of five numbers and submitted the form. The REPL counted out the answer:

What Clojure form computes the smallest...
    ```
- `G2-04` (form `(max 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'To find the maximum of 4, 6, 4, 1, and 6, she saying very little composed the ma'
    ```
    When Whirr declared the race already won, no one yet knew how long the afternoon would be.

To find the maximum of 4, 6, 4, 1, and 6, she saying very little composed the maximum of five numbers and submitted the form. The REPL counted out the answer:

Write a form whose evaluation gives the largest ...
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

#### DOUBLED_INPUT_VALUE_PARENS

- `G2-08` (form `(+ 1/2 1/4)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise divided a berry into halves and quarters. She held one half in her paw and one quarter in a small leaf. Both pieces were parts of the same whole fruit. The value at the ...
    ```
- `G9-01` (form `(let [v [1 2 3]] (conj v 4) v)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    The sun rose by the woods, and with it the question of who could outrun whom.

Three smooth stones sat in a row on the meadow path — Mossback's tally-stones for the morning's laps. Pip suggested adding a fourth stone to mark an extra stretch, but Mossback wanted her original row kept exactly as it s...
    ```
- `G9-01` (form `(let [v [1 2 3]] (conj v 4) v)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Bunny liked to talk; Cobblestone liked to listen, and the rivalry between them had grown into a small legend at the edge of the garden.

Three smooth stones sat in a row on the meadow path — Mossback's tally-stones for the morning's laps. Pip suggested adding a fourth stone to mark an extra stretch,...
    ```
- `G10-03` (form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-w`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise was tired of writing `if`/`do` by hand for every form where she wanted several steps to run only if a condition held.

She wanted a rule called `my-when` that rewrote the shorter for...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

"You can find what you want in a basket several ways,"
Sepia the tortoise with steady, careful steps said, gesturing at the woven shape:
"by the tag pinned to it, by its place in line, or by simply
asking w...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    It happened at the edge of the meadow, on a morning when the air was kind to swift feet and steady ones alike.

Sturdy the tortoise untroubled by what others thought pointed to a small basket on the path in the meadow.
"Whatever I want to do with what's inside," he
said pleased with her small fortun...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Yarrow announced the race in a voice loud enough to wake the owls, and Mossfoot accepted with a nod.

"You can find what you want in a basket several ways,"
Mossfoot the tortoise with eyes always on the path said, gesturing at the woven shape:
"by the tag pinned to it, by its place in line, or by si...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback the tortoise's pebble row held five stones laid out in order. She had lost track of the total and needed the REPL to confirm the count without her counting by hand. The value drawn fr...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Word went around at the edge of the orchard that two creatures had agreed to settle an old question with their feet.

A line of animals had formed by the orchard, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this proce...
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

#### ABSTRACT_RESULT_NARRATION

- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Boulderkin the tortoise stepping deliberately stretched a small net beneath a high jump
in the forest. "If the runner falls, the net catches them; the run
doesn't end, only the path ben...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    When Skim declared the race already won, no one yet knew how long the afternoon would be.

"What matters when something goes wrong," Wander the tortoise without complaint said,
"is that the run can continue — the runtime catches the slip,
takes the recovery path, and the answer comes back even when
...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

"This is the practice meadow," Truffle the tortoise untroubled by what others thought said near the garden,
gesturing wide. "A stumble here costs nothing. Type a form, see
what comes ba...
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

