"""Grade 6 — namespaces and modular code. Through boy-who-cried-wolf.

Subplot lens: trust-as-namespace. False alarms cross village boundaries
the way symbols cross namespace boundaries. Two cottages on opposite
sides of the village; each shepherd keeps their own copybook of forms.
The reeve / elder enforces what's exported between village namespaces —
only forms actually submitted to the REPL count as trustworthy across
the boundary.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _GOAL_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── grade-6 subplot extensions ───────────────────────
#
# Namespaces map naturally onto "trust boundaries" in the boy-wolf moral
# lens. A claim shouted from one side of the watchhouse (one namespace) only
# carries to the other side if it's been honestly submitted to the REPL —
# the elder enforces what gets exported.

_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two cottages on opposite sides of the watchhouse — each shepherd keeps
    # a separate copybook of forms. The named shepherd's claim doesn't
    # cross to the elder's side without honest evaluation.
    SubplotTemplate("""\
The two cottages stood on opposite sides of the townsfolk {place}, and
each kept its own copybook of forms. {shepherd_phrase} scribbled into
one book; {elder_phrase} kept the other. To settle a question that
morning, {elder} pointed to {concept_phrase} and asked
{shepherd_him_her} to write the form {form_display} into the REPL so
the answer would carry honestly across both copybooks."""),

    # The reeve as namespace gatekeeper — decides which forms get
    # exported between the village namespaces.
    SubplotTemplate("""\
