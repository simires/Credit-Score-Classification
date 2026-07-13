import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def criar_multilabel_binarizer():

    return MultiLabelBinarizer()



def transformar_type_of_loan(df, mlb, fit=False):

    df = df.copy()

    loans = (
        df["Type_of_Loan"]
        .fillna("")
        .apply(
            lambda x: [
                item.strip()
                for item in x.split(",")
                if item.strip()
            ]
        )
    )

    if fit:
        encoded = mlb.fit_transform(loans)
    else:
        encoded = mlb.transform(loans)

    encoded = pd.DataFrame(
        encoded,
        columns=mlb.classes_,
        index=df.index
    )

    df = df.drop(columns="Type_of_Loan")

    df = pd.concat(
        [df, encoded],
        axis=1
    )

    return df

def padronizar_nomes_colunas(df):
    """
    Padroniza os nomes das colunas para evitar problemas com alguns algoritmos.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )

    return df