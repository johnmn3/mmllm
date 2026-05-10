"""Grade 6 — namespaces and modular code. through the milkmaid fable.

Subplot lens: two characters working at separate workbenches /
copybooks / cottages, then later sharing what they've labeled. The
fable's vanity-vs-steadiness pulls in: Milkmaid wants to scribble
everything in one place, Farmer insists on naming the file the
form lives in and requiring it cleanly.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _GOAL_SUBPLOTS, _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two characters at separate workbenches, exchanging a labeled form.
    SubplotTemplate("""\
{farmer_phrase} kept a small workbench {place}, where every form had
its own labeled drawer. {milkmaid_phrase}, {emo_boastful} preferred to scribble each
expression in a single notebook. To settle a question that morning,
{farmer} pointed to {concept_phrase} and asked {milkmaid} to evaluate the
form {form_display} so they could see what name belonged with what
value."""),

    # The "two cottages" / cross-namespace beat.
    SubplotTemplate("""\
The two of them lived in cottages on opposite sides {place} —
{farmer_phrase} on one side, {milkmaid_phrase} on the other. Each kept
their own copybook of forms. When the time came to compare notes,
{farmer} read aloud {concept_phrase} and asked, {emo_patient}, what
the form {form_display} would return when the REPL reached across the
shared path."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


_PLAN_G6 = _PLAN_POOL + (
    "I require the namespace and call the function.",
    "I use the fully-qualified name to reach the var.",
    "I keep the namespaces straight and let the REPL resolve the name.",
)


# ─────────────────────── 16 grade-6 subjects ───────────────────────


