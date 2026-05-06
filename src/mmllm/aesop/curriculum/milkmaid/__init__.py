"""K-12 Clojure curriculum re-cast through the Milkmaid fable.

The fable's moral dynamic — dreaming-ahead vs. grounded patience —
informs every record:

- The **milkmaid** (Margery / Lila / Clara / Nan / Bess) is the
  dreamer/guesser. She carries the milk pail to market while
  imagining all the wealth it will bring — she assumes an answer
  before submitting the form. The pail falls when she nods her head
  in daydream; the form crashes when she guesses instead of evaluating.

- The **farmer** (Godfrey / Aldric / Mabel / Rowan / Edna) is the
  patient evaluator. "Get to market first, then count the coins." The
  farmer insists on writing the form and submitting it to the REPL
  before claiming to know the value.

The central prop is the **milk pail**: the unevaluated form balanced
in mind. Daydreaming about what it might return = guessing without
eval = nodding and spilling the pail. Getting to market = evaluating
the form and reading the REPL's actual return value.

Across all ~216 subjects, the same moral plays out over different
Clojure concepts. The model sees "submit first, count coins after"
reinforced thousands of times in hundreds of surface forms.

Each grade file exports `SUBJECTS: dict[str, SubjectCurriculum]` plus
a `smoke_test()` that generates one record per subject and verifies
shape.
"""
