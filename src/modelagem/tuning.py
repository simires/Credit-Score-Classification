import pandas as pd
import numpy as np

from sklearn.model_selection import (
    StratifiedKFold,
    cross_validate,
    RandomizedSearchCV,
    train_test_split
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


def otimizar_modelo(modelo, parametros, X, y, n_iter=30, scoring="f1_weighted", n_splits=3, random_state=42):

    """
    Realiza RandomizedSearchCV utilizando StratifiedKFold.
    """
    
    skf = StratifiedKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state
    )

    busca = RandomizedSearchCV(
        estimator=modelo,
        param_distributions=parametros,
        n_iter=n_iter,
        scoring=scoring,
        cv=skf,
        random_state=random_state,
        n_jobs=2,
        verbose=1,
        refit=True,
        return_train_score=True
    )

    busca.fit(X, y)

    return busca

from sklearn.model_selection import (
    RandomizedSearchCV,
    StratifiedKFold,
    train_test_split
)


def otimizar_modelos_arvore(modelo, parametros, X, y, sample_size=0.3, n_iter=15, scoring="f1_weighted", n_splits=3, random_state=42, n_jobs=2):
    """
    Realiza RandomizedSearchCV em uma amostra estratificada do conjunto
    de treinamento para reduzir o tempo de execução.

    Parameters
    ----------
    sample_size : float
        Proporção da base utilizada na busca (0 < sample_size <= 1).
    """

    # Amostra estratificada
    X_amostra, _, y_amostra, _ = train_test_split(
        X,
        y,
        train_size=sample_size,
        stratify=y,
        random_state=random_state
    )

    skf = StratifiedKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state
    )

    busca = RandomizedSearchCV(
        estimator=modelo,
        param_distributions=parametros,
        n_iter=n_iter,
        scoring=scoring,
        cv=skf,
        random_state=random_state,
        n_jobs=n_jobs,
        pre_dispatch=n_jobs,
        verbose=1,
        refit=True,
        return_train_score=True
    )

    busca.fit(X_amostra, y_amostra)

    return busca