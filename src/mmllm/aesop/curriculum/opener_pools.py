"""Opener and plan-preface pools per fable.

Each fable has 30 openers (the first sentence of the user_msg) and
30 plan prefaces (short assistant pre-tool-call lines). Per the
variation-pool directive, >=30 of each ensures no single phrasing
becomes the cue.

Openers are Python format strings; available placeholders include
{place}, {primary}, {secondary}, {primary_phrase},
{secondary_phrase}, {primary_he_she}, {secondary_he_she}. About
half of each opener pool references 1-2 of these so the opener
weaves a drawn value into the first line.
"""
from __future__ import annotations


# ───────────────────────── tortoise & hare ─────────────────────────

OPENERS_TORTOISE_HARE: tuple[str, ...] = (
    # — pure scene-setting (no placeholders) —
    "There was once a Hare whose pride matched her feet in speed, and a "
    "Tortoise who said nothing about either.",
    "In that part of the woods, no one ever expected the slow to outpace "
    "the swift, yet the question was always quietly asked.",
    "The Hare and the Tortoise had argued for as long as anyone could "
    "remember about who was truly the faster.",
    "A path ran from the old oak to the river stone, and on it many a "
    "boast had been measured against many a steady step.",
    "Long ago, when wagers were still settled by running rather than "
    "talking, two unlikely rivals agreed to a race.",
    "Some say it began with a yawn and a laugh; others say it began with "
    "a quiet refusal to be laughed at.",
    "The morning was bright and the dust on the road was dry, the sort "
    "of weather that invites a contest.",
    "It is one thing to have fast legs and another to know how to use "
    "them, as the meadow folk would soon be reminded.",
    "Spring had loosened the soil and the grasses had grown tall enough "
    "to brush a passing flank.",
    "Two creatures of very different gait once agreed that the ground "
    "between two stones would settle a long argument.",
    "Among the small kingdoms of the meadow, swiftness was a kind of "
    "currency, and one creature spent it loudly.",
    "The judge was a fox of solemn ear, and the prize was nothing more "
    "than the quiet certainty of being right.",
    "A wager was struck under the elm; the runners were named, the "
    "course was paced, and the day was set.",
    "There is a kind of pride that runs ahead of itself, and a kind of "
    "patience that arrives at its own pace.",
    "By the time the dew had lifted, the meadow had gathered to watch "
    "the strangest race anyone could remember.",
    "It happened in a year when the wheat came in early and the children "
    "had time to lean against fences and watch.",

    # — placeholder-bearing openers —
    "All this took place {place}, where the dust still keeps the shape "
    "of the runners' feet.",
    "{primary} liked to talk; {secondary} liked to listen, "
    "and the rivalry between them had grown into a small legend {place}.",
    "{place}, a Hare and a Tortoise once made a wager that the meadow "
    "still talks about.",
    "It happened {place}, on a morning when the air was kind to swift "
    "feet and steady ones alike.",
    "{primary} was the first to laugh and the first to boast, and "
    "{secondary} simply began to walk.",
    "When {primary} declared the race already won, no one yet "
    "knew how long the afternoon would be.",
    "The sun rose {place}, and with it the question of who could "
    "outrun whom.",
    "{primary} was certain {primary_he_she} could not lose; "
    "{secondary} was certain of nothing except the next step.",
    "A quiet wager passed between {primary} and {secondary}, and "
    "{place} the meadow folk gathered to see it answered.",
    "Word went around {place} that two creatures had agreed to settle "
    "an old question with their feet.",
    "{primary} announced the race in a voice loud enough to wake the "
    "owls, and {secondary} accepted with a nod.",
    "{place}, where the path bends past the elm, {primary} "
    "taunted {secondary} one too many times.",
    "{secondary} had nothing to prove, but {primary} "
    "had everything to lose, and the race was on.",
    "Anyone passing {place} that morning would have seen {primary} "
    "stretching for show while {secondary} simply began.",
)

