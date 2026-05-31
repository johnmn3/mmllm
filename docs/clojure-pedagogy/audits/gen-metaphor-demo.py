"""Generate metaphor-demo-{fable}.md for any fable.

Mirrors metaphor-demo-tortoise-hare.md structure: one canonical subject
per metaphor family. For each, a story-scaffold render (using authored
slots) and a family-template render (different seed → different generic
template) so the variety lands.

Usage:
    FABLE=crow_pitcher python3 gen-metaphor-demo.py
"""
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import generate_subject


FABLE = os.environ.get("FABLE", "crow_pitcher")
FABLE_DASH = FABLE.replace("_", "-")

# Metaphor annotations per family (1-2 sentences). Crow-pitcher imagery
# from docs/clojure-pedagogy/audits/metaphor-imagery-crow-pitcher.md.
ANNOTATIONS = {
    "crow_pitcher": {
        "atom": "For atoms (literals), the form IS the answer. The user_msg deliberately shows the form (`{form_display}`); copy-from-prompt is the lesson — submit the literal as-is.",
        "_POUCH_SUBPLOTS": "The clever crow tucks an intermediate value under one wing — held only for the stretch where the form needs it. After the drop, the wing opens again: the value existed only inside the form's reach. Mirrors `let`-binding scope.",
        "_RECIPE_SUBPLOTS": "The clever crow scratches a step-by-step drop-order into the pitcher's clay rim — a pattern any crow can follow. Same recipe, different stones each time. Mirrors `fn` / `defn`.",
        "_BASKET_SUBPLOTS": "The crow's gathered stone-pile sits beside the pitcher, each stone in place. Dropping a new stone doesn't move the ones already piled — the pile is the original arrangement. Mirrors persistent collections.",
        "_SIEVE_SUBPLOTS": "The crow holds each stone over the pitcher's mouth and decides: smooth round ones go in, jagged or flat ones are set aside. The rule filters the whole pile. Mirrors `filter` / `map` / transducers.",
        "_NOTEBOOK_SUBPLOTS": "The crow scratches a tally mark into the pitcher's clay face each time the water level rises — the mark persists, updated stone by stone, visible to any crow who perches there later. Mirrors `atom` / `ref` / mutable state.",
        "_ACORN_SUBPLOTS": "The clever crow counts smooth stones from the meadow floor, adding, dividing, or subtracting to calculate exactly how many more drops will raise the water. Mirrors arithmetic.",
        "_GATE_SUBPLOTS": "The crow can only drink if two gates clear in sequence — the pitcher must be deep enough AND the water must have risen past the threshold. One gate closed, no drink. Mirrors `and` / `or` / equality.",
        "_FORK_SUBPLOTS": "Perched above the pitcher's mouth, the crow decides: if the water already clears the mark, lower the beak; else drop another stone. The branch in the form is the branch on the perch. Mirrors `if` / `cond`.",
        "_ROADSIGN_SUBPLOTS": "The crow carves a name into the pitcher's clay rim — a marker any crow who perches there can read to know which calculation is stored at this spot. Mirrors `def` / namespace bindings.",
        "_SAFETYNET_SUBPLOTS": "The crow tests each stone over a soft patch of moss before committing — if the form fails, the moss catches the stone safely and the crow can try a different one without losing the water level. Mirrors `try` / `catch`.",
        "_SCROLL_SUBPLOTS": "The crow scratches an inscription into a smooth flat stone with the tip of her talon — written once in the moment, readable whenever another crow alights on the same stone later. Mirrors lazy seqs / IO.",
        "_GUILD_SUBPLOTS": "Any crow at the pitcher — Korvus, Caw, Sable — answers the same stone-drop call. Each raises the water the same amount per stone, each in their own rhythm. Mirrors protocols / polymorphism.",
        "_SORTINGTABLE_SUBPLOTS": "The pitcher's mouth has a sorting lip: stones marked with one groove go straight in; stones with two grooves are deflected. The mark on the stone decides the path. Mirrors multimethods / dispatch.",
        "_CARRYINGCASE_SUBPLOTS": "The clever crow weaves a carrying-pouch from bark strips and vine — a bespoke case with named slots for each kind of stone. The case's shape defines what fits inside. Mirrors `defrecord` / `deftype`.",
        "_TOOLSHED_SUBPLOTS": "The crow borrows an earthenware pitcher made by a human potter — a different maker's vessel, but the stone-drop sequence works the same. Mirrors Java interop.",
        "_RUNNERAHEAD_SUBPLOTS": "The clever crow sends a second crow ahead to count the stones at the far orchard — come back with the tally when done; meanwhile, keep dropping here. Mirrors agents / futures / promises.",
        "_REWRITERULE_SUBPLOTS": "The crow's talon rewrites the drop-order scratched on the rim before a single stone falls — a master revision that changes what the form will do before the REPL sees it. Mirrors `defmacro`.",
        "_SCRIBE_SUBPLOTS": "The talon-scratched notes on the clay: spacing between tally marks, parenthetical asides in the margin, shorthand that tells the REPL how to read the form before it evaluates. Mirrors reader conventions / comments.",
        "_CHALKMARK_SUBPLOTS": "The chalk mark scratched on a smooth stone names the stone — it is not the stone itself. The mark can be carried, quoted, passed around; only when the form runs does the mark become the stone's weight. Mirrors `quote` / symbols.",
        "_TALLYWALK_SUBPLOTS": "The crow walks the rim of the pitcher, dropping each stone in turn, carrying the running count in one talon — the tally grows with every drop until the last stone goes in. Mirrors `reduce` / `count`.",
        "_BEADSTRING_SUBPLOTS": "The crow threads smooth pebbles on a vine in a row — each pebble a character in the sequence, the whole vine a pebble-string. Joining two vines end-to-end extends the string. Mirrors strings / sequences.",
        "_CIRCUIT_SUBPLOTS": "The crow loops back to the stone-pile after each drop without lifting off the rim — stone after stone in a tight circuit, each iteration calling back to the start without growing the flight path. Mirrors `loop` / `recur`.",
    },
}


