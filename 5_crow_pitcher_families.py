# ─────────────────────── pitcher-notations (scribe) ─────────────────────────

_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template — generic;
    #    works for comments, whitespace, parens, do, reader macros.
    SubplotTemplate("""\
"There are conventions for how the runtime *reads* a form,"
{clever_phrase} said: "what counts as one token, what's just
spacing, what gets ignored, what gets grouped together. The
scribe and the reader both follow the same conventions." To
{goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — reading exactly by the
conventions — returned the value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template — generic.
    SubplotTemplate("""\
"A form is what the reader sees," {clever_phrase} said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you write and the form the runtime evaluates
aren't always character-for-character the same." To
{goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — reading carefully — returned
the value of what the conventions had produced."""),

    # 3. The careful-writing-careful-reading template — generic.
    SubplotTemplate("""\
{clever_phrase} unrolled a small slate {place} and scratched
the pitcher-notations slowly, paying attention to every talon-mark.
"The form has to be written so the reader can read it cleanly,"
{clever_he_she} said. "If the marks are right, the runtime gets the
right form; if not, not." To {goal_text}, {clever_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
reading exactly as written — returned the value cleanly."""),

    # 4. The Hasty-misreads-the-form template — generic fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, glanced at the pitcher-notations and
called out what {hasty_he_she} thought they would do without paying
attention to the conventions of how they were scratched.
{clever_phrase} only shook {clever_his_her} head — the runtime reads
the form exactly. To {goal_text}, {clever_he_she} composed
{concept_phrase}, submitted the form, and the REPL — reading
literally — returned the right value, while {hasty}'s guess fell
short."""),

    # 5. The form-as-it-is template — generic.
    SubplotTemplate("""\
"A form is what's actually there on the pitcher's clay,"
{clever_phrase} said, "after the conventions of writing and
reading have done their work. The runtime sees the cleaned-up form,
evaluates it, and gives back what it computes." To {goal_text},
{clever_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value."""),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she_cap} composed {concept_phrase} "
        "and submitted the form. The REPL read by the pitcher-notation "
        "conventions and returned:"
    ),
]


# ─────────────────────── chalk-scratch-vs-stone (quote/symbols) ────────

_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The chalk-mark-on-the-stone template — symbols vs values.
    SubplotTemplate("""\
{clever_phrase} pointed at a chalk mark scratched on a smooth stone
{place}, then at another stone lying nearby. "The chalk mark on
the stone is the *name*; the stone is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To {goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer."""),

    # 2. The label-the-form template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than evaluating it,"
{clever_phrase} said, "you mark the form with chalk in front.
Quoting tells the runtime: don't evaluate this, just hand
it back as the shape it is." To {goal_text}, {clever_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
respecting the chalk mark — returned the form unevaluated."""),

    # 3. The marking-vs-evaluating template — generic
    #    emphasis on the distinction without claiming a specific
    #    quote/unquote arrangement.
    SubplotTemplate("""\
"There's a difference between *marking* the form and
*evaluating* it," {clever_phrase} said. "Quote in any of its
shapes is the marking — the runtime hands you back the form,
not its value, unless you say otherwise." To {goal_text},
{clever_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — marking exactly what the form asked for —
returned the form-as-data, exactly as the chalk had directed."""),

    # 4. The Hasty-confuses-mark-with-stone template.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, mistook the chalk mark on the stone
for the stone itself. "It says crow, so the value must be the
crow!" {clever_phrase} only shook {clever_his_her} head: the
mark and the stone are never the same thing. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form,
and the REPL — keeping mark and stone distinct — returned
the right answer for the goal."""),

    # 5. The chalk-endures-the-stone-lives template — generic.
    SubplotTemplate("""\
"A chalk mark can be carried from stone to stone," {clever_phrase}
explained, "passed hand to hand, written again. The mark itself is
just a shape; the value it names is separate — a thing in the world."
To {goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — holding the mark distinct from
the value — returned exactly what the form asked for."""),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she_cap} composed {concept_phrase} "
        "and submitted the form. The REPL — distinguishing chalk-mark "
        "from stone — returned:"
    ),
]


# ─────────────────────── stone-by-stone tally (reduce/count) ──────────────

