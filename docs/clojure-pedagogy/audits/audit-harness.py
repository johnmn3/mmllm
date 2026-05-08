"""Audit any per-fable K-12 curriculum (set FABLE env var to switch).

Usage:
    python3 audit-harness.py            # audits tortoise-hare (default)
    FABLE=goose_eggs python3 ...        # audits a different fable
    FABLE_ALL=1 python3 ...             # audits every curriculum found
"""
from __future__ import annotations

import importlib
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import generate_subject


CURRICULUM_ROOT = Path("/home/user/mmllm/src/mmllm/aesop/curriculum")


def _discover_fables():
    """All sub-packages with grade_N.py files."""
    out = []
    for p in CURRICULUM_ROOT.iterdir():
        if p.is_dir() and p.name not in ("__pycache__",):
            if (p / "grade_1.py").exists():
                out.append(p.name)
    return sorted(out)


def _load_grade_modules(fable: str):
    mods = []
    for n in range(1, 13):
        try:
            mods.append(importlib.import_module(
                f"mmllm.aesop.curriculum.{fable}.grade_{n}"))
        except ModuleNotFoundError:
            break
    return mods


if os.environ.get("FABLE_ALL"):
    FABLES_TO_AUDIT = _discover_fables()
else:
    FABLES_TO_AUDIT = [os.environ.get("FABLE", "tortoise_hare")]

# Single fable mode: legacy GRADE_MODULES still works.
GRADE_MODULES = _load_grade_modules(FABLES_TO_AUDIT[0])


