from kedro.pipeline import Pipeline
from typing import Dict
import class_gender_survival_breakdown
import gender_survival_breakdown
import survival_breakdown
import hello_world


def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    return {
        "class-gender-survival-breakdown": class_gender_survival_breakdown.create_pipeline(),
        "survival-breakdown": survival_breakdown.create_pipeline(),
        "gender-survival-breakdown": gender_survival_breakdown.create_pipeline(),
        "hello_world": hello_world.create_pipeline(),
        "__default__": Pipeline([
            class_gender_survival_breakdown.create_pipeline() +
            survival_breakdown.pipeline() +
            gender_survival_breakdown.pipeline() +
            hello_world.pipeline()
        ])
    }
