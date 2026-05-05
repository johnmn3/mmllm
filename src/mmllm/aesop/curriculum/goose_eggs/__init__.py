"""Goose-eggs K-12 Clojure curriculum.

Each Clojure subject from the K-12 framework, re-cast through the
Goose-Eggs fable's moral lens — greed vs. patience.

Cast:
  - {owner}   the patient eval-trusting human (tortoise-analog)
  - {visitor} the impatient guesser who wants the answer at once
              (hare-analog)
  - {goose}   the value-yielding bird whose one-egg-per-morning
              routine parallels the REPL's one-form-at-a-time
              evaluation. Greed wants ALL the eggs at once; patience
              waits, lets the runtime hand back one value, then the
              next.

Locations: farm, village, market, barn, cottage, kitchen, cellar,
orchard, meadow — the household + village settings the fable lives in.

Per the SKILL doc, each `grade_N.py` exports a SUBJECTS dict and a
smoke_test(). Shared subplots live in `grade_1.py:_SHARED_SUBPLOTS`
and are extended grade-by-grade.
"""
