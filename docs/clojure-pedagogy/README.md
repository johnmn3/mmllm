# Clojure pedagogy — K-12 framework

A graded, dependency-ordered curriculum for learning Clojure from
absolute zero through advanced practice, modeled on the structure
of grade-school education and designed to be exercisable in a
4clojure-style REPL setting (write a form, evaluate, score against
expected output).

## Layers

Clojure rests on **5 foundational layers**, each depending on the ones
below it. Mastery of these 5 layers is the work of *elementary*
school (grades 1-5). Everything in middle and high school is built
on top.

```
              ┌─────────────────────────────────────┐
              │ L5 — control + higher-order         │
              │   (if, fn, recur, map/filter/reduce)│
              └──────┬──────────────────────────────┘
                     │ depends on naming + collections
              ┌──────┴───────────┐
              │ L4 — collections │
              │  (vec/list/map/set, get, conj, ...)│
              └──────┬───────────┘
                     │ depends on naming for clarity
              ┌──────┴───────┐
              │ L3 — naming  │
              │  (def, let, scope)                 │
              └──────┬───────┘
                     │ depends on application (substitution)
              ┌──────┴────────────────┐
              │ L2 — application      │
              │  ((f x) — eval as call)            │
              └──────┬────────────────┘
                     │ depends on values to apply to
              ┌──────┴───────┐
              │ L1 — atoms   │
              │  (numbers, strings, booleans,      │
              │   keywords, nil — eval-as-itself)  │
              └──────────────┘
```

The deepest intuition is **the lambda calculus**: everything is either
a value or an application. Grade 1 introduces values; grade 2
introduces application. The rest of the curriculum is layers of
organizing these two primitives.

## Grade-level overview

| Grade | Layer focus | Theme | Subject count |
|---|---|---|---|
| 1 | L1 + L2 (intro) | "Things, and what eval does to them" | 18 |
| 2 | L1 + L2 (mastery) | "Operators and their families" | 22 |
| 3 | L3 | "Names, scope, and substitution" | 18 |
| 4 | L4 | "Collections — vector, list, map, set" | 20 |
| 5 | L5 (intro) | "Choosing and repeating" | 22 |
| 6 | organization | "Namespaces, files, and modular code" | 16 |
| 7 | side effects | "Errors, debugging, and the world outside" | 18 |
| 8 | polymorphism | "Protocols, multimethods, and abstraction" | 16 |
| 9 | state + concurrency | "When time matters: atom, ref, agent" | 18 |
| 10 | meta | "Macros, code as data, the reader" | 16 |
| 11 | interop | "Crossing into Java, JS, Python" | 14 |
| 12 | real-world | "Libraries, transducers, async, projects" | 18 |
| **total** | | | **~216** |

(Subject counts are targets; actual curriculum may flex within ±4
per grade.)

## Documents in this directory

- [`framework.md`](framework.md) — full framework specification: layer
  dependencies, grade-by-grade subject lists, prerequisite graph, and
  the 4clojure-style exercise model.
- [`subject-template.md`](subject-template.md) — the metadata schema
  every subject file follows (concept, prereqs, examples, exercises,
  lesson plan, mastery criteria).
- [`subjects/`](subjects/) — one markdown file per subject, populated
  according to subject-template.md. Files are organized by grade:
  `subjects/grade-N/NN-subject-name.md`.

## Pedagogical principles

1. **Dependency-ordered** — no subject in grade N+1 should require
   knowledge from grade N+2. Forward references are an anti-pattern.
2. **REPL-driven** — every concept demonstrable in a 4clojure-style
   "write a form, eval, see the answer" loop. No theory without a
   form to evaluate.
3. **Lambda-calculus grounded** — when explaining a concept, prefer
   "this is just substitution" or "this is just application" over
   appeals to Clojure idiom. The substrate is universal.
4. **One concept per subject** — subjects are atomic. If a topic
   needs two concepts to explain, it splits into two subjects.
5. **Mistakes-first** — every subject lists the common errors a
   learner makes. Naming the failure mode is half the cure.
6. **Exercise-saturated** — each subject has 5-10 4clojure-style
   exercises with verifiable solutions.

## Status

This framework is the curricular backbone. Subject files are populated
incrementally. The exemplar
[`subjects/grade-1/01-eval-as-substitution.md`](subjects/grade-1/01-eval-as-substitution.md)
shows the fully-articulated form a subject takes; remaining subjects
are filled out by sub-agents working in parallel.
