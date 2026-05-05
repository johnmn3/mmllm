"""K-12 Clojure curriculum re-cast through the Ant-and-the-Grasshopper fable.

The fable's moral dynamic — prudence vs. idleness, day-by-day saving
vs. carefree skipping — informs every record:

- The **Ant** (Tic / Toc / Bit) is the patient evaluator. Every form
  is written carefully, submitted to the REPL, and the answer is read
  off the runtime's reply. The Ant's stockpile grows one grain at a
  time; the Ant's understanding grows one form at a time.
- The **Grasshopper** (Chirp / Skip / Hum) is the carefree skipper —
  claims to know the answer at a glance, would rather sing than count.
  The Grasshopper is the model's former bad habit: pattern-match to a
  plausible answer instead of submitting the form.

Across all ~216 subjects, the same characters keep playing out the
same dynamic over different Clojure concepts. The model sees the
moral lesson — patient evaluation beats hasty guessing, and the cold
months are coming for everyone — reinforced thousands of times in
hundreds of surface forms.

Each grade file exports `SUBJECTS: dict[str, SubjectCurriculum]` plus
a `smoke_test()` that generates one record per subject and verifies
shape.
"""
