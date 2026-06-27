"""Grade 11 — interop, crossing into other runtimes. Through dog-shadow.

Subplot lens: the tortoise crosses into a foreign land. JVM, JS, and
Python are different countries the racers visit; each has its own
customs (method-call syntax, static methods, type hints). The Hare
treats the foreign-language as just another sprint; the Tortoise is
careful to follow the local conventions.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _ACORN_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The two have travelled past their usual meadow into a foreign country
# whose REPL hosts another runtime. The Hare wants to barge ahead in
# his usual style; the Tortoise treats every interop call as a small
# act of diplomacy.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [

    SubplotTemplate("""\
{tortoise}, {emo_patient} and {hare_phrase} had wandered {place} into territory
where the REPL spoke to another runtime entirely. {tortoise} read the
sign and pointed at {concept_phrase}; the form to submit, written in
the foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not your meadow," {tortoise} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning." {hare_phrase}, {emo_proud}, said {hare_he_she} could read
the foreign form anyway. {tortoise} sketched {form_display} on the
ground; let the runtime, {tortoise_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form written on it — {form_display} — captured
{concept_phrase}. {hare}, {emo_tired} from running, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing."""),

    SubplotTemplate("""\
{hare} insisted the foreign-runtime forms were "just like home."
{tortoise_phrase}, {emo_patient} tapped a stone {place} where someone had inscribed
{concept_phrase}. "Then write {form_display} into the REPL," {tortoise}
said, "and we'll see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {tortoise}, {emo_patient} knelt and placed the form
{form_display} on the stone. {hare}, watching, agreed to be the one
to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {tortoise}, {emo_patient}
copied {form_display} from the page, and {hare_phrase}
agreed (for once) that one should always check the REPL before
trusting a translation."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G11 = _PLAN_POOL + (
    "I write the interop form using the host's convention.",
    "I use the dot or slash form for the host method, then submit.",
    "I express the host call as a Clojure form for the REPL.",
)


# ─────────────────────── 14 grade-11 subjects ───────────────────────