OPENERS_CROW_PITCHER: tuple[str, ...] = (
    # — pure scene-setting —
    "It had been a long, dry summer, and the rivers had pulled back "
    "from their banks in a slow and patient retreat.",
    "The orchard had not seen a real rain in weeks, and even the "
    "lavender stood with its head bowed.",
    "There was once a Crow who had flown a great distance and found "
    "nothing in any pond worth dipping a beak.",
    "Drought has its own quiet way of teaching the difference between "
    "thirst and the right answer to thirst.",
    "An old pitcher of glazed clay sat by the garden wall, half-empty "
    "and entirely useless to anyone too proud to think.",
    "In a year when the wells ran low, a single jar of water was a "
    "small kingdom unto itself.",
    "The farmstead had stored what it could, but the heat was honest "
    "and the water was patient with no one.",
    "On a long afternoon when even the bees had grown slow, a thirsty "
    "bird settled on the rim of a clay vessel.",
    "Some problems cannot be hurried; they only respond to the slow "
    "addition of small things.",
    "There was a pitcher and there was a thirst, and between them lay "
    "a question that asked for thought rather than force.",
    "The kitchen garden had been lovingly kept, but the sun that year "
    "had been merciless and constant.",
    "A row of pebbles lay at the foot of the wall, sun-warmed, "
    "unremarkable, and just heavy enough.",
    "The water sat at the bottom of the jar, deep enough to glimpse "
    "and far enough to tantalize.",
    "When the cisterns ran shallow, even the cleverest creatures had "
    "to learn the patience of small additions.",
    "On the rim of a long-shadowed pitcher, a thirsty bird considered "
    "what it had and what it lacked.",
    "It was the kind of summer that turned every shaded stone into a "
    "small kindness.",

    # — placeholder-bearing —
    "{place}, where the orchard meets the well, an old clay pitcher "
    "had stood for as long as anyone could remember.",
    "The drought had reached even {place}, and {primary} flew "
    "in slow circles searching for water.",
    "{primary} alighted on the rim of a jar {place} and peered "
    "down at the small dark gleam below.",
    "It was {place}, in the long heat of late summer, that a thirsty "
    "bird met a stubborn vessel.",
    "{primary} had flown all morning {place} without finding so much "
    "as a damp leaf to rest a beak against.",
    "{place}, a single pitcher held the last of the water, and "
    "{primary} arrived too parched to be picky.",
    "When {primary} landed by the garden wall, {primary_he_she} saw "
    "the water and saw the distance, and stood very still.",
    "{primary} was no fool, and {place} the day demanded "
    "thinking rather than complaining.",
    "Word had it that {primary} had flown over three valleys before "
    "finding the pitcher {place}.",
    "{place}, where the heat shimmered above the stones, "
    "{primary} began the slow business of solving thirst.",
    "{primary} circled twice {place} before settling on the rim of "
    "the old clay jar, eyes on the water below.",
    "The orchard {place} had grown quiet in the heat, and "
    "{primary} was the only sound at midday.",
    "In a long-dry season, {primary} found the pitcher "
    "{place} and began to consider it carefully.",
    "{primary} arrived {place} with no plan but a sharp eye "
    "and a willingness to take small steps.",
)

