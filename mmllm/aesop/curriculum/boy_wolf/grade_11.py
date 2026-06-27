"""Grade 11 — interop, crossing into other runtimes. Through boy-who-cried-wolf.

Subplot lens: the village trades with neighbouring villages whose REPLs
speak different host runtimes. Past the river the syntax changes; the
elder reads the foreign-shaped form carefully — what works in our
village's REPL may break in theirs. The shepherd treats every foreign
call like a sprint and shouts answers without checking; the elder is
careful at every border.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _ACORN_SUBPLOTS, _GOAL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The village trades with neighbouring villages whose REPLs speak
# different host runtimes. The shepherd treats every foreign call like
# a sprint; the elder is careful at every border.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{elder_phrase} and {shepherd_phrase} had wandered {place} into territory
where the REPL spoke to another runtime entirely. {elder} read the
sign and pointed at {concept_phrase}; the form to submit, written in
the foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not our meadow," {elder_phrase} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning." {shepherd_phrase}, {emo_proud}, said {shepherd_he_she}
could read the foreign form anyway. {elder} sketched {form_display}
on the ground; let the runtime, {elder_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form written on it — {form_display} — captured
{concept_phrase}. {shepherd}, {emo_tired}, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing."""),

    SubplotTemplate("""\
{shepherd_phrase} insisted the foreign-runtime forms were "just like
home." {elder_phrase} tapped a stone {place} where someone had
inscribed {concept_phrase}. "Then write {form_display} into the REPL,"
{elder} said, "and we'll see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {elder_phrase} knelt and placed the form
{form_display} on the stone. {shepherd}, watching, agreed to be the
one to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {elder_phrase} copied
the form {form_display} from the page, and {shepherd_phrase} agreed
that, on this side of the river, one should always check the REPL
before trusting a translation."""),
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
    fable="boy-wolf",
    examples=[
        # Overview subject — narrative does the educational work.
        _ex('(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)',
            ":studied",
            "the idea that Clojure has multiple host runtimes",
            "the marker value when the host overview has been studied"),
        _ex('(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)',
            ":hosts",
            "the family of Clojure host runtimes",
            "the marker keyword for the host family"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-02 — Method call syntax
G11_02 = SubjectCurriculum(
    grade=11, subject_id="G11-02",
    subject_title="Method call syntax",
    fable="boy-wolf",
    examples=[
        _ex('(.toUpperCase "abc")', "ABC",
            'the method call (.toUpperCase "abc")',
            "the uppercased string returned by the method"),
        _ex('(.startsWith "shepherd-elder" "shepherd")', True,
            "a method call (.startsWith ...) returning a boolean",
            "whether the string starts with the prefix"),
        _ex('(. "abc" toUpperCase)', "ABC",
            'the alternate dot form (. obj method)',
            "the uppercased result via the longer dot syntax"),
        _ex('(.toUpperCase "abc")', "ABC",
            'the method call (.toUpperCase "abc")',
            "the uppercased string returned by the method",
            scenario=(
                "Tom stood at the boundary between the watchhouse and the foreign smithy, "
                "studying the tools on the wall. Each tool had a name written in the smith's own language. "
                "On one shelf sat a method labeled 'toUpperCase,' attached to an object of type String."
            ),
            need=(
                "Tom wanted to call the foreign method on a string, following the smith's conventions "
                "for how to use it. The notation looked strange—a dot joining the object to the method name."
            ),
            mapping=(
                "The dot-prefix syntax `(.method object)` borrows the foreign tool directly: "
                "the runtime passes the object to the method and returns what the method computes. "
                "Tom would write the form exactly as the smith had labeled the tool, and the REPL would do the work."
            ),
            resolution=(
                "Tom composed the form, submitted it to the REPL, and watched as the smith's tool worked cleanly. The uppercased string came back, and Tom understood that crossing the boundary simply meant using the host's own calling convention (with `abc` as the input value)."
            )),
        _ex('(.startsWith "shepherd-elder" "shepherd")', True,
            "a method call (.startsWith ...) returning a boolean",
            "whether the string starts with the prefix",
            scenario=(
                "Carol led Tom to the smithy's reference shelf, where the methods were catalogued by their names. "
                "One method—'startsWith'—promised to test whether a string began with a given prefix."
            ),
            need=(
                "Tom wanted to ask the foreign method a question: did the word 'shepherd-elder' begin with 'shepherd'? "
                "The question was simple, but the answer had to come from the smith's tool, not from guessing."
            ),
            mapping=(
                "The method call `(.startsWith object prefix)` sends the prefix to the host method and receives "
                "a boolean result. The runtime bridges the value across, and the host method answers truthfully."
            ),
            resolution=(
                'Carol composed the form with both arguments in place, submitted it, and the REPL returned the verdict—the word indeed started with the prefix. Tom saw that host methods could answer yes-or-no questions just as reliably as any village computation.'
            )),
        _ex('(. "abc" toUpperCase)', "ABC",
            'the alternate dot form (. obj method)',
            "the uppercased result via the longer dot syntax",
            scenario=(
                "Tom noticed a second way to write the same kind of tool-call, using the same dot but with "
                "the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form."
            ),
            need=(
                "Tom wanted to understand whether this longer form and the shorter one were the same tool, "
                "called two different ways. Did the calling convention matter, or would both work?"
            ),
            mapping=(
                "Both forms work. The shorter `(.method object ...)` is convenient and idiomatic. "
                "The longer `(. object method ...)` is explicit and clear. The runtime treats them identically, "
                "passing the object to the host method either way."
            ),
            resolution=(
                "Tom wrote both forms, one after the other, and both returned 'ABC'. Carol smiled: different ways to call the same foreign tool, both honest to the REPL (with `abc` as the input value)."
            )),
        _ex('(.length "shepherd")', 8,
            "the method call (.length ...) on a string",
            "the length of the string via the method",
            scenario=(
                "Tom walked deeper into the smithy's catalog and found a method called 'length' "
                "that measured how many characters a string held. The method was simple and direct."
            ),
            need=(
                "Tom wanted to count the letters in the word 'shepherd' without doing it by hand. "
                "The host had a tool for this work—why not use it?"
            ),
            mapping=(
                "The method `(.length string)` sends the string to the host and receives back "
                "the count of characters. The host counts from the inside; the REPL trusts what it returns."
            ),
            resolution=(
                "Tom composed the form, the REPL called the foreign method, and the answer came back: 8. 'Shepherd' has 8 letters. The host counted faithfully, just as the watchhouse would have."
            )),
        _ex('(.isEmpty "test")', False,
            "the method call (.isEmpty ...) checking if a string is empty",
            "whether the string is empty",
            scenario=(
                "Carol took Tom to the deepest shelf in the smithy and showed him one last method: 'isEmpty'. "
                "It tested whether a string had no characters."
            ),
            need=(
                "Tom wanted to know if a string held any letters at all. The host had a method that answered this question directly."
            ),
            mapping=(
                "The method `(.isEmpty string)` sends the string to the host and receives back a boolean. "
                "The host checks if the string has zero length and returns true or false."
            ),
            resolution=(
                "Tom composed the form on the word 'test', and the host returned the verdict. The string was not empty. Tom had now crossed the boundary with dot-prefix syntax, instance methods, method chaining, and boolean returns. The smithy's tools were his to use."
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-03 — Static method call
G11_03 = SubjectCurriculum(
    grade=11, subject_id="G11-03",
    subject_title="Static method call",
    fable="boy-wolf",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        _ex("(Math/abs -7)", 7,
            "the static call (Math/abs -7)",
            "the absolute value of -7 via the static method"),
        _ex("(Math/max 3 9)", 9,
            "the static call (Math/max 3 9)",
            "the larger of 3 and 9 via the static method"),
        _ex("(Math/abs -7)", 7,
            "the static call (Math/abs -7)",
            "the absolute value of -7 via the static method",
            scenario=(
                "In the smithy's common room sat a large cabinet labeled 'Math'—not a person, but a collection "
                "of static methods that belonged to no single object. Tom studied the label 'abs' inside."
            ),
            need=(
                "Tom had a negative number and wanted its distance from zero. The Math cabinet had a tool for this, "
                "but it didn't belong to a string or array—it was a shared village utility."
            ),
            mapping=(
                "The slash notation `(Math/abs value)` calls a static method. Instead of passing the object first, "
                "the method lives in a namespace-like cabinet. The runtime looks up the tool by its full name and applies it."
            ),
            resolution=(
                'Tom composed the form, and the static method returned 7. The negative sign disappeared, and he understood that the slash-form reaches into the shared toolshed, not into a particular object (with `-7` as the input value).'
            )),
        _ex("(Math/max 3 9)", 9,
            "the static call (Math/max 3 9)",
            "the larger of 3 and 9 via the static method",
            scenario=(
                "Carol showed Tom another tool in the Math cabinet: 'max', which took two numbers and returned the larger one. "
                "Again, the tool belonged to the cabinet itself, not to any object."
            ),
            need=(
                "Tom wanted to compare 3 and 9 and find which was larger. He could guess, but why not let "
                "the host's tool decide?"
            ),
            mapping=(
                "The static method `(Math/max a b)` accepts multiple arguments in sequence. "
                "The runtime passes both values to the host method, which compares them and returns the maximum."
            ),
            resolution=(
                "The form returned 9. Tom realized that static methods worked just like instance methods, except the first 'object' was replaced by the namespace-like cabinet name."
            )),
        _ex("(Math/min 5 2)", 2,
            "the static call (Math/min 5 2)",
            "the smaller of 5 and 2 via the static method",
            scenario=(
                "Beside the 'max' tool hung 'min', its counterpart, ready to return the smaller of two numbers. "
                "Tom saw a pattern forming."
            ),
            need=(
                "Tom wanted to find the minimum of 5 and 2 without hand-counting. The host had the tool; "
                "he just needed to reach it correctly."
            ),
            mapping=(
                "The form `(Math/min a b)` follows the same slash-notation as 'max'. The REPL looks up the static method "
                "in the Math namespace and applies it to both arguments."
            ),
            resolution=(
                'The REPL returned the result. Tom submitted another form, and the host answered cleanly. The pattern held: static methods, called by namespace name, worked as well as any other tool.'
            )),
        _ex("(Math/sqrt 16)", 4.0,
            "the static call (Math/sqrt 16)",
            "the square root of 16 via the static method",
            scenario=(
                "Deep in the Math cabinet lay a more complex tool: 'sqrt', which found the square root of a number. "
                "Tom had never seen the host compute something so intricate."
            ),
            need=(
                "Tom wanted to find the square root of 16. The village didn't have a tool for this work, "
                "but the host's Math cabinet did."
            ),
            mapping=(
                "The form `(Math/sqrt value)` sends a single argument to the host's static method. "
                "The host computes the square root and returns the floating-point result."
            ),
            resolution=(
                'The REPL returned the result.0. Tom saw that even complex operations could be borrowed from the host, as long as he used the right slash-form to reach the static method inside its cabinet.'
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-04 — Field access
G11_04 = SubjectCurriculum(
    grade=11, subject_id="G11-04",
    subject_title="Field access",
    fable="boy-wolf",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        _ex('(count "shepherd")', 8,
            'the count of "shepherd"',
            'the length of "shepherd"'),
        _ex('(count "flock")', 5,
            'the count of "flock"',
            'the length of "flock"'),
        _ex('(count "shepherd")', 8,
            'the count of "shepherd"',
            'the length of "shepherd"',
            scenario=(
                "Tom found that the townsfolk's count function worked on host strings."
            ),
            need=(
                "He wanted to count letters using the village tool rather than a host method."
            ),
            mapping=(
                "The village's count function reaches into host data and counts the elements."
            ),
            resolution=(
                'The form returned the character count and Tom understood the boundary was permeable. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex('(count "flock")', 5,
            'the count of "flock"',
            'the length of "flock"',
            scenario=(
                "Carol showed Tom that the same 'count' function worked on any string the host provided. "
                "The function was general—it didn't care where the string came from."
            ),
            need=(
                "Tom wanted to count 'flock' using the meadow folk's count function, just to be sure the pattern held. "
                "Did it work the same way?"
            ),
            mapping=(
                "The form `(count string)` works on any sequence, including host strings. "
                "The village function is polymorphic; it knows how to count across the host boundary."
            ),
            resolution=(
                "The answer came back: 5. Tom submitted it and got the right answer. He saw that the townsfolk's tools could reach into the host's world cleanly, without special syntax. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."
            )),
        _ex('(count "wolf")', 4,
            'the count of "wolf"',
            'the length of "wolf"',
            scenario=(
                "Tom played with more examples, counting different strings. Each time, the valley's count function "
                "reached into the host representation and returned the right answer."
            ),
            need=(
                "Tom wanted to convince himself that the village function would work on 'wolf' too. "
                "He needed to see the pattern hold one more time."
            ),
            mapping=(
                "The form `(count \"wolf\")` applies the watchhouse's count function to the host string. "
                "The REPL bridges the boundary transparently."
            ),
            resolution=(
                "The REPL returned 4. Tom had now called count on three different strings and gotten three correct answers. He understood that the meadow folk's tools had been designed to work across the host boundary all along. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
        _ex('(count "elder")', 5,
            'the count of "elder"',
            'the length of "elder"',
            scenario=(
                "Carol and Tom sat by the watchhouse, counting strings together. Tom was getting comfortable "
                "with the idea that the townsfolk's tools just worked with host data."
            ),
            need=(
                "Tom wanted to count 'elder'—the wise one from the fable. "
                "One more time, he'd use the village's count function, and one more time it would answer true."
            ),
            mapping=(
                "The form `(count \"elder\")` sends the string to the meadow folk's count function. "
                "The function is general enough to handle any sequence the host provides."
            ),
            resolution=(
                "The answer was 5. Tom had now moved past the fear of the boundary. The village's tools and the host's data spoke to each other smoothly, and the REPL made the translation happen without fuss. Tom chalked {drawn.a} on the valley notice, and the morning record stood for the next shepherd to read."
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="boy-wolf",
    examples=[
        # Overview-ish: the form is what one would write at the top of a file.
        _ex('(do "(:import (java.util Date)) imports a host class" :imported)',
            ":imported",
            "the (:import ...) ns clause for host classes",
            "the marker for the import-form lesson"),
        _ex('(do "import is a top-of-file ns clause" :studied)',
            ":studied",
            "the role of import in a Clojure file",
            "the marker for studying import"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-06 — new and dot-construct
G11_06 = SubjectCurriculum(
    grade=11, subject_id="G11-06",
    subject_title="new and dot-construct",
    fable="boy-wolf",
    examples=[
        # Construct a host class via Class. or (new Class). String. is
        # portable across JVM and basilisp.
        _ex('(String. "hello")', "hello",
            'the constructor call (String. "hello")',
            'the string built by the dot-construct'),
        _ex('(new String "world")', "world",
            'the (new String "world") form',
            'the string built by (new ...)'),
        _ex('(String. "hello")', "hello",
            'the constructor call (String. "hello")',
            'the string built by the dot-construct',
            scenario=(
                "Tom walked past the smithy's forge and saw a tool labeled 'String.'—a constructor, the smith said, "
                "that built new String objects from raw data."
            ),
            need=(
                "Tom wanted to build a new String from the word 'hello'. The host had a constructor for this work, "
                "and Tom wanted to call it using the valley's notation."
            ),
            mapping=(
                "The dot-construct `(String. value)` calls the host's String constructor. "
                "The dot at the end of the class name signals that this is a constructor call. The REPL passes the value "
                "to the host, which builds and returns the new String object."
            ),
            resolution=(
                "The form built 'hello' and handed it back. Tom saw that constructors, too, could be borrowed from the host using the dot-construct notation."
            )),
        _ex('(new String "world")', "world",
            'the (new String "world") form',
            'the string built by (new ...)',
            scenario=(
                "Carol showed Tom a second way to call the same constructor: using the 'new' form, "
                "which was more explicit but meant the same thing."
            ),
            need=(
                "Tom wanted to build 'world' and wanted to know whether this longer form was equivalent to the dot-construct. "
                "Did both ways work?"
            ),
            mapping=(
                "Both forms work. The dot-construct `(String. value)` is idiomatic and concise. "
                "The longer form `(new String value)` is explicit about calling a constructor. The REPL treats them identically, "
                "passing the value to the host constructor either way."
            ),
            resolution=(
                "Both forms built 'world' cleanly. Tom understood that the dot-construct and the 'new' form were two ways to cross the same boundary into the host's constructor."
            )),
        _ex('(String. "village")', "village",
            'the constructor call (String. "village")',
            'the string built by the dot-construct',
            scenario=(
                "Tom practiced building strings with different inputs. Each time, the dot-construct reached into the host "
                "and built a new String from the raw word."
            ),
            need=(
                "Tom wanted to build 'village' using the dot-construct, just to see the pattern hold. "
                "Would the constructor work on any input?"
            ),
            mapping=(
                "The form `(String. \"village\")` calls the host's String constructor with the word 'village'. "
                "The constructor is polymorphic and works with any input the REPL provides."
            ),
            resolution=(
                "The constructor returned 'village'. Tom had now called it three times on three different inputs, and each time it had built a String correctly."
            )),
        _ex('(new String "shepherd")', "shepherd",
            'the (new String "shepherd") form',
            'the string built by (new ...)',
            scenario=(
                "Carol and Tom sat by the watchhouse, calling the String constructor on different words. "
                "This time, Tom would use the 'new' form, since he wanted to be explicit."
            ),
            need=(
                "Tom wanted to build 'shepherd'—the character from the fable—using the 'new' form. "
                "He wanted to practice both ways of calling the constructor until they felt natural."
            ),
            mapping=(
                "The form `(new String \"shepherd\")` is explicit about calling a constructor. "
                "The 'new' form works the same way as the dot-construct; the REPL translates it and passes the value to the host."
            ),
            resolution=(
                "The constructor built 'shepherd' cleanly. Tom had now used both forms—dot-construct and 'new'—and seen them work. The boundary was no longer a mystery; the host's constructors spoke the village's language."
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-07 — Arrays
G11_07 = SubjectCurriculum(
    grade=11, subject_id="G11-07",
    subject_title="Arrays",
    fable="boy-wolf",
    examples=[
        # int-array / aget are the canonical interop calls.
        _ex("(let [a (int-array [10 20 30])] (aget a 1))", 20,
            "indexing into an int-array via aget",
            "the value at index 1 of the array"),
        _ex("(let [a (int-array [1 2 3])] (alength a))", 3,
            "the length of an int-array via alength",
            "the length of the array"),
        _ex("(let [a (int-array [10 20 30])] (aget a 1))", 20,
            "indexing into an int-array via aget",
            "the value at index 1 of the array",
            scenario=(
                "Tom walked into the smithy's storage room and saw the host's array machinery. "
                "The smith showed him an int-array—a long shelf of integer boxes, side by side."
            ),
            need=(
                "Tom wanted to reach into an array and fetch a specific value—the second box, at index 1. "
                "The village didn't have arrays; the host did. Tom needed to use the host's tools."
            ),
            mapping=(
                "The form `(aget array index)` is the watchhouse's way of calling the host's array-get operation. "
                "Tom binds the array in a let, then uses aget to fetch the value at the given index. The REPL fetches "
                "and returns the integer inside."
            ),
            resolution=(
                "The form fetched 20 from index 1. Tom understood: the host's arrays were strange, but the watchhouse had a bridge—the aget function—that could reach inside them."         )),
        _ex("(let [a (int-array [1 2 3])] (alength a))", 3,
            "the length of an int-array via alength",
            "the length of the array",
            scenario=(
                "Carol showed Tom another host tool: 'alength', which measured how many boxes an array held. "
                "The array was a fixed container; its length never changed once it was built."
            ),
            need=(
                "Tom wanted to know how many integers fit in an array after it was built. "
                "The host had a tool for this measurement."
            ),
            mapping=(
                "The form `(alength array)` calls the host's array-length operation. Tom builds or binds an array, "
                "then uses alength to fetch its length. The REPL returns the integer count of elements."
            ),
            resolution=(
                "The form returned the result. Tom realized that arrays, like strings, had a length that could be queried. The village had bridges—aget and alength—for crossing into the host's array machinery."         )),
        _ex("(let [a (int-array [5 10 15])] (aget a 0))", 5,
            "indexing into an int-array via aget at index 0",
            "the value at index 0 of the array",
            scenario=(
                "Tom practiced fetching from arrays at different positions. He started with index 0—the first box on the shelf—"
                "and used aget to open it."
            ),
            need=(
                "Tom wanted to fetch the first element, at index 0, to see whether the indexing pattern was what he expected. "
                "Did the host count from 0, like the townsfolk?"
            ),
            mapping=(
                "The form `(aget array 0)` fetches the element at the beginning of the array. "
                "Indexing starts at 0, just as it does in the village. The REPL returns the value inside."
            ),
            resolution=(
                "The form returned 5, the first integer in the array. Tom saw that the host's indexing convention matched the meadow folk's—a good sign that crossing the boundary would feel natural."           )),
        _ex("(let [a (int-array [7 8 9])] (alength a))", 3,
            "the length of an int-array via alength",
            "the length of the array",
            scenario=(
                "Carol and Tom built more arrays and measured them. Each time, alength reached into the host "
                "and returned how many boxes the array held."
            ),
            need=(
                "Tom wanted to build an array of three integers and verify its length using alength. "
                "He wanted to see the tools work together."
            ),
            mapping=(
                "The form `(alength (int-array [7 8 9]))` builds an array and immediately measures its length. "
                "The village tool alength knows how to query the host's array structure."
            ),
            resolution=(
                "The form returned 3. Tom had now used both aget and alength several times. The host's array machinery was no longer foreign; it was just another tool the townsfolk could reach."
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-08 — Type hints
G11_08 = SubjectCurriculum(
    grade=11, subject_id="G11-08",
    subject_title="Type hints",
    fable="boy-wolf",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        _ex('(let [^String s "abc"] (.toUpperCase s))', "ABC",
            "a let-binding with a ^String type hint",
            "the uppercased string after a type-hinted binding"),
        _ex('(do "type hints are metadata that guide compilation" :studied)',
            ":studied",
            "the role of ^Type metadata as a hint",
            "the marker keyword for the type-hint lesson"),
        _ex('(let [^String s "abc"] (.toUpperCase s))', "ABC",
            "a let-binding with a ^String type hint",
            "the uppercased string after a type-hinted binding",
            scenario=(
                "Tom saw Carol writing a let-binding with a strange mark in front of the binding: "
                "a caret and the word 'String'. Carol explained: a type hint for the compiler."
            ),
            need=(
                "Tom wanted to understand what the type hint did. Would it change how the binding worked? "
                "Would the REPL behave differently?"
            ),
            mapping=(
                "The form `(let [^String s \"abc\"] ...)` attaches a type hint to the binding. "
                "The hint tells the compiler that 's' holds a String, so method calls like toUpperCase can be optimized. "
                "The value itself doesn't change; the hint just guides the compiler's work."
            ),
            resolution=(
                "The form called toUpperCase and returned 'ABC'. Tom realized the type hint didn't change the computation, only helped the compiler optimize it. The REPL worked the same way whether the hint was there or not."
            )),
        _ex('(let [^String s "def"] (.length s))', 3,
            "a let-binding with a ^String type hint and method call",
            "the length of the string via method",
            scenario=(
                "Tom practiced writing type hints on bindings. This time, he'd hint a different string and call "
                "the .length method on it."
            ),
            need=(
                "Tom wanted to see the type hint work with another method call. Did the pattern hold for all host methods?"
            ),
            mapping=(
                "The form `(let [^String s \"def\"] (.length s))` hints that 's' is a String, then calls the host method .length. "
                "The type hint helps the compiler generate fast code for the method call."
            ),
            resolution=(
                'The form returned the result, and the method call worked smoothly. Tom understood that type hints were optional metadata—useful for performance, but not necessary for correctness.'           )),
        _ex('(let [^long n 42] (+ n 8))', 50,
            "a let-binding with a ^long type hint for arithmetic",
            "the sum after arithmetic on a type-hinted value",
            scenario=(
                "Carol showed Tom that type hints worked for primitive types too, like 'long'. "
                "She bound a number with the hint and did arithmetic on it."
            ),
            need=(
                "Tom wanted to see how type hints worked with village operations like addition. "
                "Would the hint affect how arithmetic was computed?"
            ),
            mapping=(
                "The form `(let [^long n 42] (+ n 8))` hints that 'n' is a primitive long integer. "
                "The hint tells the compiler to use fast primitive arithmetic, not boxing and unboxing. "
                "The computation itself is the same, but the hint optimizes how it runs."
            ),
            resolution=(
                'The form computed the sum correctly. Tom understood that type hints optimize without changing the result.'
            )),
        _ex('(let [^double d 3.14] (* d 2))', 6.28,
            "a let-binding with a ^double type hint for floating-point arithmetic",
            "the product after arithmetic on a type-hinted double",
            scenario=(
                "Tom practiced type hints with floating-point numbers. Carol showed him the ^double hint, "
                "which told the compiler the binding held a double-precision float."
            ),
            need=(
                "Tom wanted to do floating-point arithmetic with a type hint and see the compiler optimize it. "
                "Would the hint work the same way for doubles as it did for longs?"
            ),
            mapping=(
                "The form `(let [^double d 3.14] (* d 2))` hints that 'd' is a primitive double. "
                "The hint lets the compiler use fast floating-point multiplication without boxing overhead."
            ),
            resolution=(
                'The form returned 6.28, the correct product. Tom had now used type hints on integers, strings, and floats. The pattern was clear: hints were metadata for the compiler, not instructions to change the computation.'
            )),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="boy-wolf",
    examples=[
        # Plain arithmetic works the same way for ordinary values; the
        # checked/unchecked distinction is about overflow at the host
        # primitive level. Use a value-space form for the eval, narrate
        # the distinction.
        _ex("(+ 1 2)", 3,
            "the expression (+ 1 2) under default checked math",
            "the result of (+ 1 2) under the default math regime"),
        _ex('(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            ":studied",
            "the *unchecked-math* dynamic var",
            "the marker for the checked/unchecked lesson"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="boy-wolf",
    examples=[
        _ex('(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)',
            ":studied",
            "the ClojureScript host overview",
            "the marker for studying the cljs host"),
        _ex('(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)',
            ":cljs",
            "where ClojureScript runs and how interop looks",
            "the marker for the cljs-runtime lesson"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-11 — cljs-js interop
G11_11 = SubjectCurriculum(
    grade=11, subject_id="G11-11",
    subject_title="cljs / JavaScript interop",
    fable="boy-wolf",
    examples=[
        _ex('(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)',
            ":studied",
            "the cljs-to-js interop syntax",
            "the marker for the cljs-js interop lesson"),
        _ex('(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)',
            ":cljs-interop",
            "two key cljs-js interop conventions",
            "the marker keyword for the conventions"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-12 — Basilisp overview (the Python host — this project!)
G11_12 = SubjectCurriculum(
    grade=11, subject_id="G11-12",
    subject_title="Basilisp overview (Python host)",
    fable="boy-wolf",
    examples=[
        _ex('(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)',
            ":studied",
            "the basilisp host overview",
            "the marker for studying basilisp"),
        _ex('(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)',
            ":basilisp",
            "how basilisp does Python interop",
            "the marker keyword for basilisp interop"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-13 — Cross-platform .cljc and reader-conditionals
G11_13 = SubjectCurriculum(
    grade=11, subject_id="G11-13",
    subject_title="Cross-platform .cljc and reader-conditionals",
    fable="boy-wolf",
    examples=[
        _ex('(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)',
            ":studied",
            "the reader-conditional #?(...) form",
            "the marker for the reader-conditional lesson"),
        _ex('(do ".cljc files share code across multiple hosts" :cljc)',
            ":cljc",
            "the role of .cljc files",
            "the marker keyword for the .cljc lesson"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-14 — Debugging host leaks
G11_14 = SubjectCurriculum(
    grade=11, subject_id="G11-14",
    subject_title="Debugging host leaks",
    fable="boy-wolf",
    examples=[
        _ex('(do "host stack traces leak through interop; learn to read them" :studied)',
            ":studied",
            "the topic of debugging host-runtime leaks",
            "the marker for the host-leaks lesson"),
        _ex('(try (Math/sqrt 4) (catch Exception _ :err))', 2.0,
            "wrapping a host call in try/catch in case it leaks",
            "the result when the host call succeeds"),
        _ex('(try (Math/sqrt 4) (catch Exception _ :err))', 2.0,
            "wrapping a host call in try/catch in case it leaks",
            "the result when the host call succeeds",
            scenario=(
                "Tom learned to wrap host calls safely against errors."
            ),
            need=(
                "He needed protection if the host side threw an error."
            ),
            mapping=(
                "Try/catch wraps a host call and catches any errors it throws."
            ),
            resolution=(
                "The host call succeeded cleanly, and Tom understood try/catch's value (with `4` as the input value)."
            )),
        _ex('(try (Math/abs -42) (catch Exception _ :err))', 42,
            "wrapping a host static method in try/catch",
            "the result when the host method succeeds",
            scenario=(
                "Tom practiced wrapping different kinds of host calls in try/catch. "
                "This time, he'd wrap a static method call with a different argument."
            ),
            need=(
                "Tom wanted to see that the try/catch pattern worked with all kinds of host operations—"
                "methods, static functions, constructors. He needed the defense to be universal."
            ),
            mapping=(
                "The form `(try (Math/abs -42) (catch Exception _ :err))` wraps a static method call. "
                "The catch clause is a blanket: any exception from the host lands in :err, not the REPL."
            ),
            resolution=(
                "The form succeeded and returned 42. Tom had now wrapped two host calls, and both worked smoothly. He understood that try/catch was the valley's way of saying to the host: 'Work, but if you fail, fail quietly. Let the village handle the error.'"
            )),
        _ex('(try (.length "test") (catch Exception _ :err))', 4,
            "wrapping a host method call in try/catch to guard against errors",
            "the result when the host method succeeds",
            scenario=(
                "Carol taught Tom that wrapping was good practice for any boundary crossing, not just static methods. "
                "He should wrap instance methods too."
            ),
            need=(
                "Tom wanted to wrap a simple instance method call in try/catch, to show that the pattern "
                "applied universally across the host boundary."
            ),
            mapping=(
                "The form `(try (.length \"test\") (catch Exception _ :err))` wraps an instance method in try/catch. "
                "The pattern is the same whether the call is static or instance-based."
            ),
            resolution=(
                'The form succeeded and returned the result. Tom realized that try/catch was the universal defense: it worked for any kind of host call, catching any error that leaked and turning it into a safe value.'
            )),
        _ex('(try (do (Math/sqrt 4) :success) (catch Exception _ :err))', ":success",
            "a try/catch that wraps multiple host operations and returns a marker on success",
            "the marker when the host operations succeed",
            scenario=(
                "Tom learned an advanced technique: wrapping a do-block that contained multiple host calls, "
                "returning a success marker if all of them completed."
            ),
            need=(
                "Tom wanted to execute multiple host operations safely and report success as a keyword marker. "
                "This way, he could distinguish between a successful computation and a computation that caught an error."
            ),
            mapping=(
                "The form `(try (do (Math/sqrt 4) :success) (catch Exception _ :err))` wraps a do-block with multiple forms. "
                "If all succeed, :success is returned. If any throws, the catch clause returns :err."
            ),
            resolution=(
                "The form returned :success. Tom had now mastered the try/catch pattern across many scenarios. He understood that the watchhouse's error handling could protect against the chaos of the host boundary."
            )),
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
    print(f"grade-11 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