# G11-01 — JVM vs CLR vs JS vs Python (overview)
G11_01 = SubjectCurriculum(
    grade=11, subject_id="G11-01",
    subject_title="JVM vs CLR vs JS vs Python (host overview)",
    fable="dog-shadow",
    examples=[
        # Overview subject — narrative does the educational work.
        _ex('(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)',
            ":studied",
            "understanding host runtimes",
            "the marker value when the host overview has been studied",
            goal="understand that Clojure runs on multiple hosts"),
        _ex('(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)',
            ":hosts",
            "the host runtime variants",
            "the marker keyword for the host family",
            goal="name the Clojure implementations for different hosts"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-02 — Method call syntax
G11_02 = SubjectCurriculum(
    grade=11, subject_id="G11-02",
    subject_title="Method call syntax",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(.toUpperCase "abc")',
            expected="ABC",
            concept_phrase='the host method toUpperCase',
            question_what="the capitalized result the host's toUpperCase returns on the three-letter string abc",
            goal_text="call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention",
            scenario=(
                'Rex the hound visited the kennel-master\'s shed near the '
                'stream and found a peculiar tool for transforming text — a '
                'capitalizer that worked on the foreign host. "This tool '
                'belongs to the other world," Rex said, holding the device '
                'carefully.'
            ),
            need=(
                'He had three letters — abc — and needed to learn the '
                'kennel-master\'s calling convention: how to ask the tool to '
                'transform them into their uppercase form.'
            ),
            mapping=(
                'The tool itself is the host method, the three letters are '
                'the argument passed to the tool, and the dot-prefix form is '
                'how the hound speaks to the foreign device from Clojure\'s '
                'side.'
            ),
            resolution=(
                'The REPL called the host\'s toUpperCase by its dot name, '
                'passing the string abc. The foreign method returned the '
                'transformed result, and Rex saw the kennel-master\'s tools '
                'could be trusted to do their work faithfully.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(.startsWith "hare-tortoise" "hare")',
            expected=True,
            concept_phrase="the host method startsWith checking a string prefix",
            question_what="whether the string hare-tortoise starts with the prefix hare via the host method startsWith",
            goal_text="call the host method startsWith on a string to check for a prefix",
            scenario=(
                'Bell the hound came upon a scroll carved in the host language '
                'near the pond, marked with the text "hare-tortoise." She needed '
                'to know whether it began with a familiar name.'
            ),
            need=(
                'The kennel-master\'s tool for checking prefixes was the only '
                'way to answer truly. She would need to learn how to call it '
                'correctly — using the dot convention on the string she '
                'possessed.'
            ),
            mapping=(
                'The string "hare-tortoise" is the text to examine, "hare" is '
                'the prefix sought, and the host method startsWith is the tool '
                'that does the checking. The dot-prefix form bridges between '
                'Clojure and the foreign method.'
            ),
            resolution=(
                'The REPL invoked the host\'s startsWith, passing both the text '
                'and the prefix. The method returned the verdict, confirming that the '
                'scroll\'s beginning matched what Bell sought. The crossing into '
                'the host\'s territory had yielded the hare.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(. "abc" toUpperCase)',
            expected="ABC",
            concept_phrase='the alternate dot form for a host method',
            question_what="the uppercase form of the string abc produced by the host method toUpperCase via the alternate dot syntax",
            goal_text="call the host method toUpperCase using the alternate dot form",
            scenario=(
                'Patch discovered the shed offered two ways to call tools: the '
                'dot-prefix form and an alternate arrangement.'
            ),
            need=(
                'Patch needed to call toUpperCase using the alternate syntax: '
                'dot first, then the string, then method name.'
            ),
            mapping=(
                'The string "abc" needs transformation, the alternate dot form '
                'is a different arrangement that says the same thing.'
            ),
            resolution=(
                'The REPL understood the alternate syntax. Both forms were '
                'faithful paths — abc.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-03 — Static method call
G11_03 = SubjectCurriculum(
    grade=11, subject_id="G11-03",
    subject_title="Static method call",
    fable="dog-shadow",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        SubjectExample(
            form="(Math/abs -7)",
            expected=7,
            concept_phrase="the static host method Math/abs",
            question_what="the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation",
            goal_text="call the static host method Math/abs with the argument -7",
            scenario=(
                'Rex the hound padded into the kennel-master\'s shed near the '
                'forest and found the Math class — a tool-cabinet shared by all '
                'the dogs, not belonging to any single one. "These are the '
                'standard tools," Rex said, running a paw along the labels.'
            ),
            need=(
                'He held a number marked with a backward sign: -7. He needed '
                'the shed\'s absolute-distance tool to tell him the true '
                'measure, removing the sign and leaving only the magnitude.'
            ),
            mapping=(
                'The Math cabinet is the static source, abs is its tool for '
                'absolute distance, -7 is the number to measure, and the slash '
                'notation Math/abs is how Clojure names a tool from a shared '
                'cabinet.'
            ),
            resolution=(
                'The REPL called Math/abs with the negative number. The static '
                'method computed and returned the absolute value as the true '
                'measure. Rex learned that slash-notation opened the standard '
                'tools when the dot would not fit — -7.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(Math/max 3 9)",
            expected=9,
            concept_phrase="the static host method Math/max",
            question_what="the maximum value of the integers 3 and 9 produced by calling the static host method Math/max via slash notation",
            goal_text="call the static host method Math/max to find the larger of two numbers",
            scenario=(
                'Bell the hound stood at the stream\'s edge with two bones '
                'before her — one marked 3, one marked 9 — and needed to '
                'know which was the prize. The kennel-master\'s shed held '
                'a tool for such comparisons.'
            ),
            need=(
                'Using the Math cabinet\'s max tool, Bell could ask which of '
                'the two bones was larger without guessing. The slash notation '
                'would speak the foreign language correctly.'
            ),
            mapping=(
                'The two numbers 3 and 9 are the bones to compare, Math/max is '
                'the static tool for finding the greater value, and the result '
                'the tool returns is the larger of the pair.'
            ),
            resolution=(
                'The REPL called the static method Math/max, passing both '
                'numbers. The method evaluated and returned 9 — the true maximum. '
                'Bell had learned another path through the kennel-master\'s shed — 9.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-04 — Field access
G11_04 = SubjectCurriculum(
    grade=11, subject_id="G11-04",
    subject_title="Field access",
    fable="dog-shadow",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        SubjectExample(
            form='(count "tortoise")',
            expected=8,
            concept_phrase='the count of a sequence',
            question_what='the number of characters in the string tortoise via the count function',
            goal_text="count the characters in a string",
            scenario=(
                'Patch the hound came to the stream with a carved message: the '
                'word "tortoise" scratched onto bark. To pass the ford, Patch '
                'needed to know the exact number of marks in the message.'
            ),
            need=(
                'Clojure\'s count function could reach into the host\'s string '
                'and measure its length. The hound would apply the function to '
                'find the true measure without counting by paw.'
            ),
            mapping=(
                'The string "tortoise" is the sequence to measure, the count '
                'function is the tool for finding its length, and the number '
                'returned is the precise tally of characters.'
            ),
            resolution=(
                'The REPL applied count to the string and returned the exact '
                'number of marks. Patch now knew the measure and could cross, '
                'confident in the reckoning — tortoise.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hare")',
            expected=4,
            concept_phrase='the count of a sequence',
            question_what='the number of characters in the string hare via the count function',
            goal_text="count the characters in another string",
            scenario=(
                'Bell the hound found a shorter message by the bank — the word '
                '"hare" marked on a stone — and needed to know its length. The '
                'same Clojure tool that had helped before would serve again.'
            ),
            need=(
                'She would use the count function to measure this message just '
                'as Patch had measured the longer one. The tool works the same '
                'way whether the text is long or brief.'
            ),
            mapping=(
                'The string "hare" is the new sequence to measure, the count '
                'function is the reliable tool, and what it returns is the '
                'tally of marks in the shorter word.'
            ),
            resolution=(
                'The REPL applied count and returned the number. Bell confirmed '
                'that the shorter message held four marks, and the count '
                'function proved itself consistent across both texts — hare.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="dog-shadow",
    examples=[
        # Overview-ish: the form is what one would write at the top of a file.
        _ex('(do "(:import (java.util Date)) imports a host class" :imported)',
            ":imported",
            "importing a host class",
            "the marker for the import-form lesson",
            goal="understand how to import a host class into a namespace"),
        _ex('(do "import is a top-of-file ns clause" :studied)',
            ":studied",
            "import as a namespace clause",
            "the marker for studying import",
            goal="understand where import forms go in a file"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-06 — new and dot-construct
G11_06 = SubjectCurriculum(
    grade=11, subject_id="G11-06",
    subject_title="new and dot-construct",
    fable="dog-shadow",
    examples=[
        # Construct a host class via Class. or (new Class). String. is
        # portable across JVM and basilisp.
        SubjectExample(
            form='(String. "go")',
            expected="go",
            concept_phrase='constructing a String via the dot-construct form',
            question_what='the newly constructed String object created from a text argument via the dot-construct syntax',
            goal_text="construct a host String object with the dot-construct syntax",
            scenario=(
                'Rex the hound entered the kennel-master\'s shed near the meadow '
                'and found a String tool — a factory for building new text objects. '
                '"I can make fresh strings," Rex said, "by speaking to the tool '
                'with the right form."'
            ),
            need=(
                'He needed to call the String constructor using the dot-construct '
                'form, passing the text "go" as an instruction for the new string '
                'to carry.'
            ),
            mapping=(
                'The String class is the tool-factory, the dot after its name '
                'is Clojure\'s way of speaking to a constructor, and the text '
                '"go" is the seed for the newly created string.'
            ),
            resolution=(
                'The REPL invoked the String constructor via dot-construct. It '
                'built a new String object holding the text and returned it. Rex '
                'learned that constructors could be called this way in the '
                'foreign land — go.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(new String "jump")',
            expected="jump",
            concept_phrase='constructing a String via the new form',
            question_what='the newly constructed String object created from a text argument via the new keyword',
            goal_text="construct a host String object using the new keyword",
            scenario=(
                'Bell the hound discovered another path through the same String '
                'factory. The "new" keyword was an older, more formal way to '
                'speak to a constructor — still honored in the foreign language.'
            ),
            need=(
                'To prove both forms worked, Bell called String using the new '
                'keyword form, passing the text "jump" as the seed for a fresh '
                'string object.'
            ),
            mapping=(
                'The new keyword is the formal constructor-call ceremony, String '
                'is the class being built, and "jump" is the text the new string '
                'will carry from its creation.'
            ),
            resolution=(
                'The REPL understood the new keyword form just as readily. It '
                'created a String object and returned it. Bell saw that both '
                'the dot-construct and the new keyword were paths to the same '
                'outcome — jump.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-07 — Arrays
G11_07 = SubjectCurriculum(
    grade=11, subject_id="G11-07",
    subject_title="Arrays",
    fable="dog-shadow",
    examples=[
        # int-array / aget are the canonical interop calls.
        SubjectExample(
            form="(let [a (int-array [10 20 30])] (aget a 1))",
            expected=20,
            concept_phrase="indexing into a host array",
            question_what="the element at index 1 of the int-array [10 20 30] via the aget function",
            goal_text="access an element in a host array by index",
            scenario=(
                'Patch the hound found a numbered row of bones in the kennel-master\'s '
                'shed — a host array holding three weights: 10, 20, and 30. "Arrays '
                'are like bone-rows," Patch said, "each bone in its place."'
            ),
            need=(
                'To reach the second bone in the row, Patch needed to use the aget '
                'function, which knows how to index into arrays the foreign way. '
                'The position numbered 1 would find the second bone.'
            ),
            mapping=(
                'The int-array is the host\'s ordered bone-row, the index 1 is '
                'the position to reach, and aget is the function that crosses '
                'the boundary to fetch from the foreign array.'
            ),
            resolution=(
                'The REPL applied aget to the array, asking for the element at '
                'position 1. It returned the second bone\'s weight: 20. Patch '
                'learned how to reach into host arrays by their numbered positions — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a (int-array [1 2 3])] (alength a))",
            expected=3,
            concept_phrase="getting the length of a host array",
            question_what="the length of the int-array [1 2 3] via the alength function",
            goal_text="get the length of a host array",
            scenario=(
                'Rex the hound came to the stream with a smaller array from the '
                'kennel-master\'s shed — three bones lined up: 1, 2, and 3. He '
                'needed to know the exact count of bones in the row.'
            ),
            need=(
                'The alength function would measure any host array without guessing. '
                'It reaches into the foreign structure and returns the precise tally '
                'of how many positions the array holds.'
            ),
            mapping=(
                'The int-array [1 2 3] is the bone-row to measure, alength is the '
                'function that fetches the array\'s length from the host side, and '
                'the result is the true count of positions.'
            ),
            resolution=(
                'The REPL called alength and returned the exact count: 3. Rex '
                'confirmed that the array held three positions, and alength proved '
                'itself a trustworthy path into host array properties — 3.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-08 — Type hints
G11_08 = SubjectCurriculum(
    grade=11, subject_id="G11-08",
    subject_title="Type hints",
    fable="dog-shadow",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        SubjectExample(
            form='(let [^String s "abc"] (.toUpperCase s))',
            expected="ABC",
            concept_phrase="using a type hint in a binding",
            question_what="the uppercase form of the type-hinted string abc produced by calling the host method toUpperCase on the binding",
            goal_text="add a type hint to a binding and call a method on the typed value",
            scenario=(
                'Bell held a text string "abc" and wanted to give the compiler a '
                'hint about what kind of value she was holding.'
            ),
            need=(
                'Type hints like scratching a mark to say: this is a String. The '
                'caret and type name help the compiler choose the right path.'
            ),
            mapping=(
                'The caret (^) marks the hint, String is the type, s is the binding, '
                'and the hint guides how the runtime calls the method.'
            ),
            resolution=(
                'The REPL read the hint. When it called .toUpperCase, it took the '
                'direct path. The method returned the capitalized text — abc.'
            ),
            tags=("story",),
        ),
        _ex('(do "type hints are metadata that guide compilation" :studied)',
            ":studied",
            "the purpose of type hints in Clojure",
            "the marker keyword for the type-hint lesson",
            goal="understand that type hints guide compilation"),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="dog-shadow",
    examples=[
        # Plain arithmetic works the same way for ordinary values; the
        # checked/unchecked distinction is about overflow at the host
        # primitive level. Use a value-space form for the eval, narrate
        # the distinction.
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="basic addition under the default checked math regime",
            question_what="the sum of two numbers",
            goal_text="add two numbers with the default math behavior",
            scenario=(
                'Patch the hound arranged two small bone-piles on a flat stone by '
                'the pond: one holding a single bone, the other holding two. "I '
                'will combine these," Patch said carefully.'
            ),
            need=(
                'The addition would be checked by default — the runtime watching '
                'for overflow, protecting the count against mistakes. This was the '
                'safe way: careful arithmetic that catches errors.'
            ),
            mapping=(
                'The two piles of bones are the addends (1 and 2), the plus sign '
                'is the combination rule, and the sum is the running total the '
                'runtime computes with care.'
            ),
            resolution=(
                'The REPL applied the addition with its watchful gaze. It returned '
                'the sum: 3 bones. Patch learned that ordinary arithmetic in Clojure '
                'runs in checked mode by default, guarding against silent overflow — 2.'
            ),
            tags=("story",),
        ),
        _ex('(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            ":studied",
            "overflow checking in Clojure arithmetic",
            "the marker for the checked/unchecked lesson",
            goal="understand how to disable overflow checking"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="dog-shadow",
    examples=[
        _ex('(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)',
            ":studied",
            "the ClojureScript compilation process",
            "the marker for studying the cljs host",
            goal="understand how ClojureScript compiles to JavaScript"),
        _ex('(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)',
            ":cljs",
            "where ClojureScript runs",
            "the marker for the cljs-runtime lesson",
            goal="learn where ClojureScript executes"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-11 — cljs-js interop
G11_11 = SubjectCurriculum(
    grade=11, subject_id="G11-11",
    subject_title="cljs / JavaScript interop",
    fable="dog-shadow",
    examples=[
        _ex('(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)',
            ":studied",
            "ClojureScript to JavaScript interop",
            "the marker for the cljs-js interop lesson",
            goal="understand how ClojureScript calls JavaScript globals and reads fields"),
        _ex('(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)',
            ":cljs-interop",
            "ClojureScript interop conventions",
            "the marker keyword for the conventions",
            goal="learn the conventions for ClojureScript-JavaScript interop"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-12 — Basilisp overview (the Python host — this project!)
G11_12 = SubjectCurriculum(
    grade=11, subject_id="G11-12",
    subject_title="Basilisp overview (Python host)",
    fable="dog-shadow",
    examples=[
        _ex('(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)',
            ":studied",
            "the basilisp implementation",
            "the marker for studying basilisp",
            goal="understand that basilisp is Clojure on Python"),
        _ex('(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)',
            ":basilisp",
            "basilisp Python interop",
            "the marker keyword for basilisp interop",
            goal="learn how basilisp calls Python code"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-13 — Cross-platform .cljc and reader-conditionals
G11_13 = SubjectCurriculum(
    grade=11, subject_id="G11-13",
    subject_title="Cross-platform .cljc and reader-conditionals",
    fable="dog-shadow",
    examples=[
        _ex('(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)',
            ":studied",
            "selecting code by host at read time",
            "the marker for the reader-conditional lesson",
            goal="learn how reader-conditionals choose code per host"),
        _ex('(do ".cljc files share code across multiple hosts" :cljc)',
            ":cljc",
            "files that work on multiple Clojure hosts",
            "the marker keyword for the .cljc lesson",
            goal="understand the role of .cljc files"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-14 — Debugging host leaks
G11_14 = SubjectCurriculum(
    grade=11, subject_id="G11-14",
    subject_title="Debugging host leaks",
    fable="dog-shadow",
    examples=[
        _ex('(do "host stack traces leak through interop; learn to read them" :studied)',
            ":studied",
            "debugging host-runtime errors",
            "the marker for the host-leaks lesson",
            goal="learn to read and debug host runtime errors"),
        SubjectExample(
            form='(try (Math/sqrt 4) (catch Exception _ :err))',
            expected=2.0,
            concept_phrase="catching exceptions from a host method call",
            question_what="the square root of 4 produced by the static host method Math/sqrt via slash notation when the call succeeds",
            goal_text="wrap a static host method call in error handling",
            scenario=(
                'Rex crossed into the kennel-master\'s shed to use Math/sqrt on 4. '
                'The boundary was fragile — an error could leak through.'
            ),
            need=(
                'He needed a safe wrapper to catch any exceptions the foreign tool '
                'might throw. The try form was his safety net.'
            ),
            mapping=(
                'The try begins the crossing, Math/sqrt is the host tool, the '
                'argument 4 is the value, and catch is the safety net.'
            ),
            resolution=(
                'The REPL tested the boundary and called Math/sqrt safely. It '
                'returned the result.0. The try form caught nothing because nothing went wrong — err.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G11_01, G11_02, G11_03, G11_04, G11_05, G11_06, G11_07,
    G11_08, G11_09, G11_10, G11_11, G11_12, G11_13, G11_14,
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
    print(f"grade-11 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