OPENERS_MILKMAID: tuple[str, ...] = (
    # — pure scene-setting —
    "There was once a milkmaid who walked to market with a pail of "
    "fresh milk balanced upon her head.",
    "The road from the farm to the town was long, and a daydream "
    "could fit comfortably along its length.",
    "On market mornings, the dairy yard smelled of damp grass and "
    "warm tin, and the future seemed safely arrangeable.",
    "It is an old habit to count the worth of a thing before the "
    "thing has reached the buyer.",
    "A pail of milk is a small fortune to a careful walker and a "
    "lost fortune to a careless one.",
    "Long before the market opened its stalls, a young woman had "
    "already spent her milk three times in her head.",
    "The sun had only just cleared the hedgerows when the day's "
    "first tally of imagined coins began.",
    "Milk does not forgive a tilted head, but a dreaming mind seldom "
    "remembers as much.",
    "It was the season of new chicks and first cheeses, and every "
    "small profit felt like the start of a larger one.",
    "Between the dairy and the marketplace stretched a road, a hill, "
    "and an entire life imagined into being.",
    "She had not yet sold the milk and yet had already chosen the "
    "ribbons she would wear at the dance.",
    "Every step of the road carried the soft sound of liquid against "
    "tin and the louder sound of a daydream gathering speed.",
    "Some plans grow gently from the ground up; others are built "
    "from the rooftop down, and topple just as fast.",
    "It was the kind of morning that tempts a careful person into "
    "carelessness through the back door of a happy thought.",
    "The cows had given generously that dawn, and the pail was "
    "heavier than usual, and the imagination was heavier still.",
    "A walk to market, with a full pail and a full head, is one of "
    "the oldest tests of attention there is.",

    # — placeholder-bearing —
    "{place}, the dairy stood between the lane and the meadow, and "
    "the day's milk waited to be carried to town.",
    "{primary_phrase} set out from the farm {place} with the pail "
    "balanced carefully on her head.",
    "It was {place}, on a fair-weather morning, that {primary} began "
    "the long walk to market.",
    "{primary} had walked this road {place} a hundred times before, "
    "but never quite so dreamily.",
    "The pail sat steady on {primary}'s head as {primary_he_she} "
    "started down the lane {place}.",
    "{place}, where the lane bends past the old hedge, "
    "{primary_phrase} began to add up coins she had not yet earned.",
    "{primary} was not a careless girl by nature, but {place} the "
    "morning was bright and the daydreams were brighter.",
    "By the time {primary} had reached the second milestone {place}, "
    "the milk had become eggs, and the eggs a flock.",
    "{primary_phrase} carried more than milk that morning {place}; "
    "she carried a whole imagined fortune.",
    "{place}, the road from the farmstead curved gently downhill, "
    "and {primary} walked it with her head held high.",
    "It happened {place}, on the morning {primary_phrase} took the "
    "milk to market and her thoughts ran ahead of her feet.",
    "{primary} hummed quietly {place} as she walked, the pail "
    "steady and the future already half-spent.",
    "{place}, before the cocks had finished crowing, "
    "{primary_phrase} had set out with the milk and a head full of "
    "plans.",
    "{primary_phrase} balanced the pail with the ease of long "
    "practice, and {place} the road stretched out invitingly.",
)

OPENERS_BOY_WOLF: tuple[str, ...] = (
    # — pure scene-setting —
    "There was once a shepherd boy whose afternoons were long and "
    "whose imagination was longer.",
    "The pasture lay below a rocky lookout, and the sheep were "
    "easier to count than the hours.",
    "Long days alone with a flock can teach patience, or they can "
    "teach mischief, depending on the boy.",
    "The villagers had agreed that any cry of wolf would bring them "
    "running with their sticks and lanterns.",
    "It is a serious thing to call for help, and a more serious "
    "thing to call for it falsely.",
    "On a hill above the village, a boy watched sheep, and the sheep "
    "watched the grass, and the day moved slowly.",
    "There is a difference between a real alarm and a bored one, "
    "and the village knew the difference well.",
    "The wolves of those hills were rare but not absent, and the "
    "shepherds knew it was safer to be vigilant than clever.",
    "It happened in a quiet season, when the lambs were strong and "
    "the days were long enough to grow tired of.",
    "An empty hour can sometimes be filled with mischief, and "
    "mischief once started has a way of escalating.",
    "The hilltop offered a fine view of both the flock and the road "
    "below, where help would have to come from.",
    "A boy with too little to do and too loud a voice is a small "
    "danger to himself and a larger one to his village.",
    "On those slopes, trust was a thing the village extended freely, "
    "and a thing it could not afford to lose.",
    "The sheep had grazed peacefully all morning, and there was "
    "nothing at all the matter, which was exactly the problem.",
    "Some games seem harmless until the moment they are needed in "
    "earnest, and then they cost everything.",
    "The lambs were milling in the lower meadow when the boy first "
    "thought of the joke he should not have made.",

    # — placeholder-bearing —
    "{place}, on a slope above the village, {primary_phrase} watched "
    "his flock and his shadow grow longer.",
    "{primary} had been minding the sheep {place} since the first "
    "light, and the day was wearing thin.",
    "It was {place}, where the ridge looks down on the houses, that "
    "{primary_phrase} first cried wolf.",
    "{primary} was a clever boy, and {place} cleverness had begun to "
    "look very much like trouble.",
    "{place}, in the long grass above the village road, "
    "{primary_phrase} settled in for another slow afternoon.",
    "The villagers lived just down the slope from where "
    "{primary_phrase} stood watch, and they trusted that voice.",
    "When {primary} called out {place} the first time, the village "
    "came running, and the sheep stayed exactly as they were.",
    "{primary_phrase} had been told the rules plainly: cry only when "
    "the wolf is real, and never when {primary_he_she} is bored.",
    "{place}, where the path winds up toward the lookout, "
    "{primary_phrase} watched and waited and watched some more.",
    "{primary} had a fine view {place}, but a finer talent for "
    "stretching a quiet hour into a noisy one.",
    "It happened {place}, on a hill where shouting carries far and "
    "trust carries further, until it doesn't.",
    "{primary_phrase} was supposed to keep the sheep safe; instead, "
    "{place}, he kept inventing reasons for the village to run.",
    "When {primary} climbed up to the lookout that morning, "
    "{primary_he_she} did not yet know that the day would teach a "
    "lasting lesson.",
    "{primary_phrase} had cried wolf once already, {place}, and the "
    "villagers had laughed but not entirely.",
)

