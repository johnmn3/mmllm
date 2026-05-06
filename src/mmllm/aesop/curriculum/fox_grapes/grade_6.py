"""Grade 6 — namespaces and modular code. Through fox-grapes.

Subplot lens: two foxes tending separate orchards / kitchen gardens /
arbor-rows, each with their own labeled baskets and ledgers, then later
comparing what each has named. The fable's rationalize-vs-evaluate
dynamic pulls in: the hasty fox wants to scribble every form into one
basket and trust the label, while the patient fox insists on naming the
row the form lives in and requiring the right basket cleanly — the
REPL still settles the answer.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL, _GOAL_SUBPLOTS
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS


_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two foxes at separate orchard rows, exchanging a labeled form.
    SubplotTemplate("""\
{patient_fox_phrase} tended a small arbor-row {place}, where every form
had its own labeled basket. {hasty_fox_phrase} preferred to scribble
each expression into a single ledger. To settle a question that
morning, {patient_fox} pointed to {concept_phrase} and asked
{hasty_fox_him_her} to evaluate the form {form_display} so they could
see what name belonged with what value."""),

    # The "two kitchen gardens" / cross-namespace beat.
    SubplotTemplate("""\
The two of them kept kitchen gardens on opposite sides {place} —
{patient_fox_phrase} on one side, {hasty_fox_phrase} on the other.
Each kept their own ledger of forms. When the time came to compare
notes, {patient_fox} read aloud {concept_phrase} and asked,
{emo_patient}, what the form {form_display} would return when the
REPL reached across the shared path."""),
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
    subject_title="Namespace as file", fable="fox-grapes",
    examples=[
        _ex("(name 'foo.bar)", "foo.bar",
            "the dotted-name path foo.bar", "the string path it represents",
            goal="read the string name of the namespace foo.bar without its symbol wrapper",
            scenario="Renard chalked the dotted nameplate foo.bar onto a weathered vine-post at the row's head. He needed to strip the symbol wrapper and read just the string path the post stood for.",
            need="He wanted the bare path-string, not the symbol that held it.",
            mapping="The name form unwraps a symbol to its string representation. A dotted symbol carries a path; name extracts that path as a string.",
            resolution="the post's path became readable as a string—Renard could now file it in the leather ledger.",
            tags=("story",)),
        _ex("(name 'clojure.string)", "clojure.string",
            "the library namespace clojure.string", "its string path",
            goal="extract the string form of a fully-qualified namespace symbol",
            scenario="Vix the fox stood before a foreign nameplate—clojure.string—etched in the toolshed's timber. The symbol pointed to a distant library, but she needed its string address for her ledger.",
            need="She wanted the string version to write it down without the symbol shell.",
            mapping="The name form strips any symbol to its string. Even namespace symbols from distant libraries yield their paths as strings.",
            resolution="the library's string address flowed into her ledger, clean and ready to file.",
            tags=("story",)),
        _ex("(symbol? 'orchard.fox)", True,
            "whether a dotted name is still a symbol", "whether it passes the symbol test",
            goal="confirm that a dotted-name path is recognized as a symbol",
            scenario="Sly the fox picked up a foreign notation—'orchard.fox—and wondered if it obeyed the orchard's rules. Was this dotted thing still a symbol, a name-token the REPL would honor?",
            need="He wanted proof that the odd-looking path would behave like a name in his world.",
            mapping="The symbol? predicate confirms whether something is a symbol—a name-token. Dotted paths, though they look foreign, are still symbols in Clojure's eye.",
            resolution="the predicate returned true; the path was indeed a symbol, a name-token that the REPL would obey.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="fox-grapes",
    examples=[
        _ex("(name 'orchard.fox)", "orchard.fox",
            "the namespace name 'orchard.fox extracted as a string", "its string form",
            goal="strip a namespace symbol to its bare string path",
            scenario="Renard kept a ledger of fox-arbor names. He found the symbol 'orchard.fox pinned to a corner post and needed its string equivalent for the ledger's row.",
            need="The ledger required strings, not symbols.",
            mapping="The name form converts any symbol—including namespace symbols—to its string representation.",
            resolution="the symbol melted into the ledger as a clean string entry.",
            tags=("story",)),
        _ex("(= 'orchard.fox 'orchard.fox)", True,
            "whether two identical namespace symbols are equal", "whether equality holds",
            goal="confirm that the same namespace symbol written twice is equal to itself",
            scenario="Vix chalked 'orchard.fox twice on the same slate to test the REPL's sense of sameness. Were both instances the same symbol, or would the REPL see them as different marks?",
            need="She needed certainty that naming a symbol twice yielded the same identity.",
            mapping="The = form compares two values; symbols compare by their content, not by where they appear. The same dotted path written twice is the same symbol.",
            resolution="the equality held true—both marks were identical in the REPL's eye.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="fox-grapes",
    examples=[
        _ex("(clojure.string/upper-case \"fox\")", "FOX",
            "calling the upper-case function across the fully-qualified namespace path",
            "the text in all capitals",
            goal="use a function from a distant namespace by its full dotted address",
            scenario="Renard stood at a distant library stone and called out through the fully-qualified path clojure.string/upper-case. A quiet text lay waiting: \"fox\". The function reached across, seized the text, and returned it transformed.",
            need="He could reach the library function by naming the full path; no local alias needed.",
            mapping="A fully-qualified name lets you reach a function in another namespace directly. The path includes the namespace, so the REPL knows exactly where to find it.",
            resolution="the text came back in capitals, fetched through the full dotted address.",
            tags=("story",)),
        _ex("(clojure.string/lower-case \"FOX\")", "fox",
            "calling the lower-case function via its complete namespace path", "the text lowered",
            goal="access a function by its full namespace path and apply it",
            scenario="Sly the fox found the fully-qualified path clojure.string/lower-case carved into a toolshed beam. A loud text hung nearby: \"FOX\". He traced the path, called the function, and watched it tame the shouting letters.",
            need="He used the full path as a key to unlock the faraway function.",
            mapping="Using the full namespace.function path guarantees the REPL finds the right function, even if the name is common elsewhere.",
            resolution="the loud text became quiet, lowered through the full path's reach.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="fox-grapes",
    examples=[
        _ex("(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))", True,
            "whether two calls to the same function on the same argument yield equal results",
            "whether equality holds between both uppercase calls",
            goal="verify that calling a qualified function twice with the same input produces the same value",
            scenario="Vix the fox tested the toolshed's consistency. She called clojure.string/upper-case twice, each time on the quiet letter \"x\". Did the function obey the same rule both times, or was it fickle?",
            need="She needed proof that a function, when given the same input, would always return the same answer.",
            mapping="A pure function—one with no side effects—always returns the same value for the same input. Two calls to the same function on the same argument produce identical results.",
            resolution="equality held: the function was loyal to its rule, returning the same result both times.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="fox-grapes",
    examples=[
        _ex("(clojure.string/upper-case \"fox\")", "FOX",
            "reaching clojure.string/upper-case with a quiet text",
            "the transformed uppercase text",
            goal="use the full namespace path to reach and apply a text-transformation function",
            scenario="Renard discovered a fully-qualified signpost: clojure.string/upper-case. A whispered word hung beside it: \"fox\". He followed the path, invoked the function, and the whisper became a bold shout.",
            need="The full path let him navigate to the library function without confusion.",
            mapping="Fully-qualified names are namespace/function pairs that guide the REPL to the exact function. No ambiguity; no local aliases needed.",
            resolution="the whispered text became a shout, transformed through the qualified path.",
            tags=("story",)),
        _ex("(clojure.string/reverse \"grapes\")", "separg",
            "calling the reverse function on a harvest word",
            "the harvest word reversed",
            goal="access the reverse function via its full path and flip a string",
            scenario="Sly the fox found clojure.string/reverse etched in the toolshed. He fed it the harvest word \"grapes\". The function obediently turned the word backward, letter by letter.",
            need="The qualified path gave him access to a function that would mirror the harvest's name.",
            mapping="A fully-qualified name pinpoints the function in the library. The function then operates on its input according to its code.",
            resolution="the harvest word became its mirror image, reversed through the toolshed's library path.",
            tags=("story",)),
        _ex("(namespace :orchard/fox)", "orchard",
            "extracting the namespace part of a keyword with a slash",
            "the namespace portion as a string",
            goal="read the namespace portion of a slashed keyword",
            scenario="Vix marked a tasting-card with the keyword :orchard/fox and needed to extract just the left side—the namespace label \"orchard\". The namespace form split the slashed keyword cleanly.",
            need="She wanted the namespace address without the local name that followed the slash.",
            mapping="A slashed keyword has two parts: namespace and name. The namespace form extracts the left part as a string.",
            resolution="the namespace portion appeared on her card—\"orchard\"—separated from the name.",
            tags=("story",)),
        _ex("(name :orchard/fox)", "fox",
            "extracting the local name part of a slashed keyword", "the name portion as a string",
            goal="read the name portion of a slashed keyword",
            scenario="Renard held the same tasting-card :orchard/fox and extracted the right side—the local name \"fox\". The name form peeled away the namespace and left only the creature's identity.",
            need="He wanted the local name independent of its namespace prefix.",
            mapping="The name form extracts the right part of a slashed keyword as a string, leaving the namespace behind.",
            resolution="the local name emerged from the keyword—\"fox\"—isolated and ready to file.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="fox-grapes",
    examples=[
        _ex("(:private (meta '^:private x))", True,
            "the :private metadata flag attached to a symbol by the ^:private marker",
            "whether the :private flag is present and true",
            goal="detect whether a symbol has been marked private via its metadata",
            scenario="Renard inscribed the marker ^:private before a symbol x and pinned it to the arbor-post. Later, he opened the symbol's parchment—its metadata—and checked the :private field. The flag stood there, marked true.",
            need="He needed confirmation that the private mark had stuck to the symbol.",
            mapping="Metadata is a parchment tied to a symbol. The ^:private marker attaches a :private key to that parchment, setting it to true. Querying (:private (meta ...)) reads that key.",
            resolution="the :private field in the parchment glowed true, confirming the symbol was locked away.",
            tags=("story",)),
        _ex("(:private (meta 'x))", None,
            "querying the :private field from a symbol that has no private marker",
            "whether :private is present (returns nil if absent)",
            goal="check if a symbol lacks the private metadata flag",
            scenario="Sly spotted a bare symbol x on the vine-post—no ^:private marker, no veil. He opened its parchment to see if the :private field existed. The parchment had no such field; the query returned nil.",
            need="He needed to know that an unmarked symbol has no :private entry in its parchment.",
            mapping="When metadata lacks a key, querying that key returns nil. A symbol without the ^:private marker has no :private entry in its metadata.",
            resolution="the parchment yielded nothing for the :private key—the symbol was openly visible.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="fox-grapes",
    examples=[
        _ex("(boolean (:private (meta '^:private hidden)))", True,
            "coercing the :private metadata field to a boolean truth value",
            "whether :private coerces to true",
            goal="convert the :private metadata flag to an explicit boolean value",
            scenario="Vix examined a sealed symbol marked ^:private hidden. She opened its parchment and found the :private flag set. She coerced it to boolean—a definitive yes—and nodded. The symbol was truly hidden.",
            need="She wanted a clear boolean result—not just the presence of a field, but explicit truth.",
            mapping="The boolean form converts any value to true or false. A present, truthy metadata field becomes true; absence or nil becomes false.",
            resolution="the boolean conversion confirmed it—the hidden symbol was definitively private.",
            tags=("story",)),
        _ex("(boolean (:private (meta 'public)))", False,
            "coercing a missing :private field to a boolean value", "whether the result is false",
            goal="verify that an unmarked symbol yields false when the :private field is coerced",
            scenario="Renard inspected an open symbol public with no veil. He checked its parchment for :private and found nothing. Coercing that absence to boolean gave him false—a clear answer.",
            need="He needed a boolean guarantee that the symbol was not private.",
            mapping="When a metadata key is absent, querying it returns nil. Coercing nil to boolean yields false—a decisive negative.",
            resolution="the boolean false confirmed it—the symbol was publicly visible, no lock.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="fox-grapes",
    examples=[
        _ex("(clojure.string/upper-case \"a\")", "A",
            "applying the upper-case function to a single quiet letter",
            "the single letter in capitals",
            goal="use a library function to transform a tiny string",
            scenario="Sly the fox stood at the junction where dependency paths might cross. He called clojure.string/upper-case on a single, whispered letter \"a\". The path resolved cleanly, the function ran without tangles, and the letter became a bold shout.",
            need="Even in tangled namespaces, a single function call should work without circles.",
            mapping="When dependency paths are sound, a qualified function call succeeds without loops. The namespace resolver finds the path and executes it.",
            resolution="the letter answered the call and became uppercase—no circles, no delay.",
            tags=("story",)),
        _ex("(= 'a.b 'a.b)", True,
            "testing whether a namespace symbol is equal to itself",
            "whether the equality holds",
            goal="verify that a symbol written twice is identical even in circular-dependency scenarios",
            scenario="Renard watched the dependency paths tangle, but still he wrote the symbol 'a.b twice on the same slate. Even tangled, did the symbol remain itself?",
            need="He needed proof that symbol identity survived dependency complexity.",
            mapping="Symbol equality depends on content, not structure or dependencies. The same symbol written twice is identical, regardless of the namespace graph around it.",
            resolution="equality held true—the symbol was itself, undisturbed by any circular threat.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="fox-grapes",
    examples=[
        _ex("(do (def step1 1) (def step2 (+ step1 1)) step2)", 2,
            "executing three binding steps in sequence, where the second depends on the first",
            "the value of step2 after its definition",
            goal="post two sequential bindings where the second uses the first",
            scenario="Renard chalked a post step1 with tally 1, then a second post step2 that relied on the first. He submitted the three steps in order. Step2 inherited step1's value, added one, and yielded the result.",
            need="He needed step1 to persist before step2 could reference it.",
            mapping="The do form evaluates forms in order. Each def posts a binding; later forms can use earlier bindings. When step2 references step1, the post is already there.",
            resolution="step2 returned its value—step1 plus one—because step1 had been posted first.",
            tags=("story",)),
        _ex("(let [a 1 b (+ a 1)] (+ a b))", 3,
            "binding two values in a pouch where the second uses the first", "their sum",
            goal="tuck two sequential bindings in a pouch and sum them",
            scenario="Vix reached for her berry-pouch and tucked value 1 into slot a. Then she tucked into slot b the result of adding a's value—which was now in the pouch—to 1. Finally she added both pouch values together.",
            need="The pouch let her name interdependent values and use them in one expression.",
            mapping="The let form creates a pouch. Bindings are tucked sequentially; later ones can reference earlier ones. All pouch values are available in the body.",
            resolution="the pouch yielded the sum—a plus b, both values now available for the final calculation.",
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="fox-grapes",
    examples=[
        _ex("(:deps {:deps {:a 1 :b 2}})", {":a": 1, ":b": 2},
            "the :deps key from a small deps-map literal",
            "the value at :deps in {:deps {:a 1 :b 2}}"),
        _ex("(get-in {:paths [\"src\"]} [:paths 0])", "src",
            "the first :paths entry from a tiny deps-style map",
            "the string \"src\" at [:paths 0]"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="fox-grapes",
    examples=[
        _ex("(clojure.string/split \"src:test\" #\":\")", ["src", "test"],
            "splitting a colon-separated classpath-like string",
            "the vector [\"src\" \"test\"]"),
        _ex("(count [\"src\" \"test\" \"resources\"])", 3,
            "the number of entries in a classpath-like vector",
            "the count of three classpath entries"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="fox-grapes",
    examples=[
        _ex("(count ['orchard.fox 'orchard.grapes 'orchard.shared])", 3, 'the form', 'the value the form evaluates to'),
        _ex("(map name ['orchard.fox 'orchard.grapes])", ["orchard.fox", "orchard.grapes"], 'the form', 'the value the form evaluates to'),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="fox-grapes",
    examples=[
        _ex("(let [s clojure.string/upper-case] (s \"fox\"))", "FOX",
            "binding the function clojure.string/upper-case to a local s",
            "the value (s \"fox\") where s is upper-case"),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="fox-grapes",
    examples=[
        _ex("(symbol? 'java.util.Date)",
            True,
            'the predicate that asks if a foreign dotted name is a symbol',
            'whether a host-side dotted name is still a symbol locally',
            goal="ask whether a dotted name from the host's catalogue is a symbol",
            scenario="Renard the fox stood at the stone tool-shed at the orchard's edge. The tools carried foreign dotted names — borrowed tokens that the orchard still recognised as names.",
            need='Renard wanted to know whether the foreign-looking tool label was, in his own world, still a symbol — a name-token the runtime understood.',
            mapping="Foreign dotted names from the host's catalogue are still symbols in Clojure's reader. The symbol? predicate confirms the local kind: a name-token, regardless of where it points.",
            resolution='the predicate confirmed it — the dotted token was a symbol, even pointing across the boundary.',
            tags=("story",)),
        _ex("(name 'java.util.Date)", "java.util.Date", 'the form', 'the value the form evaluates to'),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="fox-grapes",
    examples=[
        _ex("(:doc (meta '^{:doc \"sour or sweet\"} orchard))",
            "sour or sweet",
            'the :doc slot of a metadata-tagged symbol',
            'the small lesson tied to the symbol via its :doc parchment',
            goal='read the :doc metadata attached to a symbol, where the docstring carries a small lesson',
            scenario="Vix the fox had pinned a parchment to the orchard fence with a docstring tied to a symbol. The parchment's :doc note carried a small lesson the symbol kept with it wherever it was filed.",
            need="She wanted to read off just the :doc note from the parchment's metadata — the symbol's posted lesson, not the symbol itself.",
            mapping='Metadata travels with a symbol like a parchment tied to the value. The meta form unpins the parchment; the :doc keyword reads the note labeled :doc. The symbol is the value; the parchment is the metadata; the keyword pulls the right field.',
            resolution="the parchment yielded its small lesson — the docstring Vix had tied to the symbol, read off cleanly without disturbing the symbol's own value.",
            tags=("story",)),
        _ex("(:author (meta '^{:author \"Aesop\"} orchard))", "Aesop",
            "the :author metadata on 'orchard",
            "the string \"Aesop\""),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="fox-grapes",
    examples=[
        _ex("(contains? #{'clojure.string} 'clojure.string)", True, 'the form', 'the value the form evaluates to'),
        _ex("(contains? #{'clojure.string} 'clojure.set)", False, 'the form', 'the value the form evaluates to'),
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
    print(f"grade-6 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
