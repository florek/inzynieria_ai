from __future__ import annotations
from enum import Enum


class TrainingStage(str, Enum):
    POST_TRAINING = "post_training"
    PRETRAINING = "pretraining"


def focuses_on_human_preferences(stage: TrainingStage) -> bool:
    return stage is TrainingStage.POST_TRAINING


def prompting_changes_weights() -> bool:
    return False