OPENERS_DOG_SHADOW: tuple[str, ...] = (
    # — pure scene-setting —
    "There was once a dog who carried a fine bone home along a path "
    "that crossed a stream by an old wooden bridge.",
    "The stream ran clear that afternoon, and the bridge cast a long "
    "trembling shadow across the water.",
    "It is one of the oldest tricks of light to make one bone seem "
    "like two and to make a fool of the unwary.",
    "A dog with a bone in his jaws is a happy creature; a dog who "
    "looks too hard at the water may not be.",
    "The path home wound past a slow brook, and on bright days the "
    "brook was full of borrowed shapes.",
    "There is a kind of greed that does not see what it already has, "
    "and another kind that mistakes a reflection for a meal.",
    "Some lessons are taught by mirrors, and some are taught by "
    "rivers; this one was taught by both at once.",
    "On a path that ran beside the stream, a dog was carrying his "
    "supper home and looking pleased with himself.",
    "The water beneath the bridge was unhurried that day, and any "
    "creature looking down would see a perfect copy of itself.",
    "It was an afternoon of quiet sky and steady current, and the "
    "world below the surface seemed almost solid.",
    "The bone was good, the day was warm, and the path was clear, "
    "and yet the trouble was already shaped in the water.",
    "A reflection is a strange kind of promise: present and "
    "unreachable, and very hard to argue with.",
    "Down by the stream where the bank dipped low, the world above "
    "was answered politely by the world below.",
    "Some greedy creatures lose what they have to a thief; others "
    "lose it to themselves, by way of a careless glance.",
    "It happened on a day so ordinary that it seemed impossible "
    "anything could have been lost.",
    "The bridge had stood there as long as anyone remembered, and so "
    "had the temptation it offered to anyone crossing with full jaws.",

    # — placeholder-bearing —
    "{place}, where the path crosses the stream, {primary} "
    "trotted home with a fine bone in his teeth.",
    "{primary} had found the bone {place} and was carrying it home "
    "with no small amount of pride.",
    "It was {place}, on the wooden bridge above the slow brook, that "
    "{primary} looked down at the water.",
    "{primary} was crossing the stream {place} when "
    "{primary_he_she} caught a glimpse of his own reflection.",
    "{place}, the path bends down to meet the water, and "
    "{primary} stopped at exactly the wrong moment.",
    "{primary} had carried his prize all the way from the village, "
    "and {place} the bridge offered him an unwelcome second look.",
    "{place}, the stream ran clear enough to mirror anything that "
    "passed above it, and {primary} passed above it.",
    "When {primary} reached the bridge {place}, {primary_he_she} "
    "paused to admire the bone he had been so lucky to find.",
    "{primary} was nearly home {place} when the water below "
    "showed him a second bone that did not exist.",
    "{place}, on a still afternoon by the brook, {primary} learned "
    "what a reflection costs the careless.",
    "{primary} had crossed this bridge a hundred times {place}, but "
    "never with so fine a bone clamped in his jaws.",
    "It happened {place}, on the very bridge {primary} crossed "
    "every day, that he stopped longer than he should have.",
    "{primary} was halfway home {place} when the water played "
    "its old trick on a young dog.",
    "{place}, where the boards of the bridge meet the stones of the "
    "path, {primary} caught sight of himself in the stream.",
)


