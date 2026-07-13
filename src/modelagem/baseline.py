import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold, cross_validate


def avaliar_modelo(modelo, X, y, cv):
    """
    Avalia um modelo utilizando validação cruzada com StratifiedKFold. O modelo é treinado dentro da validação cruzada
    """

    scoring = {
        "accuracy": "accuracy",
        "precision_weighted": "precision_weighted",
        "recall_weighted": "recall_weighted",
        "f1_weighted": "f1_weighted",
        "f1_macro": "f1_macro"
    }

    scores = cross_validate(
        estimator=modelo,
        X=X,
        y=y,
        cv=cv,
        scoring=scoring,
        n_jobs=1
    )

    resultados = {
        "Accuracy": np.mean(scores["test_accuracy"]),
        "Precision (weighted)": np.mean(scores["test_precision_weighted"]),
        "Recall (weighted)": np.mean(scores["test_recall_weighted"]),
        "F1-score (weighted)": np.mean(scores["test_f1_weighted"]),
        "F1-score (macro)": np.mean(scores["test_f1_macro"]),
    }

    return resultados


from joblib import Parallel, delayed

def comparar_modelos(modelos, X, y, n_splits=5, shuffle=True, random_state=42):

    cv = StratifiedKFold(
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state
    )

    resultados = Parallel(n_jobs=-1)(
        delayed(avaliar_modelo)(modelo, X, y, cv)
        for modelo in modelos.values()
    )

    resultados = pd.DataFrame(
        resultados,
        index=modelos.keys()
    ).sort_values(
        "F1-score (weighted)",
        ascending=False
    )

    return resultados