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
from mmllm.aesop.curriculum.emotion_pools import (
    EMO_PROUD as EP_PROUD, EMO_PATIENT as EP_PATIENT,
    EMO_TIRED as EP_TIRED, EMO_THIRSTY as EP_THIRSTY,
    EMO_HUNGRY as EP_HUNGRY, EMO_GREEDY as EP_GREEDY,
    EMO_CONTENT as EP_CONTENT, EMO_REGRETFUL as EP_REGRETFUL,
    EMO_DESPERATE as EP_DESPERATE,
    EMO_SUSPICIOUS as EP_SUSPICIOUS,
    EMO_BOASTFUL as EP_BOASTFUL, EMO_CAUTIOUS as EP_CAUTIOUS,
)
# Also union the renderer-side pools (mmllm.aesop.fables) so the
# detector matches phrases the generator actually emits — the two sets
# overlap heavily but a handful of short phrases (e.g. "without
# complaint") live only in fables and would otherwise be undetected.
from mmllm.aesop.fables import (
    EMO_PROUD as F_PROUD, EMO_PATIENT as F_PATIENT,
    EMO_TIRED as F_TIRED, EMO_HUNGRY as F_HUNGRY,
    EMO_GREEDY as F_GREEDY, EMO_CONTENT as F_CONTENT,
    EMO_REGRETFUL as F_REGRETFUL, EMO_DESPERATE as F_DESPERATE,
)

# Cached set of all archetype-pool phrases for LOW_GROUNDING detector.
_ALL_EMO_PHRASES: tuple[str, ...] = tuple(set(
    EP_PROUD + EP_PATIENT + EP_TIRED + EP_THIRSTY + EP_HUNGRY +
    EP_GREEDY + EP_CONTENT + EP_REGRETFUL + EP_DESPERATE +
    EP_SUSPICIOUS + EP_BOASTFUL + EP_CAUTIOUS +
    F_PROUD + F_PATIENT + F_TIRED + F_HUNGRY + F_GREEDY +
    F_CONTENT + F_REGRETFUL + F_DESPERATE
))

# Regex to pull int/keyword/string/quoted-symbol literals from rec.code_str.
_LITERAL_RES = (
    re.compile(r'(?<![\w-])(-?\d+(?:/\d+)?)(?![\w-])'),  # ints, ratios
    re.compile(r':([a-zA-Z][\w.-]*)'),                   # keywords (no leading :)
    re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"'),           # strings
    re.compile(r"'([a-zA-Z][\w.-]*)"),                   # quoted symbols
)


def _drawn_literals(form: str) -> list[str]:
    """Return all int/keyword/string/quoted-symbol literals in `form`."""
    out = []
    for r in _LITERAL_RES:
        out.extend(r.findall(form))
    return out


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


# ─────────────────── Cat-J grounding helpers ──────────────────────
#
# A record is "grounded" when its prose references either a value
# drawn from the actual code (so the narrative isn't drifting from
# the form) OR carries an emotion-pool phrase (so the character has
# a stance and the prose doesn't read like dry exposition).
#
# Records that lack BOTH are flagged LOW_GROUNDING.

# Cache the EMO pool markers; computed once at module import.
def _build_emo_markers():
    """Pull short discriminating substrings from the EMO pools."""
    markers: list[str] = []
    try:
        from mmllm.aesop.fables import (
            EMO_PROUD, EMO_PATIENT, EMO_TIRED, EMO_HUNGRY,
            EMO_GREEDY, EMO_CONTENT, EMO_REGRETFUL,
            EMO_DESPERATE, EMO_THIRSTY,
        )
        for pool in (EMO_PROUD, EMO_PATIENT, EMO_TIRED, EMO_HUNGRY,
                      EMO_GREEDY, EMO_CONTENT, EMO_REGRETFUL,
                      EMO_DESPERATE, EMO_THIRSTY):
            markers.extend(pool)
    except ImportError:
        pass
    try:
        from mmllm.aesop.curriculum.generator import (
            CP_EMO_PATIENT, CP_EMO_PROUD, CP_EMO_THIRSTY,
        )
        for pool in (CP_EMO_PATIENT, CP_EMO_PROUD, CP_EMO_THIRSTY):
            markers.extend(pool)
    except ImportError:
        pass
    # Boy-wolf-specific EMO pools (added by the audit-boy-wolf-eUtZ
    # slice when LOW_GROUNDING was failing to credit the elder's
    # BW_EMO_PATIENT phrasing for patient-evaluator records).
    try:
        from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
            BW_EMO_PROUD, BW_EMO_PATIENT, BW_EMO_TIRED,
            BW_EMO_REGRETFUL, BW_EMO_DESPERATE,
        )
        for pool in (BW_EMO_PROUD, BW_EMO_PATIENT, BW_EMO_TIRED,
                      BW_EMO_REGRETFUL, BW_EMO_DESPERATE):
            markers.extend(pool)
    except ImportError:
        pass
    # Integration emotion_pools rich archetype set (>=30 entries per
    # pool) — dog_shadow and other fables draw from these rather than
    # the legacy 6-entry fables pools. Fables.py entries are a strict
    # subset so coverage widens without losing anything. Added by the
    # audit-dog-shadow-xe8M slice when LOW_GROUNDING over-flagged
    # dog_shadow records carrying rich emotion_pools phrases.
    try:
        from mmllm.aesop.curriculum.emotion_pools import (
            EMO_PROUD as EP_PROUD2, EMO_PATIENT as EP_PATIENT2,
            EMO_TIRED as EP_TIRED2, EMO_HUNGRY as EP_HUNGRY2,
            EMO_THIRSTY as EP_THIRSTY2,
            EMO_GREEDY as EP_GREEDY2, EMO_CONTENT as EP_CONTENT2,
            EMO_REGRETFUL as EP_REGRETFUL2,
            EMO_DESPERATE as EP_DESPERATE2,
            EMO_BOASTFUL as EP_BOASTFUL2,
            EMO_CAUTIOUS as EP_CAUTIOUS2,
            EMO_SUSPICIOUS as EP_SUSPICIOUS2,
        )
        for pool in (EP_PROUD2, EP_PATIENT2, EP_TIRED2, EP_HUNGRY2,
                      EP_THIRSTY2, EP_GREEDY2, EP_CONTENT2,
                      EP_REGRETFUL2, EP_DESPERATE2, EP_BOASTFUL2,
                      EP_CAUTIOUS2, EP_SUSPICIOUS2):
            markers.extend(pool)
    except ImportError:
        pass
    # De-dupe and sort longest-first so longer markers match before
    # their substrings.
    return tuple(sorted(set(markers), key=len, reverse=True))


_EMO_MARKERS = _build_emo_markers()


def _has_emo_phrase(user: str) -> bool:
    """True if user_msg contains any literal phrase from an EMO pool.

    EMO pools are intentionally short, distinctive phrases (e.g.,
    "calm and methodical", "with a smug grin"); a substring match
    is precise enough.
    """
    return any(m and m in user for m in _EMO_MARKERS)


_INT_RE     = re.compile(r"(?<![\w.:-])(-?\d+)(?![\w.])")
_KW_RE      = re.compile(r":([\w][\w-]*)")
_STR_RE     = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')