# ───────────────────────── plan prefaces ─────────────────────────

PLANS_TORTOISE_HARE: tuple[str, ...] = (
    "I'll let the REPL settle this, no point arguing about arithmetic.",
    "Let me write the form carefully and let the runtime answer.",
    "I'll compose the expression one operand at a time, then evaluate.",
    "{primary} would race to a guess; I'll write the form and let the "
    "REPL judge.",
    "Steady wins here: I'll lay the form out plainly and run it.",
    "I'll resist the urge to predict and just evaluate.",
    "Let me transcribe the form exactly, then send it to the REPL.",
    "I'll proceed at the pace of the form, not the pace of a hunch.",
    "Better to walk this through the REPL than to sprint to a wrong "
    "number.",
    "I'll trust the evaluator over my first instinct.",
    "Let me write the expression with care and check it.",
    "I'll keep my hands on the keys and my opinions to myself.",
    "A patient form is better than a clever guess; I'll write it out.",
    "I'll set the expression up and let the REPL do the running.",
    "Let me put together the form step by step, then evaluate.",
    "I'll match the form to the description, then run it.",
    "{secondary}'s pace, not {primary}'s: I'll write it carefully and "
    "evaluate.",
    "Let me build the expression deliberately and check the result.",
    "I'll favour the slow form over the fast guess.",
    "I won't sprint past this; I'll write the form and let it speak.",
    "Let me commit the form to the REPL rather than to memory.",
    "I'll take the long way: write, evaluate, report.",
    "Better to be steady than sorry; I'll set up the form and run it.",
    "I'll lay out the operands and let evaluation finish the thought.",
    "Let me write the expression and trust the runtime.",
    "I'll resist hurry and submit the form for evaluation.",
    "Step by step, the form first, then the answer.",
    "I'll proceed without boast: form, evaluate, return.",
    "Let me hand the work to the REPL, where speed loses to accuracy.",
    "I'll keep the form honest and let the evaluator finish it.",
)

PLANS_CROW_PITCHER: tuple[str, ...] = (
    "I'll add the operands one at a time and watch the value rise.",
    "Let me build the expression slowly, the way water rises by "
    "pebbles.",
    "I'll place each piece of the form in turn, then evaluate.",
    "Patience first: I'll set up the form and let the REPL bring up "
    "the answer.",
    "I'll work the form gradually, one stone at a time.",
    "Let me assemble the expression methodically, then check it.",
    "I'll resist guessing the level and let the evaluator measure it.",
    "One operand, then another, then the result; I'll write it out.",
    "I'll place the parentheses carefully and let the runtime decide.",
    "Let me build the form piece by piece, watching for balance.",
    "I'll lay each operand down with care and evaluate at the end.",
    "Slow and small: I'll compose the form and check the result.",
    "Let me drop the operators in one at a time, then run it.",
    "I'll let the REPL raise the answer the way pebbles raise water.",
    "Step by careful step, I'll write the form and evaluate.",
    "I'll trust accumulation over guesswork and let the form speak.",
    "Let me add each piece in order, then submit the whole.",
    "I'll keep the form tidy and the operations explicit.",
    "Patience over force: I'll write the expression and evaluate.",
    "Let me approach this the methodical way and let the REPL answer.",
    "I'll build the form gradually, then trust the runtime's level.",
    "One small piece at a time, then evaluation.",
    "I'll let the REPL show what each step adds.",
    "Let me lay the expression out cleanly and let it run.",
    "I'll add nothing I cannot account for, then evaluate.",
    "Better small steps than wild leaps; I'll write and run the form.",
    "Let me work in small increments and let the REPL settle it.",
    "I'll measure my way to the answer through the form, not the guess.",
    "Slowly does it: I'll compose, evaluate, and report.",
    "I'll hold to a steady rhythm and let the runtime arrive at the "
    "answer.",
)

