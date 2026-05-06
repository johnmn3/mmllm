"""Grade 10 — macros, code as data. Through fox-grapes.

Subplot lens: each macro is a cluster of fruit hanging just out of
plain sight — what the form looks like is not what the form does.
The patient fox examines every expansion carefully, the way a careful
forager inspects each grape before reaching. The hasty fox declares
the expansion not worth reading and guesses what the macro returns.
The fable's pull — rationalizing the unattainable — fits naturally:
macros reward patient inspection of the macroexpander over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _CHALKMARK_SUBPLOTS, _RECIPE_SUBPLOTS, _REWRITERULE_SUBPLOTS, _SCRIBE_SUBPLOTS


# ─────────────────────── grade-10 subplot extensions ───────────────────────
#
# The patient fox has been quietly studying a small notebook of macros
# pinned to an orchard fence. The hasty fox keeps wanting to skip past
# the expansion step and just guess what the macro returns. Each
# template lets the form carry the technical detail while the fable
# carries the manner — patience versus rationalization.

_MACRO_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{patient_fox_phrase} had spent the morning {place} sketching a tiny
language of {patient_fox_his_her} own — a notebook of macros that
wrote other forms. The next entry was {concept_phrase}, and the form
{form_display} was what {patient_fox} wanted {hasty_fox_phrase} to
submit so the REPL could show what code it produced or what value it
returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {patient_fox}
explained {place}, {emo_patient}. {hasty_fox}, {emo_proud}, said
{hasty_fox_he_she} could already see what {concept_phrase} meant.
{patient_fox_phrase} insisted they actually evaluate {form_display}
and read what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The fence {place} was lined with old macro definitions someone had
chalked into the wood. {hasty_fox_phrase} found one shaped like
{concept_phrase} and dared {patient_fox_phrase} to predict its
expansion. {patient_fox} only smiled and asked {hasty_fox_him_her} to
write {form_display} into the REPL — that, after all, was the whole
point of having a macroexpander."""),

    SubplotTemplate("""\
{hasty_fox_phrase} insisted {place} that macros were the same as
functions. {patient_fox_phrase}, {emo_patient}, drew the form
{form_display} on a wooden board. "The difference," {patient_fox_he_she}
said, "is in {concept_phrase}. Submit the form and let the runtime
tell us exactly what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where {patient_fox} had been
studying syntax-quote. The page showed {concept_phrase}, with the
form {form_display} circled in pencil. {hasty_fox_phrase}, {emo_tired}
of the lecture, agreed to write the form to settle once and for all
what it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {patient_fox_phrase} was teaching
{hasty_fox_phrase} the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was {concept_phrase}. The
form {form_display} had to be submitted; nothing else would do."""),
]


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


_PLAN_G10 = _PLAN_POOL + (
    "I write the form and let the macroexpander or REPL show the result.",
    "I expand the macro with macroexpand and read the produced form.",
    "I submit the syntax-quoted or quoted form to the REPL.",
    "I write the macro form and let the runtime evaluate or expand it.",
)


# ─────────────────────── 16 grade-10 subjects ───────────────────────


