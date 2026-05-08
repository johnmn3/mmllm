# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'VILLAGE_NOUN_OVERUSE': 1, 'HONEST_JUDGE_REPEAT': 1, 'TRUST_RHETORIC_FILLER': 1, 'FOREIGN_FABLE_IMAGERY': 3}
    - [VILLAGE_NOUN_OVERUSE] form=`\w` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [HONEST_JUDGE_REPEAT] form=`\w` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [TRUST_RHETORIC_FILLER] form=`\w` — user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    - [FOREIGN_FABLE_IMAGERY] form=`\w` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [FOREIGN_FABLE_IMAGERY] form=`\T` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [FOREIGN_FABLE_IMAGERY] form=`(char? \w)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
=======
- issues: {'STRING_AS_CHAR_MISCLAIM': 7}
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 1, 'GOAL_FALLBACK_GENERIC': 6}
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 'wolf)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? 'wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [GOAL_FALLBACK_GENERIC] form=`'wolf` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`'wolf` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`'wolf` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(= 'wolf 'wolf)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 6}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'LOW_GROUNDING': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(* 4 5)` — opener fragment 'at the edge of the orchard' also appears later in user_msg
    - [LOW_GROUNDING] form=`(+ 7 8)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 (* 2 3))` — sentence closes with a participial coda (', giving the total flock for the ledger.') — LLM-cadence; close on the verb instead

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 4, 'GOAL_FALLBACK_GENERIC': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 2)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 2)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(= "a" "a")` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [GOAL_FALLBACK_GENERIC] form=`(= :wolf :wolf)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(= :wolf :flock)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(= :wolf :flock)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 4, 'LOW_GROUNDING': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(zero? 5)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(pos? 7)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(pos? 7)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(neg? 4)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(neg? 4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(neg? 4)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1}
    - [SMALL_INT_LEAK] form=`(+ 1 2)` — small-int answer 3 leaks via resolution-slot phrasing