The reeve of the meadow folk kept a small list {place} of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned {concept_phrase}. {elder_phrase},
{emo_patient}, asked {shepherd_phrase} to submit the form
{form_display} so the runtime's answer could be carried, on the reeve's
authority, to the other side of the townsfolk."""),

    # Cross-namespace fully-qualified beat — when the shepherd's
    # claim from one cottage has to be referred to from the other.
    #
    # NOTE (boy-wolf polish, hand-audit pass): the closing "X was,
    # after all, the line in question" had a singular verb that
    # broke when {concept_phrase} was a plural NP (e.g., "two
    # identical namespace symbols"). Rewritten with a number-agnostic
    # frame: "the question on that line came down to {concept_phrase}".
    SubplotTemplate("""\
{shepherd_phrase} had shouted a claim from one side of the valley
{place}. {elder_phrase} insisted that, before the answer could be
relied on by anyone in the other cottage, the form {form_display} would
need to be evaluated under its proper name. {shepherd}, {emo_tired},
agreed; the question on that line came down to {concept_phrase}."""),
]


def _ex(form, expected, concept, what, goal=None,
        scenario="", need="", mapping="", resolution="",
        tags=()):
    canon = GOALS.get(form, {})
    if all([scenario, need, mapping, resolution]) and "story" not in tags:
        tags = tuple(tags) + ("story",)
    return SubjectExample(
        form=form, expected=expected,
        concept_phrase=canon.get("concept", concept),
        question_what=canon.get("what", what),
        goal_text=goal if goal is not None else get_goal(form, concept, what),
        scenario=scenario, need=need, mapping=mapping, resolution=resolution,
        tags=tags,
    )
_PLAN_G6 = _PLAN_POOL + (
    "I require the namespace and call the function.",
    "I use the fully-qualified name to reach the var.",
    "I keep the namespaces straight and let the REPL resolve the name.",
)


# ─────────────────────── 16 grade-6 subjects ───────────────────────


# G6-01 — Namespace as file
# A namespace's name is itself a symbol; we use `(name 'foo.bar)` to
# show the path-like string the namespace corresponds to.
G6_01 = SubjectCurriculum(grade=6, subject_id="G6-01",
    subject_title="Namespace as file", fable="boy-wolf",
    examples=[
        _ex("(name 'foo.bar)", "foo.bar",
            "the symbol foo.bar standing in for a namespace name",
            "the string form of the namespace symbol foo.bar",
            scenario=(
                "Tom stood at the village notice-post, where scrolls hung "
                "labeled with dotted names. Carol showed him the scroll "
                "marked `foo.bar`—a namespace written as a symbol."
            ),
            need=(
                "Tom wanted to know what the dotted name would look like "
                "as a plain string that could be written in the ledger."
            ),
            mapping=(
                "`name` reads the symbol aloud and writes it as a string. "
                "`foo.bar` becomes \"foo.bar\" when read to the REPL."
            ),
            resolution=(
                'Carol wrote it. The symbol `foo.bar` spoke itself back as the string "foo.bar," and Tom understood: a namespace is a path written in symbols.'
            )),
        _ex("(name 'clojure.string)", "clojure.string",
            "the namespace symbol clojure.string",
            "the string \"clojure.string\"",
            scenario=(
                "Carol pointed to a namespace symbol posted at the watchhouse notice-post."
            ),
            need=(
                "Tom wanted to convert the symbol to a plain string for the ledger."
            ),
            mapping=(
                "`name` converts a symbol to a string representation."
            ),
            resolution=(
                'The form returned the symbol as a string for the registry.'
            )),
        _ex("(symbol? 'village.flock)", True,
            "whether village.flock is a symbol",
            "the value of (symbol? 'village.flock)",
            scenario=(
                "The reeve asked Tom to check whether a name posted at the "
                "village crossroads—`village.flock`—was truly a symbol, a "
                "name that could be pinned to a scroll."
            ),
            need=(
                "Tom needed a test to confirm the dotted name was a symbol "
                "before the meadow folk would trust it as a namespace label."
            ),
            mapping=(
                "`symbol?` is the gatekeeper predicate. It asks whether the "
                "posted mark is a proper symbol—a borrowable, nameable thing."
            ),
            resolution=(
                'The predicate returned true, and the reeve approved the namespace label for posting at the crossroads.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="boy-wolf",
    examples=[
        _ex("(name 'village.shepherd)", "village.shepherd",
            "the namespace name 'village.shepherd as a string",
            "the string \"village.shepherd\"",
            scenario=(
                "Carol kept the townsfolk ledger, and she needed to convert "
                "the posted namespace name `village.shepherd` from its symbol "
                "form into plain text for the registry."
            ),
            need=(
                "Tom asked how the elder could turn the posted symbol into "
                "a string that the ledger could hold as words, not names."
            ),
            mapping=(
                "`name` reads the symbol aloud and writes what it hears as "
                "a string—the exact text of the namespace on the post."
            ),
            resolution=(
                'Carol wrote it and the REPL handed back the string "village.shepherd," ready for the ledger\'s pages.'
            )),
        _ex("(= 'village.shepherd 'village.shepherd)", True,
            "two identical namespace symbols",
            "whether the two namespace symbols are equal",
            scenario=(
                "Two copies of the village's notice-posts stood at opposite "
                "corners of the green, each bearing the same posted symbol "
                "`village.shepherd`. Tom wondered if they were truly the same."
            ),
            need=(
                "Before treating the two postings as a single, unified "
                "namespace across the meadow folk, Tom needed to verify they were "
                "identical."
            ),
            mapping=(
                "`=` is the equality check. Two symbols with the same name "
                "and form are equal—the same covenant posted in two places."
            ),
            resolution=(
                'The comparison returned true, and Tom understood: the namespace posted at both corners was one village covenant, honored everywhere.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"wolf\")", "WOLF",
            "the form using clojure.string/upper-case on \"wolf\"",
            "the upper-cased string \"WOLF\"",
            scenario=(
                "Carol led Tom to the valley smithy, where a master crafts "
                "strings in their furnace. On the smithy's post hung the sign "
                "`clojure.string/upper-case`—a foreign tool the smith had "
                "left for any shepherd to borrow."
            ),
            need=(
                "Tom wanted to shout the answer about what `upper-case` would "
                "do to the word \"wolf\", but Carol insisted he borrow the "
                "smith's tool and watch what it actually returned."
            ),
            mapping=(
                "The fully-qualified name `clojure.string/upper-case` reaches "
                "across the namespace boundary to the smithy's tool. Calling "
                "it with \"wolf\" borrows the smith's transformation."
            ),
            resolution=(
                'Carol wrote it into the REPL, crossed into the smithy by name, and the smith\'s tool returned "WOLF". Tom learned: the namespace slash is the boundary you must cross by name. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(clojure.string/lower-case \"WOLF\")", "wolf",
            "the form using clojure.string/lower-case",
            "the lower-cased string \"wolf\"",
            scenario=(
                "At the smithy door, another fully-qualified name waited: "
                "`clojure.string/lower-case`. Carol pointed to it and asked "
                "Tom what the opposite transformation would yield."
            ),
            need=(
                "Tom guessed carelessly, but Carol held up her hand. She "
                "would not accept a guess when the smith's tools were right "
                "there, waiting to be called by their proper names."
            ),
            mapping=(
                "The same namespace path, a different tool. `lower-case` "
                "does the opposite work—the REPL will show the truth when "
                "you call it by its full name from the smithy."
            ),
            resolution=(
                'The form returned "wolf" to the ledger, and Tom saw the pattern: a fully-qualified name unlocks the foreign tool; the REPL does the honest work. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="boy-wolf",
    examples=[
        _ex("(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))",
            True,
            "whether two calls to the same fully-qualified function agree",
            "the value of (= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))",
            scenario=(
                "Carol led Tom to the smithy twice, once in the morning and "
                "once at noon. Both times, she asked the smith to uppercase "
                "the same letter \"x\" using the posted tool. Tom wondered if "
                "the smith would give the same answer both times."
            ),
            need=(
                "Before trusting that the smithy's tools were reliable, Tom "
                "needed proof that the same call, made twice, would yield "
                "identical results."
            ),
            mapping=(
                "Equality `=` compares two applications of the same "
                "fully-qualified tool. If the smithy's work is honest, the "
                "same input should always yield the same output."
            ),
            resolution=(
                "Carol wrote it, calling the smith's tool twice with the same letter. The REPL returned true—the smith's work was consistent. Tom trusted the boundary now. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."           )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"shepherd\")", "SHEPHERD",
            "clojure.string/upper-case applied to \"shepherd\"",
            "the upper-cased string \"SHEPHERD\"",
            scenario=(
                "Tom stood before the smithy again, calling out the word "
                "\"shepherd\" and boasting that he knew what the smith's tool "
                "would do to it. Carol held up her hand and asked him to call "
                "the tool by its full name at the boundary."
            ),
            need=(
                "Tom needed to learn that a half-name wouldn't work at the "
                "boundary—only the fully-qualified name, slash and all, "
                "would reach the smithy's tool."
            ),
            mapping=(
                "`clojure.string/upper-case` is the complete postal address "
                "of the tool. The slash marks the boundary; the left side "
                "names the smithy, the right side names the particular tool."
            ),
            resolution=(
                'Carol wrote the full name, and the smithy returned "SHEPHERD" in uppercase. Tom saw: the slash was not decoration—it was the key to crossing safely. Tom chalked {drawn.a} on the valley notice, and the morning record stood for the next shepherd to read.'         )),
        _ex("(clojure.string/reverse \"flock\")", "kcolf",
            "clojure.string/reverse applied to \"flock\"",
            "the reversed string \"kcolf\"",
            scenario=(
                "At the smithy's next post, a different tool waited: "
                "`clojure.string/reverse`. Carol asked Tom to call it by "
                "its full name and see what it would do to the word \"flock\"."
            ),
            need=(
                "Tom was beginning to see the pattern: each tool in the "
                "smithy has a full name, posted clearly for anyone to call."
            ),
            mapping=(
                "The fully-qualified name is the postal address. The smithy "
                "keeps its tools in a library; the full name tells the REPL "
                "which smithy and which tool to use."
            ),
            resolution=(
                'Carol wrote it, and the REPL called the smith\'s reverse tool, returning "kcolf". Tom was learning to trust the boundary—the fully-qualified name was always reliable.'           )),
        _ex("(namespace :village/shepherd)", "village",
            "the namespace portion of the keyword :village/shepherd",
            "the string \"village\"",
            scenario=(
                "Carol showed Tom a keyword on the ledger: `:village/shepherd`. "
                "She asked him to extract just the left part—the namespace that "
                "qualified the keyword, the way a village name qualifies a "
                "citizen."
            ),
            need=(
                "Tom needed to learn how to read a qualified keyword and pull "
                "out just the namespace portion—the boundary marker."
            ),
            mapping=(
                "`namespace` reads the left side of the slash. For "
                "`:village/shepherd`, it returns the string \"village\", the "
                "postal code that qualifies the name."
            ),
            resolution=(
                'Carol wrote it, and the REPL handed back "village". Tom saw: every qualified name has two parts—the namespace that qualifies and the name that is qualified. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
        _ex("(name :village/shepherd)", "shepherd",
            "the name portion of the keyword :village/shepherd",
            "the string \"shepherd\"",
            scenario=(
                "After extracting the namespace, Carol asked Tom to extract "
                "the opposite part—the simple name that was qualified by the "
                "village covenant."
            ),
            need=(
                "Tom needed to see that a qualified name can be taken apart "
                "in both directions—namespace and name both matter."
            ),
            mapping=(
                "`name` reads the right side of the slash. For "
                "`:village/shepherd`, it returns the string \"shepherd\", the "
                "unqualified identity inside the qualified address."
            ),
            resolution=(
                'The form returned "shepherd", and Tom understood: a fully-qualified keyword is a map—one key splits into namespace and name, each readable by the right tool.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="boy-wolf",
    examples=[
        # The :private flag is queryable as metadata on the symbol.
        _ex("(:private (meta '^:private x))", True,
            "the :private flag on metadata of '^:private x",
            "whether the :private metadata is true",
            scenario=(
                "Carol kept the village ledger with margin-notes marking "
                "whether each symbol's definition was private or shared. Tom "
                "saw '^:private x and wanted to know if the margin held the "
                "private flag."
            ),
            need=(
                "Tom needed to read the marginalia without changing the entry—"
                "to confirm whether the private marker was truly there."
            ),
            mapping=(
                "`meta` opens the marginalia—the metadata map on the symbol. "
                "`:private` reads that specific note, the way the elder's "
                "fingers follow a written line."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned true. The private flag was there in the margin, exactly as Tom had seen it.'
            )),
        _ex("(:private (meta 'x))", None,
            "the :private flag on plain metadata of 'x",
            "the value of (:private (meta 'x))",
            scenario=(
                "Tom pointed to another symbol in the ledger—a plain `x` with "
                "no special margin-marks. He asked Carol to check whether this "
                "entry also carried a private flag."
            ),
            need=(
                "Tom was learning to distinguish: symbols with private markers "
                "and symbols without. He needed to confirm that the plain entry "
                "had no private tag."
            ),
            mapping=(
                "`meta` opens the marginalia for any symbol. If the private "
                "flag was never written there, the query returns nothing—nil, "
                "the absence that means \"not marked.\" "
            ),
            resolution=(
                'Carol wrote it, and the REPL returned nil. The plain symbol carried no private marker. Tom understood: metadata marks are optional; absence means publicly shared.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="boy-wolf",
    examples=[
        _ex("(boolean (:private (meta '^:private hidden)))", True,
            "whether the symbol 'hidden carries the :private flag",
            "the boolean of (:private (meta '^:private hidden))",
            scenario=(
                "Carol showed Tom two entries in the watchhouse log-book. One "
                "symbol, `hidden`, carried a private marker in its margin. "
                "Carol asked Tom to convert the raw answer to a simple true "
                "or false—a gatekeeper's yes-or-no."
            ),
            need=(
                "Tom needed to turn the metadata query into a decisive "
                "true-or-false answer that the watchhouse could use to decide "
                "whether the symbol could cross the namespace boundary."
            ),
            mapping=(
                "`boolean` forces the answer into true or false. A private "
                "flag, however it's written, becomes true; no flag or nil "
                "becomes false. The village's gate is open or shut."
            ),
            resolution=(
                "Carol wrote it, and the REPL returned true. The village's gate remained closed to the `hidden` symbol—it stayed private, as the margin declared."
            )),
        _ex("(boolean (:private (meta 'public)))", False,
            "whether 'public carries the :private flag",
            "the boolean of (:private (meta 'public))",
            scenario=(
                "The second entry in the ledger was `public`, with no private "
                "marker in its margin. Carol asked Tom to convert that answer "
                "to a decisive yes-or-no as well."
            ),
            need=(
                "Tom needed to confirm that the absence of a private flag "
                "meant the symbol could cross the boundary—it was publicly "
                "shared."
            ),
            mapping=(
                "`boolean` turns the absence (nil) into false. No private "
                "marker means false, which means the symbol is free to cross "
                "the namespace boundary and be used elsewhere."
            ),
            resolution=(
                "Carol wrote it, and the REPL returned false. The village's gate opened for the `public` symbol—it could be shared across cottage boundaries."
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"a\")", "A",
            "a single-direction call from one namespace to clojure.string",
            "the upper-cased string \"A\"",
            scenario=(
                "Tom had built a simple one-way bridge from his cottage to "
                "the smithy. Now Carol asked him to use the smithy's tool "
                "with the single letter \"a\"—a clean, unambiguous call "
                "across the boundary."
            ),
            need=(
                "Tom needed to see that a one-way dependency—one cottage "
                "calling the smithy, never the reverse—was safe and reliable."
            ),
            mapping=(
                "The fully-qualified call `clojure.string/upper-case` follows "
                "the one-way bridge Tom built. No circle exists; the townsfolk's "
                "rule allows this form."
            ),
            resolution=(
                'Carol wrote it, crossed the bridge, and the smithy returned "A". Tom learned: circular dependencies are the danger; one-way calls are safe. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(= 'a.b 'a.b)", True,
            "whether two references to the same namespace symbol agree",
            "the value of (= 'a.b 'a.b)",
            scenario=(
                "Tom pointed to his cottage's namespace symbol `a.b` on the "
                "notice-post. He asked whether the same symbol, written twice, "
                "would always compare as equal."
            ),
            need=(
                "Before trusting his namespace design, Tom needed to confirm "
                "that the symbol stayed consistent—that one-way dependency "
                "paths were stable."
            ),
            mapping=(
                "Equality `=` tests whether two identical namespace symbols "
                "agree. They must—there's only one posted symbol, one direction "
                "of dependency."
            ),
            resolution=(
                "Carol wrote it, and the REPL returned true. Tom's namespace was consistent. A one-way dependency, posted clearly, was a solid design."
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="boy-wolf",
    examples=[
        _ex("(do (def step1 1) (def step2 (+ step1 1)) step2)", 2,
            "two defs evaluated in order, the second using the first",
            "the final value step2 after sequential loading",
            scenario=(
                "Carol showed Tom the order of files in a project. She posted "
                "`step1` first, then `step2` on the next scroll, with step2 "
                "borrowing the value from `step1`."
            ),
            need=(
                "Tom wanted to know the final value if definitions were posted "
                "in order, with the second depending on the first."
            ),
            mapping=(
                "`do` sequences forms in order. The REPL reads step1 first "
                "and posts it. Then step2 is read and can reach back to "
                "`step1` already posted."
            ),
            resolution=(
                'Carol wrote the `do` form, and the REPL posted each definition in order. At the end, `step2` held 2. Tom saw: loading order matters. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(let [a 1 b (+ a 1)] (+ a b))", 3,
            "an in-expression analogue of file-loading order via let",
            "the value of (+ a b) given a=1 b=(+ a 1)",
            scenario=(
                "Carol showed Tom how to do the same work in a single short "
                "form, using `let` instead of posting to the notice-board. "
                "She bound `a` first, then `b` using `a`'s value."
            ),
            need=(
                "Tom needed to understand that both approaches—posting to the "
                "board and short-form bindings—respect the same sequential "
                "order."
            ),
            mapping=(
                "`let` binds values in sequence. Each binding can see the "
                "ones before it. The `a` is bound first, so `b` can use it. "
                "Then the whole form computes with both bindings alive."
            ),
            resolution=(
                'Carol wrote the `let` form, and the REPL returned 3—the sum of `a` (1) and `b` (2). Tom understood: whether you post or bind, the order is always first-to-last. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'           )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="boy-wolf",
    examples=[
        _ex("(:deps {:deps {:a 1 :b 2}})", {":a": 1, ":b": 2},
            "the :deps key from a small deps-map literal",
            "the value at :deps in {:deps {:a 1 :b 2}}",
            scenario=(
                "Carol kept a small ledger entry describing the project setup "
                "in a nested map: which dependencies the project needed, "
                "which paths to search. Tom asked how to read just the "
                "dependencies portion from the map."
            ),
            need=(
                "Before the village would approve a new project, Tom had to "
                "show he could extract the correct section from the ledger—"
                "the dependencies list."
            ),
            mapping=(
                "A map with a `:deps` key holds the dependencies. Querying "
                "the key `:deps` on the map returns the nested structure—"
                "the dependencies the project declared it would need."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned the dependencies map. Tom had read the ledger correctly; the meadow folk approved the project setup. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(get-in {:paths [\"src\"]} [:paths 0])", "src",
            "the first :paths entry from a tiny deps-style map",
            "the string \"src\" at [:paths 0]",
            scenario=(
                "The ledger also held a list of paths where project source files "
                "lived. Tom asked how to reach deep into the map to find the "
                "first path without writing many nested lookups."
            ),
            need=(
                "Tom needed a way to navigate nested structures in one form—"
                "to follow a chain of keys down into the map."
            ),
            mapping=(
                "`get-in` takes a map and a vector of keys, following them "
                "step by step. `[:paths 0]` means: get `:paths`, then get the "
                "first element."
            ),
            resolution=(
                'Carol wrote it, following the path down through the nested map. The REPL returned the first path value.'
            )),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/split \"src:test\" #\":\")", ["src", "test"],
            "splitting a colon-separated classpath-like string",
            "the vector [\"src\" \"test\"]",
            scenario=(
                "The reeve had written a list of directories on a single scroll "
                "line, separated by colons—the classpath, a road map of where "
                "the REPL would search for files. Tom wanted to turn the colon-"
                "separated string into a list he could count and read."
            ),
            need=(
                "Tom needed to split the classpath string into individual "
                "directories so he could work with each path separately."
            ),
            mapping=(
                "`clojure.string/split` cuts a string wherever it finds the "
                "separator—in this case, the colon. The smithy's tool returns "
                "a vector of the pieces between the cuts."
            ),
            resolution=(
                "Carol called the smithy's split tool with the colon pattern. The REPL cut the string and returned the vector of directory paths. Tom could now see each path clearly."
            )),
        _ex("(count [\"src\" \"test\" \"resources\"])", 3,
            "the number of entries in a classpath-like vector",
            "the count of three classpath entries",
            scenario=(
                "The reeve showed Tom a vector of three directory paths on the "
                "ledger—the classpath split into its pieces. Tom asked how many "
                "directories the REPL would search when loading a project."
            ),
            need=(
                "Tom needed to count the classpath entries to confirm the "
                "village had enough directories to hold all the project's files."
            ),
            mapping=(
                "`count` walks through the vector and tallies each entry, "
                "returning the number of paths the classpath held. Each "
                "directory is one step the REPL will check."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned 3. The classpath held three directories. Tom understood: count lets you measure any collection to know its size.'
            )),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="boy-wolf",
    examples=[
        _ex("(count ['village.shepherd 'village.elder 'village.shared])", 3,
            "the number of namespaces in a small project",
            "the count of namespace symbols in the vector",
            scenario=(
                "Carol kept a ledger of all the project's files, listing the "
                "namespace for each one: `village.shepherd`, `village.elder`, "
                "`village.shared`. Tom asked how many files the project held."
            ),
            need=(
                "Tom needed to count the project's namespaces to understand the "
                "scope of work—how many files the townsfolk had to maintain."
            ),
            mapping=(
                "`count` tallies the symbols in the vector, one for each file "
                "the project declared. The number of symbols equals the number "
                "of files."
            ),
            resolution=(
                "Carol wrote it, and the REPL returned 3. The project held three files. Tom could now plan the work knowing the project's true size."
            )),
        _ex("(map name ['village.shepherd 'village.elder])",
            ["village.shepherd", "village.elder"],
            "the names of two namespaces as strings",
            "the vector of namespace name strings",
            scenario=(
                "Tom pointed to a list of namespace symbols in the ledger: two "
                "of them, `village.shepherd` and `village.elder`. He wanted to "
                "turn both symbols into plain strings at once."
            ),
            need=(
                "Tom needed to extract the string names from a vector of "
                "namespace symbols—to read all the file paths at once without "
                "converting them one by one."
            ),
            mapping=(
                "`map` applies the `name` function to each symbol in the vector, "
                "turning each one into a string. The result is a new vector, "
                "one string per original symbol."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned the vector of namespace names as strings. Tom saw: `map` lets you transform every element in a collection at once.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="boy-wolf",
    examples=[
        _ex("(let [s clojure.string/upper-case] (s \"wolf\"))", "WOLF",
            "binding the function clojure.string/upper-case to a local s",
            "the value (s \"wolf\") where s is upper-case",
            scenario=(
                "Tom visited the smithy often, calling `clojure.string/upper-case` "
                "repeatedly. Carol showed him a shorthand: he could write `s` "
                "as a local alias for the full name."
            ),
            need=(
                "Tom was tired of writing the full-qualified name each time he "
                "wanted the smithy's tool. He needed a shorthand for one form."
            ),
            mapping=(
                "`let` binds the long name to `s`. Wherever `s` appears in the "
                "form, the runtime substitutes the real tool. The shorthand is "
                "temporary."
            ),
            resolution=(
                'Carol wrote it with the alias, and the REPL called the smithy\'s tool as if fully named. The result was "WOLF". Aliases shorten the form without changing the work. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="boy-wolf",
    examples=[
        _ex("(symbol? 'java.util.Date)", True,
            "whether 'java.util.Date is a symbol",
            "the value of (symbol? 'java.util.Date)",
            scenario=(
                "Carol led Tom toward the valley smithy—a foreign workshop "
                "with its own tools and naming conventions. On the lintel was "
                "a dotted name in the smith's host language: `java.util.Date`."
            ),
            need=(
                "Tom wanted to know whether the smithy's marker was a name "
                "they could refer to. Borrowing across the boundary required "
                "knowing what the foreign label was."
            ),
            mapping=(
                "`symbol?` asks whether the dotted-class label is a symbol—"
                "a name the runtime can reach across to. Quoted names from "
                "the smithy are still names."
            ),
            resolution=(
                'The predicate confirmed it as a symbol—a borrowable name. Tom understood the boundary could be crossed by name, not by guessing.'
            )),
        _ex("(name 'java.util.Date)", "java.util.Date",
            "the dotted-class symbol's name",
            "the string \"java.util.Date\"",
            scenario=(
                "Now that Tom knew the smithy's tool-label was a symbol, Carol "
                "asked him to extract just the text of the name — to read the "
                "label aloud without all the dot-marks."
            ),
            need=(
                "Tom needed to turn the symbol back into a plain string so the "
                "ledger could record the foreign tool's postal address."
            ),
            mapping=(
                "`name` reads the symbol aloud as a string. The dotted name "
                "speaks itself: \"java.util.Date\", a borrowable address for "
                "the smith's tool."
            ),
            resolution=(
                "Carol wrote it, and the REPL handed back the string. Tom had the foreign tool's name written in the ledger now—proof the boundary could be crossed and recorded."
            )),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="boy-wolf",
    examples=[
        _ex("(:doc (meta '^{:doc \"trust the runtime\"} village))",
            "trust the runtime",
            "the :doc metadata attached to the symbol 'village",
            "the docstring \"trust the runtime\" from the metadata",
            scenario=(
                "Carol kept the village log-book on a stand in the watchhouse—"
                "leather-bound, with marginalia in the elder's hand. Today's "
                "entry: a symbol `village` with a margin note reading "
                "`trust the runtime`."
            ),
            need=(
                "Tom wanted to read just the marginalia—the note Carol pinned "
                "to the symbol—without reading the symbol's value."
            ),
            mapping=(
                "`meta` opens the marginalia—the metadata map on the symbol. "
                "`:doc` reads the specific `:doc` note from that map, the way "
                "you'd read one line from the margin."
            ),
            resolution=(
                "The log-book returned the marginalia exactly as Carol had pinned it—the elder's note, ready for whoever consulted the entry next."
            )),
        _ex("(:author (meta '^{:author \"Aesop\"} village))", "Aesop",
            "the :author metadata on 'village",
            "the string \"Aesop\"",
            scenario=(
                "Another symbol in the log-book—`village` again—carried a "
                "different kind of marginalia. In the margin was written "
                "`:author \"Aesop\"`. Tom asked Carol to read that particular "
                "note from the metadata."
            ),
            need=(
                "Tom wanted to know the author's name written in the margin, "
                "to credit the elder who had authored that part of the ledger."
            ),
            mapping=(
                "`meta` opens all the marginalia. `:author` pulls out just the "
                "author note from the map—the way you'd point to one word in "
                "the margin and read it aloud."
            ),
            resolution=(
                'Carol wrote it, and the REPL spoke the author\'s name: "Aesop". The credit was written there in the ledger, and Tom saw how the REPL could read and deliver the elder\'s notes.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="boy-wolf",
    examples=[
        _ex("(contains? #{'clojure.string} 'clojure.string)", True,
            "whether the require list still contains 'clojure.string",
            "the value of (contains? #{'clojure.string} 'clojure.string)",
            scenario=(
                "The reeve audited the project's posted requires, keeping a set "
                "of the libraries that were still in use: `{clojure.string}`. "
                "Carol asked Tom to check whether `clojure.string` was still on "
                "the kept list."
            ),
            need=(
                "Before cleaning up old requires, Tom had to confirm which "
                "libraries were still actively used by the watchhouse's forms."
            ),
            mapping=(
                "`contains?` checks whether a name appears in a set. The set "
                "holds the libraries that remain in use; the predicate confirms "
                "whether a given library still has a home on the require list."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned true. The library was still needed. Tom marked it safe to keep; no cleanup required.'
            )),
        _ex("(contains? #{'clojure.string} 'clojure.set)", False,
            "whether the require list contains an unused 'clojure.set",
            "the value of (contains? #{'clojure.string} 'clojure.set)",
            scenario=(
                "Tom then asked whether `clojure.set`—a library the project "
                "had once used—was still on the kept-libraries list."
            ),
            need=(
                "Tom needed to know if the set library could be removed from "
                "the require list without breaking anything. The predicate "
                "would tell him."
            ),
            mapping=(
                "`contains?` returns false if the name is not in the set. "
                "A false answer means the library can be safely deleted from "
                "the require list—no form in the project needs it anymore."
            ),
            resolution=(
                'Carol wrote it, and the REPL returned false. The set library was not on the kept list. Tom approved the cleanup: `clojure.set` could be struck from the requires.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G6_01, G6_02, G6_03, G6_04, G6_05, G6_06, G6_07, G6_08,
    G6_09, G6_10, G6_11, G6_12, G6_13, G6_14, G6_15, G6_16,
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
    print(f"grade-6 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