# G10-01 — quote / unquote / unquote-splice
G10_01 = SubjectCurriculum(
    grade=10, subject_id="G10-01",
    subject_title="quote, unquote, unquote-splice",
    fable="fox-grapes",
    examples=[
        _ex("(quote (+ 1 2))",
            ["+", 1, 2],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had chalked a tag onto a vine-post — the name, not the cluster behind it.',
            need="Sly wanted to ask the form a question about the tag's nature, not about what the tag named.",
            mapping='`quote` sets a token aside as a name, not a value to evaluate. Symbol predicates ask of any token: is this one of those name-tokens?',
            resolution='the form returned the verdict the predicate had asked of the tag — name or value, drawn cleanly.',
            tags=("story",)),
        _ex("'(1 2 3)", [1, 2, 3], 'a quoted list of three values', 'the value the form evaluates to',
            goal='evaluate a quoted list',
            scenario='Renard the fox had scratched three chalk-marks onto a wooden post — the names themselves, not the clusters behind them.',
            need='Renard wanted to see what the quoted sequence gave him — a list of names, not values.',
            mapping='`quote` preserves a form as a symbol-sequence. The three chalk-marks are now a three-element list of symbols, untouched by evaluation.',
            resolution='the REPL returned the three quoted marks as a list, sealed in their order, ready to read but not yet to compute.',
            tags=("story",)),
        _ex("(let [x 5] `(a ~x b))", ["a", 5, "b"], 'a syntax-quoted template with an unquoted value spliced in', 'the value the form evaluates to',
            goal='evaluate a syntax-quoted list with one value spliced in at the middle position',
            scenario='Vix the fox was drafting a tiny language. She had pinned a card to the fence: a shape with one blank. The blank was meant to hold a named bucket.',
            need='Vix wanted to see the card after filling in the blank with the value in her bucket — the shape complete, the blank replaced.',
            mapping='Syntax-quote with unquote splices a value into a template. The `a` and `b` stay as chalk-marks; the `~x` becomes the value 5 that Vix had tucked away.',
            resolution='the card showed its full shape: three elements, the middle one the spliced-in number, the edges still marked as names.',
            tags=("story",)),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-02 — syntax-quote
G10_02 = SubjectCurriculum(
    grade=10, subject_id="G10-02",
    subject_title="syntax-quote",
    fable="fox-grapes",
    examples=[
        _ex("(let [x 10] `(+ ~x ~x))",
            ["+", 10, 10],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had chalked a tag onto a vine-post — the name, not the cluster behind it.',
            need="Sly wanted to ask the form a question about the tag's nature, not about what the tag named.",
            mapping='`quote` sets a token aside as a name, not a value to evaluate. Symbol predicates ask of any token: is this one of those name-tokens?',
            resolution='the form returned the verdict the predicate had asked of the tag — name or value, drawn cleanly.',
            tags=("story",)),
        _ex("(let [xs [1 2 3]] `(list ~@xs))", ["list", 1, 2, 3], 'a syntax-quoted form with a sequence spliced in', 'the value the form evaluates to',
            goal='evaluate a syntax-quoted list with unquote-splice spreading three values into the template',
            scenario='Sly the fox had discovered a pattern: one card says "list" at the top, and below it slots for ingredients. She had gathered three berries in a basket.',
            need='Sly wanted to unpack the berries from the basket directly into the card, giving the card four elements — the word "list" plus each berry in turn.',
            mapping='Unquote-splice opens the basket and spreads its contents into the template. The `list` stays a name; the `~@xs` spreads the three numbers into positions.',
            resolution='the card came back with four elements: the name "list" and then the three berries, no basket wrapper, all in a flat row.',
            tags=("story",)),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-03 — defmacro introduction
G10_03 = SubjectCurriculum(
    grade=10, subject_id="G10-03",
    subject_title="defmacro introduction",
    fable="fox-grapes",
    examples=[
        _ex("(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
            "(my-when true 1 2 3))",
            3,
            'the value the rewritten guarded-block returns from its last step',
            "the value of the last step in the macro's expanded guarded block",
            goal='define a macro that wraps body in a guarded do-block, and call it with three steps',
            scenario="Vix the fox kept a rewriting-quill at the orchard's posting wall. Whenever a shorthand tasting-card came in, she rewrote it into a longer card before any fox followed it — the new card had explicit checks and an in-order block the runtime would actually run.",
            need='She wanted the shorthand card to expand into a guarded block: the test up front, then all the body steps in order. Once expanded, the rewritten card would behave as if she had written the long form by hand.',
            mapping="A macro is a quill that rewrites the card before reading. `defmacro` registers the rewriting rule; the syntax-quote and unquote-splice splice the body into the new card's block. The expansion happens before runtime; only the rewritten form runs.",
            resolution="the rewritten card ran in order; the body's last step's value was what came back, just as if she had written the long form herself.",
            tags=("story",)),
        _ex("(do (defmacro twice [x] `(do ~x ~x)) (twice 7))", 7, 'a macro that repeats its argument twice, called with the number 7', 'the value the form evaluates to',
            goal='define a macro that repeats its unevaluated argument twice in a do-block, then call it',
            scenario='Vix the fox kept her rewriting-quill at the fence post. A forager wanted a shorthand: "twice 7" to mean "do 7 twice". The quill would rewrite the shorthand into the long form.',
            need='Vix defined the rewriting rule: when she saw the shorthand "twice [x]", the quill would expand it to "(do x x)" — the argument copied in both slots.',
            mapping='A macro is a rewriting rule. `defmacro twice` registers how to expand the shorthand. When `(twice 7)` arrives, the quill rewrites it to `(do 7 7)` before the REPL sees it.',
            resolution='the rewritten form ran: it evaluated 7, then evaluated 7 again, returning the last value — which was still 7, since each eval of the number gives itself back.',
            tags=("story",)),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-04 — Macro expansion rule
G10_04 = SubjectCurriculum(
    grade=10, subject_id="G10-04",
    subject_title="Macro expansion rule",
    fable="fox-grapes",
    examples=[
        _ex("(macroexpand-1 '(when true 1))", ["if", True, ["do", 1]], 'the macro form (when true 1) one level of expansion', 'the value the form evaluates to',
            goal='expand the shorthand (when true 1) one step to see what the quill produced',
            scenario='Renard the fox held up a worn notebook. On one page, a shorthand scrawl: "when true 1". On the next, its expansion written in full.',
            need='Renard wanted to see just one rewriting step — what the quill turned the shorthand into before passing it on.',
            mapping='`macroexpand-1` asks the quill to show just one layer of its rewriting. The shorthand "when" becomes an "if" with a "do" block inside.',
            resolution='the page showed the one-step expansion: the guard at the front (true), then the block inside — the form the quill had rewritten.',
            tags=("story",)),
        _ex("(macroexpand-1 '(or a b))", ["let*", ["or__1__auto__", "a"],
             ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]], 'the macro form (or a b) one level of expansion', 'the value the form evaluates to',
            goal='expand the shorthand (or a b) one step to see the quill\'s first rewrite',
            scenario='Vix the fox examined the quill\'s notebook entry for the shorthand "or". The first expansion showed a temporary binding and a guarded step.',
            need='Vix wanted to read just the first rewriting — how the quill introduced a fresh name to cache the test.',
            mapping='The "or" shorthand gets rewritten to a "let*" that binds a fresh symbol, then checks its value. The fresh name avoids double-evaluation.',
            resolution='the expansion revealed the quill\'s strategy: cache the first test in a temporary name, then guard the second step on that cached result.',
            tags=("story",)),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-05 — macroexpand
G10_05 = SubjectCurriculum(
    grade=10, subject_id="G10-05",
    subject_title="macroexpand",
    fable="fox-grapes",
    examples=[
        _ex("(macroexpand '(when true 1))", ["if", True, ["do", 1]], 'the macro form (when true 1) fully expanded', 'the value the form evaluates to',
            goal='fully expand the shorthand (when true 1) until no more macro calls remain',
            scenario='Sly the fox had tacked a long scroll to the fence post showing the full expansion of "when" — all the way through, nested and complete.',
            need='Sly wanted to trace the quill\'s complete rewriting, following every macro call until nothing remained to expand.',
            mapping='`macroexpand` asks the quill to keep rewriting until the form stops changing — all layers at once. The final form has no remaining shorthand calls.',
            resolution='the scroll showed the ultimate shape: the guard test, then the do-block with its statement — no more "when" left, only the bones the REPL would read.',
            tags=("story",)),
        _ex("(macroexpand '(-> 1 inc inc))", ["inc", ["inc", 1]], 'the threading macro (-> 1 inc inc) fully expanded', 'the value the form evaluates to',
            goal='fully expand the threading shorthand (-> 1 inc inc) through all its layers',
            scenario='Renard the fox followed the quill\'s work as it unwound the shorthand step by step. The first inc would wrap the number; the second would wrap that result.',
            need='Renard wanted to see the complete unwinding — how the threading had layered each step inside the one before.',
            mapping='Threading is a quill that nests function calls left-to-right. `-> 1 inc inc` becomes `(inc (inc 1))` — each step wraps the result of the one before.',
            resolution='the full expansion showed the nesting: the innermost call with 1, then that result fed to the next inc — the readable form of what threading had done.',
            tags=("story",)),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-06 — when / unless macros
G10_06 = SubjectCurriculum(
    grade=10, subject_id="G10-06",
    subject_title="when and when-not as macros",
    fable="fox-grapes",
    examples=[
        _ex("(when true 1 2 3)", 3, 'the guarded block (when true 1 2 3) with three steps', 'the value the form evaluates to',
            goal='evaluate a guarded block that runs three steps only if the guard is true',
            scenario='Vix the fox had written a rule on a card: "if the test holds, run the steps in order, return the last." The test was true; the steps were three.',
            need='Vix wanted to see the block run through its three steps, each in turn, and return what the last step produced.',
            mapping='`when` is a guarded do-block. The test comes first; if it passes, the body runs in order. The value of the last step is what the whole block returns.',
            resolution='the guard held, the steps ran: 1, then 2, then 3. The block returned what the last step gave — the final value, which was 3.',
            tags=("story",)),
        _ex("(when false 1 2 3)", None, 'the guarded block (when false 1 2 3) with a guard that does not hold', 'the value the form evaluates to',
            goal='evaluate a guarded block when the guard is false and none of the steps run',
            scenario='Sly the fox read the same card, but with the test set to false. The three steps were ready, but the guard said no.',
            need='Sly wanted to see what happens when the guard blocks the way — whether the block would return nothing or something else.',
            mapping='When the guard is false, `when` skips the body entirely. No steps run; the whole block returns nil.',
            resolution='the guard failed; the steps never ran. The block returned nil — the absence of a result, since the body was never entered.',
            tags=("story",)),
        _ex("(when-not false :ok)", ":ok", 'the guarded block (when-not false :ok) with a negated guard that holds', 'the value the form evaluates to',
            goal='evaluate a guarded block using when-not, which runs only if the guard is false',
            scenario='Renard the fox held up a variation: "when-not" — the guard inverted. The test was false; the step was a keyword.',
            need='Renard wanted to see the block run, since the inverted guard meant the condition was met.',
            mapping='`when-not` is when with the guard logic flipped. If the test is false, the body runs. The value of the last step is what returns.',
            resolution='the inverted guard held (the test was false), so the single step ran and returned the keyword — the result the block produced.',
            tags=("story",)),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-07 — Threading macros revisited
G10_07 = SubjectCurriculum(
    grade=10, subject_id="G10-07",
    subject_title="Threading macros revisited",
    fable="fox-grapes",
    examples=[
        _ex("(-> 5 inc inc inc)", 8, 'threading a value through three increment steps with ->', 'the value the form evaluates to',
            goal='thread a starting value through three steps, each incrementing by one',
            scenario='Vix the fox placed a tasting-card on the fence: five berries at the start, then three steps that each added one more.',
            need='Vix wanted to see the berries pass through all three steps, counted up at each stage, and read the final total.',
            mapping='The `->` threading macro feeds a value left-to-right into function calls. The 5 enters the first inc, giving 6; that result enters the next inc, giving 7; that enters the last, giving 8.',
            resolution='the berries counted up through the three steps: 5 to 6 to 7 to 8. The final tasting returned 8, the value after all three increments.',
            tags=("story",)),
        _ex("(->> [1 2 3 4] (filter even?) (map inc) (reduce +))", 8, 'threading a vector through filter, map, and reduce steps with ->>', 'the value the form evaluates to',
            goal='thread a vector through filtering for evens, incrementing each, and summing all',
            scenario='Sly the fox had a basket with four berries: 1, 2, 3, 4. She wanted to pick out the even ones, increase each by one, and add them up.',
            need='Sly needed the pipeline: filter to keep only even berries, map to increase each, reduce to sum the result.',
            mapping='The `->>` threading macro feeds a value right-to-right into the last position of each call. The basket filters to [2, 4], maps to [3, 5], then reduces to 8.',
            resolution='the pipeline ran: [1,2,3,4] filtered to the evens [2,4], incremented to [3,5], then summed to 8 — the final count.',
            tags=("story",)),
        _ex("(macroexpand '(-> x f g))", ["g", ["f", "x"]], 'the threading shorthand (-> x f g) expanded to see the nesting', 'the value the form evaluates to',
            goal='expand the threading shorthand to see how the macro nests the function calls',
            scenario='Renard the fox read the quill\'s expansion of the shorthand "->". The notebook showed how the first function wrapped the value, then the second wrapped that.',
            need='Renard wanted to trace the nesting: which function call was inside, which was outside.',
            mapping='Threading is a macro that rewrites calls left-to-right as nested calls. `(-> x f g)` becomes `(g (f x))` — the value enters f, then that result enters g.',
            resolution='the expansion showed the bones: g wrapping f wrapping x — the nested form that threading had created for the REPL to evaluate.',
            tags=("story",)),
    ],
    subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-08 — macro vs fn
G10_08 = SubjectCurriculum(
    grade=10, subject_id="G10-08",
    subject_title="Macro vs fn",
    fable="fox-grapes",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        _ex("(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))", 7, 'the form', 'the value the form evaluates to'),
        _ex("(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))", 7, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-09 — hygiene and gensym
G10_09 = SubjectCurriculum(
    grade=10, subject_id="G10-09",
    subject_title="Hygiene and gensym",
    fable="fox-grapes",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        _ex("(symbol? (gensym))", True, 'the form', 'the value the form evaluates to'),
        _ex("(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))", False, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-10 — anaphoric macros are a bad idea
G10_10 = SubjectCurriculum(
    grade=10, subject_id="G10-10",
    subject_title="Anaphoric macros are confusing",
    fable="fox-grapes",
    examples=[
        # An anaphoric `aif` would inject `it` un-hygienically. We illustrate
        # the safer hygienic alternative: an explicit name.
        _ex("(do (defmacro safe-if-let [bind then else] "
            "`(if-let ~bind ~then ~else)) "
            "(safe-if-let [x 5] (* x 2) 0))", 10, 'the form', 'the value the form evaluates to'),
        _ex("(if-let [x 7] (* x x) 0)", 49, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-11 — Reader macros overview
G10_11 = SubjectCurriculum(
    grade=10, subject_id="G10-11",
    subject_title="Reader macros overview",
    fable="fox-grapes",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        _ex("'(1 2 3)", [1, 2, 3], 'the form', 'the value the form evaluates to'),
        _ex("(#(* % %) 6)", 36, 'the form', 'the value the form evaluates to'),
        _ex("[1 #_ 2 3]", [1, 3], 'the form', 'the value the form evaluates to'),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-12 — Tagged literals
G10_12 = SubjectCurriculum(
    grade=10, subject_id="G10-12",
    subject_title="Tagged literals",
    fable="fox-grapes",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        _ex("(inst? #inst \"2024-01-01\")", True, 'the form', 'the value the form evaluates to'),
        _ex("(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")", True, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-13 — Data readers (EDN extension)
G10_13 = SubjectCurriculum(
    grade=10, subject_id="G10-13",
    subject_title="Data readers and EDN extension",
    fable="fox-grapes",
    examples=[
        # EDN read-string with a default tag handler.
        _ex("(clojure.edn/read-string \"42\")", 42, 'the form', 'the value the form evaluates to'),
        _ex("(clojure.edn/read-string \"[:a :b :c]\")", [":a", ":b", ":c"], 'the form', 'the value the form evaluates to'),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-14 — eval
G10_14 = SubjectCurriculum(
    grade=10, subject_id="G10-14",
    subject_title="eval (the function)",
    fable="fox-grapes",
    examples=[
        _ex("(eval '(+ 1 2 3))", 6, 'the form', 'the value the form evaluates to'),
        _ex("(eval (list '+ 4 5))", 9, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-15 — When NOT to write a macro
G10_15 = SubjectCurriculum(
    grade=10, subject_id="G10-15",
    subject_title="When not to write a macro",
    fable="fox-grapes",
    examples=[
        # Most of the time, a function suffices. Test forms that show
        # a function would do.
        _ex("(do \"a function suffices when no syntax shaping is needed\" "
            "((fn [x y] (+ x y)) 3 4))", 7, 'the form', 'the value the form evaluates to'),
        _ex("(do \"prefer fn unless you must shape syntax\" "
            "(map inc [1 2 3]))", [2, 3, 4], 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-16 — Macro pattern library (with-X, def-X-thing)
G10_16 = SubjectCurriculum(
    grade=10, subject_id="G10-16",
    subject_title="Macro pattern library",
    fable="fox-grapes",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        _ex("(do (defmacro with-tortoise-pace [& body] "
            "`(let [pace# :slow-and-steady] ~@body)) "
            "(with-tortoise-pace 42))", 42, 'the form', 'the value the form evaluates to'),
        # A `def-X-thing` style: macro that defs a named thing.
        _ex("(do (defmacro def-pace [name v] `(def ~name ~v)) "
            "(def-pace race-pace :slow) race-pace)", ":slow", 'the form', 'the value the form evaluates to'),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G10_01, G10_02, G10_03, G10_04, G10_05, G10_06, G10_07, G10_08,
    G10_09, G10_10, G10_11, G10_12, G10_13, G10_14, G10_15, G10_16,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        assert recs, f"no records for {sid}"
        for r in recs:
            assert r.tool_calls, f"no tool_calls for {sid}"
            assert r.tool_calls[0]["name"] == "eval"
            assert r.user_msg
            assert r.assistant_msg
    print(f"grade-10 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
