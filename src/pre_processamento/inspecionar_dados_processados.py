import pandas as pd

def visualizar_preprocessamento(preprocessador, X_train, X_valid=None):
    """
    Ajusta o preprocessador ao conjunto de treino e retorna os
    conjuntos transformados como DataFrames.
    """

    X_train_proc = preprocessador.fit_transform(X_train)

    colunas = preprocessador.get_feature_names_out()

    X_train_proc = pd.DataFrame(
        X_train_proc,
        columns=colunas,
        index=X_train.index
    )

    if X_valid is None:
        return X_train_proc

    X_valid_proc = preprocessador.transform(X_valid)

    X_valid_proc = pd.DataFrame(
        X_valid_proc,
        columns=colunas,
        index=X_valid.index
    )

    return X_train_proc, X_valid_proc