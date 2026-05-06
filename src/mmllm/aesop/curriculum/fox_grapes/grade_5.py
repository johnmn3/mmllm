"""Grade 5 — control flow + higher-order intro. Through fox-grapes.

Reuses the grade-1 8-subplot pool and adds two HOF-flavored subplots
in fox voice: the patient fox demonstrates how a single operation, when
mapped/reduced/applied across a cluster, settles a long calculation —
while the hasty fox keeps wanting to skip the eval entirely.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import (
    _CIRCUIT_SUBPLOTS,
    _FORK_SUBPLOTS,
    _GATE_SUBPLOTS,
    _RECIPE_SUBPLOTS,
    _SIEVE_SUBPLOTS,
    _TALLYWALK_SUBPLOTS,
)


_HOF_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{patient_fox_phrase} demonstrated {place} how a single operation,
applied to a whole cluster at once, was the heart of every long
calculation. The form {form_display} captured {concept_phrase}, and
{hasty_fox_phrase} agreed to write it for the REPL."""),

    SubplotTemplate("""\
"Every jump, every reach, every attempt at the cluster — the same
trick repeated cleverly," {patient_fox} said {place}, sketching the
form {form_display} into the dust. {hasty_fox}, {emo_proud}, claimed
to know exactly what {concept_phrase} would produce — but {patient_fox}
insisted, again, that the REPL was the only honest judge."""),
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


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="fox-grapes",
    examples=[
        _ex("(if true :a :b)",
            ":a",
            'the if-fork with a true test',
            "the keyword on the prong the fork's true test selects",
            goal='choose :a when the test is true, otherwise :b',
            scenario='Renard the fox came to a fork in the orchard path. A small wooden sign at the fork carried a test; the left prong led to one keyword, the right prong to another.',
            need="Renard had to take exactly one prong, and the choice depended on whether the test held. The other prong would stay untravelled; only one branch's value would be returned.",
            mapping="`if` is the fork: the test decides which prong runs, the other is skipped entirely. When the test holds, the left prong's value is returned; when it does not, the right prong's is. One branch evaluates; the other is not even visited.",
            resolution='the test held, the left prong was taken, and the form returned the value at that branch — exactly the destination the fork had pointed Renard toward.',
            tags=("story",)),
        _ex("(if false :a :b)",
            ":b",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Renard had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
        _ex("(if (> 5 3) :a :b)",
            ":a",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Vix had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="fox-grapes",
    examples=[
        _ex("(+ 1 (if true 10 20))",
            11,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Sly had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="fox-grapes",
    examples=[
        _ex("(when true :yes)",
            ":yes",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Renard had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
        _ex("(when false :yes)",
            None,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Vix had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="fox-grapes",
    examples=[
        _ex("(cond (= 1 2) :a (= 1 1) :b :else :c)",
            ":b",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Sly had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="fox-grapes",
    examples=[
        _ex("(cond false :a false :b :else :c)",
            ":c",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Renard had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="fox-grapes",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)",
            ":two",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Vix had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
        _ex("(case 99 1 :one 2 :two :default)",
            ":default",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox came to a fork in the orchard path, its prongs marked with the test's two outcomes.",
            need='Sly had to take exactly one prong; the test would settle which, and the other prong stayed untravelled.',
            mapping="`if` and its kin are forks: the test decides which prong runs, and only one branch's value is returned. The branch not taken is not even visited.",
            resolution='the prong the test selected was the one travelled, and its value was what came back.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="fox-grapes",
    examples=[
        _ex("(and 1 2 3)",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Renard needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
        _ex("(or nil false :found)",
            ":found",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Vix needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="fox-grapes",
    examples=[
        _ex("(not (> 1 2))",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Sly needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="fox-grapes",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Renard fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="fox-grapes",
    examples=[
        _ex("(map inc [1 2 3])",
            [2,3,4],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Vix wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Vix had wanted to keep.",
            tags=("story",)),
        _ex("(map #(* % %) [1 2 3 4])",
            [1,4,9,16],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Sly wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Sly had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="fox-grapes",
    examples=[
        _ex("(filter even? [1 2 3 4])",
            [2,4],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Renard wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Renard had wanted to keep.",
            tags=("story",)),
        _ex("(filter pos? [-2 -1 0 1 2])",
            [1,2],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Vix wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Vix had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="fox-grapes",
    examples=[
        _ex("(reduce + [1 2 3 4])",
            10,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox walked the vine-row with a slate, ticking off each cluster as their passed it.',
            need="Sly wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
        _ex("(reduce * [1 2 3 4 5])",
            120,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox walked the vine-row with a slate, ticking off each cluster as his passed it.',
            need="Renard wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
        _ex("(reduce max [3 1 4 1 5 9 2 6])",
            9,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox walked the vine-row with a slate, ticking off each cluster as her passed it.',
            need="Vix wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="fox-grapes",
    examples=[
        _ex("(reduce + 100 [1 2 3])",
            106,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox walked the vine-row with a slate, ticking off each cluster as their passed it.',
            need="Sly wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
        _ex("(reduce + 0 [])",
            0,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox walked the vine-row with a slate, ticking off each cluster as his passed it.',
            need="Renard wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="fox-grapes",
    examples=[
        _ex("(apply + [1 2 3 4])",
            10,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Vix fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
        _ex("(apply max [3 1 4 1 5])",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Sly fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="fox-grapes",
    examples=[
        _ex("((comp inc inc) 5)",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Renard fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
        _ex("((comp str inc) 9)",
            "10",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Vix fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="fox-grapes",
    examples=[
        _ex("((partial + 10) 5)",
            15,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Sly fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
        _ex("(map (partial * 3) [1 2 3])",
            [3,6,9],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Renard fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="fox-grapes",
    examples=[
        _ex("((juxt inc dec) 5)",
            [6,4],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox pinned a tasting-card to the orchard post, listing the steps of a paw-step routine in order.',
            need="Vix fed the card its ingredients and asked for what the routine's last step would serve.",
            mapping="A function in Clojure is a tasting-card: parameters are ingredients; the body's last form is what gets served when the card is called.",
            resolution="the card's last step served back the value the routine had been written to produce.",
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="fox-grapes",
    examples=[
        _ex("(some even? [1 3 5 8 7])",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Sly wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Sly had wanted to keep.",
            tags=("story",)),
        _ex("(some neg? [1 2 3])",
            None,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Renard wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Renard had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="fox-grapes",
    examples=[
        _ex("(every? pos? [1 2 3])",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Vix wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Vix had wanted to keep.",
            tags=("story",)),
        _ex("(every? even? [1 2 3])",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Sly wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Sly had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="fox-grapes",
    examples=[
        _ex("(take 3 [10 20 30 40 50])",
            [10,20,30],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Renard wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Renard had wanted to keep.",
            tags=("story",)),
        _ex("(drop 2 [10 20 30 40 50])",
            [30,40,50],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Vix wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Vix had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="fox-grapes",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])",
            [1,2,3,4],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Sly wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Sly had wanted to keep.",
            tags=("story",)),
        _ex("(sort [3 1 2])",
            [1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Renard wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Renard had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="fox-grapes",
    examples=[
        _ex("(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            120,
            'the loop-recur factorial of five',
            'the row-end product after walking the five-vine row',
            goal='compute the factorial of 5 by looping a counter down to 0 with a running product',
            scenario="Sly the fox stood at the head of a five-vine row, slate in paw. On each lap he would multiply the running tally by the current vine's number, then walk back to the head of the row with the new tally and the next vine to count.",
            need='Sly wanted the running product of all five vine-numbers — five times four times three and so on down — landing as the row-end tally on the slate.',
            mapping="`loop` sets the head of the row with starting bindings; `recur` is walking back to that head with new values, not stacking new walks on the old. The base case `zero?` is the row's end — no more vines to multiply, return the tally.",
            resolution="after the fifth lap the row's end was reached, and the slate held the running product of every vine — exactly the factorial Sly had set out to count.",
            tags=("story",)),
    ], subplots=_CIRCUIT_SUBPLOTS, plan_pool=_PLAN_G5)


SUBJECTS = {s.subject_id: s for s in (
    G5_01, G5_02, G5_03, G5_04, G5_05, G5_06, G5_07, G5_08, G5_09, G5_10,
    G5_11, G5_12, G5_13, G5_14, G5_15, G5_16, G5_17, G5_18, G5_19, G5_20,
    G5_21, G5_22,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-5 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
