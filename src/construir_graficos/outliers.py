import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

def boxplots(df, dicionario, ncols=3, figsize=(18, 12), color="#9370DB"):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica'")
    ["Variável"]
    .to_list()
    )
    
    nrows = math.ceil(len(variaveis) / ncols)

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=figsize,
        constrained_layout=True
    )

    axes = axes.flatten()

    fig.suptitle(
        "Boxplots das variáveis numéricas",
        fontsize=18,
        fontweight="bold"
    )

    for i, variavel in enumerate(variaveis):

        ax = sns.boxplot(
            x=df[variavel],
            color=color,
            ax=axes[i]
        )

        ax.set_title(variavel)
        ax.set_xlabel("")

        sns.despine(ax=ax)

    for j in range(len(variaveis), len(axes)):
        fig.delaxes(axes[j])

    plt.show()

def resumo_outliers(df, dicionario):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica'")
    ["Variável"]
    .to_list()
    )
    
    resultados = []

    for coluna in variaveis:

        serie = df[coluna].dropna()

        q1 = serie.quantile(.25)
        q3 = serie.quantile(.75)

        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        mascara = (
            (serie < limite_inferior) |
            (serie > limite_superior)
        )

        resultados.append({
            "Variável": coluna,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Limite inferior": limite_inferior,
            "Limite superior": limite_superior,
            "Outliers": mascara.sum(),
            "% Outliers": round(100 * mascara.mean(), 2)
        })

    return (
        pd.DataFrame(resultados)
        .sort_values("% Outliers", ascending=False)
    )