# G6-01 — Namespace as file
# A namespace's name is itself a symbol; we extract the string form
# to show the path-like string the namespace corresponds to.
G6_01 = SubjectCurriculum(grade=6, subject_id="G6-01",
    subject_title="Namespace as file", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(name 'foo.bar)",
            expected="foo.bar",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                "The milkmaid arrived at the market-board in the village square — a "
                "board nailed with names and namespaces of all the registered vendors. "
                "She wanted to read the string name from one of the posted symbols."
            ),
            need=(
                "She needed to extract the board-entry as a readable string — not a "
                "symbol, but the text the symbol stands for, as it would appear "
                "written on the market-board."
            ),
            mapping=(
                "`name` is the market-board reader: it takes a quoted namespace symbol "
                "and returns the string the board has posted — the human-readable "
                "market address, not the runtime name-object."
            ),
            resolution=(
                'The REPL returned the string the market-board carried — the dotted vendor address, readable and ready to hand to a buyer (with `foo.bar` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name 'clojure.string)",
            expected="clojure.string",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
        ),
        SubjectExample(
            form="(symbol? 'tortoise.race)",
            expected=True,
            concept_phrase="checking whether a value is a symbol",
            question_what="whether a value is a symbol",
            goal_text="test whether a quoted namespace-like value is a symbol",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(name 'race.tortoise)",
            expected="race.tortoise",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                "The market-board in the village square had a posted symbol for the "
                "racing league's namespace. The milkmaid needed to read the string "
                "the board displayed, not handle the raw symbol object."
            ),
            need=(
                "She needed to pull the printed text off the board's entry — the "
                "dotted string that named the namespace section — so she could copy "
                "it onto her order slip."
            ),
            mapping=(
                "`name` reads the board entry: given the quoted namespace symbol, it "
                "returns the string the board has posted — the readable market "
                "address rather than the symbol itself."
            ),
            resolution=(
                'The REPL returned the dotted string the board carried — the namespace address she could write down and hand to the next vendor (with `race.tortoise` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 'race.tortoise 'race.tortoise)",
            expected=True,
            concept_phrase="checking equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two identical namespace symbols are equal",
            scenario=(
                "Two entries on the market-board appeared identical — the same dotted "
                "vendor name posted on opposite sides of the panel. The farmer "
                "challenged the milkmaid to confirm whether the board truly listed "
                "the same namespace twice."
            ),
            need=(
                "She needed to compare the two posted symbols and settle the question "
                "before the vendor stall opened — the board could not have two "
                "conflicting names for the same section."
            ),
            mapping=(
                "`=` reads both entries off the board and compares them; identical "
                "namespace symbols on the board resolve to the same runtime object, "
                "so equality holds."
            ),
            resolution=(
                'The REPL confirmed the two board entries matched — the same namespace was indeed posted on both sides of the panel (with `race.tortoise` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hare")',
            expected="HARE",
            concept_phrase="calling a fully-qualified string function",
            question_what="the capitalized form returned by the upper-case routine on the scroll",
            goal_text="call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare",
            scenario=(
                "The market-board in the village square listed the clojure.string "
                "vendor's section. The milkmaid had a word written in small letters "
                "and needed to use the board's registered uppercasing service to "
                "produce the full-capitals version."
            ),
            need=(
                "She needed to consult the board, locate the vendor's section, and "
                "call the uppercasing routine — without that board entry she could "
                "not reach the function by its full qualified name."
            ),
            mapping=(
                "The board's namespace section is `clojure.string`; the vendor's "
                "listed routine is `upper-case`. Reading the board entry and calling "
                "it produces the transformed output."
            ),
            resolution=(
                'The REPL returned the all-capitals version of the word, confirming the board-listed routine had been reached and applied correctly (with `hare` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(clojure.string/lower-case "ZEBRA")',
            expected="zebra",
            concept_phrase="calling a fully-qualified string function",
            question_what="the lowercase form of the string ZEBRA produced by clojure.string/lower-case",
            goal_text="call the lowercasing function from clojure.string on a test string",
            scenario=(
                "A word had arrived at the dairy door in all-capitals lettering, "
                "posted from a distant market. The milkmaid checked the village "
                "square board for the clojure.string section and located the "
                "lowercasing service registered there."
            ),
            need=(
                "She needed to convert the all-capitals word to its lowercase form "
                "by consulting the board's registered routine — the board's entry "
                "was the only way to reach the service by its full name."
            ),
            mapping=(
                "The board's namespace section `clojure.string` names the vendor; "
                "`lower-case` is the routine posted on that section. Calling the "
                "fully-qualified name on the board delivers the lowercased result."
            ),
            resolution=(
                'The REPL returned the all-lowercase version of the word, proving the board-listed lowercasing service had been found and applied (with `ZEBRA` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))',
            expected=True,
            concept_phrase="testing equality of two identical function calls",
            question_what="whether two calls to the same function with the same argument produce the same result",
            goal_text="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal",
            scenario=(
                "The farmer had posted the clojure.string section on the market-board "
                "and the milkmaid called the same board-listed routine twice in a row "
                "on the same letter, once from each side of the stall."
            ),
            need=(
                "She needed to confirm that referring to the same board entry twice "
                "with the same input always produced the same output — proving the "
                "board's function was deterministic."
            ),
            mapping=(
                "Both sides of the `=` form consult the same board entry — the "
                "namespace section and routine name are identical — so equality holds "
                "when the routine is pure."
            ),
            resolution=(
                'The REPL returned that both calls produced the same result, confirming the board-listed function behaves consistently (with `x` as the input value) (with `) (clojure.string/upper-case ` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hello")',
            expected="HELLO",
            concept_phrase="calling a fully-qualified string function",
            question_what="the uppercase form of the string hello produced by clojure.string/upper-case",
            goal_text="call the uppercasing function from clojure.string on a test string",
            scenario=(
                "The market-board's clojure.string section listed an uppercasing "
                "service. The milkmaid had a greeting written in small letters on a "
                "slip of paper and wanted to transform it using the board's registered "
                "routine."
            ),
            need=(
                "She needed the fully-qualified name from the board to reach the "
                "routine — without the namespace section she could not distinguish "
                "this vendor's service from any other."
            ),
            mapping=(
                "`clojure.string` names the board's section; `upper-case` is the "
                "routine posted there. Writing the fully-qualified name reads the "
                "board entry and invokes the posted service."
            ),
            resolution=(
                'The REPL returned the all-capitals greeting, confirming the board entry had been found and the uppercasing service applied (with `hello` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(clojure.string/reverse "abc")',
            expected="cba",
            concept_phrase="calling a fully-qualified string function",
            question_what="the reversed form of the string abc produced by clojure.string/reverse",
            goal_text="call the reversing function from clojure.string on a test string",
            scenario=(
                "The vendor's board section for clojure.string also listed a reversing "
                "service. The milkmaid had written a short label on her pail and "
                "needed to read it back in reverse order to satisfy a delivery note."
            ),
            need=(
                "She needed to reach the board's reverse routine by its full namespace "
                "address — consulting the correct section prevented her from calling "
                "the wrong vendor's tool."
            ),
            mapping=(
                "The board's namespace section `clojure.string` combined with the "
                "posted routine `reverse` forms the fully-qualified name. Calling it "
                "reverses the characters in the string."
            ),
            resolution=(
                "The REPL returned the reversed string, confirming the board's reversing service had been located and applied correctly (with `abc` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(namespace :owner/item)",
            expected="owner",
            concept_phrase="extracting the namespace portion of a keyword",
            question_what="the namespace part of a qualified keyword",
            goal_text="extract the namespace portion of a qualified keyword",
            scenario=(
                "A qualified keyword appeared on the board — a compound entry of the "
                "form section/name. The farmer asked the milkmaid to read just the "
                "board section — the left-hand part that named which vendor's area "
                "the keyword belonged to."
            ),
            need=(
                "She needed to separate the board section from the entry name so she "
                "could route the keyword to the correct vendor's stall without "
                "carrying the full compound label."
            ),
            mapping=(
                "`namespace` reads the board-section half of a qualified keyword — "
                "it returns the string naming the section, ignoring the entry name "
                "after the slash."
            ),
            resolution=(
                "The REPL returned the section string — the left-hand portion of the — :owner. "
                "compound keyword, identifying which vendor's board the entry belonged to."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name :owner/item)",
            expected="item",
            concept_phrase="extracting the name portion of a keyword",
            question_what="the name part of a qualified keyword",
            goal_text="extract the name local portion of a qualified keyword",
            scenario=(
                "The same qualified keyword sat on the board, section-slash-name. "
                "This time the milkmaid needed only the right-hand portion — the "
                "local entry name after the slash — to label the product in the "
                "delivery pail."
            ),
            need=(
                "She needed to strip away the board section and read just the entry's "
                "local name, so the label on the pail carried only the product "
                "identifier without the vendor prefix."
            ),
            mapping=(
                "`name` reads the local-name half of a qualified keyword — it returns "
                "the string after the slash, the entry's own identifier within its "
                "board section."
            ),
            resolution=(
                "The REPL returned the local name string — just the right-hand — :owner. "
                "portion of the keyword, ready to write on the pail's label."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(:private (meta '^:private x))",
            expected=True,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a symbol",
            goal_text="check whether the :private flag is present in the metadata of a symbol with :private marker",
            scenario=(
                "The farmer had posted a vendor entry on the village-square board "
                "and tucked a private-access slip behind the name-plate, marking the "
                "stall as restricted. The milkmaid needed to read whether the board "
                "entry carried that restriction marker."
            ),
            need=(
                "She needed to reach into the board entry's attached slip and read "
                "the `:private` field — confirming the restriction before allowing "
                "any outsider to consult the stall."
            ),
            mapping=(
                "`meta` opens the annotation slip behind the board entry; the "
                "`:private` keyword reads the restriction field from that slip. "
                "A symbol annotated with `^:private` carries the flag set to true."
            ),
            resolution=(
                "The REPL returned the value the slip carried for the restriction "
                "field, confirming the board entry was marked as private."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:private (meta 'x))",
            expected=None,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a plain symbol",
            goal_text="check whether the :private flag is present in the metadata of a plain symbol without markers",
            scenario=(
                "A plain name appeared on the market-board with no annotation slip "
                "attached — just the bare vendor entry. The milkmaid checked behind "
                "the name-plate looking for a restriction marker, but the entry had "
                "no metadata tucked behind it."
            ),
            need=(
                "She needed to confirm that a board entry with no annotation slip "
                "carried no private restriction — so she could route buyers to that "
                "stall freely."
            ),
            mapping=(
                "`meta` reaches behind the board entry for its slip; with no slip "
                "present the `:private` lookup returns nothing — the entry carries "
                "no restriction field."
            ),
            resolution=(
                "The REPL returned nothing for the restriction field, confirming "
                "the plain board entry had no private marker attached."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(boolean (:private (meta '^:private hidden)))",
            expected=True,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol with :private marker evaluates to true when converted to boolean",
            goal_text="convert the :private metadata flag of a symbol marked with :private to a boolean",
            scenario=(
                "The farmer had posted a hidden stall on the village-square board "
                "with a restriction slip tucked behind its name-plate. The milkmaid "
                "needed to read that slip and convert the restriction flag into a "
                "clear yes-or-no answer for the gatekeeper."
            ),
            need=(
                "She needed to produce a definite true-or-false signal — the "
                "gatekeeper at the dairy door would only accept a boolean, not the "
                "raw flag value from the annotation slip."
            ),
            mapping=(
                "`meta` opens the annotation slip; `:private` reads the restriction "
                "field; `boolean` converts whatever the slip holds into a clean "
                "boolean — truthy flag becomes true, absent value becomes false."
            ),
            resolution=(
                "The REPL returned the boolean equivalent of the restriction flag, "
                "giving the gatekeeper a clear access decision for the hidden stall."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean (:private (meta 'public)))",
            expected=False,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol without :private marker evaluates to false when converted to boolean",
            goal_text="convert the :private metadata flag of a plain symbol to a boolean",
            scenario=(
                "A stall posted on the market-board under the name `public` had no "
                "annotation slip behind it at all. The milkmaid tried to read the "
                "restriction field and convert it to a boolean for the gatekeeper "
                "at the dairy door."
            ),
            need=(
                "She needed to confirm that an entry with no restriction slip "
                "converted cleanly to a negative boolean — so the gatekeeper "
                "could wave buyers through without hesitation."
            ),
            mapping=(
                "`meta` finds no slip; `:private` returns nothing; `boolean` "
                "converts the absent value to false — an unmarked board entry "
                "is treated as openly accessible."
            ),
            resolution=(
                "The REPL returned the boolean for an absent restriction flag, "
                "confirming the unmarked stall was openly accessible."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "a")',
            expected="A",
            concept_phrase="calling a function from a required namespace",
            question_what="the uppercase form of the character a produced by clojure.string/upper-case",
            goal_text="call the string uppercasing function from clojure.string on the character a",
            scenario=(
                "Two vendor sections on the village-square board had once pointed "
                "to the same stall, creating a circular dependency that froze the "
                "market. The farmer resolved the tangle and re-posted the board "
                "entries cleanly, then asked the milkmaid to confirm a routine still "
                "worked."
            ),
            need=(
                "She needed to call the board-listed uppercasing service on a single "
                "character to prove the namespace was reachable again without any "
                "circular reference blocking the path."
            ),
            mapping=(
                "The board's `clojure.string` section lists `upper-case`; calling "
                "the fully-qualified name reaches the vendor's routine directly — "
                "no circular reference intervenes when the dependency is resolved."
            ),
            resolution=(
                "The REPL returned the uppercased character, confirming the "
                "board-listed namespace was reachable and the circular tangle cleared."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 'a.b 'a.b)",
            expected=True,
            concept_phrase="testing equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two references to the same namespace symbol are equal",
            scenario=(
                "After the market-board was re-posted, the same namespace symbol "
                "appeared on two separate vendor entries. The farmer pointed to both "
                "entries and asked the milkmaid to confirm they referred to the same "
                "board section."
            ),
            need=(
                "She needed to compare the two posted namespace symbols and settle "
                "whether they were truly the same — any mismatch would mean the "
                "circular dependency had merely been disguised, not resolved."
            ),
            mapping=(
                "`=` reads both board entries and compares them; identical namespace "
                "symbols on the market-board resolve to the same runtime object, "
                "so the equality check returns a clear result."
            ),
            resolution=(
                'The REPL confirmed the two board entries matched, proving the namespace symbols were identical and the dependency graph was clean (with `a.b` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def step1 1) (def step2 (+ step1 1)) step2)",
            expected=2,
            concept_phrase="evaluating definitions in sequence to establish dependency order",
            question_what="the value of the second variable after both definitions are loaded in order",
            goal_text="define step1 as 1, then define step2 as step1 plus 1, then return step2",
            scenario=(
                "The farmer had posted the vendor names on the market-board in a "
                "deliberate order — each stall's entry depended on the one posted "
                "before it. The milkmaid needed to follow that order exactly when "
                "reading the board to fill her pail correctly."
            ),
            need=(
                "She needed to define each board entry in sequence so the later "
                "ones could safely refer to the earlier ones — posting out of order "
                "would leave a stall with an undefined predecessor."
            ),
            mapping=(
                "`do` evaluates the definitions in the order posted: `step1` is "
                "written to the board first, then `step2` reads it to compute its "
                "own value. The final expression returns the last entry's value."
            ),
            resolution=(
                "The REPL returned the value of the last board entry after both "
                "definitions were posted in order, confirming the sequence was sound."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 1 b (+ a 1)] (+ a b))",
            expected=3,
            concept_phrase="establishing local bindings with dependent values",
            question_what="the sum of two variables with the second depending on the first",
            goal_text="bind a to 1, bind b to a plus 1, then return the sum of a and b",
            scenario=(
                "At a small corner of the market-board the farmer chalked two local "
                "entries in sequence — the second entry's value was computed from "
                "the first. The milkmaid read them off in order to tally the total "
                "for the morning's delivery."
            ),
            need=(
                "She needed both local entries to be bound in the right order before "
                "she could add them together — the second entry had to read the first "
                "to know its own value."
            ),
            mapping=(
                "`let` binds entries in left-to-right order on the board: `a` is "
                "chalked first, then `b` reads `a` to set its own value. The body "
                "sums both entries to produce the total."
            ),
            resolution=(
                'The REPL returned the sum of the two local board entries, confirming the dependent binding order was respected (with `1` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="milkmaid",
    examples=[
        _ex("(:deps {:deps {:a 1 :b 2}})", {":a": 1, ":b": 2},
            "accessing a key from a nested map structure",
            "the value at the :deps key in a deps-style map",
            goal="extract the value at the :deps key from a nested map"),
        _ex("(get-in {:paths [\"src\"]} [:paths 0])", "src",
            "accessing a nested value in a map using a path vector",
            "the first element from a :paths vector in a deps-style map",
            goal="extract the first entry from the :paths vector in a deps-style map"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="milkmaid",
    examples=[
        _ex("(clojure.string/split \"src:test\" #\":\")", ["src", "test"],
            "splitting a string by a delimiter",
            "the vector of parts after splitting a colon-separated path string",
            goal="split a colon-separated classpath-like string into its individual entries"),
        _ex("(count [\"src\" \"test\" \"resources\"])", 3,
            "counting the number of elements in a vector",
            "the number of entries in a classpath-like vector",
            goal="count the number of entries in a vector of classpath directories"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count ['race.tortoise 'race.hare 'race.shared])",
            expected=3,
            concept_phrase="counting the number of namespace symbols in a project",
            question_what="the number of namespaces in a small project",
            goal_text="count the number of namespace symbols in a vector of three namespaces",
            scenario=(
                "The farmer had posted three vendor sections on the village-square "
                "board — one for each file in the project. Before opening the "
                "market, the milkmaid needed to tally the board entries to make "
                "sure all sections were accounted for."
            ),
            need=(
                "She needed a count of the posted namespace entries so she could "
                "confirm that no file had been left off the board before the "
                "morning's trading began."
            ),
            mapping=(
                "`count` tallies the namespace symbols posted in the vector — each "
                "symbol stands for one board entry, and the total tells her how "
                "many vendor sections the project board carries."
            ),
            resolution=(
                "The REPL returned the number of namespace entries on the board, confirming all the project's files were represented (with `race.tortoise` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(map name ['race.tortoise 'race.hare])",
            expected=["race.tortoise", "race.hare"],
            concept_phrase="extracting string names from namespace symbols",
            question_what="the vector of namespace names as strings",
            goal_text="extract the string form of each namespace symbol in a vector of two namespaces",
            scenario=(
                "The market-board carried two namespace symbols for the project's "
                "vendor sections. The milkmaid needed to copy the string name off "
                "each entry so she could write them legibly on the delivery slip."
            ),
            need=(
                "She needed the readable string text from each board entry — not "
                "the symbol objects themselves but the printed names that would "
                "appear on the slip handed to the next courier."
            ),
            mapping=(
                "`map` applies `name` to each namespace symbol in the board's "
                "section list, reading the string the board has posted for each "
                "entry in turn and collecting the results."
            ),
            resolution=(
                'The REPL returned the sequence of string names, one per board entry, ready to be written onto the delivery slip (with `race.tortoise` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(let [s clojure.string/upper-case] (s "hare"))',
            expected="HARE",
            concept_phrase="aliasing a fully-qualified function and calling it through the alias",
            question_what="the uppercase form of the string hare when clojure.string/upper-case is called through a local alias",
            goal_text="bind the fully-qualified string uppercasing function to a local alias s and call it on hare",
            scenario=(
                "The market-board's clojure.string section was posted with a long "
                "vendor name that would tire a customer to repeat. The milkmaid "
                "chalked a short alias on her pail so she could call the board's "
                "uppercasing service by a compact local name."
            ),
            need=(
                "She needed to bind the board's fully-qualified routine to a brief "
                "alias and call it on a word — confirming the alias reached the "
                "same vendor entry as the full board path."
            ),
            mapping=(
                "`let` writes the alias `s` pointing to the fully-qualified board "
                "entry `clojure.string/upper-case`; calling `s` consults the same "
                "posted routine as the full namespace path would."
            ),
            resolution=(
                'The REPL returned the uppercased word, confirming the alias reached the board-listed routine just as the full name would (with `hare` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(symbol? 'java.util.List)",
            expected=True,
            concept_phrase="testing whether a value is a symbol",
            question_what="whether a dotted Java class name is a symbol",
            goal_text="test whether a Java class name written as a quoted symbol is a symbol",
            scenario=(
                "The neighbor's toolshed held a milking stool labeled with a "
                "dotted Java class name — a borrowed tool from the adjacent farm. "
                "The milkmaid needed to confirm the label on the stool was a "
                "proper symbol before she could carry it to her dairy."
            ),
            need=(
                "She needed to verify that the borrowed tool's dotted class name "
                "was recognized as a symbol — the dairy door would only accept "
                "tools whose labels passed the symbol check."
            ),
            mapping=(
                "`symbol?` examines the borrowed tool's label — a quoted dotted "
                "class name — and confirms it is a symbol, just as it would be "
                "for any other qualified name on the neighbor's rack."
            ),
            resolution=(
                'The REPL confirmed the dotted class name was indeed a symbol, clearing the borrowed tool for use at the dairy (with `java.util.List` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name 'java.util.Map)",
            expected="java.util.Map",
            concept_phrase="extracting the string form of a class symbol",
            question_what="the string form of a Java class symbol",
            goal_text="extract the string form of a Java class symbol",
            scenario=(
                "A tool borrowed from the neighbor's farm bore a class name stamped "
                "in dotted notation on its handle. The milkmaid needed to read that "
                "name as a plain string so she could copy it onto the delivery slip "
                "for the dairy ledger."
            ),
            need=(
                "She needed to extract the string text from the borrowed tool's "
                "class symbol — the ledger required a readable string, not the "
                "raw symbol object from the neighbor's toolshed."
            ),
            mapping=(
                "`name` reads the string off the borrowed tool's symbol handle — "
                "it returns the dotted class name as printed text, the same "
                "technique used for any namespace symbol on the market-board."
            ),
            resolution=(
                'The REPL returned the dotted string name from the class symbol, ready to be written into the dairy ledger (with `java.util.Map` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(:doc (meta \'\\{:doc "steady wins"\\} race))',
            expected="steady wins",
            concept_phrase="accessing the :doc metadata from a symbol",
            question_what="the docstring value from a symbol's metadata",
            goal_text="extract the :doc metadata value from a symbol with a docstring",
            scenario=(
                "The farmer had annotated a symbol called `race` with a slip of paper "
                "tucked into its metadata: a docstring recording the dairy's guiding "
                "principle. She needed to read that annotation back from the slip."
            ),
            need=(
                "She needed to unwrap the market order — reach into the symbol's "
                "metadata, find the `:doc` key, and return the value written on "
                "the slip."
            ),
            mapping=(
                "`meta` opens the order-slip envelope tied to the symbol; the `:doc` "
                "keyword reads the line on the slip labeled doc. The form retrieves "
                "the annotation, not the symbol itself."
            ),
            resolution=(
                "The REPL returned the docstring the farmer had tucked into the slip "
                "— the principle she had recorded for the day's dairy run."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(:author (meta \'\\{:author "Aesop"\\} race))',
            expected="Aesop",
            concept_phrase="accessing the :author metadata from a symbol",
            question_what="the author value from a symbol's metadata",
            goal_text="extract the :author metadata value from a symbol with an author tag",
            scenario=(
                "A market order on a slip of paper had been tucked into the `race` "
                "symbol's metadata pocket, recording who had commissioned the order. "
                "The milkmaid needed to pull the author's name off the slip to "
                "complete the ledger entry."
            ),
            need=(
                "She needed to open the metadata envelope tied to the symbol and "
                "read the `:author` field on the slip — the ledger required the "
                "commissioner's name before the order could be filed."
            ),
            mapping=(
                "`meta` opens the order-slip envelope; the `:author` keyword reads "
                "the line on the slip labeled author. The form retrieves the "
                "name written there, not the symbol itself."
            ),
            resolution=(
                "The REPL returned the author name the farmer had tucked into "
                "the slip, completing the ledger entry for the commissioned order."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.string)",
            expected=True,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a namespace is in the set of required namespaces",
            goal_text="test whether the clojure.string namespace is in the set of required namespaces",
            scenario=(
                "The farmer was clearing stale vendor entries off the market-board "
                "and maintaining a list of board sections she still needed. The "
                "milkmaid needed to check whether a particular namespace was still "
                "on that active list before deciding to keep or remove it."
            ),
            need=(
                "She needed to confirm the clojure.string section was in the "
                "maintained set of required board entries — removing a section "
                "still in use would break the next vendor's route."
            ),
            mapping=(
                "`contains?` checks whether the namespace symbol appears in the "
                "set of required board sections; a present entry means the board "
                "listing is still active and should not be removed."
            ),
            resolution=(
                "The REPL confirmed the namespace was in the required set, "
                "telling the milkmaid to leave that board entry in place."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.set)",
            expected=False,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a different namespace is in the set of required namespaces",
            goal_text="test whether the clojure.set namespace is in the set of required namespaces",
            scenario=(
                "While still clearing the market-board, the milkmaid checked a "
                "second vendor section against the maintained active list. This "
                "board entry was for clojure.set, which nobody had recently "
                "required from the village square."
            ),
            need=(
                "She needed to confirm whether the clojure.set section was still "
                "needed — if it was absent from the active set the board entry "
                "could safely be removed without breaking anything."
            ),
            mapping=(
                "`contains?` checks the active-section set for the clojure.set "
                "namespace symbol; its absence from the set means no vendor has "
                "required it and the board entry is a stale listing."
            ),
            resolution=(
                "The REPL returned a negative result, confirming the namespace "
                "was not in the required set and could be removed from the board."
            ),
            tags=("story",),
        ),
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
    print(f"grade-6 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