## Grade 2

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(< 3 2 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(> 5 4 3 2 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(>= 3 3 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(>= 3 3 2)` — sentence closes with a participial coda (', confirming the whole chain holds.') — LLM-cadence; close on the verb instead

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not= 1 2)` — sentence closes with a participial coda (', confirming the two lambs had separate weights.') — LLM-cadence; close on the verb instead
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= 1 1 1)` — sentence closes with a participial coda (", confirming the lamb's steady count across the full day.") — LLM-cadence; close on the verb instead
=======
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 1 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Wenceslas\nsimply began counting — to find the maximum of 2, 3, 5, 6, and 4 requi'

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1}
    - [SMALL_INT_LEAK] form=`(mod 17 5)` — small-int answer 2 leaks via resolution-slot phrasing

<<<<<<< HEAD
### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(inc -1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(inc -1)` — sentence closes with a participial coda (', canceling the debt.') — LLM-cadence; close on the verb instead

=======
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(abs 5)` — sentence closes with a participial coda (', ignoring the sign.') — LLM-cadence; close on the verb instead
=======
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs -5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(abs -5)` — sentence closes with a participial coda (', leaving the magnitude.') — LLM-cadence; close on the verb instead

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 5 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(str "flock")` — sentence closes with a participial coda (', leaving the original\nuntouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(str "flock")` — sentence closes with a participial coda (', leaving the original\nuntouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(str "x" "y" "z")` — sentence closes with a participial coda (', leaving the original\nuntouched.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 8 commas reads as AI-output cadence: 'To use str to join the integer 6, the plus sign, the integer 8, the equals sign,'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 8 commas reads as AI-output cadence: 'To use str to join the integer 8, the plus sign, the integer 6, the equals sign,'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(print "x")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(print "x")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
=======
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(or false true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(or false true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
<<<<<<< HEAD
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(and 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(and 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(and 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
=======
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [BOOL_LEAK_RESOLUTION] form=`(not true)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not true)` — sentence closes with a participial coda (", confirming the gate wasn't closed — it was open.") — LLM-cadence; close on the verb instead

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'GOAL_FALLBACK_GENERIC': 3, 'LOW_GROUNDING': 2}
    - [GOAL_FALLBACK_GENERIC] form=`(if nil :truthy :falsey)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(if nil :truthy :falsey)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [LOW_GROUNDING] form=`(if nil :truthy :falsey)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [GOAL_FALLBACK_GENERIC] form=`(if false :truthy :falsey)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [LOW_GROUNDING] form=`(if false :truthy :falsey)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'LOW_GROUNDING': 2, 'GOAL_FALLBACK_GENERIC': 1, 'THE_FORM_OVERUSE': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:wolf {:wolf 1 :flock 2})` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:wolf {:wolf 1 :flock 2})` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:flock {:wolf 1 :flock 2})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(:flock {:wolf 1 :flock 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [GOAL_FALLBACK_GENERIC] form=`(:missing {:wolf 1})` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:missing {:wolf 1})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:flock {:wolf 1 :flock 2})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(:flock {:wolf 1 :flock 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:missing {:wolf 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'GOAL_FALLBACK_GENERIC': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
=======
- issues: {'ANSWER_LEAK_STRING': 3, 'LOW_GROUNDING': 4, 'GOAL_FALLBACK_GENERIC': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [ANSWER_LEAK_STRING] form=`(quote wolf)` — answer string 'wolf' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'flock` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`'flock` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [GOAL_FALLBACK_GENERIC] form=`'flock` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'ONLY_SHOOK_HEAD_TIC': 1, 'SMALL_INT_LEAK': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', notching the\ntally-stick — returned the final number.') — LLM-cadence; close on the verb instead
    - [ONLY_SHOOK_HEAD_TIC] form=`(count [1 2 3])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'SMALL_INT_LEAK': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The runtime does this the same way for any kind of collection."\nTo count the ele'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [SMALL_INT_LEAK] form=`(count "hello")` — small-int answer 5 leaks via resolution-slot phrasing
    - [SMALL_INT_LEAK] form=`(count "hello")` — small-int answer 5 leaks via resolution-slot phrasing

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'THE_FORM_OVERUSE': 3, 'SMALL_INT_LEAK': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "shepherd")` — sentence closes with a participial coda (', leaving the original\nuntouched.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "shepherd")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(count "shepherd")` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "wolf")` — sentence closes with a participial coda (', leaving the original\nuntouched.') — LLM-cadence; close on the verb instead
    - [SMALL_INT_LEAK] form=`(count "wolf")` — small-int answer 4 leaks via resolution-slot phrasing
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "wolf")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'ANSWER_LEAK': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'SMALL_INT_LEAK': 1}
    - [ANSWER_LEAK] form=`(count "shepherd")` — answer 8 in narrative
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "shepherd")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [SMALL_INT_LEAK] form=`(count "wolf")` — small-int answer 4 leaks via resolution-slot phrasing
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "wolf")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(subs "shepherd" 0 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(quot (+ 100 50) 5)` — answer 30 in narrative
    - [ANSWER_LEAK] form=`(quot (+ 100 50) 5)` — answer 30 in narrative
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 247 words
=======
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 246 words
    - [SMALL_INT_LEAK] form=`(let [x 3] (+ x 1))` — small-int answer 4 leaks via resolution-slot phrasing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(let [a 1 b 2] (+ a b))` — user_msg 201 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 5 y 3] (- x y))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'HIGH_LENGTH': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [HIGH_LENGTH] form=`(let [a 1 b 2] (+ a b))` — user_msg 201 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 5 b (* a 2)] b)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5 b (* a 2)] b)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s\nedge and the pouch is empty again." To bind a to 5, then bi'
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] (+ x 1)) 4)` — user_msg 224 words
=======
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1}
    - [HIGH_LENGTH] form=`((fn [x] (+ x 1)) 4)` — user_msg 222 words
    - [SMALL_INT_LEAK] form=`((fn [x] (+ x 1)) 4)` — small-int answer 5 leaks via resolution-slot phrasing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The earlier steps prepare the way; the last\nstep is the answer." To create an an'

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'BOY_WOLF_NOUN_SATURATION': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [BOY_WOLF_NOUN_SATURATION] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — boy-wolf metaphor noun 'drill-card' appears 4× in user_msg — vary the imagery
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(#(+ % 1) 5)` — answer 6 in narrative

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'BOY_WOLF_NOUN_SATURATION': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words
    - [BOY_WOLF_NOUN_SATURATION] form=`((fn [x] x x x 99) 1)` — boy-wolf metaphor noun 'drill-card' appears 5× in user_msg — vary the imagery

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'REPL_TRIPLE_VOICE': 1, 'LOW_GROUNDING': 1}
    - [REPL_TRIPLE_VOICE] form=`(do 1 2 3)` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [+ 99] +)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — answer 6 in narrative
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`[1 2 3]` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`[]` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`["a" "b"]` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(nth [10 20 30] 0)` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 2)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 2)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
=======
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(conj [] :wolf)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(conj [] :wolf)` — sentence with 5 commas reads as AI-output cadence: 'The lookout returned with 14, 16, 19, 16, and 10 on his slate, the valley long b'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [] :wolf)` — sentence closes with a participial coda (', growing the empty form into a one-element vector.') — LLM-cadence; close on the verb instead

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`'()` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`{:wolf 1 :flock 2}` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`{:wolf 1 :flock 2}` — sentence with 8 commas reads as AI-output cadence: "The slate showed {('__kw__', 'apricot'): 15, ('__kw__', 'pomegranate'): 18, ('__"

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1} :missing :default)` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1} :missing :default)` — sentence with 8 commas reads as AI-output cadence: "The fold gate held tight against the count of {('__kw__', 'elderberry'): 8, ('__"

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(dissoc {:a 1 :b 2} :a)` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 6 commas reads as AI-output cadence: "{('__kw__', 'tangerine'): 20, ('__kw__', 'raspberry'): 7} stood as the answer th"
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence closes with a participial coda (', yielding the total number of pouches.') — LLM-cadence; close on the verb instead

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'LOW_GROUNDING': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count #{1 2 3})` — sentence closes with a participial coda (', giving the total count of distinct items in the set.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'BOOL_LEAK_RESOLUTION': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly, he wrot'
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 4)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 4)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 4)` — sentence with 5 commas reads as AI-output cadence: 'Carol marked 6, 5, 8, 11, and 14 on the watchhouse beam, the lookout high above '

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 5 commas reads as AI-output cadence: 'The fold gate held tight against the count of 15, 15, 15, 9, and 8, slate cool u'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3 4 5])` — sentence closes with a participial coda (', yielding the total.') — LLM-cadence; close on the verb instead

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 6}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(empty? [])` — sentence with 6 commas reads as AI-output cadence: '18, 3, 16, and 7 stood as the answer the fold required, slate, chalk, and a stea'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [1])` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [1])` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'GOAL_FALLBACK_GENERIC': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [GOAL_FALLBACK_GENERIC] form=`(last  [10 20 30])` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [TRAILING_PARTICIPLE_CLOSER] form=`(last  [10 20 30])` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(last  [10 20 30])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30 properly, he wrot'
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30 properly, he wrot'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(last  [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'The fold gate held tight against the count of 6, 6, 19, 8, and 3, slate cool und'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [HIGH_LENGTH] form=`(into [] '(1 2 3))` — user_msg 208 words
=======
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(into [] '(1 2 3))` — user_msg 207 words
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To convert a list containing 1, 2, and 3 into a vector, he composed building a v'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(into [] '(1 2 3))` — sentence closes with a participial coda (', preserving the order.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(into #{} [1 2 2 3])` — sentence closes with a participial coda (', collapsing the duplicate weight 2 into a single entry.') — LLM-cadence; close on the verb instead

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 225 words
=======
- issues: {'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 222 words
    - [BOOL_LEAK_RESOLUTION] form=`(= [1 2 3] '(1 2 3))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= [1 2 3] '(1 2 3))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: '6, 5, and 16 stood as the answer the fold required, slate, chalk, and a steady e'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= [1 2 3] '(1 2 3))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= [1 2 3] '(1 2 3))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (range 5))` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (seq [1 2 3]))` — sentence closes with a participial coda (', leaving the first\none exactly where it was.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_DRAWN_PLACEHOLDER': 1, 'DRAWN_PLACEHOLDER_LEAK': 1}
    - [HIGH_LENGTH] form=`(if (> 5 3) :a :b)` — user_msg 211 words
    - [UNFILLED_DRAWN_PLACEHOLDER] form=`(if (> 5 3) :a :b)` — user_msg has un-substituted `{drawn.east}` placeholder — slot mismatch or render-time gap
    - [DRAWN_PLACEHOLDER_LEAK] form=`(if (> 5 3) :a :b)` — user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 223 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when true :yes)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 220 words
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HIGH_LENGTH] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg 216 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
=======
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg 213 words
    - [ANSWER_LEAK_STRING] form=`(case 2 1 :one 2 :two 3 :three :default)` — answer string ':two' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'AND_HANDED_BACK_CADENCE': 1}
    - [AND_HANDED_BACK_CADENCE] form=`((fn [f x] (f (f x))) inc 5)` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 264 words
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(map #(* % %) [1 2 3 4])` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
=======
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'NUMERAL_LIST_IN_GOAL': 3}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 263 words
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: 'To apply a squaring operation to each element of the vector containing 1, 2, 3, '
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 7 commas reads as AI-output cadence: 'To apply a squaring operation to each element of the vector containing 1, 2, 3, '
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: '2, 16, and 2 stood as the answer the fold required, slate, chalk, and a steady e'

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'ONLY_SHOOK_HEAD_TIC': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + [1 2 3 4])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [ONLY_SHOOK_HEAD_TIC] form=`(reduce + [1 2 3 4])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce * [1 2 3 4 5])` — sentence closes with a participial coda (', notching the\ntally-stick — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence closes with a participial coda (', notching the\ntally-stick — returned the final number.') — LLM-cadence; close on the verb instead
=======
- issues: {'NUMERAL_LIST_IN_GOAL': 9, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 6}
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce * [1 2 3 4 5])` — goal_text contains 5 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 2, 'SENTENCE_START_LOWER_PRONOUN': 2, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 241 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', carrying the old count forward.') — LLM-cadence; close on the verb instead
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 100 [1 2 3])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 0 [])` — sentence closes with a participial coda (', walking\nthe flock — returned the final tally.') — LLM-cadence; close on the verb instead
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 0 [])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [ONLY_SHOOK_HEAD_TIC] form=`(reduce + 0 [])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
=======
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 241 words
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The runtime does this the same way for any kind of collection."\nTo fold + over t'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(apply + [1 2 3 4])` — sentence closes with a participial coda (', returning the result.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count

<<<<<<< HEAD
### G5-15: comp

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

=======
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'CONCEPT_AS_VERB': 1, 'HIGH_LENGTH': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [HIGH_LENGTH] form=`(map (partial * 3) [1 2 3])` — user_msg 236 words

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'The earlier steps prepare the way; the last\nstep is the answer." To apply a part'
    - [HIGH_LENGTH] form=`(map (partial * 3) [1 2 3])` — user_msg 235 words

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(some even? [1 3 5 8 7])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(drop 2 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(drop 2 [10 20 30 40 50])` — sentence with 5 commas reads as AI-output cadence: 'To drop the first 2 elements from the vector containing 10, 20, 30, 40, and 50, '
    - [NUMERAL_LIST_IN_GOAL] form=`(drop 2 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(distinct [1 1 2 3 3 4])` — user_msg 205 words
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 6 commas reads as AI-output cadence: '5, 18, 17, and 13 stood as the answer the fold required, slate, chalk, and a ste'
    - [HIGH_LENGTH] form=`(sort [3 1 2])` — user_msg 204 words
    - [CLAUSE_STACK_OVERFLOW] form=`(sort [3 1 2])` — sentence with 5 commas reads as AI-output cadence: 'To sort the vector containing 3, 1, and 2 in ascending order, she composed sorti'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(sort [3 1 2])` — sentence closes with a participial coda (', making the pattern clear.') — LLM-cadence; close on the verb instead
=======
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'What Clojure form computes the sequence produced by passing 1, 1, 2, 3, 3, 4 thr'
    - [HIGH_LENGTH] form=`(distinct [1 1 2 3 3 4])` — user_msg 206 words
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 6 commas reads as AI-output cadence: 'With one, the\nwalker knows when the circuit is done and the answer is the final\n'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'LOW_GROUNDING': 5, 'GOAL_FALLBACK_GENERIC': 3, 'BOOL_LEAK_RESOLUTION': 2}
=======
- issues: {'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 5, 'BOOL_LEAK_RESOLUTION': 2}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 'village.flock)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? 'village.flock)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
<<<<<<< HEAD
=======

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(clojure.string/lower-case "WOLF")` — answer string 'wolf' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [HIGH_LENGTH] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg 209 words
    - [BOOL_LEAK_RESOLUTION] form=`(= (clojure.string/upper-case "x") (clojure.string` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'ANSWER_LEAK_STRING': 1, 'REPL_TRIPLE_VOICE': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [ANSWER_LEAK_STRING] form=`(clojure.string/reverse "flock")` — answer string 'kcolf' appears in user_msg
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/reverse "flock")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
=======
- issues: {'ANSWER_LEAK_STRING': 2, 'REPL_TRIPLE_VOICE': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [ANSWER_LEAK_STRING] form=`(clojure.string/reverse "flock")` — answer string 'kcolf' appears in user_msg
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/reverse "flock")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [ANSWER_LEAK_STRING] form=`(namespace :village/shepherd)` — answer string 'village' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(name :village/shepherd)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [VILLAGE_NOUN_OVERUSE] form=`(boolean (:private (meta '^:private hidden)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)
=======
- issues: {'BOOL_LEAK_RESOLUTION': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'PATIENT_ROLE_BOASTFUL': 3, 'VILLAGE_NOUN_OVERUSE': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(:deps {:deps {:a 1 :b 2}})` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    - [VILLAGE_NOUN_OVERUSE] form=`(:deps {:deps {:a 1 :b 2}})` — `the village` appears 4 times (noun-saturation tic — vary or drop)
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(:deps {:deps {:a 1 :b 2}})` — sentence with 6 commas reads as AI-output cadence: 'To extract the value at the :deps key from a nested map,\nthe elder, letting the '

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'REPL_TRIPLE_VOICE': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "src:test" #":")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(clojure.string/split "src:test" #":")` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
=======
- issues: {'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "src:test" #":")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(count ["src" "test" "resources"])` — sentence with 6 commas reads as AI-output cadence: 'To count the number of entries in a vector of classpath directories,\nthe elder, '

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'GOAL_FALLBACK_GENERIC': 3}
    - [GOAL_FALLBACK_GENERIC] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 0.99
- issues: {'REPL_TRIPLE_VOICE': 1, 'RESOLUTION_REPL_DOUBLED': 3}
    - [REPL_TRIPLE_VOICE] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [RESOLUTION_REPL_DOUBLED] form=`(:author (meta '^{:author "Aesop"} village))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(:author (meta '^{:author "Aesop"} village))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(:author (meta '^{:author "Aesop"} village))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 0.98
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 0.99
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try 7 (finally :cleanup))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence with 5 commas reads as AI-output cadence: 'To throw an ex-info with data, catch it, and extract the value at key :k require'

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'ABSTRACT_RESULT_NARRATION': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — sentence closes with a participial coda (', stopping the bad input cold.') — LLM-cadence; close on the verb instead

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (assert (= 1 1)) :ok)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (prn 42))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'REPL_TRIPLE_VOICE': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(tap> :hello)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(tap> :hello)` — sentence closes with a participial coda (', proving the value had been tapped.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(tap> :hello)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(tap> 42)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

<<<<<<< HEAD
=======
### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (Exception. "oops")) (catch Exception ` — answer string 'oops' appears in user_msg

>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'REPL_TRIPLE_VOICE': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [REPL_TRIPLE_VOICE] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [ONLY_SHOOK_HEAD_TIC] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
=======
- issues: {'SMALL_INT_LEAK': 1, 'REPL_TRIPLE_VOICE': 1}
    - [SMALL_INT_LEAK] form=`(count (clojure.string/split-lines "a\nb\nc"))` — small-int answer 3 leaks via resolution-slot phrasing
    - [REPL_TRIPLE_VOICE] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 0.99
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (print "x"))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1, 'LOW_GROUNDING': 3, 'PROCEDURAL_OPENER': 2, 'GOAL_FALLBACK_GENERIC': 3}
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg 222 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [GOAL_FALLBACK_GENERIC] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
=======
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 3, 'PROCEDURAL_OPENER': 2, 'GOAL_FALLBACK_GENERIC': 3}
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg 215 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [GOAL_FALLBACK_GENERIC] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — sentence with 5 commas reads as AI-output cadence: 'Edmund, untroubled by what others thought, held up a small wooden tally-box near'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — sentence closes with a participial coda (', filling its compartments — returned the value\nthe tally-bo') — LLM-cadence; close on the verb instead
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — sentence with 5 commas reads as AI-output cadence: 'Edmund, untroubled by what others thought, held up a small wooden tally-box near'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'ANSWER_LEAK_STRING': 3}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — answer string 'elder' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — answer string 'elder' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — answer string 'elder' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — sentence closes with a participial coda (", running the word-keeper's implementation.") — LLM-cadence; close on the verb instead
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — sentence with 5 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — answer string ':string-alarm' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1}
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti tag :kind) (defmethod tag :lantern [` — sentence closes with a participial coda (',\ndispatching the sheep — returned the pen-specific value.') — LLM-cadence; close on the verb instead

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :wolf` — sentence closes with a participial coda (',\ndispatching the sheep — returned the pen-specific value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence closes with a participial coda (',\ndispatching the sheep — returned the pen-specific value.') — LLM-cadence; close on the verb instead

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 8 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'LOW_GROUNDING': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — sentence closes with a participial coda (',\ndispatching the sheep — returned the pen-specific value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(isa? java.lang.Long java.lang.Number)` — sentence closes with a participial coda (',\ndispatching the sheep — returned the pen-specific value.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Watch (look [this])) (defrecord S` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 5 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 0 to a new map, then return the unchanged '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 5 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 5 to a new map, then return the unchanged '

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
<<<<<<< HEAD
=======
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'The page\nchanges only when someone writes — and only as the REPL allows." To\ncon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'The REPL holds any second\nwriter at the threshold so the slate is never half-wri'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The page\nchanges only when someone writes — and only as the REPL allows." To\ncon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 5, perform a compare-and-set checking for 0 and set'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 5 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The REPL holds any second\nwriter at the threshold so the slate is never half-wri'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 228 words
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 221 words
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 223 words
=======
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 5}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 216 words
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send-off to asynchronously apply inc, await'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'LOW_GROUNDING': 2, 'AND_HANDED_BACK_CADENCE': 1}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AND_HANDED_BACK_CADENCE] form=`@(future (* 6 7))` — user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
=======
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (* 6 7))` — sentence with 5 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p 42) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver 42 to it, and dereference to get the delivered v'
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 6 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 6 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'The\nruntime makes that easier than it sounds." To construct a promise, deliver a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p 42) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver 42 to it, and dereference to get the delivered v'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p 42) @p)` — sentence with 6 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 203 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 0.99
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A\nrewrite-rule takes one form and produces a different form — only after\nthat do'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(macroexpand-1 '(or a b))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(when true 1))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(when true 1))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(or a b))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand '(-> 1 inc inc))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'REPEATED_OPENER_FRAGMENT': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(when true 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(when false 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [REPEATED_OPENER_FRAGMENT] form=`(when-not false :ok)` — opener fragment 'at the edge of the forest,' also appears later in user_msg
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(when-not false :ok)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
=======
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK_STRING': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(when-not false :ok)` — opener fragment 'at the edge of the forest,' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(when-not false :ok)` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [ANSWER_LEAK_STRING] form=`(when-not false :ok)` — answer string ':ok' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she chalke'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he chalked'
    - [CONCEPT_AS_VERB] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
=======
- issues: {'ANSWER_LEAK': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she chalke'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he chalked'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'EXPECTED_META_PHRASE': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [EXPECTED_META_PHRASE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'EXPECTED_META_PHRASE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 205 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [EXPECTED_META_PHRASE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [CLAUSE_STACK_OVERFLOW] form=`(if-let [x 7] (* x x) 0)` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: '2, 16, and 2 stood as the answer the fold required, slate, chalk, and a steady e'
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval '(+ 1 2 3))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval (list '+ 4 5))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(eval (list '+ 4 5))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro with-careful-watch [& body] `(let [p` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
=======
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-watch [name v] `(def ~name ~v)) ` — answer string ':alert' appears in user_msg
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — sentence with 6 commas reads as AI-output cadence: 'To understand that Clojure runs on multiple hosts,\nthe elder, with eyes always o'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence with 6 commas reads as AI-output cadence: 'To name the Clojure implementations for different north,\nthe elder, untroubled b'

### G11-02: Method call syntax

- examples: 8
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2, 'GOAL_FALLBACK_GENERIC': 3}
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 207 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 207 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [GOAL_FALLBACK_GENERIC] form=`(.length "shepherd")` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(.isEmpty "test")` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2, 'GOAL_FALLBACK_GENERIC': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G11-03: Static method call

- examples: 6
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'PROCEDURAL_OPENER': 2}
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
=======
- issues: {'PROCEDURAL_OPENER': 2, 'CLAUSE_STACK_OVERFLOW': 4}
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G11-04: Field access

- examples: 6
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 1}
    - [PROCEDURAL_OPENER] form=`(count "shepherd")` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G11-07: Arrays

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'GOAL_FALLBACK_GENERIC': 1}
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (int-array [10 20 30])] (aget a 1))` — the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (int-array [10 20 30])] (aget a 1))` — the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (int-array [10 20 30])] (aget a 1))` — the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G11-08: Type hints

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [^long n 42] (+ n 8))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'GOAL_FALLBACK_GENERIC': 1, 'LOW_GROUNDING': 1, 'PROCEDURAL_OPENER': 1}
    - [GOAL_FALLBACK_GENERIC] form=`(+ 1 2)` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [LOW_GROUNDING] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "ClojureScript compiles to JavaScript via the ` — sentence with 6 commas reads as AI-output cadence: 'To understand how ClojureScript compiles to JavaScript,\nthe elder, saying very l'

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — sentence with 6 commas reads as AI-output cadence: 'To understand how ClojureScript calls JavaScript globals and reads fields,\nthe e'
    - [AI_OUTPUT_CADENCE] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "basilisp is a Clojure-like Lisp implemented o` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 6 commas reads as AI-output cadence: 'To understand that basilisp is Clojure on Python,\nthe elder, with eyes always on'

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "#?(:clj … :cljs …) selects a form per host at` — sentence with 6 commas reads as AI-output cadence: 'To learn how reader-conditionals choose code per host,\nthe elder, with eyes alwa'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "#?(:clj … :cljs …) selects a form per host at` — sentence with 6 commas reads as AI-output cadence: 'To learn how reader-conditionals choose code per host,\nthe elder, without compla'
    - [CLAUSE_STACK_OVERFLOW] form=`(do ".cljc files share code across multiple hosts"` — sentence with 6 commas reads as AI-output cadence: 'To understand the role of .hard files,\nthe elder, stepping deliberately, compose'
    - [AI_OUTPUT_CADENCE] form=`(do ".cljc files share code across multiple hosts"` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G11-14: Debugging host leaks