PLANS_MILKMAID: tuple[str, ...] = (
    "I'll verify before I claim — the REPL is the only honest market.",
    "Let me check the form against the runtime before counting any "
    "answer.",
    "I won't tally before evaluation; I'll write the form and run it.",
    "Better to confirm than to assume; I'll send it to the REPL.",
    "I'll keep the pail steady: form first, then answer.",
    "Let me write the expression carefully and not get ahead of it.",
    "I'll resist imagining the result and just evaluate it.",
    "No counting chickens — I'll commit the form to the REPL.",
    "Let me put the form together cleanly and let the runtime check it.",
    "I'll confirm with evaluation rather than with a hopeful guess.",
    "Better to walk carefully than to spill the answer; I'll evaluate.",
    "I'll write the expression as given and let the REPL settle it.",
    "Let me check the work before announcing anything.",
    "I'll trust the runtime, not my arithmetic daydreams.",
    "No premature conclusions; I'll write and evaluate.",
    "Let me carry the form steadily to the REPL.",
    "I'll submit the form for evaluation before saying a word about "
    "results.",
    "Confirm first, claim later: I'll run it.",
    "Let me put the operands in order and check with the runtime.",
    "I won't get ahead of the evaluator; I'll write the form.",
    "Better cautious than confident: I'll evaluate and then report.",
    "Let me set the expression up and let the REPL verify it.",
    "I'll keep my balance and let the runtime do the talking.",
    "No plans built on unsold milk; I'll send it to the REPL.",
    "Let me write the form precisely and check the value.",
    "I'll evaluate before I summarize.",
    "Better to confirm with the runtime than to imagine a number.",
    "Let me put the form to the REPL and see what it actually returns.",
    "I'll keep my expectations quiet and let the evaluator answer.",
    "{primary} would tally too early; I'll write the form and check.",
)

PLANS_BOY_WOLF: tuple[str, ...] = (
    "I won't shout an answer I haven't checked; let me run the form.",
    "Only the REPL's verdict counts; I'll evaluate.",
    "Let me write the expression and trust the runtime, not a hunch.",
    "I'll skip the false alarm and go straight to evaluation.",
    "No crying wolf about results; I'll send it to the REPL.",
    "I'll wait for the real answer, the one the runtime returns.",
    "Let me check the form against the evaluator before claiming "
    "anything.",
    "I won't raise an alarm without evidence; I'll run the form first.",
    "I'll trust the evaluator over my own first guess.",
    "Better to evaluate than to declare; I'll write and run.",
    "Let me check before I call out any number.",
    "I won't pre-announce; I'll let the REPL speak.",
    "I'll quiet the guess and listen to the runtime.",
    "Let me submit the form and wait for the verdict.",
    "No premature shouting; I'll evaluate the expression.",
    "I'll keep my voice down until the REPL gives me a value.",
    "Let me run the form and let the result stand on its own.",
    "I'll trust evaluation, not anticipation.",
    "No false alarms; I'll write the form and let it run.",
    "Let me write the expression and confirm with the evaluator.",
    "I'll wait for the runtime before saying anything definitive.",
    "Only what the REPL returns counts; I'll send it.",
    "I'll be careful with my certainty and let the evaluator do its "
    "work.",
    "Let me check it through the runtime before I commit to an answer.",
    "I'll let the form speak through evaluation, not through me.",
    "No claim without proof; I'll evaluate.",
    "Let me submit it and wait for the real answer.",
    "I'll match my words to the runtime's output, not the other way "
    "around.",
    "Better silent now and accurate later; I'll run the form.",
    "I'll let the REPL be the one to answer.",
)