def _has_drawn_value(user: str, code_str: str) -> bool:
    """True if user_msg references any int/keyword/string literal
    drawn from code_str.

    The grounding signal we want: when the rendered prose names the
    operands ("the value 7", "the :hare slot", '"hello" string')
    rather than only operating on placeholders. We exclude tiny
    integers (|n| <= 1) because those occur incidentally in prose.
    """
    # Integer literals from code_str.
    for n in _INT_RE.findall(code_str):
        if abs(int(n)) <= 1:
            continue
        if re.search(rf"(?<![\d-]){re.escape(n)}(?!\d)", user):
            return True
    # Keyword literals (':foo', ':hare').
    for kw in _KW_RE.findall(code_str):
        if len(kw) >= 2 and (f":{kw}" in user or f" {kw} " in user):
            return True
    # String literals (must be at least 3 chars to avoid trivial hits).
    for s in _STR_RE.findall(code_str):
        if s and len(s) >= 3 and s in user:
            return True
    return False


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
    # be "on/at the farm"), "on the village/market" (should be at/in/near).
    # Pitfall #22 family.
    #
    # The "in the X" cases use `(?!\w)` — they catch any "in the hilltop…"
    # regardless of what follows (a hilltop never takes "in").
    # The "on the {village|market}" cases must NOT match compound nouns
    # like "on the market pitcher's clay" (idiomatic), so we require
    # a phrase-terminator after the location (punctuation or end-of-line),
    # which is what `place_phrase` produces.
    for bad in ("in the hilltop", "in the road", "in the beach",
                 "in the farm"):
        # Use word-boundary check so "in the farmyard" doesn't false-positive
        # on the "in the farm" pattern.
        if re.search(re.escape(bad) + r"(?!\w)", user):
            issues.append(("BAD_PLACE_PREP", f"'{bad}' (wrong preposition)"))
            break
    for bad in ("on the village", "on the market"):
        # Only flag when the phrase ends here (punctuation / end-of-line);
        # don't fire on compound nouns ("on the market pitcher's").
        if re.search(re.escape(bad) + r"\b(?=[\s]*(?:[.,;:!?]|$))",
                     user, re.MULTILINE):
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

    # Milkmaid hand-audit (claude/audit-milkmaid-Wvxw):
    #
    # SENTENCE_START_LOWER_PRONOUN — a pronoun starts a sentence in
    # lowercase. Source pattern: a template uses {X_he_she} (lowercase
    # pronoun) right after a sentence-ending period, when it should
    # have been {X_he_she_cap}. Example rendered: 'asked. she replied'.
    if re.search(r"[.!?]\"?\s+(he|she|they)\b", user):
        issues.append(("SENTENCE_START_LOWER_PRONOUN",
                        "pronoun starts a sentence in lowercase — template "
                        "should use the _cap variant after a sentence-ending "
                        "punctuation"))

    # PRONOUN_AS_VOCATIVE — a bare pronoun used as a vocative inside
    # dialogue, e.g. '"They, what did you do?"' or '"He, where did you
    # go?"'. Source pattern: {X_he_she_cap} placed at the start of a
    # quoted address; should be the character's NAME, not the pronoun.
    if re.search(r'"(He|She|They), ', user):
        issues.append(("PRONOUN_AS_VOCATIVE",
                        "pronoun used as vocative inside dialogue — template "
                        "should use the character's name, not the pronoun"))

    # FOR_GOAL_TEXT_VERB_INCONGRUITY — 'For [imperative verb]' is
    # ungrammatical when goal_text starts with an infinitive verb.
    # Pattern: 'For create a vector', 'For find the minimum',
    # 'For test whether'. Source: a template that wrote 'For {goal_text}'
    # where goal_text begins with an imperative verb; should be
    # 'To {goal_text}'.
    if re.search(
        r"\bFor (create|find|test|add|subtract|multiply|divide|compute|"
        r"apply|append|extract|get|return|count|build|name|read|write|"
        r"submit|evaluate|call|check|use|swap|deref|throw|catch|throw|"
        r"sort|filter|map|reduce|increment|decrement) ",
        user
    ):
        issues.append(("FOR_GOAL_TEXT_VERB_INCONGRUITY",
                        "'For [imperative-verb]' rendered in user_msg — "
                        "template should use 'To {goal_text}', not "
                        "'For {goal_text}'"))

    # HANGING_FORM_THAT — 'the form that the [noun phrase]' with no
    # verb between 'that' and 'the X'. Source: a template wrote
    # 'the form that {concept_phrase}' where concept_phrase is itself a
    # noun phrase. Should be 'the form for {concept_phrase}' or
    # 'the form that does {concept_phrase}'.
    if re.search(
        r"\bform that\s+(the |an |a |this )"
        r"(?!says|reads|computes|prints|returns|writes|posts|opens|"
        r"reaches|calls|catches|throws|sets|gets|builds|filters|maps|"
        r"reduces|sorts|appends|removes|knows)",
        user
    ):
        issues.append(("HANGING_FORM_THAT",
                        "'form that <noun>' rendered without a verb — "
                        "template should be 'form for {concept_phrase}'"))

    # Crow-pitcher hand-audit (claude/audit-crow-pitcher-R81D):
    #
    # CAP_PRONOUN_MID_SENTENCE — capitalized pronoun (She/He/They)
    # mid-sentence after a comma, typically from a `_he_she_cap`
    # placeholder placed after a comma in a story-template.
    # E.g., "To bind X, She composed..." should be "...she composed..."
    # since the comma is mid-sentence, not a sentence boundary.
    cap_mid_re = re.compile(
        r",\s+(She|He|They)\s+"
        r"(?:composed|wrote|submitted|chose|set|tested|checked|added|"
        r"swapped|paused|brought|read|laid|scratched|extracted|built|"
        r"intended|coordinated|reached|ran|dispatched|started|prepared)"
        r"\b"
    )
    m = cap_mid_re.search(user)
    if m:
        issues.append(("CAP_PRONOUN_MID_SENTENCE",
                       f"'{m.group(0)[:40]}…' (capitalized pronoun "
                       "mid-sentence after comma — should be lowercase)"))

    # DEFINITE_BODY_PART — bird-body participle phrases that prefix
    # the body part with a definite article ("clicking the beak",
    # "cocking the head"). The CP_EMO_PROUD pool used to ship these
    # entries; the audit catches any future regression in the pool
    # OR any new fable that copies the pattern.
    body_part_re = re.compile(
        r"\b(?:clicking|cocking|tilting|preening|fluffing|ruffling|"
        r"tucking|spreading|opening|flicking|stretching|smoothing)"
        r"\s+the\s+"
        r"(?:beak|head|wings?|feathers?|tail|throat|crest)\b"
    )
    m = body_part_re.search(user)
    if m:
        issues.append(("DEFINITE_BODY_PART",
                       f"'{m.group(0)}' (definite-article body-part "
                       "in participle; use possessive-free phrasing)"))

    # Cat-J — insufficient emotion-and-adjective grounding. The user's
    # affirmative directive: prose should NAME the character's emotion
    # at appropriate intensity AND name an environmental adjective that
    # maps to the algorithmic situation. Two failure modes:
    #
    #   (1) total grounding deficit: user_msg lacks BOTH any drawn-value
    #       reference (literals from rec.code_str's ints/keywords/strings)
    #       AND any phrase from the rich EMO pools (EMO_PATIENT,
    #       EMO_REGRETFUL, EMO_CONTENT, EMO_BOASTFUL, EMO_PROUD,
    #       EMO_DESPERATE, EMO_HUNGRY).
    #   (2) generic-adverb shortcut: user_msg has an emotion phrase BUT
    #       it's "softly" / "quietly" / "gently" / "calmly" — bare adverb
    #       rather than an environment-anchored EMO phrase.
    #
    # PREDICATE_QUESTION_COLLISION — a Clojure predicate ends in ``?``,
    # and when the question framing appends its own ``?`` or ``.`` the
    # rendered text reads ``contains??``, ``empty??``, ``zero??.``,
    # ``contains?.`` etc. Surfaced as a Cat-C papercut by the
    # crow-pitcher 0HIm deep audit.
    if re.search(r"\b\w+\?[?]", user) or re.search(r"\b\w+\?\.(?!\.)", user):
        issues.append(("PREDICATE_QUESTION_COLLISION",
                       "predicate-suffix ``?`` collides with the question "
                       "framing's trailing ``?`` or ``.``"))

    # WRONG_FABLE_LITERAL — a tortoise-hare-specific named character
    # appears in a non-tortoise-hare record's user_msg. Either as a
    # defrecord field-name string or in narrative prose. Cat-E
    # (semantic — wrong-fable imagery leakage).
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
    # Cat-H (plot coherence).
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

    # Tortoise-hare hand-audit (claude/audit-tortoise-hare-GCVH):
    #
    # POST_COMMA_CAPITAL_PRONOUN — capitalized pronoun (He/She/They)
    # immediately after a comma in a continuation clause; should be
    # lowercase. Symptom of {X_he_she_cap} placed mid-sentence.
    if re.search(
        r",\s+(?:He|She|They)\s+(?:composed|wrote|took|scratched|"
        r"sketched|chalked|placed|sent|inspected|borrowed|pulled|"
        r"drew|laid|stamped|threaded|walked|rolled|carved|spliced|"
        r"hammered|reached|lined)\b",
        user,
    ):
        issues.append(("POST_COMMA_CAPITAL_PRONOUN",
                       "capitalized pronoun (He/She/They) immediately "
                       "after a comma in a continuation clause — the "
                       "story-scaffold template should use {X_he_she} "
                       "(lowercase) here, not {X_he_she_cap}"))

    # SMALL_INT_LEAK — extends ANSWER_LEAK (which only fires for
    # `abs(expected) > 5`) to catch leaks of small ints 1-5 in
    # resolution slots ("the running total stood at 4").
    if isinstance(example.expected, int) and 1 <= example.expected <= 5:
        ans_str = str(example.expected)
        if ans_str not in example.form:
            leak_re = re.compile(
                rf"\b(?:stood at|came to|settled at|equaled|gave|"
                rf"yielded|returned|resolved to|amounted to|"
                rf"ended at|came out to)\s+{ans_str}\b"
            )
            if leak_re.search(user):
                issues.append(("SMALL_INT_LEAK",
                               f"small-int answer {ans_str} leaks via "
                               "resolution-slot phrasing"))

    # COLLECTION_LEAK — when expected is a collection, flag if its
    # elements appear comma-separated in user_msg AND ≥1 element is
    # absent from the form text (so the model would otherwise have
    # to compute it).
    if isinstance(example.expected, (list, tuple, set)) and \
       2 <= len(example.expected) <= 10:
        elems = [str(x) for x in example.expected
                 if isinstance(x, int) and abs(x) > 1]
        if len(elems) >= 2 and any(e not in example.form for e in elems):
            joined_re = r",\s*(?:and\s+)?".join(re.escape(e) for e in elems)
            if re.search(joined_re, user):
                issues.append(("COLLECTION_LEAK",
                               f"elements of expected {example.expected!r} "
                               "appear comma-separated in user_msg "
                               "(collection answer leak)"))

    # BOOL_LEAK_RESOLUTION — bool answers leaked via "returned true"
    # / "gave false" / etc. in the resolution slot.
    if isinstance(example.expected, bool):
        word = "true" if example.expected else "false"
        leak_re = re.compile(
            rf"\b(?:returned|gave|yielded|came back|answered|"
            rf"replied with|came to)\s+{word}\b"
        )
        if leak_re.search(user):
            issues.append(("BOOL_LEAK_RESOLUTION",
                           f"resolution leaks boolean answer {word!r} — "
                           "describe the verdict abstractly instead"))

    # Milkmaid k7Pq-remediated additions:
    #
    # CONCEPT_AS_VERB — concept_phrase substituted into a slot that
    # requires a finite verb. Renders as "must calling X", "I applying Y".
    # Distinct from FOR_GOAL_TEXT_VERB_INCONGRUITY (which is goal_text
    # after "For"); CONCEPT_AS_VERB is the gerund-after-modal /
    # bare-subject pattern with object-prep tail.
    concept_as_verb_modal_re = re.compile(
        r"\b(?:must|should|can|will|may|own way of doing)"
        r"\s+(?:[a-z]+ing)\s+(?:a|the|an|to|by|via|on|in|at|of|for|with)\b"
    )
    concept_as_verb_subj_re = re.compile(
        r"(?:^|(?<=\W))(\w+\s)?\b(I|you|we)"
        r"\s+(?:[a-z]+ing)\s+(?:a|the|an|to|by|via|on|in|at|of|for|with)\b"
    )
    licensors = {
        "am", "is", "are", "was", "were", "been", "being", "keep", "kept",
        "keeps", "started", "continued", "finished", "stopped", "while",
        "after", "before", "by", "from", "since", "without", "for", "of",
        "to", "and", "or", "but", "than"
    }
    has_concept_as_verb = bool(concept_as_verb_modal_re.search(user))
    if not has_concept_as_verb:
        for m in concept_as_verb_subj_re.finditer(user):
            prev_word = (m.group(1) or "").strip().lower()
            if prev_word in licensors:
                continue
            has_concept_as_verb = True
            break
    if has_concept_as_verb:
        issues.append(("CONCEPT_AS_VERB",
                        "concept_phrase substituted into a finite-verb slot "
                        "(e.g. 'must calling X', 'I applying Y')"))

    # LOWERCASE_CONCEPT_AFTER_PERIOD — sentence ends, next opens with
    # lowercase "the X verb" pattern (concept_phrase as subject after
    # period). Caught by the milkmaid k7Pq deep audit.
    if re.search(
        r"\.\s+the\s+(?:[a-z]+\s+){1,4}"
        r"(?:does|is|means|chooses|examines|reads|"
        r"writes|walks|stacks|fires|takes)\b",
        user,
    ):
        issues.append(("LOWERCASE_CONCEPT_AFTER_PERIOD",
                        "sentence-initial 'the X verb' (lowercase "
                        "concept_phrase as subject after a period)"))

    # ─────────────────── crow-pitcher slice 4YJl additions ──────────────
    #
    # Three new detectors authored during the crow-pitcher hand audit
    # (slice 4YJl, branch claude/audit-crow-pitcher-4YJl). Each surfaces
    # a papercut pattern not caught by any of the ~46 existing detectors.

    # EXPECTED_META_PHRASE — meta-language that talks about "the
    # expected" answer instead of describing what the runtime returned.
    # E.g., "the expected total arrived at the rim", "settled at the
    # expected count". Breaks immersion (the *expected* value is the
    # graded answer; the prose should describe what *did* return, not
    # talk about what was "expected"). Cat-E (semantic) / Cat-I.
    if re.search(
        r"\bthe expected (?:total|count|value|result|number|product|"
        r"sum|tally|answer)\b",
        user, re.IGNORECASE,
    ):
        issues.append(("EXPECTED_META_PHRASE",
                       "user_msg uses 'the expected X' meta-language — "
                       "describes the answer in graders'-vocabulary "
                       "instead of letting the runtime's return speak "
                       "for itself"))

    # PARAMETRIC_LITERAL_NUMERALS — when the example is parametric (its
    # form_template is set, so the actual operands are drawn at render
    # time), scenario/need/mapping/resolution slots should reference
    # the draws via {drawn.X}, not via fixed English numerals
    # ("one, two, three, four, five"). The latter drifts off the
    # actual draws and produces Cat-A logical mismatches such as
    # form (* 5 8 2 2 1) with prose "five groups: one, two, three,
    # four, five stones in each".
    if getattr(example, "form_template", None):
        slot_text = " ".join(
            getattr(example, slot, "") or ""
            for slot in ("scenario", "need", "mapping", "resolution")
        )
        # Only flag enumerated numeral runs of length >=2 (a single
        # "one" is licit; a sequence of 3+ is the parametric-drift
        # signature).
        if re.search(
            r"\b(?:one,\s*two,\s*three|two,\s*three,\s*four|"
            r"three,\s*four,\s*five|four,\s*five,\s*six|"
            r"five,\s*six,\s*seven|six,\s*seven,\s*eight)\b",
            slot_text, re.IGNORECASE,
        ):
            issues.append(("PARAMETRIC_LITERAL_NUMERALS",
                           "parametric example has enumerated English "
                           "numerals (one, two, three, …) hard-coded in "
                           "a story slot — won't track the actual draws "
                           "that {form_template} produces"))

    # REPL_AS_TIME_TRAVELLER — meta-narrator phrases implying the
    # answer pre-existed evaluation. "had been there all along",
    # "the value the operation called for", "the precise number the
    # operation called for". These foreground the concept of an
    # external graded answer rather than the form's evaluated value.
    if re.search(
        r"\b(?:had been there all along|the value the operation "
        r"called for|the (?:precise|exact) number the operation "
        r"called for|the answer that had been waiting)\b",
        user,
    ):
        issues.append(("REPL_AS_TIME_TRAVELLER",
                       "user_msg uses meta-narrator language that "
                       "implies the answer pre-existed evaluation — "
                       "describe the form's evaluation, not a "
                       "pre-existing 'right' answer"))

    # ─────────── slice xe8M (dog-shadow) detector additions ───────────
    #
    # Three new detectors authored during the dog-shadow hand audit
    # (slice xe8M, branch claude/audit-dog-shadow-xe8M). Each surfaces
    # a Cat-K storytelling-coherence pattern that detectors did not
    # previously catch.

    # NARRATIVE_NUMERAL_HARDCODE — when example.form_template is set
    # (form is parametric and operands are drawn at render time), the
    # scenario / need / mapping / resolution slots SHOULDN'T hard-code
    # English-numeral count phrases like "five bones", "ten stones",
    # "three bundles" since those drift from the actual draws.
    # Distinct from PARAMETRIC_LITERAL_NUMERALS (which only catches
    # enumerations like "one, two, three, four, five"). This catches
    # the singleton-numeral-quantifier pattern.
    if getattr(example, "form_template", None):
        slot_text = " ".join(
            getattr(example, slot, "") or ""
            for slot in ("scenario", "need", "mapping", "resolution")
        )
        # Only flag if a slot quantifies a count using a fixed English
        # numeral immediately followed by a content noun. Restricted
        # to count-words 3-10 to avoid catching grammatical "one bone"
        # / "a single line".
        m = re.search(
            r"\b(three|four|five|six|seven|eight|nine|ten)\s+"
            r"(bones?|stones?|bundles?|piles?|heaps?|values?|"
            r"numbers?|counts?|integers?|elements?|items?)\b",
            slot_text, re.IGNORECASE,
        )
        if m:
            issues.append(("NARRATIVE_NUMERAL_HARDCODE",
                           f"parametric example has hard-coded English "
                           f"numeral '{m.group(0)}' in a story slot — "
                           f"the actual draws may differ from this fixed "
                           f"count"))

    # META_FILLER_RESOLUTION — generic resolution phrases that don't
    # close the loop on what the form computed. "Returned exactly",
    # "settled with certainty", "handed back with certainty",
    # "the answer was exact" — these are template-output filler that
    # tells the reader the runtime gave a value (which is trivially
    # true) without saying what the value WAS or what made it land.
    # Cat-K K-3 (AI-output cadence) / K-4 (missing causality).
    META_FILLER_RES_RE = re.compile(
        r"\b(?:settled with certainty|handed back with certainty|"
        r"the (?:answer|result|product|sum|tally) was exact|"
        r"returned with certainty|with certainty\.|returned exactly\.|"
        r"returned exact\.)",
    )
    if META_FILLER_RES_RE.search(user):
        issues.append(("META_FILLER_RESOLUTION",
                       "user_msg uses generic 'returned exactly' / "
                       "'settled with certainty' filler — describe what "
                       "actually came back, not just that something did"))

    # FORM_DISPLAY_AND_FORM_NOUN — when {form_display} (the rendered
    # backticked form) appears in close proximity with "the form" used
    # as a noun phrase (template tic). Distinct from THE_FORM_OVERUSE
    # which counts global "the form" occurrences; this targets the
    # specific co-location pattern: backticked form + "the form ..."
    # within ~120 chars. Cat-I distraction (over-explained transitions).
    backtick_form_re = re.compile(r"`[^`]*`")
    backticks = list(backtick_form_re.finditer(user))
    flagged_form_collision = False
    for m in backticks:
        # Skip very short backticked tokens (e.g. `let`, `if`).
        if m.end() - m.start() < 5:
            continue
        nearby = user[m.end():m.end() + 120]
        if re.search(r"\bthe form\b", nearby, re.IGNORECASE):
            flagged_form_collision = True
            break
    if flagged_form_collision:
        issues.append(("FORM_DISPLAY_AND_FORM_NOUN",
                       "user_msg places `<form>` adjacent to a 'the "
                       "form ...' noun-phrase reference within 120 "
                       "chars — template tic that doubles the form "
                       "reference (vary the second mention)"))

    # Both modes are LOW_GROUNDING.
    _check_grounding(user, rec, issues)

    # ─────────── slice QVez (dog-shadow) detector additions ────────────

    # GOAL_TEXT_REPETITION — `{goal_text}` rendered three or more times
    # in the same user_msg. Catches templates that drop the goal_text in
    # multiple beats (intro + question + connective) without restating
    # the action; the resulting prose feels like an over-explained
    # tutorial instead of a scenario.
    if example.goal_text and len(example.goal_text) >= 12:
        gt = example.goal_text.strip(".? ")
        # Count case-insensitive overlapping-free occurrences.
        if gt and user.lower().count(gt.lower()) >= 3:
            issues.append(("GOAL_TEXT_REPETITION",
                            f"goal_text {gt[:40]!r} repeated {user.lower().count(gt.lower())}× in user_msg"))

    # PATIENT_ROLE_BOASTFUL — for fables whose patient/evaluator
    # character is named (tortoise / farmer / hound / elder), flag any
    # record that places a clearly-boastful EMO phrase in the same
    # sentence as that character's name. This is a polarity-flip
    # signal: the patient role should never be the one boasting.
    boastful_markers = (
        "with a smug grin", "puffed up with pride", "boasting at every",
        "loudly claiming the credit", "with the broad voice of a bragging",
        "with great whoops of laughter", "with the swagger of an unrepentant",
    )
    patient_names = {
        "tortoise": ("Mossback", "Slowpoke", "Shelly"),
        "milkmaid": ("the farmer", "Farmer"),
        "boy_wolf": ("the elder", "the villager", "Carol"),
        "dog_shadow": ("the hound", "Hound"),
        "crow_pitcher": ("the crow", "Crow"),
    }
    fable_id = sub.fable.replace("-", "_") if hasattr(sub, "fable") else ""
    if fable_id in patient_names:
        for name in patient_names[fable_id]:
            for sentence in re.split(r"[.!?]\s+", user):
                if name in sentence:
                    for bm in boastful_markers:
                        if bm in sentence:
                            issues.append(("PATIENT_ROLE_BOASTFUL",
                                            f"patient role {name!r} co-occurs with "
                                            f"boastful EMO phrase {bm[:30]!r}"))
                            break
                    else:
                        continue
                    break

    # STORY_RESOLUTION_NO_DRAWN — for story-tagged examples, the
    # `resolution` slot should reference at least one drawn-from-form
    # literal so the resolution closes the algorithmic loop, not just a
    # generic "the REPL returned the value." Skips examples that don't
    # have story tags and skips when the form has no extractable
    # literals to begin with.
    #
    # Parametric examples (form_template + slots) interpolate drawn
    # values via `{drawn.<slot>}` placeholders. A resolution that
    # contains `{drawn.X}` IS closing the loop — the renderer will
    # substitute the actual drawn value at render time. Treat any
    # `{drawn.<slot>}` placeholder in the resolution as a positive
    # signal so this detector doesn't penalize parametric authoring.
    if "story" in getattr(example, "tags", ()) and example.resolution:
        form = rec.code_str or ""
        lits = _drawn_literals(form)
        if lits:
            res_text = example.resolution
            # A drawn-value reference closes the loop if ANY of the four
            # story slots (scenario / need / mapping / resolution) contains
            # either a form-literal or a `{drawn.<slot>}` placeholder.
            slots_text = " ".join(filter(None, (
                getattr(example, "scenario", ""),
                getattr(example, "need", ""),
                getattr(example, "mapping", ""),
                res_text,
            )))
            has_lit = any(
                (lit and lit in slots_text) for lit in lits
            )
            has_drawn_placeholder = "{drawn." in slots_text
            if not has_lit and not has_drawn_placeholder:
                issues.append(("STORY_RESOLUTION_NO_DRAWN",
                                f"story-tagged example's resolution slot has no "
                                f"drawn-value reference (form has literals "
                                f"{lits[:3]!r}, resolution doesn't close the loop)"))

    # ─────────── slice QTA5 (tortoise-hare) detector additions ─────────

    # PROCEDURAL_OPENER — body jumps straight to "To {goal}, he/she
    # composed ..." without any prior scene-setting sentence. After
    # the fable opener line (first paragraph), the first content
    # sentence should introduce a character / place; jumping
    # immediately to "To X, she composed Y" reads like a stage
    # direction, not a story. Detection: a `\n\nTo ` immediately
    # followed by an action-clause within the first 350 chars of
    # user_msg.
    procedural_opener_re = re.compile(
        r"^(?:[^\n]{1,300}\n\n)?To [^,\n]+,\s+(?:he|she|they)\s+"
        r"(?:composed|wrote|chose|set|took|reached|laid|scratched|"
        r"intended|coordinated|dispatched|built|read)",
        re.IGNORECASE,
    )
    if procedural_opener_re.match(user):
        issues.append(("PROCEDURAL_OPENER",
                        "user_msg jumps from fable-opener directly to "
                        "'To {goal}, [pronoun] composed ...' without a "
                        "scene-setting sentence"))

    # STIFF_DIALOGUE_TAG — 3+ DIALOGUE-attribution "said" tags in the
    # same user_msg, no variation. Counts only attribution patterns
    # ("[Name|pronoun] said", `," X said`, etc.), not "saying" inside
    # an EMO phrase or "says true" inside metaphor prose.
    said_attrib_re = re.compile(
        r'(?:'
        r'"\s*,?\s+(?:he|she|they|[A-Z][a-z]+)(?:\s+the\s+\w+)?\s+said\b'
        r'|\b[A-Z][a-z]+(?:\s+the\s+\w+)?\s+said\b'
        r'|\b(?:he|she|they)\s+said\b'
        r'|\bsaid\s*,'
        r')',
    )
    n_said = len(said_attrib_re.findall(user))
    if n_said >= 3:
        issues.append(("STIFF_DIALOGUE_TAG",
                        f"user_msg has {n_said} 'said'-form attributions "
                        "(stiff repetition; vary the speech verb)"))

    # PRONOUN_BEFORE_NAME — a sentence-initial 'He'/'She'/'They'
    # appears before any character name has been introduced in the
    # user_msg. The pronoun has no antecedent. Detection: split into
    # sentences; if the first sentence starting with "He"/"She"/
    # "They" precedes any character name (look for "[Capital] the
    # [species]" pattern, or any of the canonical names from the
    # fable's character pool). For tortoise-hare the canonical names
    # include: Mossback, Slowpoke, Furrow, Bough, Tuber, Snail,
    # Rush, Daisy, Hopper, Whisker, Dash, Sprig, Polecat, Shuffle.
    # Cheap test: search for "[A-Z][a-z]+ the (tortoise|hare)" and
    # for sentence-initial "(He|She|They)" — flag if pronoun
    # position < first-name position.
    pronoun_match = re.search(r"(?:^|\.\s+|\n)(He|She|They)\s+\w", user)
    name_match = re.search(
        r"\b([A-Z][a-z]{2,})(?: the (?:tortoise|hare|crow|dog|hound|"
        r"shepherd|elder|villager|farmer|milkmaid|ant|grasshopper))?\b",
        user,
    )
    if (pronoun_match and name_match and
            pronoun_match.start() < name_match.start()):
        # Only flag when no character name appears in the first 200
        # chars (otherwise the pronoun likely refers to a name set
        # in dialogue, which is fine).
        head = user[:200]
        if not re.search(r"\b[A-Z][a-z]{2,}\s+the\s+\w+", head):
            issues.append(("PRONOUN_BEFORE_NAME",
                            f"sentence-initial '{pronoun_match.group(1)}' "
                            "appears before any named character is "
                            "introduced"))
    # ─────────── crow-pitcher audit slice (claude/audit-crow-pitcher-kaLA) ──
    #
    # Three new detectors added by this slice. None duplicates an
    # existing one (verified by greping `issues.append` for the codes
    # before authoring).

    # MULTIPLE_SAID_TAGS — three or more "said" dialogue tags in one
    # user_msg. Records with that many attribution tags read like
    # over-announced theatre rather than a flowing narrative; the model
    # learns the dialogue structure better when characters' speech is
    # tagged sparingly. Threshold 3 catches the worst offenders without
    # flagging legitimate two-character exchanges.
    n_said_tags = len(re.findall(r"\b(said|replied|answered|asked|cried|"
                                   r"declared|exclaimed|whispered)\b,?\s+\"",
                                   user))
    if n_said_tags >= 3:
        issues.append(("MULTIPLE_SAID_TAGS",
                        f"user_msg has {n_said_tags} dialogue-attribution "
                        "tags — over-announcing the speakers"))

    # REPEATED_OPENER_FRAGMENT — a clause-length fragment from the
    # user_msg's first sentence appears verbatim later in the same
    # user_msg. Catches templates whose subplot body re-uses an
    # aesopian-opener clause word-for-word (e.g., "At the foot of a
    # tall pitcher" appearing twice). Walks every 4-7-word ngram of
    # the first sentence; if any one of those phrase-grams reappears
    # in the rest of the user_msg, flag.
    first_sent_end = re.search(r"[.!?](?:\s|$)", user)
    if first_sent_end:
        first_sent = user[:first_sent_end.start()]
        rest = user[first_sent_end.end():]
        words = first_sent.split()
        for n in (7, 6, 5):
            if len(words) < n:
                continue
            for i in range(len(words) - n + 1):
                gram = " ".join(words[i:i + n])
                if len(gram) >= 25 and gram in rest:
                    issues.append(("REPEATED_OPENER_FRAGMENT",
                                    f"opener fragment {gram!r} also appears "
                                    "later in user_msg"))
                    break
            else:
                continue
            break

    # METAPHOR_DISAPPEARS — fable-keyed check: the rendered prose
    # mentions none of the fable's primary metaphor nouns. Crow-pitcher
    # records that don't reference pitcher / water / pebble / stone /
    # throat / rim — the central imagery — have lost the metaphor
    # entirely (a Cat-F polarity-adjacent failure mode). Same shape
    # extends to other fables; see _METAPHOR_NOUNS table.
    fable_name = getattr(sub, "fable", "") or ""
    metaphor_nouns = _METAPHOR_NOUNS.get(fable_name, ())
    if metaphor_nouns:
        ul = user.lower()
        if not any(n in ul for n in metaphor_nouns):
            issues.append(("METAPHOR_DISAPPEARS",
                            f"user_msg has none of the fable's primary "
                            f"metaphor nouns ({', '.join(metaphor_nouns[:4])}...)"))
    # ─────────── slice eUtZ (boy-wolf) detector additions ────────────

    # THE_FORM_OVERUSE — boy-wolf 0HIm-style templates string together
    # "the form" 5+ times in close succession ("the REPL ran the form
    # against the form, then the form's scope handed back the form
    # the form had requested"). Five+ occurrences in one rendered
    # user_msg reads as a tic, not as natural English. Cat-I
    # (distractions: over-announcing the operation).
    if user.lower().count("the form") >= 5:
        issues.append(("THE_FORM_OVERUSE",
                       f"`the form` appears "
                       f"{user.lower().count('the form')} times in "
                       "user_msg (template tic — vary references)"))

    # HONEST_JUDGE_REPEAT — boy-wolf-specific bombast: "honest as the
    # watchhouse slate" plus "the only honest judge" plus "honestly
    # answered" stack up across the goal-template + story-scaffold
    # closing. Two "honest" hits in one record reads as moralizing.
    # Cat-G (emotional / tone — pretentious closing).
    if sub.fable == "boy-wolf" and len(re.findall(r"\bhonest", user.lower())) >= 2:
        issues.append(("HONEST_JUDGE_REPEAT",
                       "two or more 'honest' uses in one boy-wolf "
                       "user_msg (judge-bombast tic — drop one)"))

    # VILLAGE_NOUN_OVERUSE — boy-wolf template-tic: "the village" used
    # 4+ times (one in opener, one in story-scaffold, one in
    # resolution, plus extras from per-template). Drains the noun of
    # specificity. Cat-I distraction.
    if sub.fable == "boy-wolf" and user.lower().count("the village") >= 4:
        issues.append(("VILLAGE_NOUN_OVERUSE",
                       f"`the village` appears "
                       f"{user.lower().count('the village')} times "
                       "(noun-saturation tic — vary or drop)"))

    # ─────── slice ncvo (crow_pitcher "make it make sense") detectors ───────

    # CONCEPT_PHRASE_COMMA_LIST — `concept_phrase` rendered as 3+
    # comma-separated bare tokens (no determiner / preposition / noun-
    # phrase shape). Reads as a comma-list of operation names instead
    # of a noun phrase the template can interpolate naturally.
    # Examples caught: "atom, swap, deref" / "agent, send, await,
    # deref" / "lock, locking, literal".
    cp = example.concept_phrase or ""
    cp_tokens = [t.strip() for t in cp.split(",")]
    if len(cp_tokens) >= 3 and all(
        len(t.split()) <= 3 and t and not re.match(
            r"^(?:the|a|an|of|with|for|by|to|on|in|at|as|its|from|"
            r"that|after|before|over|under|inside|past|along|through|"
            r"whose|which)\b",
            t.lower(),
        )
        for t in cp_tokens
    ):
        issues.append(("CONCEPT_PHRASE_COMMA_LIST",
                        f"concept_phrase {cp!r} is a comma-list of bare "
                        "tokens — rewrite as a noun phrase that flows "
                        "into subplot prose"))

    # AI_OUTPUT_CADENCE — sentences with the "with the X of one who Y"
    # / "with the X of someone who Y" elaborate-clause-stack cadence.
    # This pattern reads as model-generated rather than fable-prose;
    # it usually accompanies tight clause-stacks that decorate without
    # narrative work.
    ai_cadence_re = re.compile(
        r"\bwith the [a-z]+ of (?:one|someone|a [a-z]+|an [a-z]+) "
        r"who\b",
    )
    if ai_cadence_re.search(user):
        issues.append(("AI_OUTPUT_CADENCE",
                        "user_msg has 'with the X of one who Y' "
                        "elaborate-clause-stack cadence (reads like "
                        "model output, not storybook prose)"))

    # RESOLUTION_GENERIC — the user_msg's resolution beat is canned
    # boilerplate ("the count of whatever the operation had produced",
    # "the precise number the operation called for", "the value the
    # operation had produced", etc.) that doesn't tie back to the
    # fable's metaphor or the drawn values. Cat-K-6 (under-earned
    # metaphor) source signal.
    canned_resolution_re = re.compile(
        r"\b(?:the (?:count|value|number|answer)) of (?:whatever|"
        r"the operation|the runtime|the call) (?:[a-z]+ )?"
        r"(?:had )?(?:produced|called for|returned|computed)"
        r"|the precise (?:count|number|value|answer) "
        r"the (?:operation|runtime|call) called for"
        r"|the value the (?:operation|runtime|call) "
        r"(?:had )?produced",
    )
    if canned_resolution_re.search(user):
        issues.append(("RESOLUTION_GENERIC",
                        "user_msg has canned 'the X the operation "
                        "produced' resolution boilerplate — tie it to "
                        "the fable's metaphor / drawn values"))
    # ─────────── slice XOE6 (boy-wolf, Cat-K theme) detector additions ────────────

    # EMPTY_GOAL_RENDERED — when the {goal_text} placeholder is empty
    # but the template still wraps it in "To {goal_text}, X composed",
    # the user_msg renders with the abandoned phrase "To , X composed"
    # (or "To , he composed", "To , she composed"). Cat-A logical: this
    # makes the sentence read as if a noun got dropped between "To"
    # and the comma.
    if re.search(r"\bTo\s*,\s*(?:he|she|they|[A-Z]\w+)\s+composed\b", user):
        issues.append(("EMPTY_GOAL_RENDERED",
                       "user_msg has 'To , <pronoun> composed' — the "
                       "{goal_text} placeholder rendered empty (audited "
                       "by boy-wolf XOE6)"))

    # STRING_AS_CHAR_MISCLAIM — a record's form is a string literal
    # ("foo") but the prose calls it "the character \\foo" (using
    # Clojure's `\` char prefix). Cat-E semantic: the concept_phrase
    # contradicts the form's actual type. Caught when reading G1-08
    # records where the form was a multi-character string but the
    # template's concept_phrase still used the char idiom.
    code = (rec.code_str or "").strip()
    if code.startswith('"') and code.endswith('"') and len(code) >= 4:
        # form is a multi-char string. Look for "the character \X" or
        # "the value \X" where X is a string fragment.
        if re.search(r"\bthe character \\[a-zA-Z]{2,}", user):
            issues.append(("STRING_AS_CHAR_MISCLAIM",
                           "form is a multi-character string but the "
                           "prose refers to it as a single character "
                           r"(`the character \X` idiom)"))

    # PARAGRAPH_FRAGMENTATION — 4+ very short paragraphs in a row
    # each making one statement. Reads as a bullet-listed manual
    # rather than a fable. Cat-K K-2 pacing failure (rendered when
    # scenario / need / mapping / resolution slots each consume one
    # short paragraph and the story-scaffold connector adds another).
    paragraphs = [p for p in user.split("\n\n") if p.strip()]
    if len(paragraphs) >= 5:
        # Count short paragraphs (≤ 25 words) in the body
        # (skipping the opener and the question line).
        short_count = sum(
            1 for p in paragraphs[1:-1]
            if len(p.split()) <= 25
        )
        if short_count >= 4:
            issues.append(("PARAGRAPH_FRAGMENTATION",
                           f"user_msg has {short_count} short "
                           "(≤25-word) paragraphs in body — reads "
                           "as a bullet list, not a story"))
    # ─────────── slice GrkS (dog-shadow) detector additions ────────────
    #
    # Three new detectors targeting Cat-K storytelling failures the
    # existing 60+ detectors don't catch.

    # OUT_OF_REGISTER_CONNECTIVE — Cat-K-5: vocabulary register doesn't
    # fit a children's storybook. Words like "thereby", "consequently",
    # "thus", "henceforth", "moreover", "furthermore" mark formal
    # academic prose, not a fable about a dog and a reflection.
    # Children's storybook reading-level prose uses "and so", "then",
    # "because" instead.
    if re.search(
        r"\b(thereby|consequently|henceforth|moreover|furthermore|"
        r"insofar|inasmuch|notwithstanding|whereupon|whereunto)\b",
        user, re.IGNORECASE
    ):
        m = re.search(
            r"\b(thereby|consequently|henceforth|moreover|furthermore|"
            r"insofar|inasmuch|notwithstanding|whereupon|whereunto)\b",
            user, re.IGNORECASE
        )
        issues.append(("OUT_OF_REGISTER_CONNECTIVE",
                        f"formal-academic connective {m.group(0)!r} in user_msg "
                        "— storybook register should be 5th-grade reading level"))

    # DOUBLE_NAME_INTRO — Cat-K-1 / Cat-H: same character introduced
    # twice as "<Name> the <species>" within ~120 chars. Pacing
    # failure: a name introduction is a one-time-per-record beat, and
    # repeating it within a few sentences reads as a template-stitch
    # error rather than story prose.
    name_intro_re = re.compile(
        r"\b([A-Z][a-z]+) the (hound|dog|crow|tortoise|hare|farmer|"
        r"milkmaid|elder|shepherd|villager|fox)\b"
    )
    intros = list(name_intro_re.finditer(user))
    seen_intros = {}
    for m in intros:
        key = (m.group(1), m.group(2))
        if key in seen_intros:
            prev_end = seen_intros[key]
            if m.start() - prev_end <= 200:
                issues.append(("DOUBLE_NAME_INTRO",
                                f"character {m.group(0)!r} introduced twice "
                                f"within 200 chars — drop the second 'the {m.group(2)}'"))
                break
        seen_intros[key] = m.end()

    # HEDGING_NEAR_FORM — Cat-K-3 / Cat-A-adjacent: prose hedges about
    # what the form does ("or something close to it", "more or less",
    # "approximately what it returns", "roughly the value", "kind of
    # like X"). The eval-deterministic curriculum's narrative voice
    # should be confident — the form returns exactly what it returns.
    # Hedging signals an AI cadence that's covering its uncertainty.
    if re.search(
        r"\b(or something close to it|more or less|"
        r"approximately what|roughly the value|kind of like|"
        r"sort of like|in a sense it|as it were)\b",
        user, re.IGNORECASE
    ):
        m = re.search(
            r"\b(or something close to it|more or less|"
            r"approximately what|roughly the value|kind of like|"
            r"sort of like|in a sense it|as it were)\b",
            user, re.IGNORECASE
        )
        issues.append(("HEDGING_NEAR_FORM",
                        f"hedge {m.group(0)!r} in user_msg — eval-deterministic "
                        "narratives shouldn't hedge about the form's value"))
    # ─────────── slice jDPM (dog-shadow) — Cat-K structural detectors ─

    # CLAUSE_STACK_OVERFLOW (K-3) — a single sentence with 4+ comma-
    # separated clauses, often produced by the "X did Y, with the Z of
    # one who W, and the result of A, was B" template-output cadence.
    # 5+ commas inside a single sentence is almost always a sign of
    # template-output rhythm rather than fable prose.
    for sentence in re.split(r"[.!?]\s+", user):
        # Skip dialogue-quoted sentences (lots of internal commas
        # legitimately) and Clojure form snippets.
        if "`" in sentence or sentence.count('"') >= 2:
            continue
        n_commas = sentence.count(",")
        if n_commas >= 5 and len(sentence) > 60:
            issues.append(("CLAUSE_STACK_OVERFLOW",
                            f"sentence with {n_commas} commas reads as "
                            f"AI-output cadence: {sentence[:80]!r}"))
            break

    # AS_ONE_WHO_CADENCE (K-3) — the signature "as one who X" /
    # "with the Y of one who Z" / "in the Z of one who Y" cadence is
    # the most reliable AI-output signal in fable prose. A real
    # children's-fable register uses concrete actions, not
    # appositive-of-appositive structures.
    if re.search(
        r"\b(?:as one who|as a [a-z]+ who|with the [a-z ]+ of one who|"
        r"in the [a-z ]+ of one who)\b",
        user,
    ):
        issues.append(("AS_ONE_WHO_CADENCE",
                        "user_msg contains 'as one who…' / 'with the X "
                        "of one who Y' template-output cadence"))

    # OUT_OF_REGISTER_VOCAB (K-5) — words that don't belong in a
    # 5th-grade-reading-level fable: "thereby", "consequently",
    # "henceforth", "hitherto", "ostensibly", "moreover",
    # "notwithstanding", "purportedly", "qua", "wherein", "whereby".
    if re.search(
        r"\b(?:thereby|consequently|henceforth|hitherto|ostensibly|"
        r"moreover|notwithstanding|purportedly|wherein|whereby|"
        r"insofar|inasmuch|qua)\b",
        user,
        re.IGNORECASE,
    ):
        issues.append(("OUT_OF_REGISTER_VOCAB",
                        "user_msg uses an out-of-register word that "
                        "doesn't fit a children's-fable register"))

    return issues