- examples: 6
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 1, 'GOAL_FALLBACK_GENERIC': 4}
=======
- issues: {'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 1, 'CLAUSE_STACK_OVERFLOW': 7, 'GOAL_FALLBACK_GENERIC': 4}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [LOW_GROUNDING] form=`(try (Math/abs -42) (catch Exception _ :err))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [GOAL_FALLBACK_GENERIC] form=`(try (Math/abs -42) (catch Exception _ :err))` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(try (.length "test") (catch Exception _ :err))` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    - [GOAL_FALLBACK_GENERIC] form=`(try (.length "test") (catch Exception _ :err))` — user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 0.99
<<<<<<< HEAD
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_INPUT_VALUE_PARENS': 2}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 218 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
=======
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'NUMERAL_LIST_IN_GOAL': 3}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 216 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (filter even?) [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To use the filter-even transducer with into to keep only the even numbers from t'
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 212 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'REPL_TRIPLE_VOICE': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
=======
- issues: {'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [REPL_TRIPLE_VOICE] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "go-blocks let you write async code as if it w` — sentence with 6 commas reads as AI-output cadence: 'To learn how go-blocks let you write asynchronous code in a synchronous style,\nt'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do "go-blocks let you write async code as if it w` — sentence closes with a participial coda (', making the form readable.') — LLM-cadence; close on the verb instead

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'To study how pipe, mult, mix, and pipeline-async route values across channels, h'

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'To study how s/exercise produces sample inputs from a spec,\nthe elder, untrouble'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "spec generators turn specs into property-base` — sentence with 6 commas reads as AI-output cadence: 'To understand how coral,\nthe elder, letting the runtime have the last word, comp'

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'REPL_TRIPLE_VOICE': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
=======
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'REPL_TRIPLE_VOICE': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(= (+ 1 2) 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [REPL_TRIPLE_VOICE] form=`(= (+ 1 2) 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'AI_OUTPUT_CADENCE': 1}
    - [AI_OUTPUT_CADENCE] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'FORM_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
=======
- issues: {'FORM_LEAK': 1, 'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 2}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [FORM_LEAK] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — form '(= (reverse (reverse [1 2 3])) [1 2 3])' appears in user_msg of a goal-style subject
    - [CLAUSE_STACK_OVERFLOW] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To verify the property that reversing a vector twice returns the original vector'
    - [CLAUSE_STACK_OVERFLOW] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To verify the property that reversing a vector twice returns the original vector'

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "project.clj declares :dependencies, :main, :p` — sentence with 8 commas reads as AI-output cadence: 'To study the project.clj file and how it declares dependencies, main entry point'
    - [AI_OUTPUT_CADENCE] form=`(do "Leiningen reads project.clj at the project ro` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "deps.edn declares :deps and :aliases for the ` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 6 commas reads as AI-output cadence: 'To study the deps.edn file and how it declares dependencies and aliases for the '

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "`clj -M:test` runs the :test alias from deps.` — sentence with 6 commas reads as AI-output cadence: 'To study how the clj command with -M flag runs aliases defined in deps.edn,\nthe '
    - [CLAUSE_STACK_OVERFLOW] form=`(do "`clj -M:test` runs the :test alias from deps.` — sentence with 6 commas reads as AI-output cadence: 'To study how the clj command with -M flag runs aliases defined in deps.edn,\nthe '
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 10 commas reads as AI-output cadence: 'To understand how hard compose extra classpath entries, dependencies, and JVM op'
    - [AI_OUTPUT_CADENCE] form=`(do "aliases compose extra paths, deps, and main o` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 6 commas reads as AI-output cadence: 'To understand how low compose extra classpath entries, dependencies, and JVM opt'

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 8 commas reads as AI-output cadence: 'To study Datomic and XTDB as immutable, time-aware database systems using datalo'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 8 commas reads as AI-output cadence: 'To study Datomic and XTDB as immutable, time-aware database systems using datalo'

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — sentence with 6 commas reads as AI-output cadence: 'To study how thread structures,\nthe elder, untroubled by what others thought, co'

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
<<<<<<< HEAD
- issues: {'PATIENT_ROLE_BOASTFUL': 5, 'VILLAGE_NOUN_OVERUSE': 5, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "good libraries expose data, then functions, t` — patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "good libraries expose data, then functions, t` — `the village` appears 4 times (noun-saturation tic — vary or drop)
=======
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    - [CLAUSE_STACK_OVERFLOW] form=`(do "small public API surface, plain data inputs, ` — sentence with 6 commas reads as AI-output cadence: 'To understand the Clojure convention of a small public API surface with plain da'

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer pure functions, name predicates with ?` — sentence with 8 commas reads as AI-output cadence: 'To learn the Clojure naming conventions: pure function preference, question-mark'
    - [AI_OUTPUT_CADENCE] form=`(do "prefer pure functions, name predicates with ?` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer pure functions, name predicates with ?` — sentence with 8 commas reads as AI-output cadence: 'To learn the Clojure naming conventions: pure function preference, question-mark'

---

## Summary

### Issue counts (across all examples × 3 records)

<<<<<<< HEAD
- **TRAILING_PARTICIPLE_CLOSER**: 70
- **LOW_GROUNDING**: 68
- **CLAUSE_STACK_OVERFLOW**: 68
- **FORM_DISPLAY_AND_FORM_NOUN**: 54
- **NARRATIVE_NUMERAL_HARDCODE**: 36
- **GOAL_FALLBACK_GENERIC**: 35
- **SENTENCE_START_LOWER_PRONOUN**: 27
- **HIGH_LENGTH**: 24
- **VILLAGE_NOUN_OVERUSE**: 23
- **BOOL_LEAK_RESOLUTION**: 23
- **ONLY_SHOOK_HEAD_TIC**: 20
- **PATIENT_ROLE_BOASTFUL**: 20
- **HONEST_JUDGE_REPEAT**: 18
- **TRUST_RHETORIC_FILLER**: 15
- **FOREIGN_FABLE_IMAGERY**: 14
- **REPL_TRIPLE_VOICE**: 14
- **THE_FORM_OVERUSE**: 13
- **CONCEPT_AS_VERB**: 12
=======
- **CLAUSE_STACK_OVERFLOW**: 201
- **LOW_GROUNDING**: 68
- **NARRATIVE_NUMERAL_HARDCODE**: 60
- **NUMERAL_LIST_IN_GOAL**: 48
- **BOOL_LEAK_RESOLUTION**: 34
- **ANSWER_LEAK_STRING**: 31
- **GOAL_FALLBACK_GENERIC**: 30
- **HIGH_LENGTH**: 24
- **FORM_DISPLAY_AND_FORM_NOUN**: 22
- **ANSWER_LEAK**: 15
- **REPL_TRIPLE_VOICE**: 13
- **SMALL_INT_LEAK**: 8
- **STRING_AS_CHAR_MISCLAIM**: 7
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
- **PROCEDURAL_OPENER**: 7
- **DOUBLED_INPUT_VALUE_PARENS**: 6
- **STORY_RESOLUTION_NO_DRAWN**: 6
- **AI_OUTPUT_CADENCE**: 6
- **SMALL_INT_LEAK**: 5
- **REPEATED_OPENER_FRAGMENT**: 4
- **ANSWER_LEAK**: 3
- **ANSWER_LEAK_STRING**: 3
- **RESOLUTION_REPL_DOUBLED**: 3
<<<<<<< HEAD
- **ABSTRACT_RESULT_NARRATION**: 3
- **STORY_SLOT_NOUN_REPEAT**: 3
- **AND_HANDED_BACK_CADENCE**: 2
=======
- **HONEST_JUDGE_REPEAT**: 3
- **STORY_SLOT_NOUN_REPEAT**: 3
- **BOY_WOLF_NOUN_SATURATION**: 2
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
- **UNFILLED_DRAWN_PLACEHOLDER**: 1
- **DRAWN_PLACEHOLDER_LEAK**: 1
- **EXPECTED_META_PHRASE**: 1
- **COLLECTION_LEAK**: 1
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
<<<<<<< HEAD
| 1 | 18 | 80 | 91 | — |
| 2 | 22 | 88 | 95 | — |
| 3 | 18 | 31 | 26 | — |
| 4 | 20 | 39 | 67 | — |
| 5 | 22 | 39 | 41 | — |
| 6 | 16 | 33 | 43 | — |
| 7 | 18 | 36 | 32 | — |
| 8 | 16 | 31 | 32 | — |
| 9 | 18 | 34 | 28 | — |
| 10 | 16 | 36 | 41 | — |
| 11 | 14 | 58 | 51 | — |
| 12 | 18 | 37 | 63 | — |

### Sample issues by severity

#### HONEST_JUDGE_REPEAT

- `G1-01` (form `0`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

The elder of the village kept a small slate in the village, untroubled by what others thought,
with a tally of expressions the shepherds had honestly submitted versus
ones they had on...
    ```
- `G1-01` (form `(+ 1 2)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

The elder of the village kept a small slate in the village, saying very little,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guessed at. The valley ...
    ```
- `G1-02` (form `7`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    near the hilltop, on a slope above the village, Zenta watched his flock and his shadow grow longer.

The elder of the village kept a small slate near the hilltop, letting the runtime have the last word,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guesse...
    ```
- `G1-02` (form `0`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

The elder of the village kept a small slate near the orchard, untroubled by what others thought,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guessed at. ...
    ```
- `G1-02` (form `100`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

The elder of the village kept a small slate at the edge of the meadow, with the calm of a long watch well kept,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guess...
    ```

#### TRUST_RHETORIC_FILLER

- `G1-01` (form `0`): user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

The elder of the village kept a small slate in the village, untroubled by what others thought,
with a tally of expressions the shepherds had honestly submitted versus
ones they had on...
    ```
- `G1-01` (form `(+ 1 2)`): user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

The elder of the village kept a small slate in the village, saying very little,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guessed at. The valley ...
    ```
- `G1-02` (form `7`): user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    ```
    near the hilltop, on a slope above the village, Zenta watched his flock and his shadow grow longer.

The elder of the village kept a small slate near the hilltop, letting the runtime have the last word,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guesse...
    ```
- `G1-02` (form `0`): user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

The elder of the village kept a small slate near the orchard, untroubled by what others thought,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guessed at. ...
    ```
- `G1-02` (form `100`): user_msg has 2 stacked 'only voice/judge we trust / honest tally' filler phrases — replace with concrete algorithm narration
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

The elder of the village kept a small slate at the edge of the meadow, with the calm of a long watch well kept,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guess...
    ```

#### VILLAGE_NOUN_OVERUSE

- `G1-01` (form `(+ 1 2)`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

The elder of the village kept a small slate in the village, saying very little,
with a tally of expressions the shepherds had honestly submitted versus
ones they had only guessed at. The valley ...
    ```
- `G1-01` (form `"hello"`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    near the village, on a slope above the village, Kari watched his flock and his shadow grow longer.

Halfway through the morning watch, Kari, as if the village would always believe,
called out near the village, demanding a verdict on `"willow"`
and refusing to come back to the flock until somebody co...
    ```
- `G1-08` (form `\w`): `the village` appears 4 times (noun-saturation tic — vary or drop)
=======
| 1 | 18 | 80 | 36 | — |
| 2 | 22 | 88 | 65 | — |
| 3 | 18 | 31 | 30 | — |
| 4 | 20 | 39 | 55 | — |
| 5 | 22 | 39 | 82 | — |
| 6 | 16 | 33 | 33 | — |
| 7 | 18 | 36 | 24 | — |
| 8 | 16 | 31 | 50 | — |
| 9 | 18 | 34 | 75 | — |
| 10 | 16 | 36 | 35 | — |
| 11 | 14 | 58 | 61 | — |
| 12 | 18 | 37 | 49 | — |

### Sample issues by severity

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```
    When Andrej called out in the village the first time, the village came running, and the sheep stayed exactly as they were.

Andrej called down from a stone at the village where someone had
<<<<<<< HEAD
chalked the character \t on a flat board. Andrej, with a smug grin,
declared he already knew what would come ba...
    ```
- `G6-07` (form `(boolean (:private (meta '^:private hidden)))`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol showed Tom two entries in the village log-book. One symbol, `hidden`, carried a private marker in its margin. Carol asked Tom to convert the raw answer to a simple true or...
    ```
- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the value at the :deps key from a nested map. Melina, with great whoops of laughter, started
to shout an ans...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `(* 4 5)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(* 7 4)`, and the line
abo...
    ```
- `G1-01` (form `(+ 1 (* 2 3))`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Danuta had been minding the sheep by the woods since the first light, and the day was wearing thin.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(+ 1 (* 4 0))`, a...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Cesare had been minding the sheep by the farm since the first light, and the day was wearing thin.

A small slate sat on a flat stone at the farm; the day was long and the
slate filled slowly, mark by mark. On it the reeve recorded each
expression a shepherd had submitted to the REPL alongside each ...
    ```
- `G1-03` (form `(* 2 1/2)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    near the farm, in the long grass above the village road, Csilla settled in for another slow afternoon.

A small slate sat on a flat stone by the farm; the day was long and the
slate filled slowly, mark by mark. On it the reeve recorded each
expression a shepherd had submitted to the REPL alongside e...
    ```
- `G1-03` (form `(- 1 1/3)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    When Adriana called out by the woods the first time, the village came running, and the sheep stayed exactly as they were.

A small slate sat on a flat stone at the edge of the woods; the day was long and the
slate filled slowly, mark by mark. On it the reeve recorded each
expression a shepherd had s...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G1-02` (form `-3`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

Ulvilda, without complaint, kept a small leather notebook of
=======
chalked the character \indigo on a flat board. Andrej, with a smug grin,
declared he already knew what would co...
    ```
- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

The elder of the meadow folk kept a small slate near the orchard, with the calm of a long watch well kept,
with a tally of expressions the shepherds had directly submitted versus
ones they had only ...
    ```
- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Iarlaith was a clever boy, and by the forest cleverness had begun to look very much like trouble.

Crispin, with steady, careful steps, kept a small slate-pocket of
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
every expression the shepherds of the valley had actually evaluated —
each entry slow as the rising sun, the page-count climbing only
w...
    ```
<<<<<<< HEAD
- `G1-02` (form `-25`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

Gunhilda, with eyes always on the slate, kept a small leather notebook of
every expression the shepherds of the valley had actually evaluated —
each entry slow as the rising sun, the page-count cl...
    ```
- `G1-03` (form `1/2`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Gildas, with the calm of a long watch well kept, kept a small leather notebook of
every expression the shepherds of the valley had actually evaluated —
each entry slow as the rising ...
    ```
- `G1-04` (form `"flock"`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    Tunde was supposed to keep the sheep safe; instead, at the village, he kept inventing reasons for the village to run.

Theodelinda, letting the runtime have the last word, kept a small leather notebook of
every expression the shepherds of the valley had actually evaluated —
each entry slow as the ri...
    ```
- `G1-04` (form `"watch the meadow"`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    at the farm, on a slope above the village, Yara watched his flock and his shadow grow longer.

Walpurga, stepping deliberately, kept a small leather notebook of
every expression the shepherds of the valley had actually evaluated —
each entry slow as the rising sun, the page-count climbing only
when ...
=======
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Manfred called down from a stone by the meadow where someone had
chalked the character \space on a flat board. Manfred, as if the watchhouse would always believe,
declared he already knew what would come back....
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Wojciech had cried wolf once already, near the forest, and the villagers had laughed but not entirely.

Casimir had been trying to teach Wojciech how the REPL
works. "Look here," he said, pointing to the character \space.
"You hand `"marble"` to the runtime, and the runtime hands
you back what it ev...
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(symbol? 'wolf)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself. The village's notes must not mix chalk marks with the things they name. Tom had to te...
    ```
- `G1-15` (form `(= 1 2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had two tally-marks on a stone by the fold: one from the morning count, one from midday. Tom claimed they must differ because sheep move. Carol wrote them side by side to test. Before th...
    ```
- `G1-15` (form `(= 1 2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Carol had two tally-marks on a stone by the fold: one from the morning count, one from midday. Tom claimed they must differ because sheep move. Carol wrote them side by side to test. Before the...
    ```
- `G1-15` (form `(= "a" "a")`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol had written the letter `a` on the slate twice — once in the morning lesson, once in the afternoon. Tom wondered if the two marks were truly the same mark. The elder's teaching depended on sta...
    ```
- `G1-15` (form `(= 1 1 1 1)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Ulrich was a clever boy, and near the village cleverness had begun to look very much like trouble.

Carol had the stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test. Before the day's work ...
    ```

#### LOW_GROUNDING

- `G1-09` (form `(symbol? 'wolf)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself. The village's notes must not mix chalk marks with the things they name. Tom had to te...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Renzo had a fine view at the farm, but a finer talent for stretching a quiet hour into a noisy one.

Tom brought lambs from the north pen, Carol brought lambs from the south. Together they needed the total for the morning record. The day's first count had to lock in before the flock left for pasture...
    ```
- `G1-15` (form `(= 1 1 1 1)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Ulrich was a clever boy, and near the village cleverness had begun to look very much like trouble.

Carol had the stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test. Before the day's work ...
    ```
- `G1-16` (form `(pos? 7)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had tracked the flock's change from morning to afternoon: +0 sheep had returned. Tom asked if the predicate could confirm that the change was positive. The village's ledger recorded gains ...
    ```
- `G1-16` (form `(neg? 4)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The villagers lived just down the slope from where Veronika stood watch, and they trusted that voice.

Carol had tallied a gain of 0 fleeces. Tom asked if `neg?` would mistakenly mark the gain as negative. Gains and losses had to stay distinct. Tom had to trust that `neg?` would correctly reject pos...
    ```

#### GOAL_FALLBACK_GENERIC

- `G1-09` (form `'wolf`): user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Ingrid, sounding sure of every word, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Onorata reached for chalk: the mark and the shee...
    ```
- `G1-09` (form `'wolf`): user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    ```
    It happened in the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Rhys pointed at the chalk-mark `wolf` on the slate.
"That's a wolf," he said. Henriette, untroubled by what others thought,
shook her head and pointed at the empty meadow beyond the
pen: "T...
    ```
- `G1-09` (form `'wolf`): user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

"To talk about the form itself rather than evaluating it,"
Remigius, stepping deliberately, said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't evaluate this, just h...
    ```
- `G1-09` (form `(= 'wolf 'wolf)`): user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Clementine, saying very little, pointed at a name chalked onto the slate near the woods,
then at an actual sheep standing in the fold. "The mark on the
slate is the *name*; the sheep is the *valu...
    ```
- `G1-09` (form `(= 'wolf 'wolf)`): user_msg uses generic 'To evaluate the X, ...' fallback AND no drawn-literal anchor — add a canonical GOALS entry for richer prose
    ```
    Conrad had cried wolf once already, in the forest, and the villagers had laughed but not entirely.

Conrad pointed at the chalk-mark `wolf` on the slate.
"That's a wolf," he said. Benedict, without complaint,
shook his head and pointed at the empty meadow beyond the
pen: "That mark is the name of a ...
    ```

#### TRAILING_PARTICIPLE_CLOSER

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol had chalked an addition on the slate with a dashed line and notes in smaller chalk to the right — annotation only, for the next shepherd's eye. Tom worried the runtime might mix annotatio...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    on the farm, where the path winds up toward the lookout, Yelena watched and waited and watched some more.

Yelena, with a smug grin, glanced at the form and called out
what she thought it would do without paying attention to
the conventions of how it was written. Kasimir only
shook his head — the ru...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

Evangelos, puffed up with pride, glanced at the form and called out
what he thought it would do without paying attention to
the conventions of how it was written. Theodelinda only
shook her head — the runtime r...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    When Dorina called out in the village the first time, the village came running, and the sheep stayed exactly as they were.

"The runtime reads our forms the way the watchhouse reads its
posted notices," Euclid said, stepping deliberately, chalk in hand at
the cool slate. "What counts as one word, wh...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    in the village, where the path winds up toward the lookout, Ivan watched and waited and watched some more.

Ivan, as if the village would always believe, glanced at the form and called out
what he thought it would do without paying attention to
the conventions of how it was written. Oswald only
shoo...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-13` (form `(* 4 5)`): opener fragment 'at the edge of the orchard' also appears later in user_msg
    ```
    When Evangelos called out at the edge of the orchard the first time, the village came running, and the sheep stayed exactly as they were.

Evangelos eyed the grazing flock at the edge of the orchard, boasting at every turn, and called out a
guess about how many sheep were there without bothering to ...
    ```
- `G10-06` (form `(when-not false :ok)`): opener fragment 'at the edge of the forest,' also appears later in user_msg
    ```
    at the edge of the forest, where the path winds up toward the lookout, Giulia watched and waited and watched some more.

Zephaniah, stepping deliberately, sat at a small writing desk at the edge of the forest, slate and chalk
in hand. "A macro," he said, "is a rule that rewrites
the shorthand before...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): opener fragment 'at the edge of the meadow,' also appears later in user_msg
    ```
    at the edge of the meadow, on a slope above the village, Calista watched his flock and his shadow grow longer.

The village's rule, by long agreement at the edge of the meadow, was simple: a
question was answered by a form, never by a claim. To understand that basilisp is Clojure on Python,
the elde...
    ```
- `G12-12` (form `(do "deps.edn declares :deps and :aliases for the Clojure CL`): opener fragment 'at the edge of the meadow,' also appears later in user_msg
    ```
    at the edge of the meadow, on a slope above the village, Calista watched his flock and his shadow grow longer.

The village's rule, by long agreement at the edge of the meadow, was simple: a
question was answered by a form, never by a claim. To study the deps.edn file and how it declares dependencie...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Ulrich was a clever boy, and near the village cleverness had begun to look very much like trouble.

Carol had the stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test. Before the day's work ...
    ```
- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    The villagers lived just down the slope from where Carlotta stood watch, and they trusted that voice.

Carlotta, as if the watchhouse would always believe, watched the fold-gates atop the hilltop and claimed to
know exactly what they would do without checking the condition. "I just know,"
she insist...
    ```
- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

"So the gate just says yes or no?" Donata asked.
Valentina, with eyes always on the slate, shook her head and tapped the heavy
timber. "Look closely. The gate carries the actual value...
    ```
- `G2-18` (form `'(1 2 3)`): parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Sabina, as if the village would always believe, tried to fetch the value that the
chalk mark should carry, insisting it must be there waiting.
Hilda picked up the slate and pointed: the mark...
    ```
- `G2-18` (form `'(1 2 3)`): parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Anouk pointed at the chalk-mark `wolf` on the slate.
"That's a wolf," she said. Bertilda, untroubled by what others thought,
shook her head and pointed at the empty meadow beyond the
pen: "That mark is the na...
    ```

#### REPL_TRIPLE_VOICE

- `G1-17` (form `42`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol had chalked a number on the watchhouse slate. Tom peered at it and asked whether that mark on the stone was the value itself or just a record. Tom had to understand that the runtime's return ...
    ```
<<<<<<< HEAD
- `G3-14` (form `(do 1 2 3)`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Carol had written 1 numbers on her slate in a column: 4, then 8, then 1. She asked Tom: if I ask the REPL to read this whole sequence, what comes back? Tom needed to learn that `do` groups forms together, but ...
    ```
=======
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
- `G6-05` (form `(clojure.string/reverse "flock")`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

At the smithy's next post, a different tool waited: `clojure.string/reverse`. Carol asked Tom to call it by its full name and see what it would do to the word "flock". Tom was beginni...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Maarten had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

The reeve had written a list of directories on a single scroll line, separated by colons—the classpath, a road map of where the REPL would search for files. Tom wanted to turn the colon-separated st...
    ```
- `G6-15` (form `(:doc (meta '^{:doc "trust the runtime"} village))`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

"The world outside the REPL is bigger than the REPL,"
Yolanda, with steady, careful steps, said, "and the log-book out there has its own
discipline — open it carefully, handle it with care, close it when
you're...
    ```
- `G7-08` (form `(with-out-str (prn 42))`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

"The world outside the REPL is bigger than the REPL,"
Theodoric, with the calm of a long watch well kept, said, "and the log-book out there has its own
discipline — open it carefully, handle it with...
    ```

#### SMALL_INT_LEAK

- `G1-18` (form `(+ 1 2)`): small-int answer 3 leaks via resolution-slot phrasing
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Tom hesitated at the practice-pen behind the watchhouse. Carol had set out a slate and chalk to demonstrate. Tom was anxious about errors. Carol explained the pen made careless tries cost noth...
    ```
- `G2-05` (form `(mod 17 5)`): small-int answer 2 leaks via resolution-slot phrasing
    ```
    It was in the orchard, where the ridge looks down on the houses, that Nikolai first cried wolf.

Carol worked with `mod` to sort lambs by a five-day cycle. On day 12 of the year, she wanted to know which position in the cycle it occupied. The position in the five-day cycle mattered for rotation. Tom...
    ```
- `G2-20` (form `(count "hello")`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    Eamon had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Carol wrote the word 'marble' on the slate and wanted to know how many characters it held. The character count mattered for the ledger. Tom said five; Carol insisted the form would walk the string and...
    ```
- `G2-20` (form `(count "hello")`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    It was near the hilltop, where the ridge looks down on the houses, that Leonardo first cried wolf.

Carol wrote the word 'myrtle' on the slate and wanted to know how many characters it held. The character count mattered for the ledger. Tom said five; Carol insisted the form would walk the string and...
    ```
- `G2-21` (form `(count "wolf")`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol wrote 'myrrh' on the slate and wanted to know its length. The name appeared shorter than 'shepherd'. The comparison mattered for the record. Tom said four; Carol insisted it would settle t...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G2-04` (form `(max 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'Wenceslas\nsimply began counting — to find the maximum of 2, 3, 5, 6, and 4 requi'
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Galina eyed the grazing flock in the meadow, with the swagger of an unrepentant fibber, and called out a
guess about how many sheep were there without bothering to count. Wenceslas
si...
    ```
- `G2-11` (form `(str 1 "+" 2 "=" 3)`): sentence with 8 commas reads as AI-output cadence: 'To use str to join the integer 6, the plus sign, the integer 8, the equals sign,'
    ```
    near the hilltop, in the long grass above the village road, Krystyna settled in for another slow afternoon.

Krystyna, boasting at every turn, yanked at the tally-cord atop the hilltop
without bothering to count the knots. Horatio stopped
her firmly: a cord's knots are precise — every one
in its pla...
    ```
- `G2-11` (form `(str 1 "+" 2 "=" 3)`): sentence with 8 commas reads as AI-output cadence: 'To use str to join the integer 8, the plus sign, the integer 6, the equals sign,'
    ```
    It was at the edge of the hilltop, where the ridge looks down on the houses, that Isabella first cried wolf.

Isabella, sounding sure of every word, yanked at the tally-cord on the hilltop
without bothering to count the knots. Dorotheus stopped
her firmly: a cord's knots are precise — every one
in i...
    ```
<<<<<<< HEAD
- `G4-03` (form `(conj [] :wolf)`): sentence with 5 commas reads as AI-output cadence: 'The lookout returned with 14, 16, 19, 16, and 10 on his slate, the valley long b'
=======
- `G2-13` (form `(or nil false 5)`): sentence with 5 commas reads as AI-output cadence: 'To apply or to nil, false, and 1, she composed\nthe logical or, submitted it, and'
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```
    Genevieve had a fine view on the road, but a finer talent for stretching a quiet hour into a noisy one.

Carol brought an empty wool-basket to the fold. Tom wanted to add a single marker, the keyword `:wolf`, to track which fleeces came from the wolf-shearing. The form had to write a basket with jus...
    ```
- `G4-06` (form `{:wolf 1 :flock 2}`): sentence with 8 commas reads as AI-output cadence: "The slate showed {('__kw__', 'apricot'): 15, ('__kw__', 'pomegranate'): 18, ('__"
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol stitched a wool-basket with two named pouches inside: one labeled `:wolf` holding 1 fleece from the south pasture, another `:flock` holding 2 from the north morning shearing. The for...
    ```

#### ANSWER_LEAK

- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume. The cube volume required multiplying 2 three times. Tom estimated; Carol dr...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): answer 6 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Tom handed Carol a count of 5 sheep, and Carol needed to add one more to it for the fold's requirement. She wanted a quick shorthand for the addition. The add-one operation was so brief, Carol ...
    ```
- `G10-10` (form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~t`): answer 10 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol warned Tom about a tempting but dangerous macro style: anaphoric macros that secretly inject a name into the user's code. She showed him a safe alternative: `safe-if-let`, which bound the...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G2-07` (form `(abs -5)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Carol recorded -7 on the slate — a loss of five fleeces. For the shipment ledger, she needed the magnitude alone. The distance from zero mattered, not the direction. Tom said the los...
    ```
- `G2-12` (form `(print "x")`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol wanted to write a single character `lichen` to the slate without moving to a new line. She asked what it would return. The character needed to appear, and the form's return value had...
    ```
- `G2-12` (form `(print "x")`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    in the meadow, in the long grass above the village road, Roswitha settled in for another slow afternoon.

Carol wanted to write a single character `garnet` to the slate without moving to a new line. She asked what it would return. The character needed to appear, and the form's return value had to be...
    ```
- `G2-17` (form `(:flock {:wolf 1 :flock 2})`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol's wool-basket held the same two pouches: one for the wolf-fleeces, one for the flock-fleeces. Tom wanted the count from the flock-pouch. A clean lookup was needed without disturbing the ...
    ```
- `G2-21` (form `(count "shepherd")`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Carol wrote the word 'willow' on the slate as a long bead-string. She wanted to count every bead in the cord. The string length mattered for labeling in the ledger. Tom said roughly ...
    ```

<<<<<<< HEAD
#### SENTENCE_START_LOWER_PRONOUN

- `G2-20` (form `(count [])`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    The villagers lived just down the slope from where Kasper stood watch, and they trusted that voice.

Kasper, in a panic, was beginning to understand: the
tally-stick walk was not magic, only patient. Nikodemus took the
goal — to count the elements in an empty vector — and composed the count operatio...
    ```
- `G2-20` (form `(count [])`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    When Theobald called out by the meadow the first time, the village came running, and the sheep stayed exactly as they were.

Theobald, calling out without confidence anyone would come, was beginning to understand: the
tally-stick walk was not magic, only patient. Magnus took the
goal — to count the ...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Gudrun had been minding the sheep along the road since the first light, and the day was wearing thin.

Gudrun, wide-eyed with fear, was beginning to understand:
the belt-pouch was not magic, only careful. Cordelia took the
goal — to bind a value of 5 to a local name x for one stretch, then return th...
    ```
- `G3-04` (form `(let [x 5 y 3] (- x y))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Brendan, with the fear of a watch that no one trusts, was beginning to understand:
the belt-pouch was not magic, only careful. Engelberta took the
goal — to bind x to 3 and y to 7, then subt...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

Soren, calling out without confidence anyone would come, was beginning to understand:
the belt-pouch was not magic, only careful. Jacquelyn took the
goal — to bind a to 8, then bind b to twice a, and return b —...
=======
#### ANSWER_LEAK_STRING

- `G2-18` (form `(quote wolf)`): answer string 'wolf' appears in user_msg
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol drew a chalk mark on the slate and labeled it `wolf`. She wanted the mark itself — the symbol — not what it named. The village needed the chalk mark as a name, not a direction to run. To...
    ```
- `G2-18` (form `(quote wolf)`): answer string 'wolf' appears in user_msg
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Carol drew a chalk mark on the slate and labeled it `wolf`. She wanted the mark itself — the symbol — not what it named. The village needed the chalk mark as a name, not a direction to run. Tom...
    ```
- `G2-18` (form `(quote wolf)`): answer string 'wolf' appears in user_msg
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Carol drew a chalk mark on the slate and labeled it `wolf`. She wanted the mark itself — the symbol — not what it named. The village needed the chalk mark as a name, not a direction to run. Tom said 'wolf' wa...
    ```
- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol posted a watch-order at the fold: if the lambs were restless today, Tom was to ring the bell and post a notice at the townsfolk stone. Tom checked the pen, and warm — the lambs were paci...
    ```
- `G5-06` (form `(case 2 1 :one 2 :two 3 :three :default)`): answer string ':two' appears in user_msg
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol marked east lambing-pens with numbers: 4 for north-fold lambs, 2 for south-fold, 7 for those born late. Tom held a tally-token marked with the number 2. The form would read the token...
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```

#### HIGH_LENGTH

<<<<<<< HEAD
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 247 words
=======
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 246 words
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 7 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the ...
    ```
- `G3-04` (form `(let [a 1 b 2] (+ a b))`): user_msg 201 words
    ```
    It happened at the edge of the hilltop, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol the elder had watched two separate morning counts: 2 lamb at the upper pasture, 3 at the lower fold. She slipped both tally-tokens into her belt-pouch at once. The village...
    ```
<<<<<<< HEAD
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): user_msg 224 words
=======
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): user_msg 222 words
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg 201 words
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had written a drill-card with three steps: read x, read x again, read x a third time. But then she realized the final step should return 99 instead. Tom asked: if the drill-card lists many...
    ```
- `G4-16` (form `(into [] '(1 2 3))`): user_msg 207 words
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

Carol set up the fleece-comb at the watchhouse, an empty wool-basket beneath it. Three fleeces arrived from the morning shearing, threaded onto a rough cord ready to be fed through the comb. The villa...
    ```

<<<<<<< HEAD
#### CONCEPT_AS_VERB

- `G3-08` (form `((fn [a b c] (+ a b c)) 1 2 3)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

"A drill-card is only useful when it runs," Ignatius, saying very little, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime doe...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It happened near the woods, on a hill where shouting carries far and trust carries further, until it doesn't.

"A drill-card is only useful when it runs," Kasimir, with steady, careful steps, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the r...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

"A drill-card is only useful when it runs," Leonora, stepping deliberately, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runti...
    ```
- `G3-15` (form `(do (println "hi") 42)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the hilltop, on a slope above the village, Carys watched his flock and his shadow grow longer.

"A drill-card is only useful when it runs," Bartholomew, with the calm of a long watch well kept, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds...
    ```
- `G5-15` (form `((comp inc inc) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the hilltop, on a slope above the village, Carys watched his flock and his shadow grow longer.

"A drill-card is only useful when it runs," Bartholomew, letting the runtime have the last word, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds,...
=======
#### BOY_WOLF_NOUN_SATURATION

- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): boy-wolf metaphor noun 'drill-card' appears 4× in user_msg — vary the imagery
    ```
    Owain had a fine view by the woods, but a finer talent for stretching a quiet hour into a noisy one.

Carol noticed shepherds constantly asking her to sum three separate counts — north, east, and fold — all morning. She decided to post a standing drill-card. A named routine would save time. The vill...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): boy-wolf metaphor noun 'drill-card' appears 5× in user_msg — vary the imagery
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had written a drill-card with three steps: read x, read x again, read x a third time. But then she realized the final step should return 99 instead. Tom asked: if the drill-card lists many...
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
    ```

#### UNFILLED_DRAWN_PLACEHOLDER

- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg has un-substituted `{drawn.east}` placeholder — slot mismatch or render-time gap
    ```
    near the hilltop, on a slope above the village, Tove watched his flock and his shadow grow longer.

Tom stood sorting wool by weight at the watchhouse. Carol had given him a simple rule: if a fleece weighed more than three coins' worth, send it to the dyer; if not, keep it for the lambing-pen. A fle...
    ```

#### DRAWN_PLACEHOLDER_LEAK

- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg contains an un-substituted {drawn.<slot>} placeholder — interpolation pipeline missed it
    ```
    near the hilltop, on a slope above the village, Tove watched his flock and his shadow grow longer.

Tom stood sorting wool by weight at the watchhouse. Carol had given him a simple rule: if a fleece weighed more than three coins' worth, send it to the dyer; if not, keep it for the lambing-pen. A fle...
    ```

<<<<<<< HEAD
#### AND_HANDED_BACK_CADENCE

- `G5-09` (form `((fn [f x] (f (f x))) inc 5)`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol drew a drill-card on the watchhouse wall with a blank slot for a recipe and a blank slot for a starting number. Tom came with the recipe `inc` (add one) and the number 5. Carol said the card ...
    ```
- `G9-13` (form `@(future (* 6 7))`): user_msg tail has 3 performed/handed-back/returned verbs — AI-output verb-and-verb cadence
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Krystyna, sounding sure of every word, reached for the runner's pouch
before the runner had even returned. Severina held
her back: a runner sent ahead must be allowed to
finish. To construct a f...
    ```

#### DOUBLED_INPUT_VALUE_PARENS

- `G5-10` (form `(map #(* % %) [1 2 3 4])`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

Carol gave Tom a comb with four knots and asked him to square each one. Tom needed to apply a complex recipe to each value in the basket. `map` applies a recipe to each value in the collection and r...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Maarten had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

The reeve had written a list of directories on a single scroll line, separated by colons—the classpath, a road map of where the REPL would search for files. Tom wanted to turn the colon-separated st...
    ```
- `G8-01` (form `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Carol had called a meeting of the shepherds' fellowship on the village green — sheep-shepherd, goat-shepherd, geese-keeper, all gathered. Each kind of keeper had their own way of raising an ...
    ```
- `G10-06` (form `(when-not false :ok)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

Carol had another shorthand that inverted the test. Some watches ran only when a condition was false. `when-not` is a macro that inverts the condition and expands to a negated-test form.

To use whe...
    ```
- `G12-01` (form `(into [] (filter even?) [1 2 3 4 5])`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Carol attached a filtering rule to the fleece-comb. The village wanted only the even-numbered items collected together. `into` feeds items through the transducer into a receiver vector.

To use the filter-even...
    ```

#### ANSWER_LEAK_STRING

- `G6-05` (form `(clojure.string/reverse "flock")`): answer string 'kcolf' appears in user_msg
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

At the smithy's next post, a different tool waited: `clojure.string/reverse`. Carol asked Tom to call it by its full name and see what it would do to the word "flock". Tom was beginni...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form. Tom wanted to understan...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form. Tom wanted to understan...
    ```

#### PATIENT_ROLE_BOASTFUL

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the value at the :deps key from a nested map. Melina, with great whoops of laughter, started
to shout an ans...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): patient role 'the elder' co-occurs with boastful EMO phrase 'with the swagger of an unrepen'
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Melina, with the swagger of an unrepentant fibbe...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): patient role 'the elder' co-occurs with boastful EMO phrase 'puffed up with pride'
    ```
    Renzo had a fine view at the edge of the orchard, but a finer talent for stretching a quiet hour into a noisy one.

At the village notice-stone in the orchard, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Renzo, puffed up with pride, ...
    ```
- `G11-01` (form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :`): patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

At the village notice-stone at the farm, the question of the day was
posted: how to understand that Clojure runs on multiple hosts. Calista, boasting at every turn, started
to shout an ans...
    ```
- `G11-05` (form `(do "(:import (java.util Date)) imports a host class" :impor`): patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    ```
    Floarea was supposed to keep the sheep safe; instead, on the road, he kept inventing reasons for the village to run.

At the village notice-stone on the road, the question of the day was
posted: how to understand how to import a host class into a namespace. Floarea, with a smug grin, started
to shou...
    ```

=======
>>>>>>> origin/claude/round3-group4-boy-wolf-V7dL
#### RESOLUTION_REPL_DOUBLED

- `G6-15` (form `(:author (meta '^{:author "Aesop"} village))`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

"There's the world inside the REPL," Vespasia, letting the runtime have the last word, said, "and the
world outside it. Watch-roll scrolls are how the two meet — a value
crosses out and be...
    ```
- `G6-15` (form `(:author (meta '^{:author "Aesop"} village))`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

Helene, boasting at every turn, claimed she could guess
what the leather-bound village log-book would say without bothering
to open it. Cornelius opened the book near the village, dipping a quill
into...
    ```
- `G6-15` (form `(:author (meta '^{:author "Aesop"} village))`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

"Reading and writing watch-roll scrolls is just like reading and
writing forms," Gertrude, untroubled by what others thought, said. "You ask the runtime for what's
on the parchment, you write what y...
    ```

#### ABSTRACT_RESULT_NARRATION

- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

"There's a discipline to running safely," Jacquelyn, without complaint, said, "and it starts
with checking — making sure the form does what it claims, catching what could go
wrong before it does." To call a fun...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    The villagers lived just down the slope from where Gabriel stood watch, and they trusted that voice.

"There's a discipline to running safely," Xaverius, letting the runtime have the last word, said, "and it starts
with checking — making sure the form does what it claims, catching what could go
wron...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

"This is the practice-pen," Ferdinand, letting the runtime have the last word, said in the village, gesturing wide. "A slip
here costs nothing. Write a form, see what comes back, fix ...
    ```

#### PROCEDURAL_OPENER

- `G8-01` (form `(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "b`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

To evaluate the form, she composed speak applied to :flock via cond-dispatch and submitted it. The REPL — checking the fellowship roll — dispatched cleanly:

Write a Clojure expression that computes what speak ...
    ```
- `G8-01` (form `(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "b`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    When Shimon called out at the edge of the hilltop the first time, the village came running, and the sheep stayed exactly as they were.

To evaluate the form, she composed speak applied to :flock via cond-dispatch and submitted it. The REPL — checking the fellowship roll — dispatched cleanly:

Write ...
    ```
- `G11-03` (form `(Math/abs -7)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

To call the static host method Math/abs with the argument -7, she composed the static host method Math/abs and submitted it. The REPL — calling into the foreign smithy — returned:

Write a for...
    ```
- `G11-03` (form `(Math/abs -7)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

To call the static host method Math/abs with the argument -7, she composed the static host method Math/abs and submitted it. The REPL — calling into the foreign smithy — returned:

Write a for...
    ```
- `G11-04` (form `(count "shepherd")`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It happened at the edge of the hilltop, on a hill where shouting carries far and trust carries further, until it doesn't.

To evaluate the form, he composed the count of "thistle" and submitted it. The REPL — calling into the foreign smithy — returned:

Question: write a Clojure expression for the l...
    ```

#### HONEST_JUDGE_REPEAT

- `G8-05` (form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Carol had posted a Greet protocol at the fold-gate. A number-keeper — a tender of the tally-sticks — offered their pledge: any number greeting would return the keyword `:number`. The ...
    ```
- `G8-07` (form `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol defined a tally-box shape called Shepherd — a box with a name slot. She also declared: any Shepherd box that lives in the world must implement the Alarm protocol with its ...
    ```
- `G8-16` (form `(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] `): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    at the farm, in the long grass above the village road, Idun settled in for another slow afternoon.

Carol had a Sound protocol. Shepherds cried out alarms when danger came; Elders stayed calm and measured. Two tally-boxes, two pledges. One named method `cry` that both kinds answered, but each with t...
    ```

#### EXPECTED_META_PHRASE

- `G10-10` (form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~t`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol warned Tom about a tempting but dangerous macro style: anaphoric macros that secretly inject a name into the user's code. She showed him a safe alternative: `safe-if-let`, which bound the...
    ```

#### STORY_SLOT_NOUN_REPEAT

- `G11-07` (form `(let [a (int-array [10 20 30])] (aget a 1))`): the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Damien, with great whoops of laughter, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Drusilla sighed and walked over: to...
    ```
- `G11-07` (form `(let [a (int-array [10 20 30])] (aget a 1))`): the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Philippa, with the swagger of an unrepentant fibber, reached for a foreign tool from the
toolshed and tried to call it his own way, without checking the label.
Diogenes caught her. "Each tool in the foreign
t...
    ```
- `G11-07` (form `(let [a (int-array [10 20 30])] (aget a 1))`): the noun 'the host's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    When Philippa called out by the orchard the first time, the village came running, and the sheep stayed exactly as they were.

Philippa, with the swagger of an unrepentant fibber, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Is...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G11-07` (form `(let [a (int-array [1 2 3])] (alength a))`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Octavia, with steady, careful steps, pointed past the cool stone wall behind
the watchhouse to the smith's shed. "Our toolshed is on this side; the
smith's is on that side. When we need a smith...
    ```
- `G11-07` (form `(let [a (int-array [1 2 3])] (alength a))`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    ```
    on the farm, in the long grass above the village road, Pieter settled in for another slow afternoon.

Carol showed Tom another host tool: 'alength', which measured how many boxes an array held. The array was a fixed container; its length never changed once it was built. Tom wanted to know how many i...
    ```
- `G11-07` (form `(let [a (int-array [1 2 3])] (alength a))`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    ```
    Tegan had cried wolf once already, in the forest, and the villagers had laughed but not entirely.

Tegan, boasting at every turn, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Isidora sighed and walked over: to
get the length o...
    ```
- `G11-07` (form `(let [a (int-array [5 10 15])] (aget a 0))`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10', '15'), resolution doesn't close the loop)
    ```
    When Jutta called out near the road the first time, the village came running, and the sheep stayed exactly as they were.

Jutta, sounding sure of every word, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Salomea sighed and walk...
    ```
- `G11-07` (form `(let [a (int-array [5 10 15])] (aget a 0))`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10', '15'), resolution doesn't close the loop)
    ```
    The villagers lived just down the slope from where Yannis stood watch, and they trusted that voice.

Yannis, as if the village would always believe, reached for a foreign tool from the
toolshed and tried to call it his own way, without checking the label.
Septimus caught him. "Each tool in the forei...
    ```

#### AI_OUTPUT_CADENCE

- `G11-11` (form `(do "js/<name> namespaces JS globals; .- prefix marks field `): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Albertina, letting the runtime have the last word, had been showing Ula
the way the meadow folk's careful shepherds settled questions on the
long valley road. To learn the conventions for ClojureScript-JavaScr...
    ```
- `G11-13` (form `(do ".cljc files share code across multiple hosts" :cljc)`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    Valeria was a clever boy, and atop the hilltop cleverness had begun to look very much like trouble.

Joachim, with the calm of a long watch well kept, had been showing Valeria
the way the meadow folk's careful shepherds settled questions on the
long valley road. To understand the role of .low files,...
    ```
- `G12-09` (form `(do "(use-fixtures :each f) wraps every deftest in setup/tea`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Ignatius, with steady, careful steps, had been showing Cyril
the way the meadow folk's careful shepherds settled questions on the
long valley road. To study how use-fixtures wraps ev...
    ```
- `G12-11` (form `(do "Leiningen reads project.clj at the project root" :lein)`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Albertina, letting the runtime have the last word, had been showing Ula
the way the meadow folk's careful shepherds settled questions on the
long valley road. To understand how Leiningen reads project.clj from...
    ```
- `G12-13` (form `(do "aliases compose extra paths, deps, and main opts" :alia`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    Valeria was a clever boy, and atop the hilltop cleverness had begun to look very much like trouble.

Joachim, with the calm of a long watch well kept, had been showing Valeria
the way the meadow folk's careful shepherds settled questions on the
long valley road. To understand how low compose extra c...
    ```

#### COLLECTION_LEAK

- `G12-03` (form `(into #{} (map inc) [1 2 3])`): elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had an empty unique-only basket — one that would not hold duplicates. The fleece-comb with its increment rule waited. the numbers sat ready to be poured through. The numbers needed to be...
    ```

#### FORM_LEAK

- `G12-10` (form `(= (reverse (reverse [1 2 3])) [1 2 3])`): form '(= (reverse (reverse [1 2 3])) [1 2 3])' appears in user_msg of a goal-style subject
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol taught Tom about properties: claims that should be true for all inputs. Reverse of reverse should always equal identity. Tom had only hand-tested a few cases. Carol wanted him to see that...
    ```