PLANS_DOG_SHADOW: tuple[str, ...] = (
    "I won't grab at a reflection; I'll trust the form, not the "
    "appearance.",
    "Let me work from the expression itself, not from what it looks "
    "like at a glance.",
    "I'll evaluate the form rather than guess from its surface.",
    "Better to trust the structure than the shimmer; I'll run it.",
    "Let me submit the actual form, not my impression of it.",
    "I'll check the expression carefully and let the runtime answer.",
    "No reaching for a quick shape; I'll evaluate the real form.",
    "Let me look past the look of it and run the expression.",
    "I'll keep what I have, write the form, and evaluate.",
    "Better the form in hand than a guess in the water; I'll run it.",
    "Let me transcribe the expression exactly and trust the REPL.",
    "I'll resist the surface impression and evaluate the form.",
    "Let me focus on the structure of the expression and run it.",
    "I won't trade a real form for a quick guess; I'll evaluate.",
    "Let me read the expression as written and submit it.",
    "I'll trust the form's behaviour, not its appearance.",
    "Better steady possession than greedy reflection; I'll run the "
    "form.",
    "Let me hold to what the expression actually says and evaluate.",
    "I'll check the structure, then let the runtime answer.",
    "Let me write what is there, not what it seems to promise.",
    "I'll let the REPL see the form and tell me the value.",
    "No grabbing at appearances; I'll evaluate.",
    "Let me work the actual expression and not its echo.",
    "I'll set the form down faithfully and let it run.",
    "Better the form's truth than my reflection of it; I'll evaluate.",
    "Let me submit the expression as given and trust the runtime.",
    "I'll keep my eyes on the form, not on a quick guess.",
    "Let me run the expression and accept the value it returns.",
    "I'll trust the structure on the page, not the shape in my head.",
    "Let me commit the actual form and let the evaluator decide.",
)


# ───────────────────────── smoke test ─────────────────────────


def _smoke_test() -> None:
    opener_pools = {
        "OPENERS_TORTOISE_HARE": OPENERS_TORTOISE_HARE,
        "OPENERS_CROW_PITCHER":  OPENERS_CROW_PITCHER,
        "OPENERS_MILKMAID":      OPENERS_MILKMAID,
        "OPENERS_BOY_WOLF":      OPENERS_BOY_WOLF,
        "OPENERS_DOG_SHADOW":    OPENERS_DOG_SHADOW,
    }
    plan_pools = {
        "PLANS_TORTOISE_HARE":   PLANS_TORTOISE_HARE,
        "PLANS_CROW_PITCHER":    PLANS_CROW_PITCHER,
        "PLANS_MILKMAID":        PLANS_MILKMAID,
        "PLANS_BOY_WOLF":        PLANS_BOY_WOLF,
        "PLANS_DOG_SHADOW":      PLANS_DOG_SHADOW,
    }
    for n, p in opener_pools.items():
        assert len(p) >= 30, f"{n}: only {len(p)} openers"
        assert len(p) == len(set(p)), f"{n}: duplicates"
    for n, p in plan_pools.items():
        assert len(p) >= 30, f"{n}: only {len(p)} plans"
        assert len(p) == len(set(p)), f"{n}: duplicates"
    # Probe placeholder coverage: >=30% of openers reference at least
    # one placeholder.
    for n, p in opener_pools.items():
        with_ph = sum(1 for s in p if "{" in s and "}" in s)
        assert with_ph >= 9, (
            f"{n}: only {with_ph} of {len(p)} openers use placeholders")
    print(f"opener_pools.py smoke_test: ok "
          f"({sum(len(p) for p in opener_pools.values())} openers, "
          f"{sum(len(p) for p in plan_pools.values())} plans)")


if __name__ == "__main__":
    _smoke_test()
