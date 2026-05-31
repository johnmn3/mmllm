# Subject metadata schema

Every file under `subjects/grade-N/NN-subject-name.md` follows this
shape. The schema is intentionally explicit so that a sub-agent (or
a script, or a curriculum tool) can populate / validate / regenerate
any subject deterministically.

## Frontmatter (YAML, machine-readable)

```yaml
---
id: G1-01
title: Eval as substitution
grade: 1
layer: L1                                # one of L1..L5 or "org"/"err"/"poly"/"conc"/"meta"/"interop"/"real"
subject_index: 1                         # ordinal within the grade
prereqs: []                              # list of subject ids; first lesson has []
duration_min: 30                         # estimated lesson length
mastery_score: 0.8                       # passing fraction of exercises
tags: [primitive, repl, semantics]
---
```

## Sections (markdown body)

The body uses these named sections, in this order. Sub-agents must
emit all of them (empty section if not applicable).

### `## Concept`

One paragraph. Plain English. What is the student going to know
after this subject? No code, no jargon — just the idea.

### `## Lambda-calculus intuition`

One short paragraph that maps the concept to its lambda-calculus
analogue. For atoms: "values that are themselves." For application:
"β-reduction." For naming: "α-conversion / let-binding." For
collections: not directly mappable — say so.

This section is the **load-bearing** one for the pedagogy. The whole
point of grounding the curriculum in lambda calculus is so that
students develop a substrate-agnostic intuition.

### `## Setup`

What the student needs in front of them. Almost always: "a Clojure
or basilisp REPL." Some grade-7 subjects need a file system; some
grade-11 subjects need a JVM. Be specific.

### `## Walkthrough`

3-6 small REPL transcripts. Each shows: the form typed, the value
returned, and a one-line explanation. Example:

```
;; Single integer evaluates to itself.
42
;=> 42

;; A function call: + applied to 1 and 2.
(+ 1 2)
;=> 3
```

The walkthrough teaches by demonstration. Each transcript should
introduce one new wrinkle.

### `## Common mistakes`

Bullet list. The 3-5 most common errors a learner makes. Name the
error, give a one-line example, give the fix.

```
- Forgetting the `+` in front of operands:
    (1 2)        ;=> ClassCastException — 1 isn't a function
    (+ 1 2)      ;=> 3
```

### `## Exercises`

5-10 4clojure-style exercises. Each is a Clojure map literal:

```clojure
{:id "G1-01-1"
 :prompt "What does the REPL print?"
 :form "42"
 :expected 42}

{:id "G1-01-2"
 :prompt "Evaluate the form."
 :form "(+ 1 2)"
 :expected 3}

{:id "G1-01-3"
 :prompt "Predict the value."
 :form "(+ 1 (* 2 3))"
 :expected 7}
```

For exercises that don't have a single expected value (e.g.
"write code that does X"), use a `:test` key with a predicate:

```clojure
{:id "G3-07-5"
 :prompt "Define a function `dbl` that doubles its argument."
 :test    "(and (= 4 (dbl 2)) (= 0 (dbl 0)) (= -10 (dbl -5)))"}
```

### `## Lesson plan`

A 30-minute schedule with 5-min granularity:

```
0-5:   Hook — show one weird REPL transcript and ask why
5-15:  Walkthrough — instructor types each transcript, students
       predict the value before the return
15-25: Exercises — students work the first 5 in pairs
25-30: Recap — the one sentence to remember from this subject
```

### `## Mastery criteria`

Bullet list of observable behaviors. The student has mastered the
subject if they can:
- Recall and recognize the concept's name
- Predict the value of a never-seen example correctly
- Explain the concept in their own words to a peer
- Apply the concept in a new context (transfer)

For 4clojure-style automated grading: a student passes if they
correctly answer ≥ `mastery_score` fraction of the exercises (and
their answers must be syntactically valid Clojure that evaluates
to the expected value).

### `## Connections`

Bullet list. Where this subject leads (forward references) and what
it builds on (backward references):

- **Builds on**: G1-00 — the REPL exists at all
- **Leads to**: G1-13 (first arithmetic call), G2-22 (compose pure
  arithmetic)

This section is auto-derivable from the dependency graph but writing
it explicitly helps the human teacher tell the story.

## Validation

A subject file is valid if:
- All frontmatter fields present and well-typed.
- All section headers present (in order).
- `prereqs` references existing subject ids of LOWER `(grade,
  subject_index)`.
- All exercises have either `:expected` or `:test`.
- Every form in walkthrough/exercises parses as Clojure.
- The exercise count is between 5 and 10.

A small lint script (`scripts/lint-subjects.py`) checks all of these
when the curriculum is built.
