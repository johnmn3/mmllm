---
id: G1-01
title: Eval as substitution
grade: 1
layer: L1
subject_index: 1
prereqs: []
duration_min: 30
mastery_score: 0.8
tags: [primitive, repl, semantics, lambda-calculus]
---

## Concept

When you type something into the Clojure REPL, two things can happen:
the thing **evaluates to itself** (it's already a value, like `42`
or `"hello"`), or the REPL **substitutes** something else in its
place (because it was an instruction to compute something, like
`(+ 1 2)`). This subject teaches the difference. Everything else in
Clojure is built on this one rule: every form either is a value, or
becomes one through substitution.

## Lambda-calculus intuition

In the lambda calculus there are exactly two kinds of expressions:
**values** (variables and lambdas) and **applications** (`(f x)`).
Evaluation is the act of repeatedly applying β-reduction —
substituting argument values for parameter names — until no more
reductions are possible. What's left is a value.

Clojure's REPL does the same thing. The form `42` is already a value;
no reduction is needed. The form `(+ 1 2)` is an application; the
REPL β-reduces it (substitutes 1 and 2 into +'s body) and prints
what's left: `3`.

## Setup

A Clojure or basilisp REPL. No files, no editor — just the prompt
and the printed return values.

## Walkthrough

```clojure
;; A number is a value. It evaluates to itself.
42
;=> 42

;; Same for a string. Itself, no work to do.
"hello"
;=> "hello"

;; Booleans are values too.
true
;=> true

;; nil is a special value — it's not 0, not "", not false. It's nil.
nil
;=> nil

;; Now: a parenthesized form. The REPL sees `(+ 1 2)` and asks:
;; "what does + applied to 1 and 2 evaluate to?" The answer is 3.
(+ 1 2)
;=> 3

;; Nesting: the inner call evaluates first, then the outer.
;; (* 2 3) is 6, then (+ 1 6) is 7.
(+ 1 (* 2 3))
;=> 7
```

The whole REPL session can be summarized in one sentence: every
form you type is replaced — either by itself (already a value) or
by what it computes to.

## Common mistakes

- **Treating numbers as functions.** `(1 2)` looks like a function
  call but `1` is not a function:
  ```clojure
  (1 2)         ; ClassCastException: 1 isn't callable
  (+ 1 2)       ; 3 — + IS callable
  ```
- **Expecting `+` alone to print something.** `+` by itself evaluates
  to a function value. The REPL shows you the function, but doesn't
  apply it because no arguments were given:
  ```clojure
  +             ;=> #function[clojure.core/+]
  ```
- **Forgetting the prefix order.** Clojure puts the operator first:
  ```clojure
  (1 + 2)       ; ClassCastException
  (+ 1 2)       ; 3
  ```
- **Confusing print and return.** When you type at the REPL, the
  printed thing is the *return value*, not a side effect. Both
  `42` and `(+ 1 2)` print their value because that's what the
  REPL does — not because the form said "print me."

## Exercises

```clojure
{:id "G1-01-1"
 :prompt "What does the REPL print for this form?"
 :form "42"
 :expected 42}

{:id "G1-01-2"
 :prompt "What does the REPL print for this form?"
 :form "\"hello\""
 :expected "hello"}

{:id "G1-01-3"
 :prompt "What does the REPL print for this form?"
 :form "true"
 :expected true}

{:id "G1-01-4"
 :prompt "Evaluate."
 :form "(+ 1 2)"
 :expected 3}

{:id "G1-01-5"
 :prompt "Evaluate."
 :form "(* 4 5)"
 :expected 20}

{:id "G1-01-6"
 :prompt "Evaluate. Inner form first."
 :form "(+ 1 (* 2 3))"
 :expected 7}

{:id "G1-01-7"
 :prompt "Evaluate."
 :form "(- 10 (+ 2 3))"
 :expected 5}

{:id "G1-01-8"
 :prompt "Evaluate. Order matters."
 :form "(- 10 3 2)"
 :expected 5}

{:id "G1-01-9"
 :prompt "Predict before evaluating."
 :form "(+ (+ 1 1) (+ 2 2))"
 :expected 6}

{:id "G1-01-10"
 :prompt "What does this form evaluate to?"
 :form "nil"
 :expected nil}
```

## Lesson plan

```
0-5:   Hook
       Type three things at a REPL — `42`, `"hello"`, `(+ 1 2)` —
       and ask the class: are these all the same kind of thing?
       What did the REPL just do for each one?

5-15:  Walkthrough
       Live-type each transcript above. Before each return value,
       ask the class to predict. Reveal the value. Discuss any
       wrong predictions.

15-25: Exercises
       Pair up. Work problems 1-7 in pairs at the REPL.
       Instructor circulates, especially watching for:
       - Anyone trying (1 + 2) (operator-position confusion)
       - Anyone surprised that `+` alone returns a function

25-30: Recap
       One sentence to remember:
       "A form evaluates to itself, or to what it computes."
       Note the two cases on the board. Tell them every other
       Clojure subject in elementary school is just elaborating
       on what 'computes' means.
```

## Mastery criteria

A student has mastered this subject if they can:
- Look at a form like `42` or `"hi"` and say "that's a value, it
  evaluates to itself."
- Look at a form like `(+ 1 2)` and say "that's a function call;
  the REPL replaces it with the return value."
- Predict the printed value of a never-seen nested form like
  `(- 10 (+ 2 3))` correctly.
- Explain the difference between a value and an application in
  their own words.

For automated grading: ≥ 8 of the 10 exercises evaluated correctly.

## Connections

- **Builds on**: nothing — this is the first subject.
- **Leads to**:
  - G1-02 (numbers as values)
  - G1-04 (strings as values)
  - G1-13 (first arithmetic call — extending to multiple arguments)
  - G1-14 (nested call evaluation — formalizing the inner-first rule)
- **Lambda-calculus parallel**: this subject IS lambda-calculus
  evaluation, just with Clojure syntax. Students who later see
  "λx.x+1 applied to 3 reduces to 4" will recognize it as the
  same idea.
