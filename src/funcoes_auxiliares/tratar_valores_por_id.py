import pandas as pd
import numpy as np

def verificar_constancia(df, coluna):
    """
    Verifica quantos valores distintos cada Customer_ID possui em uma coluna
    e retorna uma tabela com a distribuição.
    """

    tabela = (
        df.groupby("Customer_ID")[coluna]
          .nunique(dropna=True)
          .value_counts()
          .sort_index()
          .rename_axis("Quantidade de valores distintos")
          .reset_index(name="Quantidade de Customer_IDs")
    )

    print(f"\nConstância da coluna: {coluna}")
    print(tabela)


def corrigir_por_moda_customer_id(df, coluna, id_col="Customer_ID"):
    """
    Corrige variáveis que deveriam possuir um único valor por Customer_ID.

    Se um Customer_ID possuir mais de um valor distinto para a variável,
    todos os seus registros serão substituídos pela moda do grupo.
    """

    # quantidade de valores distintos por cliente
    distintos = (
        df.groupby(id_col)[coluna]
          .nunique(dropna=True)
    )

    # clientes com inconsistência
    clientes_inconsistentes = distintos[distintos > 1].index

    # calcula a moda de cada cliente
    moda_por_cliente = (
        df.groupby(id_col)[coluna]
          .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
    )

    # corrige apenas os clientes inconsistentes
    mascara = df[id_col].isin(clientes_inconsistentes)

    df.loc[mascara, coluna] = (
        df.loc[mascara, id_col]
          .map(moda_por_cliente)
    )

    print(f"\nColuna: {coluna}")
    print(f"Customer_IDs corrigidos: {len(clientes_inconsistentes)}")

def imputar_nulos_por_moda_customer_id(df, colunas, id_col="Customer_ID"):
    """
    Imputa apenas os valores nulos das colunas informadas utilizando a moda
    dos registros pertencentes ao mesmo Customer_ID.

    Caso um Customer_ID não possua nenhuma moda válida (todos os valores nulos),
    o NaN é mantido.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame a ser modificado.
    colunas : list
        Lista de colunas a serem imputadas.
    id_col : str, default="Customer_ID"
        Coluna identificadora do cliente.

    """

    df = df.copy()

    for coluna in colunas:

        def preencher(grupo):
            moda = grupo.mode(dropna=True)

            if moda.empty:
                return grupo

            return grupo.fillna(moda.iloc[0])

        df[coluna] = (
            df.groupby(id_col)[coluna]
              .transform(preencher)
        )

    return df