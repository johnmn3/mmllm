"""FIM (Fill-in-the-Middle) corpus, training, and eval support.

See docs/fim-plan.md for the rationale + design."""

from mmllm.fim.markers import FIM_PRE, FIM_SUF, FIM_MID, FIM_EOM, ALL_FIM_MARKERS
from mmllm.fim.generator import make_fim_example, build_fim_corpus
from mmllm.fim.loss_mask import fim_loss_mask

__all__ = [
    "FIM_PRE", "FIM_SUF", "FIM_MID", "FIM_EOM", "ALL_FIM_MARKERS",
    "make_fim_example", "build_fim_corpus",
    "fim_loss_mask",
]
