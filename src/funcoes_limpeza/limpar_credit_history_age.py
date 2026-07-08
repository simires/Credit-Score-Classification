import pandas as pd

def limpar_credit_history_age(df):
    """
    Converte Credit_History_Age para a quantidade total de meses.
    """

    extraido = df["Credit_History_Age"].str.extract(
        r'(?P<anos>\d+)\s+Years?\s+and\s+(?P<meses>\d+)\s+Months?'
    )

    df["Credit_History_Age"] = (
        pd.to_numeric(extraido["anos"], errors="coerce") * 12
        + pd.to_numeric(extraido["meses"], errors="coerce")
    ).astype("Int64")

    print("Coluna: Credit_History_Age")
    print(f"Valores convertidos: {df['Credit_History_Age'].notna().sum()}")
    print(f"Valores ausentes: {df['Credit_History_Age'].isna().sum()}")