def load_modules(fable: str):
    mods = []
    for n in range(1, 13):
        try:
            mods.append(importlib.import_module(
                f"mmllm.aesop.curriculum.{fable}.grade_{n}"))
        except ModuleNotFoundError:
            break
    return mods


def get_pool_id(fable: str):
    """Map id(pool_object) → pool_name."""
    pool_mod = importlib.import_module(
        f"mmllm.aesop.curriculum.{fable}._metaphor_pools")
    pools = {}
    for name in dir(pool_mod):
        if name.endswith("_SUBPLOTS"):
            obj = getattr(pool_mod, name)
            pools[id(obj)] = name
    return pools


def find_canonical(modules, pool_ids):
    """For each metaphor family, find one subject+example with story slots."""
    canonicals = {}  # pool_name -> (sid, subject, example)
    for mod in modules:
        for sid, sub in mod.SUBJECTS.items():
            pool_name = pool_ids.get(id(sub.subplots), None)
            if pool_name is None:
                continue
            # Find an example with story slots
            for ex in sub.examples:
                if ex.scenario and ex.need and ex.mapping and ex.resolution \
                        and "story" in (ex.tags or ()):
                    if pool_name not in canonicals:
                        canonicals[pool_name] = (sid, sub, ex)
                    break
    return canonicals


def find_atom_subject(modules):
    """Find a literal-as-form atom subject (G1-01 style)."""
    for mod in modules:
        for sid, sub in mod.SUBJECTS.items():
            for ex in sub.examples:
                # Atoms: form is a single literal (no parens/whitespace)
                # Take the first one we find at G1
                if sub.grade == 1 and ex.form == "42":
                    return sid, sub, ex
    # Fallback: first literal-shaped form
    for mod in modules:
        for sid, sub in mod.SUBJECTS.items():
            for ex in sub.examples:
                if "(" not in ex.form and sub.grade == 1:
                    return sid, sub, ex
    return None


def render_record(sub, ex, seed):
    """Render exactly one record matching `ex.form` for sub at given seed."""
    from mmllm.aesop.curriculum.generator import generate_subject
    s = seed
    while s < seed + 500:
        recs = generate_subject(sub, n_per_example=1, seed=s)
        for r in recs:
            if r.code_str == ex.form:
                return r, s
        s += 1
    return None, None


def render_record_with_tag(sub, ex, seed, want_story_template):
    """Render a record where the chosen subplot template is/isn't a story template."""
    s = seed
    while s < seed + 1000:
        recs = generate_subject(sub, n_per_example=1, seed=s)
        for r in recs:
            if r.code_str != ex.form:
                continue
            # Heuristic: story-template renders contain '{scenario}'-derived
            # text segments (the scenario starts the message body, after
            # the opener). Check if scenario substring appears.
            if want_story_template:
                if ex.scenario and ex.scenario[:50] in r.user_msg:
                    return r, s
            else:
                if ex.scenario and ex.scenario[:50] not in r.user_msg:
                    return r, s
        s += 1
    return None, None


def fmt_record(r):
    """Format the user_msg + tool call as the demo doc shows it."""
    msg = r.user_msg
    return f"{msg}\n\n---\n\n{r.assistant_msg}"


