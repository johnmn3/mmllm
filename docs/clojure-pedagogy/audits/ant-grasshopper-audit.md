# ant-grasshopper curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 4 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(* 4 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 1/2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2 1/2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"grain"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`""` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(= 1 1)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= 1 2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? false)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= nil nil)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:ant` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(= :ant :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'STRING_AS_CHAR_MISCLAIM': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 2}
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\space` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\G` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\G` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FOREIGN_FABLE_IMAGERY': 3}
    - [LOW_GROUNDING] form=`(symbol? 'ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(symbol? 42)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= 'ant 'ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(= 'ant 'ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= 'ant 'ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2) ; sum of one and two` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`42 ;; the answer` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+
  1
  2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'ANSWER_LEAK': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'ANSWER_LEAK': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 5 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 5 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [ANSWER_LEAK] form=`(- 20 7)` — answer 13 in narrative
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 20 7)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 20 7)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= :ant :ant)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2 3 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 1 2 3 4 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'LOW_GROUNDING': 2, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(<= 1 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(<= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(<= 1 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(> 5 4 3 2 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(>= 3 3 2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(>= 3 3 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-03: not= and = with multiple args

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(not= 1 1)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-04: min and max

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(min 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(min 5 -2 0 9)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-05: quot, rem, mod

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quot 17 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(rem 17 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(mod -1 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-06: inc and dec

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 5}
    - [LOW_GROUNDING] form=`(inc 4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(dec 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(dec 4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(inc -1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(inc -1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(dec 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-07: abs (absolute value)

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'LOW_GROUNDING': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(Math/abs -7)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(Math/abs 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(Math/abs 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(Math/abs 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(Math/abs 9)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(Math/abs 9)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2/3 3/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(* 2/3 3/4)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2/3 3/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 1 1/3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-09: Floats vs ints

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(/ 10 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-10: Power by repeated multiplication

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 3 3 3 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(* 3 3 3 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 5 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 6, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(str "a" "b")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(str "a" "b")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(str "ant-" 42)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(str "ant-" 42)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(str)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(str)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-12: print and println

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(with-out-str (println "x"))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(with-out-str (println "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-13: and / or — short-circuit and value

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(and 1 nil 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(or nil false :found)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(or nil false :found)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-14: not — turning truthy to false

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'LOW_GROUNDING': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-15: Falsey values

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(boolean false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-16: Coercion pitfalls in if

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if 0 :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if 0 :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if nil :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-17: Keyword as function

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'FOREIGN_FABLE_IMAGERY': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:a {:a 1 :b 2})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:a {:a 1} :default)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:a {:a 1} :default)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(:missing {:a 1} :default)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:missing {:a 1} :default)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(:missing {:a 1} :default)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-18: Symbols evaluate to their bindings

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def winter :coming) winter)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-19: Quoting introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`'ant` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-21: rand and rand-int

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [r (rand-int 10)] (and (>= r 0) (< r 10)))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def x 42) x)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def x 1) (def x 99) x)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [n 10] (* n n))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(let [n 10] (* n n))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 5] a)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(let [a 5] a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 1 b 2] (+ a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 1 b 2] (+ a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 2 b 3 c 4] (+ a b c))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'ANSWER_LEAK': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(let [a 5 b (* a 2)] b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`((fn [a b] (* a b)) 3 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`((fn [a b c] (+ a b c)) 1 2 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(#(+ % 1) 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [a 7] (+ a a))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`[]` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`["a" "b"]` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(conj [1 2] 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(conj [] :ant)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(cons 0 '(1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(get {:a 1 :b 2} :a)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(assoc {:a 1} :b 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(dissoc {:a 1 :b 2} :a)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(count #{1 1 1})` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count #{:a :b :c})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(count "grasshopper")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? "")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count (rest [10 20 30]))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(into [] '(1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= [1 2 3] '(1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count (range 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count (range 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(first (range 1 100))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(seq [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if true :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if true :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if false :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if (> 5 3) :a :b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when false :yes)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(when false :yes)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(and 1 2 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not (> 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(map inc [1 2 3])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(filter even? [1 2 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(filter even? [1 2 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(filter pos? [-2 -1 0 1 2])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'ANSWER_LEAK': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(reduce + [1 2 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(reduce * [1 2 3 4 5])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(apply + [1 2 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(apply + [1 2 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(apply max [3 1 4 1 5])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`((comp str inc) 9)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`((partial + 10) 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`((partial + 10) 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`((juxt inc dec) 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(some even? [1 3 5 8 7])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(some neg? [1 2 3])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(every? pos? [1 2 3])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(every? pos? [1 2 3])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(take 3 [10 20 30 40 50])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(drop 2 [10 20 30 40 50])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(distinct [1 1 2 3 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(distinct [1 1 2 3 3 4])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(sort [3 1 2])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(sort [3 1 2])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'ant.stockpile)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'ant.stockpile)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(name 'meadow.ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'meadow.ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'meadow.ant 'meadow.ant)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.string/lower-case "GRASSHOPPER")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(boolean (:private (meta 'public)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(clojure.string/upper-case "a")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 'a.b 'a.b)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`(count ['meadow.ant 'meadow.grasshopper 'meadow.sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count ['meadow.ant 'meadow.grasshopper 'meadow.sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(map name ['meadow.ant 'meadow.grasshopper])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(map name ['meadow.ant 'meadow.grasshopper])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['meadow.ant 'meadow.grasshopper])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(try (try (/ 1 0) (finally :ran)) (catch Exception` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(with-out-str (prn :grasshopper))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(defn speak [k] (cond (= k :grasshopper) "swift" (` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defprotocol Pace (speed [this])) (defrecord A` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defmulti pace :species) (defmethod pace :gras` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (defmulti show identity) (defmethod show :gras` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defprotocol Pace (speed [this])) (extend-type` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'PREDICATE_QUESTION_COLLISION': 1, 'LOW_GROUNDING': 2}
    - [PREDICATE_QUESTION_COLLISION] form=`(do (derive ::grasshopper ::runner) (isa? ::grassh` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 5] `(a ~x b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [x 10] `(+ ~x ~x))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 10] `(+ ~x ~x))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(let [x 10] `(+ ~x ~x))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 10] `(+ ~x ~x))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand-1 '(when true 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand-1 '(or a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand-1 '(or a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand '(when true 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(macroexpand '(-> 1 inc inc))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand '(-> 1 inc inc))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when true 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when true 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when false 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when-not false :ok)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(-> 5 inc inc inc)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(-> 5 inc inc inc)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(if-let [x 7] (* x x) 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(if-let [x 7] (* x x) 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(if-let [x 7] (* x x) 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(#(* % %) 6)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.edn/read-string "42")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval '(+ 1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval '(+ 1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(eval (list '+ 4 5))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'FOREIGN_FABLE_IMAGERY': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "a function suffices when no syntax shaping is` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(do "prefer fn unless you must shape syntax" (map ` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(.toUpperCase "abc")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(.toUpperCase "abc")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(.toUpperCase "abc")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(. "abc" toUpperCase)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(Math/abs -7)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "ant")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(:import (java.util Date)) imports a host cla` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(new String "world")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [a (int-array [10 20 30])] (aget a 1))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp is a Clojure-like Lisp implemented o` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(into #{} (map inc) [1 2 3])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipe, mult, mix, pipeline-async route values ` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "s/exercise produces sample inputs for a spec"` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "s/exercise produces sample inputs for a spec"` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= (+ 1 2) 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "(deftest …), (is …), (testing …) are the core` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn declares :deps and :aliases for the ` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "queries are written in datalog over EDN-shape` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "components are functions returning Hiccup vec` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "small public API surface, plain data inputs, ` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "kebab-case names, two-space indent, threading` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "kebab-case names, two-space indent, threading` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do "prefer pure functions, name predicates with ?` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

---

## Summary

### Issue counts (across all examples × 3 records)

- **FORM_DISPLAY_AND_FORM_NOUN**: 186
- **LOW_GROUNDING**: 76
- **FOREIGN_FABLE_IMAGERY**: 74
- **STRING_AS_CHAR_MISCLAIM**: 6
- **ANSWER_LEAK**: 6
- **PREDICATE_QUESTION_COLLISION**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 53 | — |
| 2 | 22 | 77 | 83 | — |
| 3 | 18 | 31 | 19 | — |
| 4 | 20 | 39 | 30 | — |
| 5 | 22 | 39 | 33 | — |
| 6 | 16 | 33 | 21 | — |
| 7 | 18 | 36 | 5 | — |
| 8 | 16 | 31 | 10 | — |
| 9 | 18 | 34 | 21 | — |
| 10 | 16 | 36 | 40 | — |
| 11 | 14 | 29 | 11 | — |
| 12 | 18 | 37 | 23 | — |

### Sample issues by severity

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `0`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened in the woods.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today by the woods, the next entry
was the value 2. Skip the g...
    ```
- `G1-01` (form `(* 4 5)`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the woods, the next entry
was the form (* 5 5). Hum the grasshopper peered over...
    ```
- `G1-01` (form `"hello"`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened near the garden.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today at the edge of the garden, the next entry
was the strin...
    ```
- `G1-05` (form `(= 1 1)`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    All summer long, the Ant worked while the Grasshopper sang.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today on the farm, the next entry
was the equality (= 1 1). Hum the grasshopper peered over
his shoulder at the form `(= 8 8)` and asked wha...
    ```
- `G1-05` (form `(= 1 2)`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today near the farm, the next entry
was the equality (= 4 7). Chirp the grasshopper peered over
their shoulder at the form...
    ```

#### LOW_GROUNDING

- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened in the woods.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today by the woods, the next entry
was the value 2. Skip the g...
    ```
- `G1-02` (form `7`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Hum the grasshopper blocked
Bit the ant's path in the forest and refused to step aside until someone
could prove what the form `2` evaluated to. Hum
called it impossible. Bit the ant, walk...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small audience of meadow creatures had gathered near the meadow to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the ratio 1/2 and read the form aloud:
`1/2`. The crowd wait...
    ```
- `G1-03` (form `(* 2 1/2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    All summer long, the Ant worked while the Grasshopper sang.

A small audience of meadow creatures had gathered on the hilltop to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (* 2 1/2) and read the form aloud:
`(* 0 1/2)`. The crowd waited to ...
    ```
- `G1-06` (form `(nil? false)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the woods, the next entry
was the predicate (nil? false). Skip the grasshopper peered over
his shoulder at the form ...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `(* 4 5)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path by the orchard and refused to step aside until someone
could prove what the form `(* 3 3)` evaluated to. Hum
called it impossible. Tic the a...
    ```
- `G1-03` (form `(* 2 1/2)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path at the edge of the forest and refused to step aside until someone
cou...
    ```
- `G1-04` (form `"grain"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate at the edge of the orchard: whoever
predicted the result of `"river"` first would set the next day's
ration. Bit the ant, stepping delibe...
    ```
- `G1-04` (form `""`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play.

Skip the grasshopper chalked a wager on a flat slate on the farm: whoever
predicted the result of `"marble"` first would set the next day's
ration. Toc the ant, saying very little, said it would be simpler to type
the form ...
    ```
- `G1-06` (form `(nil? nil)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    All summer long, the Ant worked while the Grasshopper sang.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the orchard: whoever
predicted the result of `(nil? nil)` first would set the next day's
ration. Tic the ant, stepping deliberately, said it would be simpler to type
the ...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Skip the grasshopper blocked
Bit the ant's path near the orchard and refused to step aside until someone
could prove what the form `"harbor"` evaluated t...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    All summer long, the Ant worked while the Grasshopper sang.

Chirp the grasshopper chalked a wager on a flat slate near the forest: whoever
predicted the result of `"pewter"` first would set the next day's
ration. Toc the ant, without complaint, said it would be simpler to type
the form into the REP...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened near the meadow.

Bit the ant and Chirp the grasshopper stopped by the meadow where someone had
written the character \space on a flat stone. Chirp, as if the race were already w...
    ```
- `G1-08` (form `\G`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Hum the grasshopper said,
boasting at every turn. "Anyone can see what the character \willow comes to."
Bit the ant, who near the meadow had grown used ...
    ```
- `G1-08` (form `\G`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk in the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `"bridge"`. Hum
laughed, boasting at every turn, and declared it too easy. Toc said patiently
that the on...
    ```

#### ANSWER_LEAK

- `G1-12` (form `(* (+ 1 2) 3)`): answer 9 in narrative
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small audience of meadow creatures had gathered at the edge of the woods to watch
Hum the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (* (+ 3 6) 9) and read the form aloud:
`(* (...
    ```
- `G1-13` (form `(- 20 7)`): answer 13 in narrative
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(- 13 6)` first would set the next day's
ration. Bit the ant, untroubled by what others...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): answer 7 in narrative
    ```
    All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

"There is no need to evaluate that," Hum the grasshopper said,
with great whoops of laughter. "Anyone can see what the nested form (+ 8 (* 1 7)) comes to."
Toc the ant, who at the farm had grown used to s...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): answer 8 in narrative
    ```
    It is the way of the Ant to gather, and the way of the Grasshopper to play. This was by the forest.

Skip the grasshopper chalked a wager on a flat slate in the forest: whoever
predicted the result of `(let [a 2 b (+ a 8) c (* b 7)] c)` first would set the next day's
ration. Bit the ant, without com...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): answer 8 in narrative
    ```
    All summer long, the Ant worked while the Grasshopper sang.

Beside a small stockpile in the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(let [a 8 b (+ a 4) c (* b 5)] c)`
first would win the right to set the next day's count.
Toc the ant, with eye...
    ```

#### PREDICATE_QUESTION_COLLISION

- `G8-15` (form `(do (derive ::grasshopper ::runner) (isa? ::grasshopper ::ru`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to deriving ::grasshopper from ::runner and asking isa...
    ```

