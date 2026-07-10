import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def variaveis_discretas(
    df,
    dicionario,
    ncols=3,
    figsize=(18, 12),
    color="#9467bd"
):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica' and Subtipo == 'discreta'")
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
        "Distribuição das variáveis numéricas discretas",
        fontsize=18,
        fontweight="bold"
    )

    for i, variavel in enumerate(variaveis):

        serie = df[variavel].dropna()

        minimo = int(serie.min())
        maximo = int(serie.max())

        bins = np.arange(minimo - 0.5, maximo + 1.5, 1)

        ax = sns.histplot(
            serie,
            kde=True,
            bins=bins,
            color=color,
            edgecolor="white",
            alpha=0.9,
            ax=axes[i]
        )

        media = serie.mean()
        mediana = serie.median()
        desvio = serie.std()

        ax.axvline(media, color="red", linestyle="--", linewidth=2, label="Média")
        ax.axvline(mediana, color="green", linestyle="-.", linewidth=2, label="Mediana")

        texto = (
            f"Média: {media:.2f}\n"
            f"Mediana: {mediana:.2f}\n"
            f"DP: {desvio:.2f}\n"
        )

        ax.text(
            0.98,
            0.98,
            texto,
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=9,
            bbox=dict(facecolor="white", alpha=0.85)
        )

        ax.set_title(variavel)
        ax.set_xlabel("")
        ax.set_ylabel("Frequência")

        sns.despine(ax=ax)
        ax.grid(axis="y", alpha=0.3)
        ax.legend()

    for j in range(len(variaveis), len(axes)):
        fig.delaxes(axes[j])

    plt.show()


def variaveis_continuas(
    df,
    dicionario,
    bins=30,
    ncols=3,
    figsize=(18, 12),
    color="#4C72B0"
):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica' and Subtipo == 'contínua'")
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
        "Distribuição das variáveis numéricas contínuas",
        fontsize=18,
        fontweight="bold"
    )

    for i, variavel in enumerate(variaveis):

        ax = sns.histplot(
            data=df,
            x=variavel,
            bins=bins,
            kde=True,
            color=color,
            alpha=0.8,
            ax=axes[i]
        )

        ax.set_title(variavel)
        ax.set_xlabel("")
        ax.set_ylabel("Frequência")

        sns.despine(ax=ax)
        ax.grid(axis="y", alpha=0.3)

    for j in range(len(variaveis), len(axes)):
        fig.delaxes(axes[j])

    plt.show()


def plot_variaveis_continuas(
    df,
    dicionario,
    bins=30,
    ncols=3,
    figsize=(18, 12),
    color="#9467bd"
):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica' and Subtipo == 'contínua'")
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
        "Distribuição das variáveis numéricas contínuas",
        fontsize=18,
        fontweight="bold"
    )

    for i, variavel in enumerate(variaveis):

        serie = df[variavel].dropna()

        ax = sns.histplot(
            serie,
            bins=bins,
            kde=True,
            color=color,
            edgecolor="white",
            alpha=0.85,
            ax=axes[i]
        )

        media = serie.mean()
        mediana = serie.median()
        desvio = serie.std()

        ax.axvline(media, color="red", linestyle="--", linewidth=2, label="Média")
        ax.axvline(mediana, color="green", linestyle="-.", linewidth=2, label="Mediana")

        texto = (
            f"Média: {media:.2f}\n"
            f"Mediana: {mediana:.2f}\n"
            f"DP: {desvio:.2f}\n"
        )

        ax.text(
            0.98,
            0.98,
            texto,
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=9,
            bbox=dict(facecolor="white", alpha=0.85)
        )

        ax.set_title(variavel)
        ax.set_xlabel("")
        ax.set_ylabel("Frequência")

        sns.despine(ax=ax)
        ax.grid(axis="y", alpha=0.3)
        ax.legend()

    for j in range(len(variaveis), len(axes)):
        fig.delaxes(axes[j])

    plt.show()