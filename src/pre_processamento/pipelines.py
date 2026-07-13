from joblib import Memory

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier


def criar_pipelines(
    preprocessador_log,
    preprocessador_tree
):

    memory = Memory(
        location="cache_pipeline",
        verbose=0
    )

    pipeline_log = Pipeline(
        steps=[
            ("prep", preprocessador_log),
            ("modelo",
             LogisticRegression(
                 random_state=42,
                 max_iter=500
             ))
        ],
        memory=memory
    )

    pipeline_rf = Pipeline(
        steps=[
            ("prep", preprocessador_tree),
            ("modelo",
             RandomForestClassifier(
                 n_estimators=50,
                 random_state=42,
                 n_jobs=1
             ))
        ],
        memory=memory
    )

    pipeline_lgbm = Pipeline(
        steps=[
            ("prep", preprocessador_tree),
            ("modelo",
             LGBMClassifier(
                 random_state=42,
                 verbose=-1,
                 n_jobs=1
             ))
        ],
        memory=memory
    )

    return pipeline_log, pipeline_rf, pipeline_lgbm