# Per-fable primary metaphor nouns. A record that mentions none of these
# has lost the metaphor — a sign that the template fired without
# fable-specific imagery (often a tortoise-hare-shaped template carried
# across without lifting). Conservative: only the fables I've audited
# get listed; absent fables don't trigger this check.
_METAPHOR_NOUNS = {
    "crow-pitcher":  ("pitcher", "water", "pebble", "stone", "throat",
                      "rim", "crow"),
}


# Cached EMO-pool fragments for fast LOW_GROUNDING detection.
_EMO_FRAGMENTS = None


def _emo_fragments():
    """Distinctive opening fragments from the rich EMO pools so we can
    detect whether the user_msg carries an environment-anchored emotion
    phrase (as opposed to a bare adverb)."""
    global _EMO_FRAGMENTS
    if _EMO_FRAGMENTS is not None:
        return _EMO_FRAGMENTS
    try:
        from mmllm.aesop.fables import (
            EMO_PROUD, EMO_PATIENT, EMO_REGRETFUL, EMO_CONTENT,
            EMO_DESPERATE, EMO_HUNGRY,
        )
    except ImportError:
        _EMO_FRAGMENTS = ()
        return _EMO_FRAGMENTS
    pools = (EMO_PROUD, EMO_PATIENT, EMO_REGRETFUL, EMO_CONTENT,
             EMO_DESPERATE, EMO_HUNGRY)
    # ALSO include the integration branch's full archetype pools so
    # records that draw from the larger 33+ entry pools register as
    # grounded. The legacy fables.py pools are short (≤8 entries); the
    # emotion_pools versions overlap heavily but include extra
    # environment-anchored variants the detector should recognize.
    try:
        from mmllm.aesop.curriculum.emotion_pools import (
            EMO_PROUD as EP_PROUD2, EMO_PATIENT as EP_PATIENT2,
            EMO_REGRETFUL as EP_REGRETFUL2, EMO_CONTENT as EP_CONTENT2,
            EMO_DESPERATE as EP_DESPERATE2, EMO_HUNGRY as EP_HUNGRY2,
            EMO_TIRED as EP_TIRED2, EMO_THIRSTY as EP_THIRSTY2,
            EMO_GREEDY as EP_GREEDY2, EMO_SUSPICIOUS as EP_SUSPICIOUS2,
            EMO_BOASTFUL, EMO_CAUTIOUS,
        )
        pools = pools + (
            EP_PROUD2, EP_PATIENT2, EP_REGRETFUL2, EP_CONTENT2,
            EP_DESPERATE2, EP_HUNGRY2, EP_TIRED2, EP_THIRSTY2,
            EP_GREEDY2, EP_SUSPICIOUS2,
            EMO_BOASTFUL, EMO_CAUTIOUS,
        )
    except ImportError:
        pass
    # Crow-pitcher-specific EMO pools (CP_EMO_*) live in generator.py
    # and are what the crow-pitcher renderer actually draws from. Without
    # them in the marker set, every crow-pitcher record would fail the
    # EMO half of LOW_GROUNDING even when the renderer emits a rich
    # EMO phrase. (Same goes for any other fable's bespoke pools.)
    try:
        from mmllm.aesop.curriculum.generator import (
            CP_EMO_PATIENT, CP_EMO_PROUD, CP_EMO_THIRSTY,
            GE_EMO_GREEDY, GE_EMO_CONTENT, GE_EMO_REGRETFUL,
        )
        pools = pools + (CP_EMO_PATIENT, CP_EMO_PROUD, CP_EMO_THIRSTY,
                          GE_EMO_GREEDY, GE_EMO_CONTENT, GE_EMO_REGRETFUL)
    except ImportError:
        pass
    out = set()
    for pool in pools:
        for phrase in pool:
            # Use the first 12-20 characters as the distinctive fragment.
            frag = phrase[:18].lower().rstrip(",.!?;:")
            if len(frag) >= 8:
                out.add(frag)
    _EMO_FRAGMENTS = tuple(out)
    return _EMO_FRAGMENTS


