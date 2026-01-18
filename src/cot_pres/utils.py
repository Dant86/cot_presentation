"""Utility functions."""

from __future__ import annotations

import os

import transformers

from cot_pres import constants


def load_model() -> transformers.TextGenerationPipeline:
    if os.path.exists(constants.PRETRAINED_MODEL_DIR):
        return transformers.pipeline(
            task="text-generation",
            model=constants.PRETRAINED_MODEL_DIR,
        )
    
    model = transformers.pipeline(
        task="text-generation",
        model=constants.MODEL_NAME,
    )

    os.makedirs(constants.PRETRAINED_MODEL_DIR, exist_ok=True)
    model.save_pretrained(constants.PRETRAINED_MODEL_DIR)

    return model