def check_record(rec, sub, example):
    issues = []
    user = rec.user_msg
    asst = rec.assistant_msg

    # length
    n_words = len(user.split())
    if n_words < 35:
        issues.append(("LOW_LENGTH", f"user_msg only {n_words} words"))
    elif n_words > 200:
        issues.append(("HIGH_LENGTH", f"user_msg {n_words} words"))

    # singular-they verb agreement
    for m in re.finditer(r"\bthey\s+(?:eats|walks|runs|has\b|is\b|knows|hopes|reaches|jumps|drops)\b", user, re.IGNORECASE):
        issues.append(("VERB_AGREEMENT", f"singular-they: '{m.group(0)}'"))

    # un-substituted placeholder
    if "{form_display}" in user or "{concept_phrase}" in user or "{place}" in user:
        issues.append(("UNFILLED_PLACEHOLDER", "user_msg has un-substituted placeholder"))

    # answer-leak detection: only if the answer is an int that's NOT a substring of the form
    if isinstance(example.expected, int) and abs(example.expected) > 5:
        ans_str = str(example.expected)
        if ans_str not in example.form:
            # Strip every occurrence of the form, then look for the answer
            user_clean = user.replace(example.form, "")
            ans_re = rf"(?<![0-9-]){re.escape(ans_str)}(?![0-9])"
            if re.search(ans_re, user_clean):
                issues.append(("ANSWER_LEAK", f"answer {ans_str} in narrative"))

    # asst leak: strip the JSON form arg properly (handles escaped quotes)
    if isinstance(example.expected, int) and abs(example.expected) > 5:
        ans_str = str(example.expected)
        if ans_str not in example.form:
            # Strip everything between "form":" and the closing unescaped "
            asst_clean = re.sub(
                r'"form":"(?:[^"\\]|\\.)*"', '', asst
            )
            ans_re = rf"(?<![0-9-]){re.escape(ans_str)}(?![0-9])"
            if re.search(ans_re, asst_clean):
                issues.append(("ANSWER_LEAK_ASST", f"answer {ans_str} in asst preface"))

    # nested 'computes' in question_what (real bug — the question_phrase
    # template already says "Write a Clojure expression that computes X.",
    # so X containing "computes" produces "computes ... computes ...")
    if "computes" in example.question_what.lower():
        issues.append(("NESTED_COMPUTES", "question_what already says 'computes'"))

    # Targeted commentary-paren check: only flag specific pedagogical-aside
    # patterns ("(note ...)", "(it isn't)", "(the REPL ...)", "(returns ...)",
    # "(an addition ...)", "(it does ...)"). Avoids false positives on
    # Clojure source forms which legitimately contain parens.
    #
    # Boy-wolf hand-audit added new aside patterns: "(no change)",
    # "(none set)", "(as if read by slurp)", "(edn-shaped roundtrip)",
    # "(dedup'd)", "(count)", "(finally is for side effects)",
    # "(tap> always returns true on send)", "(it is)" / "(it isn't)".
    aside_re = re.compile(
        r"\((?:note(?:\:|\s)|it isn'?t|it is\)|the REPL\s|returns\s|the return\s|"
        r"first truthy|empty string|the comment\s|integer quotient|"
        r"it does|it doesn'?t|no change|none set|as if read|"
        r"edn-shaped|dedup'?d|count\)|finally is|tap>\s)"
    )
    for label, val in (("concept_phrase", example.concept_phrase),
                        ("question_what",  example.question_what)):
        if aside_re.search(val):
            issues.append(("ASIDE_PAREN",
                            f"{label} has pedagogical-aside parenthetical"))

    # Em-dash commentary: e.g., "X — note: ...", "X — first truthy".
    # The em-dash is followed by lowercase commentary, not part of a
    # legitimate noun-phrase title.
    #
    # Boy-wolf hand-audit added: "— what doc would print",
    # "— host-portable length", "— a basic spec check", "— the unevaluated
    # list", "— 0 is not nil".
    emdash_re = re.compile(
        r" — (?:note|first|empty|returns|integer|"
        r"what doc|host-portable|a basic|a failing|the unevaluated|"
        r"0 is not|the keyword|the integer)"
    )
    if emdash_re.search(example.question_what) or emdash_re.search(example.concept_phrase):
        issues.append(("EMDASH_COMMENTARY",
                        "concept_phrase or question_what has em-dash commentary"))

    # Boy-wolf hand-audit pitfall: ", which is X" trailing answer leak
    # in question_what — "the value of (first nil), which is nil",
    # "the count of nil, which is 0". The aside states the answer, which
    # the eval-first design forbids.
    if re.search(r",\s+which is\s+\S+", example.question_what):
        issues.append(("WHICH_IS_LEAK",
                        "question_what '..., which is X' leaks the answer in narrative"))

    # "said EMO_PROUD" without comma (subplot template bug — EMO entries
    # that are participles don't fit "said X" without comma).
    # Extended to cover other speaking verbs (declared, cried) — same
    # pitfall, different head verb. The audit caught a bare
    # "declared puffed up with pride" in ant-grasshopper grade 2.
    bad_said = [
        "said boasting", "said puffed", "said swaggering",
        "said with a smug grin",
        "declared boasting", "declared puffed", "declared swaggering",
        "declared with a smug grin",
        "cried boasting", "cried puffed", "cried swaggering",
        "cried with a smug grin",
    ]
    for p in bad_said:
        if p in user.lower():
            issues.append(("SAID_PARTICIPLE", f"'{p}' (missing comma after speech-verb)"))
            break

    # Double "from" / generalized DOUBLE_OF check.
    # Pitfall #13: when EMO_TIRED already terminates with "from X" (or
    # "at X", "of X"), a template-supplied tail duplicates the preposition.
    double_tail_re = re.compile(
        r"(from \w+ing|weary from \w+|drowsy from \w+|"
        r"yawning at [a-z ]+?|legs heavy from \w+) "
        r"(from|of|at) (a |the )"
    )
    if double_tail_re.search(user.lower()):
        issues.append(("DOUBLE_FROM",
                        "EMO_TIRED tail duplicates an already-terminated prep "
                        "phrase (e.g., 'from sprinting from a recent sprint', "
                        "'weary from the morning's effort from a season of song')"))

    # Meta-meta question_what: "the value of the form X" inside
    # "Write a form whose evaluation gives X" wrapping → meta-meta.
    if re.search(r"the value of the form \S", example.question_what):
        issues.append(("META_META",
                        "question_what 'the value of the form X' creates meta-meta wrap"))

    # Bad place-preposition combos: "in the hilltop" (should be "on/atop"),
    # "in the road" (should be "on the road"), "in the farm" (should
    # be "on/at the farm"), etc. Pitfall #22 family.
    for bad in ("in the hilltop", "in the road", "in the beach",
                 "in the farm"):
        # Use word-boundary check so "in the farmyard" doesn't false-positive
        # on the "in the farm" pattern.
        if re.search(re.escape(bad) + r"(?!\w)", user):
            issues.append(("BAD_PLACE_PREP", f"'{bad}' (wrong preposition)"))
            break

    # Verb-preposition mismatch: "stopped across X" — you don't "stop
    # across" a place.
    if "stopped across " in user:
        issues.append(("BAD_VERB_PREP",
                        "'stopped across X' (verb+prep mismatch)"))

    # FORM_LEAK — for non-atom subjects (those with goal_text), the
    # literal form must NOT appear in user_msg. If it does, the model
    # is being trained to copy the form from the prompt instead of
    # producing it from the goal description. Atom subjects (G1-01..08-
    # style; goal_text empty) are exempt because for them the form IS
    # the answer.
    if getattr(example, "goal_text", "") and example.form:
        # Normalize whitespace in form before searching (since the form
        # may have been re-flowed in the user_msg).
        form_norm = re.sub(r"\s+", " ", example.form).strip()
        user_norm = re.sub(r"\s+", " ", user)
        # Only flag forms ≥ 5 chars to avoid trivial substring noise
        # (single-char operators / digits will appear naturally).
        if len(form_norm) >= 5 and form_norm in user_norm:
            issues.append(("FORM_LEAK",
                f"form {form_norm!r} appears in user_msg of a goal-style subject"))

    # Also catch string/keyword answer leaks in non-atom subjects:
    # if expected is a string or keyword, the literal value must NOT
    # appear in user_msg (e.g., "HARE" for upper-case form, ":caught"
    # for catch branch).
    if getattr(example, "goal_text", "") and isinstance(example.expected, str):
        ans = example.expected
        # Skip very short answers (<= 2 chars) and bool-ish strings
        if len(ans) >= 3 and ans not in ("yes", "no"):
            if ans in user:
                issues.append(("ANSWER_LEAK_STRING",
                    f"answer string {ans!r} appears in user_msg"))

    # STORY_TAG_MISMATCH — examples with the "story" tag should have
    # all four story slots filled (scenario / need / mapping /
    # resolution). Conversely, examples with all four slots filled
    # should declare tags=("story",) so story-scaffold templates fire.
    has_story_tag = "story" in getattr(example, "tags", ())
    has_all_slots = all(
        getattr(example, slot, "")
        for slot in ("scenario", "need", "mapping", "resolution")
    )
    has_any_slot = any(
        getattr(example, slot, "")
        for slot in ("scenario", "need", "mapping", "resolution")
    )
    if has_story_tag and not has_all_slots:
        issues.append(("STORY_TAG_MISMATCH",
                       'example tagged "story" but is missing one or '
                       'more of scenario/need/mapping/resolution slots'))
    elif has_any_slot and not has_all_slots:
        issues.append(("STORY_TAG_MISMATCH",
                       "example has some story slots filled but not "
                       "all four; either fill all four or remove all"))
    elif has_all_slots and not has_story_tag:
        issues.append(("STORY_TAG_MISMATCH",
                       "example has all four story slots filled but "
                       'is not tagged "story"; story-scaffold '
                       "template will not fire"))

    # ─────────────────────── deep-audit additions ───────────────────────
    # Checks added after the goose-eggs and ant-grasshopper hand-audits
    # surfaced patterns the original structural rules missed. Each was
    # found in ≥1 grade by the 12 reader sub-agents.

    # DOUBLE_PREP — verb's preposition + place_phrase's preposition.
    # `place_phrase()` returns a string that ALREADY starts with a
    # preposition ("in the meadow", "deep inside the cellar", "on the
    # hilltop"), so verbs that need their own preposition stack two
    # prepositions: "Halfway to in the meadow", "On the way to market
    # near the market". Pitfall #21 in the SKILL doc.
    if re.search(
        r"\b(?:to|at|from|with|onto|into|toward|towards|past|outside|beneath)"
        r"\s+(?:in the|near the|on the|atop the|by the|along the|"
        r"inside the|deep inside the|at the edge of the|inside a|"
        r"deep inside a|atop a|by a|near a|in a)\b",
        user,
    ):
        issues.append(("DOUBLE_PREP",
                       "verb+preposition followed by {place} which "
                       "already carries its own preposition"))

    # BAD_PLACE_PREP_FARM — "in the farm" reads as inside a building;
    # idiomatic English: "on the farm" / "at the farm". Same family as
    # the existing "in the hilltop / road / beach" check but the original
    # didn't enumerate "farm".
    if (re.search(r"in the farm(?!\w)", user, re.IGNORECASE)
            and "into the farm" not in user.lower()):
        issues.append(("BAD_PLACE_PREP",
                       "'in the farm' (use 'on the farm' / 'at the farm')"))

    # GENDERED_EMO — possessive pronoun in EMO_* phrase ("her eyes",
    # "his shoulder", "her legs", "her hands") attached to a clearly-
    # opposite-gender named character. Catches the
    # "her eyes always on the path" / "his hands itching" leakage.
    # Heuristic: a male-coded name within 60 chars BEFORE "her <body>",
    # or a female-coded name within 60 chars BEFORE "his <body>".
    male_names = (
        # Humans
        "Bob", "Charlie", "David", "Edward", "Frank", "George", "Henry",
        "Oliver", "Tom", "Will",
        # Hares (tortoise-hare)
        "Whisker", "Hopper",
        # Tortoises
        "Slowpoke", "Mossback",
        # Geese (goose-eggs)
        "Quill",
        # Other animals (used by other fables but harness shared)
        "Korvus", "Renard", "Squeak", "Roar", "Greyfang", "Rex",
        "Stilt", "Thorn", "Boulder", "Tic", "Chirp",
    )
    female_names = (
        # Humans
        "Alice", "Beatrice", "Carol", "Diana", "Emily", "Fiona", "Grace",
        "Helen", "Margery", "Lila", "Jess", "Lou",
        # Hares
        "Bramble",
        # Tortoises
        "Shelly",
        # Geese
        "Honk",
        # Other
        "Caw", "Vix", "Whisk", "Mane", "Howl", "Bell", "Reeda", "Gale",
        "Toc", "Skip",
    )
    body_parts_re = r"\b(eyes|legs|hands|shoulders?|grin|stride|gaze|"\
                    r"stomach|belly|mouth|beak|heart|voice|thoughts?)\b"
    # Tighter pattern: require the pronoun to be in APPOSITION to the
    # name (i.e., right after `{name}, ` or `{name} the {species}, ` or
    # in a `said,` clause). The original loose proximity check produced
    # false positives like "Bramble peered over his shoulder" — where
    # "his" refers to the tortoise mentioned earlier, not to Bramble.
    # Apposition templates we care about:
    #   "{name}, her eyes always on the path"
    #   "{name} the hare, her legs heavy"
    #   "{name} said, her eyes ..."
    for fem_name in female_names:
        # female name + male possessive in apposition
        if re.search(
            rf"\b{fem_name}\b(?:\s+the\s+\w+)?(?:\s+(?:said|declared|"
            rf"explained|laughed|insisted|asked|nodded))?,\s+"
            rf"his\s+{body_parts_re}",
            user,
        ):
            issues.append(("GENDERED_EMO",
                           f"'{fem_name}' followed in apposition by "
                           f"'his <body>' — EMO has hardcoded male "
                           f"possessive"))
    for masc_name in male_names:
        if re.search(
            rf"\b{masc_name}\b(?:\s+the\s+\w+)?(?:\s+(?:said|declared|"
            rf"explained|laughed|insisted|asked|nodded))?,\s+"
            rf"her\s+{body_parts_re}",
            user,
        ):
            issues.append(("GENDERED_EMO",
                           f"'{masc_name}' followed in apposition by "
                           f"'her <body>' — EMO has hardcoded female "
                           f"possessive"))

    # OBJECT_AS_SUBJECT — object-case pronoun used in subject position.
    # E.g., "agreed to wait while {owner_him_her} submitted the form"
    # renders as "while her submitted" / "while him submitted" /
    # "while them submitted" — all ungrammatical.
    if re.search(
        r"\b(?:while|so|as|after|before|until|when)\s+(?:her|him)\s+"
        r"(?:submitted|asked|wrote|said|chalked|drew|read|typed|"
        r"explained|insisted|agreed|added|counted|tallied|peered|"
        r"pointed|sketched|laid)\b",
        user,
    ):
        issues.append(("OBJECT_AS_SUBJECT",
                       "object-case pronoun (her/him) used in subject "
                       "position — should be subjective case or the name"))

    # LOWER_PLACE_AFTER_PERIOD — "{place}" rendered after a sentence-
    # ending period, where {place} starts with a lowercase preposition.
    # E.g., "...on first glance. near the market, he typed..." should be
    # "Near the market" or restructured. Bug surfaces in grade-5/7/10/12
    # extension subplots.
    if re.search(
        r"\.\s+(?:in the|near the|on the|atop the|by the|along the|"
        r"inside the|deep inside the|at the edge of the|inside a|"
        r"deep inside a|atop a|by a|near a|in a)\s+[a-z]",
        user,
    ):
        issues.append(("LOWER_PLACE_AFTER_PERIOD",
                       "{place} renders lowercase right after a period — "
                       "sentence starts mid-prep"))

    # DOUBLED_PLACE — a hardcoded location in the template followed by
    # {place} that resolves to the SAME or NEARBY location, producing
    # "in the kitchen deep inside the kitchen" / "kitchen table in the
    # kitchen" / "stood in the farm at the edge of the farm".
    doubled_place_re = re.compile(
        r"\b(?:kitchen|cellar|barn|cottage|farm|orchard|meadow|"
        r"village|market)\b[^.]{0,40}?\b(?:in|near|on|atop|by|along|"
        r"inside|deep inside|at the edge of)\s+(?:the|a)\s+"
        r"(?:kitchen|cellar|barn|cottage|farm|orchard|meadow|"
        r"village|market)\b"
    )
    for m in doubled_place_re.finditer(user):
        # Skip false positives where the two locations are genuinely
        # different (e.g., "kitchen table in the cellar" — table-in-
        # cellar is implausible but is actually flagged correctly).
        if m.group(0).count("kitchen") >= 2 or m.group(0).count(
                "farm") >= 2 or m.group(0).count("cellar") >= 2:
            issues.append(("DOUBLED_PLACE",
                           f"location stutter: '{m.group(0)[:60]}...'"))
            break

    # BUT_PLEASED_TAUTOLOGY — banquet template appends "but pleased"
    # after EMO_CONTENT, but EMO_CONTENT entries are positive ("happy
    # with the day's small gift", "pleased with the steady fortune"),
    # so "but" reads as a wrong contrast. Also "pleased ... but pleased"
    # is duplicate.
    if re.search(
        r"(?:happy|pleased|grateful|content|calm|settled|untroubled|"
        r"unhurried)\s+[^,.]{0,60}?\bbut pleased\b",
        user,
    ):
        issues.append(("BUT_PLEASED_TAUTOLOGY",
                       "'but pleased' appended to already-positive EMO "
                       "phrase (banquet template tautology)"))

    # OF_THE_LECTURE — trailing genitive glued onto an EMO phrase in
    # the grade-10 ledger-notebook subplot. Renders "with hands itching
    # to count more of the lecture", "tempted by the thought of plenty
    # of the lecture", etc.
    if " of the lecture" in user:
        issues.append(("OF_THE_LECTURE",
                       "'of the lecture' tail attached to EMO phrase — "
                       "produces ungrammatical run-on"))

    # MISSING_SPACE_QUOTES — concept_phrase with adjacent quoted strings
    # missing inter-quote space, e.g., `["a" "b""c"]` (G7-12 ex1 typo).
    if re.search(r'""[a-zA-Z]', example.concept_phrase + " " +
                  example.question_what):
        issues.append(("MISSING_SPACE_QUOTES",
                       "concept_phrase or question_what has \"X\"\"Y\" "
                       "(missing space between adjacent quoted strings)"))

    # EMDASH_COMMENTARY_EXTENDED — extends the original EMDASH check
    # (note|first|empty|returns|integer) to catch additional commentary
    # patterns the goose-eggs audit found.
    emdash_ext_re = re.compile(
        r" — (?:host-portable|a basic spec check|a failing spec check|"
        r"what doc would print|0 is not nil|last wins|the unevaluated|"
        r"args evaluated|the 2 is dropped|they aren'?t|after expansion|"
        r"finally is for)"
    )
    if emdash_ext_re.search(example.question_what) or \
       emdash_ext_re.search(example.concept_phrase):
        issues.append(("EMDASH_COMMENTARY",
                       "concept_phrase or question_what has em-dash "
                       "commentary (extended pattern)"))

    # ASIDE_PAREN_EXTENDED — extends the original ASIDE_PAREN check to
    # catch additional pedagogical-aside parentheticals goose-eggs found.
    aside_ext_re = re.compile(
        r"\((?:it is nil|none set|the 2 is dropped|args evaluated|"
        r"they aren'?t|a list, not a function call|5!|dedup'?d|count\)|"
        r"a correct form)"
    )
    for label, val in (("concept_phrase", example.concept_phrase),
                        ("question_what",  example.question_what)):
        if aside_ext_re.search(val):
            issues.append(("ASIDE_PAREN",
                           f"{label} has pedagogical-aside (extended)"))
            break

    # ANSWER_LEAK_PHRASE — concept_phrase or question_what contains the
    # literal answer when the answer is "nil" / "true" / "false". The
    # original ANSWER_LEAK only handles integers > 5; goose-eggs G6-06
    # ex1 leaks "nil" via "which is nil" and G2-12 leaks "nil" via "(it
    # is nil)" — both grammatically caught by ASIDE_PAREN, but
    # belt-and-suspenders.
    if example.expected is None and \
       re.search(r"\b(?:which is|it is|returns)\s+nil\b",
                  example.question_what + " " + example.concept_phrase):
        issues.append(("ANSWER_LEAK_PHRASE",
                       "concept_phrase or question_what leaks the "
                       "literal answer 'nil'"))
    # Unclosed dialogue quote — odd number of `"` in user_msg means a
    # subplot template opened a dialogue quote without closing it.
    if user.count('"') % 2 != 0:
        issues.append(("UNCLOSED_DIALOGUE_QUOTE",
                        "user_msg has an odd number of dialogue quotes "
                        "(subplot opened a `\"` but did not close it)"))

    # `who, {participial-phrase},` — relative-clause `who` immediately
    # followed by a participial phrase; the `who` expects a finite verb.
    if re.search(
        r",\s+who,\s+(?:[a-z]+ \w+|drowsy|weary|lulled|yawning|"
        r"her|his|their)\s",
        user,
    ):
        issues.append(("WHO_PARTICIPLE",
                        "subplot template has 'who,' immediately followed by a "
                        "participial phrase (drop the redundant 'who,')"))

    # "X insisted they already knew" — singular-they ambiguity after a
    # named singular subject; use the name instead of the pronoun.
    if re.search(r"\b\w+ insisted they already knew\b", user):
        issues.append(("INSISTED_THEY",
                        "boast subplot 'X insisted they already knew' reads as "
                        "plural after singular-named subject (pitfall #19)"))

    # PREDICATE_QUESTION_COLLISION — a Clojure predicate ends in ``?``,
    # and when the question framing appends its own ``?`` or ``.`` the
    # rendered text reads ``contains??``, ``empty??``, ``zero??.``,
    # ``contains?.`` etc. Surfaced as a Cat-C papercut by the
    # crow-pitcher 0HIm deep audit (G4-12, G4-14, G4-19). Only flag
    # when the predicate ``?`` and the trailing punctuation are
    # adjacent (no whitespace) — ``(symbol? ...)`` ellipses and
    # similar inline code references are fine.
    if re.search(r"\b\w+\?[?]", user) or re.search(r"\b\w+\?\.(?!\.)", user):
        issues.append(("PREDICATE_QUESTION_COLLISION",
                       "predicate-suffix ``?`` collides with the question "
                       "framing's trailing ``?`` or ``.``"))

    # WRONG_FABLE_LITERAL — a tortoise-hare-specific named character
    # (Mossback, Shelly, Slowpoke, Pip, Bramble, Hopper, Whisker,
    # Speedwick, Speedy, Zephyr) appears in a non-tortoise-hare
    # record's user_msg. Either as a defrecord field-name string
    # ((->Hare "Pip")) or in narrative prose ("the Hare pouch").
    # Cat-E (semantic — wrong-fable imagery leakage). Tortoise-hare
    # itself is exempt because those names are native there.
    if sub.fable != "tortoise-hare":
        for ghost in ("Mossback", "Shelly", "Slowpoke", "Pip",
                      "Bramble", "Hopper", "Whisker", "Speedwick",
                      "Speedy"):
            if re.search(r"\b" + ghost + r"\b", user):
                issues.append(("WRONG_FABLE_LITERAL",
                               f"tortoise-hare ghost name '{ghost}' "
                               f"appears in {sub.fable} user_msg"))
                break

    # FOREIGN_FABLE_IMAGERY — wrong-fable props in narrative prose.
    # A non-tortoise-hare record renders text like "moss-covered
    # milestone", "leather notebook", "twig in the path", "halfway
    # through the race" — these are tortoise-hare's specific props /
    # phrasings and read as imagery leakage in another fable. Cat-H
    # (plot coherence). Caught by the crow-pitcher 0HIm deep audit
    # in grade-1 _SHARED_SUBPLOTS templates inherited from TH.
    if sub.fable != "tortoise-hare":
        TH_IMAGERY = (
            "moss-covered milestone",
            "leather notebook",
            "wooden sign nailed to a tree",
            "small audience of forest creatures",
        )
        for ph in TH_IMAGERY:
            if ph in user:
                issues.append(("FOREIGN_FABLE_IMAGERY",
                               f"tortoise-hare-specific imagery "
                               f"'{ph}' leaks into {sub.fable} prose"))
                break

    # LOW_GROUNDING — Cat-J: a record that names the operation but
    # doesn't FEEL it. Flag any record whose user_msg lacks BOTH:
    #   (i)  a drawn-value reference — any literal lexeme from the
    #        rendered form (a number, a keyword name, a quoted symbol,
    #        a string body) appearing in the prose, AND
    #   (ii) any phrase from the fable's emotion pools (EMO_PROUD,
    #        EMO_PATIENT, EMO_THIRSTY, EMO_GREEDY, EMO_CONTENT,
    #        EMO_REGRETFUL, EMO_DESPERATE, EMO_TIRED, EMO_HUNGRY).
    # If neither anchor is present the prose reads as abstract
    # restatement of the goal — the affirmative-grounding lift the
    # crow-pitcher 0HIm slice's directive asks for.
    code_str = getattr(rec, 'code_str', '') or ''
    drawn_lexemes = set()
    for tok in re.findall(r'[a-zA-Z][a-zA-Z0-9_-]{2,}|[0-9]{2,}', code_str):
        if tok.lower() not in ("def", "let", "fn", "do", "if", "and",
                               "or", "not", "when", "true", "false",
                               "nil", "this", "case", "cond", "loop",
                               "recur", "for"):
            drawn_lexemes.add(tok)
    has_drawn = any(lx in user for lx in drawn_lexemes)
    has_emo = False
    if not has_drawn:
        # Lazy-import the emotion pools so the detector also runs on
        # branches that don't yet have the new emotion_pools module.
        try:
            from mmllm.aesop.fables import (
                EMO_PROUD, EMO_PATIENT, EMO_TIRED, EMO_HUNGRY,
                EMO_GREEDY, EMO_CONTENT, EMO_REGRETFUL,
                EMO_DESPERATE, EMO_THIRSTY,
            )
            from mmllm.aesop.curriculum.generator import (
                CP_EMO_THIRSTY, CP_EMO_PATIENT, CP_EMO_PROUD,
            )
            EMO_ALL = (
                tuple(EMO_PROUD) + tuple(EMO_PATIENT) + tuple(EMO_TIRED)
                + tuple(EMO_HUNGRY) + tuple(EMO_GREEDY) + tuple(EMO_CONTENT)
                + tuple(EMO_REGRETFUL) + tuple(EMO_DESPERATE)
                + tuple(EMO_THIRSTY) + tuple(CP_EMO_THIRSTY)
                + tuple(CP_EMO_PATIENT) + tuple(CP_EMO_PROUD)
            )
            has_emo = any(p in user for p in EMO_ALL if len(p) > 5)
        except ImportError:
            has_emo = True  # don't flag if pools unavailable
    if not has_drawn and not has_emo:
        issues.append(("LOW_GROUNDING",
                       "user_msg lacks both a drawn-value reference "
                       "and any emotion-pool phrase (Cat-J: prose "
                       "names the operation but doesn't feel it)"))

    return issues


