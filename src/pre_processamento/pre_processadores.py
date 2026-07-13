from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


def criar_preprocessador_logistico(
    variaveis_numericas,
    variaveis_ordinais,
    variaveis_nominais,
    ordinal_encoder,
    onehot_encoder
):

    return ColumnTransformer(

        transformers=[

            (
                "num", StandardScaler(), variaveis_numericas
            ),

            (
                "ord", ordinal_encoder, variaveis_ordinais
            ),

            (
                "nom", onehot_encoder, variaveis_nominais
            )

        ],

        remainder="passthrough",
        verbose_feature_names_out=False,
        sparse_threshold=1.0
    )


def criar_preprocessador_arvores(
    variaveis_numericas,
    variaveis_ordinais,
    variaveis_nominais,
    ordinal_encoder,
    onehot_encoder
):

    return ColumnTransformer(

        transformers=[

            (
                "num", "passthrough", variaveis_numericas
            ),

            (
                "ord", ordinal_encoder, variaveis_ordinais
            ),

            (
                "nom", onehot_encoder, variaveis_nominais
            )

        ],

        remainder="passthrough",
        verbose_feature_names_out=False
    )