def _drawn_literals(form: str):
    """Extract distinctive scalar literals from a form for grounding
    detection: numbers, keywords, and string contents (>=2 chars)."""
    if not form:
        return ()
    literals = []
    # ints (positive + negative)
    for m in re.finditer(r"-?\d+", form):
        v = m.group(0)
        # Skip very common numbers that appear ambient in prose.
        if v not in ("0", "1", "2"):
            literals.append(v)
    # keywords (:foo)
    for m in re.finditer(r":[a-zA-Z][a-zA-Z0-9-]*", form):
        literals.append(m.group(0))
    # double-quoted strings
    for m in re.finditer(r'"([^"]{2,})"', form):
        literals.append(m.group(1))
    return tuple(literals)


def _check_grounding(user, rec, issues):
    """LOW_GROUNDING — affirmative Cat-J check."""
    user_lower = user.lower()
    # generic-adverb shortcut: presence of bare adverbs without an
    # accompanying rich EMO fragment.
    has_generic_adverb = bool(re.search(
        r"\bsaid (softly|quietly|gently|calmly)\b", user_lower
    ))
    has_emo_fragment = any(frag in user_lower for frag in _emo_fragments())
    if has_generic_adverb and not has_emo_fragment:
        issues.append(("LOW_GROUNDING",
                        "user_msg uses a bare 'said softly/quietly/"
                        "gently/calmly' adverb without a rich EMO phrase"))
        return
    # total grounding deficit: no drawn-literal reference AND no EMO
    # fragment.
    literals = _drawn_literals(rec.code_str)
    has_literal_in_user = False
    for lit in literals:
        if lit and lit in user:
            has_literal_in_user = True
            break
    if not has_literal_in_user and not has_emo_fragment:
        issues.append(("LOW_GROUNDING",
                        "user_msg lacks both a form-literal anchor and "
                        "an EMO-pool phrase — no environmental grounding"))


def per_example_records(sub, example, n: int, seed: int):
    """Generate `n` records for ONE specific example.

    Legacy examples (form_template empty): filter by code_str ==
    example.form, since every record renders the same form string.

    Parametric examples (form_template set): each record renders a
    DIFFERENT form string drawn from slot pools, so equality
    filtering never matches. Stride into generate_subject's output
    instead — records are emitted in example-order, so example-index
    gives us the right offset.
    """
    is_parametric = bool(getattr(example, "form_template", ""))
    if is_parametric:
        ex_idx = sub.examples.index(example)
        recs = generate_subject(sub, n_per_example=n, seed=seed)
        start = ex_idx * n
        return recs[start:start + n]
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
