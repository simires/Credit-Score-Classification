import re
import pandas as pd
import numpy as np


def encontrar_variaveis_float(tabela_problemas, dicionario):
    variaveis = (
        tabela_problemas.loc[
            tabela_problemas["Problema identificado"] == "Valores numéricos em formato de string",
            "Variáveis"
        ]
        .str.split(", ")
        .explode()
        .tolist()
    )

    variaveis_float = (
        dicionario.loc[
            dicionario["Variável"].isin(variaveis)
            & (dicionario["Subtipo"] == "contínua"),
            "Variável"
        ]
        .tolist()
    )

    return variaveis_float


def encontrar_ruidos_float(df, coluna):
    
    # identifica valores inválidos em uma coluna que deveria conter números reais.

    valores = df[coluna].dropna().astype(str)

    # inteiros ou decimais
    mascara = ~valores.str.fullmatch(r'-?\d+(\.\d+)?')

    ruidos = valores[mascara].value_counts()

    print(f"\nColuna: {coluna}")
    print(f"Valores distintos com ruído: {len(ruidos)}")
    print(f"Total de registros com ruído: {mascara.sum()}")

    if not ruidos.empty:
        print("\nOcorrências:")
        print(ruidos)


def limpar_coluna_float(df, coluna):
    """
    Limpa uma coluna que deveria conter números reais (float).

    Etapas:
    1. Remove o caractere '_';
    2. Se a string ficar vazia, transforma em NaN;
    3. Converte para float;
    4. Valores inválidos tornam-se NaN.
    """
    
    # converte para string
    valores = df[coluna].astype(str)

    # conta quantos NaN haviam no início
    nans_antes = df[coluna].isna().sum()
    
    # conta quantos valores possuem "_"
    qtd_underscores = valores.str.contains("_", regex=False, na=False).sum()

    # valores compostos apenas por "_"
    somente_underscores = valores.str.fullmatch(r"_+").sum()

    # remove "_"
    valores = valores.str.replace("_", "", regex=False)

    # strings vazias viram NaN
    valores = valores.replace("", pd.NA)

    # converte para float
    valores = pd.to_numeric(valores, errors="coerce")
    
    # atualiza a coluna
    df[coluna] = valores

    # conta quantos novos NaN foram gerados
    nans_depois = valores.isna().sum()
    novos_nans = nans_depois - nans_antes

    print(f"\nColuna: {coluna}")
    print(f"Valores com '_' corrigidos: {qtd_underscores}")
    print(f"Valores compostos apenas por '_': {somente_underscores}")
    print(f"Valores convertidos para NaN: {novos_nans}")