def per_example_records(sub, example, n: int, seed: int):
    """Generate `n` records for ONE specific example by filtering."""
    out = []
    s = seed
    while len(out) < n and s < seed + n * 50:
        recs = generate_subject(sub, n_per_example=1, seed=s)
        for r in recs:
            if r.code_str == example.form:
                out.append(r)
                if len(out) >= n:
                    break
        s += 1
    return out


def main():
    fable = FABLES_TO_AUDIT[0]
    fable_dash = fable.replace("_", "-")
    out = Path(
        f"/home/user/mmllm/docs/clojure-pedagogy/audits/{fable_dash}-audit.md"
    )
    out.parent.mkdir(parents=True, exist_ok=True)

    summary = Counter()
    issue_examples: dict[str, list] = {}
    per_grade_stats: dict[int, dict] = {}

    with open(out, "w") as f:
        f.write(f"# {fable_dash} curriculum audit\n\n")
        f.write("Auto-generated audit — each subject's examples checked at "
                "3 records per example, properly matched.\n\n")
        f.write("---\n\n")

        for grade_n, mod in enumerate(GRADE_MODULES, 1):
            f.write(f"## Grade {grade_n}\n\n")
            grade_stats = {"subjects": 0, "examples": 0, "issues": 0,
                            "low_variety": []}
            for sid, sub in mod.SUBJECTS.items():
                grade_stats["subjects"] += 1
                grade_stats["examples"] += len(sub.examples)

                # Variety
                seed_base = int(sid[3:].replace("-", "")) * 7
                recs50 = generate_subject(sub, n_per_example=50, seed=seed_base)
                n_unique = len({r.user_msg for r in recs50})
                variety = n_unique / len(recs50)
                if variety < 0.95:
                    grade_stats["low_variety"].append((sid, variety))

                # Per-example checks
                subj_issues = []
                for example in sub.examples:
                    sample = per_example_records(sub, example, n=3, seed=seed_base)
                    for r in sample:
                        for sev, msg in check_record(r, sub, example):
                            summary[sev] += 1
                            grade_stats["issues"] += 1
                            subj_issues.append((sev, msg, example.form, r.user_msg[:200]))
                            if sev not in issue_examples:
                                issue_examples[sev] = []
                            if len(issue_examples[sev]) < 5:
                                issue_examples[sev].append(
                                    (sid, msg, example.form, r.user_msg[:300])
                                )

                if subj_issues or variety < 0.95:
                    f.write(f"### {sid}: {sub.subject_title}\n\n")
                    f.write(f"- examples: {len(sub.examples)}\n")
                    f.write(f"- variety @ n=50: {variety:.2f}\n")
                    if subj_issues:
                        # Group by severity
                        by_sev = Counter(i[0] for i in subj_issues)
                        f.write(f"- issues: {dict(by_sev)}\n")
                        for sev, msg, form, snip in subj_issues[:6]:
                            f.write(f"    - [{sev}] form=`{form[:50]}` — {msg}\n")
                    f.write("\n")
            per_grade_stats[grade_n] = grade_stats

        f.write("---\n\n## Summary\n\n")
        f.write("### Issue counts (across all examples × 3 records)\n\n")
        for sev, n in summary.most_common():
            f.write(f"- **{sev}**: {n}\n")
        f.write("\n### Per-grade summary\n\n")
        f.write("| Grade | Subjects | Examples | Issues | Low-variety |\n|---|---|---|---|---|\n")
        for g, s in per_grade_stats.items():
            lv = "; ".join(f"{sid}({v:.2f})" for sid, v in s["low_variety"][:3]) or "—"
            f.write(f"| {g} | {s['subjects']} | {s['examples']} | {s['issues']} | {lv} |\n")
        f.write("\n### Sample issues by severity\n\n")
        for sev, samples in issue_examples.items():
            f.write(f"#### {sev}\n\n")
            for sid, msg, form, snippet in samples:
                f.write(f"- `{sid}` (form `{form[:60]}`): {msg}\n")
                f.write(f"    ```\n    {snippet[:300]}...\n    ```\n")
            f.write("\n")

    print(f"audit → {out}")
    print(f"total issues: {sum(summary.values())}")
    print(f"breakdown: {dict(summary)}")


if __name__ == "__main__":
    main()
