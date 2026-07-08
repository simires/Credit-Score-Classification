import re
import pandas as pd
import numpy as np


def encontrar_variaveis_int(tabela_problemas, dicionario):
    variaveis = (
        tabela_problemas.loc[
            tabela_problemas["Problema identificado"] == "Valores numéricos em formato de string",
            "Variáveis"
        ]
        .str.split(", ")
        .explode()
        .tolist()
    )

    variaveis_inteiras = (
        dicionario.loc[
            dicionario["Variável"].isin(variaveis)
            & (dicionario["Subtipo"] == "discreta"),
            "Variável"
        ]
        .tolist()
    )
    
    return variaveis_inteiras


def encontrar_ruidos_int(df, coluna):
    
    # identifica valores inválidos em uma coluna que deveria conter apenas inteiros.

    valores = df[coluna].dropna().astype(str)

    # apenas números inteiros positivos
    mascara = ~valores.str.fullmatch(r'\d+')

    ruidos = valores[mascara].value_counts()

    print(f"\nColuna: {coluna}")
    print(f"Valores distintos com ruído: {len(ruidos)}")
    print(f"Total de registros com ruído: {mascara.sum()}")

    if not ruidos.empty:
        print("\nOcorrências:")
        print(ruidos)


def limpar_coluna_int(df, coluna):
    """
    Limpa uma coluna que deveria conter números inteiros.

    Etapas:
    1. Remove o caractere '_';
    2. Converte para inteiro (Int64);
    3. Valores inválidos tornam-se NaN;
    4. Valores negativos tornam-se NaN.
    """

    # contabiliza quantos valores possuem "_"
    qtd_underscores = df[coluna].astype(str).str.contains("_", regex=False, na=False).sum()

    # remove "_"
    valores = (
        df[coluna]
        .astype(str)
        .str.replace("_", "", regex=False)
    )

    # converte para inteiro
    valores = pd.to_numeric(valores, errors="coerce")

    # conta negativos
    qtd_negativos = (valores < 0).sum()

    # negativos viram NaN
    valores = valores.mask(valores < 0)

    # salva como inteiro com suporte a NaN
    df[coluna] = valores.astype("Int64")

    print(f"\nColuna: {coluna}")
    print(f"Valores com '_' corrigidos: {qtd_underscores}")
    print(f"Valores negativos convertidos para NaN: {qtd_negativos}")


def remover_negativos_int(df, coluna):
    """
    Substitui valores negativos por NaN em uma coluna inteira.
    """

    # garante o tipo inteiro anulável
    df[coluna] = df[coluna].astype("Int64")

    # conta quantos negativos existem
    qtd_negativos = (df[coluna] < 0).sum()

    # substitui por NaN
    df.loc[df[coluna] < 0, coluna] = np.nan

    print(f"\nColuna: {coluna}")
    print(f"Valores negativos convertidos para NaN: {qtd_negativos}")