_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-rim-with-tally template — reduce.
    SubplotTemplate("""\
{clever_phrase} walked the rim of the pitcher {place}, one claw at a
time, a small smooth stone held in the other talon for the running tally.
"Reduce is this walk," {clever_he_she} said: "at each drop-point, you
combine the stone into the tally; at the end, the tally is your answer."
To {goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — walking the rim, carrying the
tally — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {clever_phrase}
said, holding up a stone already marked with a number. "If you
start with a different value, the walk begins from there — the
combine-step adds each stone in from that starting point." To
{goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — starting from the given tally,
walking the rim — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting,"
{clever_phrase} said: "step along the rim, add one at every
drop-point, no other operation. The runtime does this for any
collection — vector, list, map, string." To {goal_text},
{clever_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — walking the rim, counting the steps —
returned the count."""),

    # 4. The Hasty-guesses-the-total template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, called out guesses at the pitcher
without bothering to walk the rim and carry the tally. {clever_phrase}
only smiled and reached for a stone. "The tally grows with every drop,"
{clever_he_she} said patiently. To {goal_text},
{clever_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — walking and counting stone by stone —
handed back the true total {hasty} had been guessing at."""),

    # 5. The rim-returns-a-number template — generic.
    SubplotTemplate("""\
"Walk the rim this way," {clever_phrase} instructed,
"and what you carry back is always a single number — the one
you set out with, combined with each stone as you pass." To
{goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — carrying the tally forward
with every step — returned the number the walk had produced."""),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she_cap} composed {concept_phrase} "
        "and submitted the form. The REPL walked the rim carrying the "
        "tally:"
    ),
]


# ─────────────────────── pebble-string-on-a-vine (str/subs) ──────────────

_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-pebbles template — `str` concat.
    SubplotTemplate("""\
{clever_phrase} held up a vine with small smooth pebbles threaded
on it in a row {place}. "Strings in Clojure are like this,"
{clever_he_she} said: "a threaded line of characters, in order.
Concat strings together, and the vines are spliced; cut a substring
out, and you get a shorter vine." To {goal_text},
{clever_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — splicing or cutting as the form said —
returned the new pebble-string."""),

    # 2. The counting-pebbles template — string length / substring.
    SubplotTemplate("""\
"To count the pebbles, walk the vine,"
{clever_phrase} said. "Want a section of pebbles? Cut from one
position to another and you get a smaller vine, the original
untouched." To {goal_text}, {clever_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — counting or
cutting — returned the answer the pebble-vine had given up."""),

    # 3. The reassembling-the-string template — generic string building.
    SubplotTemplate("""\
{clever_phrase} took two vines with pebbles threaded on them
{place}. "Join two vines together and you have one longer vine,"
{clever_he_she} said, "or take a piece from one and attach it
elsewhere." To {goal_text}, {clever_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — manipulating
the pebble-strings exactly — returned the new vine."""),

    # 4. The Hasty-yanks-at-the-vine template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, yanked at the pebble-vine {place}
without bothering to count the pebbles first. {clever_phrase}
stopped {hasty_him_her}: strings are precise — every pebble in
its place, every position counted. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form,
and the REPL — handling the vine carefully — returned the right
answer."""),

    # 5. The splice-or-slice template — generic string ops.
    SubplotTemplate("""\
"A pebble-string can be spliced with others," {clever_phrase}
said, "or sliced into pieces, characters counted and rearranged.
Whatever you ask the string to do, it does it precisely." To
{goal_text}, {clever_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — treating each pebble as the
form directed — returned the result."""),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she_cap} composed {concept_phrase} "
        "and submitted the form. The REPL spliced or counted as the "
        "form said:"
    ),
]


# ─────────────────────── looping-drop-without-growth (recur/loop) ────────

_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The circuit-without-growth template — recur.
    SubplotTemplate("""\
{clever_phrase} walked a small circle around the pitcher {place},
each lap returning to the same starting point with a slightly
different tally in talon. "Recur is this circuit," {clever_he_she}
said: "back to the top with new bindings, no extra trail laid
down behind us." To {goal_text}, {clever_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every circuit has a stopping condition," {clever_phrase}
said. "Without one, the crow walks forever. With one, the
crow knows when the laps are done and the tally is the
answer." To {goal_text}, {clever_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping
until the base case — returned the value the final lap
produced."""),

    # 3. The Hasty-distrusts-the-circuit template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, distrusted the very idea of a
circuit: surely you'd just walk forever? {clever_phrase}
smiled patiently — the base case is the runner's compass.
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — looping the right number
of times, then stopping — returned the value cleanly."""),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she_cap} composed {concept_phrase} "
        "and submitted the form. The REPL looped without growing the "
        "trail:"
    ),
]