def make_demo(fable: str):
    """Generate the demo doc."""
    modules = load_modules(fable)
    pool_ids = get_pool_id(fable)
    canonicals = find_canonical(modules, pool_ids)

    annotations = ANNOTATIONS.get(fable, {})
    out_path = Path(
        f"/home/user/mmllm/docs/clojure-pedagogy/audits/metaphor-demo-{fable.replace('_', '-')}.md"
    )

    # 22 family order matching imagery doc
    family_order = [
        "_POUCH_SUBPLOTS", "_RECIPE_SUBPLOTS", "_BASKET_SUBPLOTS",
        "_SIEVE_SUBPLOTS", "_NOTEBOOK_SUBPLOTS", "_ACORN_SUBPLOTS",
        "_GATE_SUBPLOTS", "_FORK_SUBPLOTS", "_ROADSIGN_SUBPLOTS",
        "_SAFETYNET_SUBPLOTS", "_SCROLL_SUBPLOTS", "_GUILD_SUBPLOTS",
        "_SORTINGTABLE_SUBPLOTS", "_CARRYINGCASE_SUBPLOTS",
        "_TOOLSHED_SUBPLOTS", "_RUNNERAHEAD_SUBPLOTS",
        "_REWRITERULE_SUBPLOTS", "_SCRIBE_SUBPLOTS",
        "_CHALKMARK_SUBPLOTS", "_TALLYWALK_SUBPLOTS",
        "_BEADSTRING_SUBPLOTS", "_CIRCUIT_SUBPLOTS",
    ]

    lines = []
    lines.append(f"# Metaphor demo — {fable.replace('_', '-')} curriculum\n")
    lines.append("One canonical subject per metaphor family. For each, two")
    lines.append("renders are shown:\n")
    lines.append("- **Story-scaffold render** — the example's authored")
    lines.append("  `scenario` / `need` / `mapping` / `resolution` slots")
    lines.append("  composed into a 5-act grounded story by the")
    lines.append("  `_story()` template (Phase C framework). The metaphor")
    lines.append("  *drives* the action — concrete situation, specific need,")
    lines.append("  explicit mapping, resolution that closes the loop.")
    lines.append("- **Family-template render** — one of the family pool's")
    lines.append("  generic templates, for contrast. Same example, no story")
    lines.append("  slots used.\n")

    # Quick coverage stats
    total_subj = sum(len(m.SUBJECTS) for m in modules)
    total_ex = sum(len(s.examples) for m in modules for s in m.SUBJECTS.values())
    story_ex = 0
    for m in modules:
        for s in m.SUBJECTS.values():
            for e in s.examples:
                if "story" in (e.tags or ()):
                    story_ex += 1

    lines.append(f"Coverage: 22 metaphor families + atoms + the goal-fallback")
    lines.append(f"for abstract subjects. Across {total_subj} subjects there are")
    lines.append(f"{total_ex} examples; {story_ex} carry story-scaffold slots.\n")
    lines.append("---\n")

    # ── ATOM render (G1-01-style)  ─────────────────────────────────────
    atom_data = find_atom_subject(modules)
    if atom_data:
        sid, sub, ex = atom_data
        lines.append(f"## atom — {sid}: {sub.subject_title}\n")
        lines.append("_pool_: `_SHARED_SUBPLOTS`\n")
        lines.append(f"**The metaphor:** {annotations.get('atom', '')}\n")
        lines.append("### Atom render\n")
        lines.append(f"**form**: `{ex.form}`  •  **expected**: `{ex.expected}`\n")
        rec, _ = render_record(sub, ex, seed=int(sid[3:].replace("-", "")) * 7)
        if rec:
            lines.append("````text")
            lines.append(fmt_record(rec))
            lines.append("````\n")
        lines.append("---\n")

    # ── one canonical per family ───────────────────────────────────────
    for pool_name in family_order:
        if pool_name not in canonicals:
            continue
        sid, sub, ex = canonicals[pool_name]
        title_label = pool_name.lstrip("_").replace("_SUBPLOTS", "").lower()
        lines.append(f"## {title_label} — {sid}: {sub.subject_title}\n")
        lines.append(f"_pool_: `{pool_name}`\n")
        lines.append(f"**The metaphor:** {annotations.get(pool_name, '')}\n")

        # Story render
        seed_base = int(sid[3:].replace("-", "")) * 7
        rec_story, _ = render_record_with_tag(sub, ex, seed_base,
                                              want_story_template=True)
        rec_generic, seed_g = render_record_with_tag(sub, ex, seed_base + 1000,
                                                     want_story_template=False)

        if rec_story:
            lines.append("### Story-scaffold render\n")
            lines.append(f"**form**: `{ex.form}`  •  **expected**: `{ex.expected}`\n")
            lines.append("````text")
            lines.append(fmt_record(rec_story))
            lines.append("````\n")

        if rec_generic:
            lines.append(f"### Family-template render _(seed {seed_g})_\n")
            lines.append(f"**form**: `{ex.form}`  •  **expected**: `{ex.expected}`\n")
            lines.append("````text")
            lines.append(fmt_record(rec_generic))
            lines.append("````\n")

        lines.append("---\n")

    out_path.write_text("\n".join(lines))
    print(f"wrote → {out_path}")
    print(f"  subjects: {total_subj}, examples: {total_ex}, story examples: {story_ex}")
    print(f"  families with canonicals: {len(canonicals)}/22")


if __name__ == "__main__":
    make_demo(FABLE)
