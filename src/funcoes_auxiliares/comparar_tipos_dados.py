import pandas as pd

def comparar_tipos_dados(df_train, df_test):
    tipos_train = df_train.dtypes.rename("Tipo_train")
    tipos_test = df_test.dtypes.rename("Tipo_test")

    comparacao = pd.concat([tipos_train, tipos_test], axis=1)
    comparacao["Mesmo_tipo"] = comparacao["Tipo_train"] == comparacao["Tipo_test"]

    return comparacao