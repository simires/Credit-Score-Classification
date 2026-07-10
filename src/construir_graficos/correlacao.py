import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(df, dicionario):
    
    variaveis_numericas = (
    dicionario
    .query("Tipo == 'numérica'")
    ["Variável"]
    .to_list()
    )
    
    corr = df[variaveis_numericas].corr(method="spearman")
    
    plt.figure(figsize=(12,10))
    
    sns.heatmap(
        corr,
        annot=True,
        annot_kws={"size": 10},
        cmap="coolwarm",
        center=0,
        fmt=".2f"
    )
    
    plt.title("Matriz de correlação")
    plt.show()

def boxplots_por_alvo(
    df,
    dicionario,
    variavel_alvo="Credit_Score",
    hue="Credit_Score",
    legend=False,
    ncols=3,
    figsize=(18, 5),
    palette="Set2"
):

    variaveis = (
    dicionario
    .query("Tipo == 'numérica'")
    ["Variável"]
    .to_list()
    )
    
    if variaveis is None:
        variaveis = (
            df.select_dtypes(include="number")
              .columns
              .drop(variavel_alvo, errors="ignore")
              .tolist()
        )

    n = len(variaveis)
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(figsize[0], figsize[1] * nrows)
    )

    if nrows == 1 and ncols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for ax, var in zip(axes, variaveis):
        sns.boxplot(
            data=df,
            x=variavel_alvo,
            y=var,
            hue=hue,
            ax=ax,
            palette=palette,
            legend=legend
        )

        ax.set_title(var)
        ax.set_xlabel(variavel_alvo)
        ax.set_ylabel("")

    # Remove eixos vazios
    for ax in axes[n:]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.show()


def boxplots_logaritmicos(
    df,
    variavel_alvo="Credit_Score",
    variaveis=None,
    ncols=3,
    figsize=(18, 5),
    palette="Set2"
):

    if variaveis is None:
        variaveis = [
            "Annual_Income",
            "Total_EMI_per_month",
            "Amount_invested_monthly"
        ]

    n = len(variaveis)
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(figsize[0], figsize[1] * nrows),
        constrained_layout=True
    )

    if n == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for ax, var in zip(axes, variaveis):

        # Mantém apenas valores positivos (escala log não aceita <= 0)
        dados = df[df[var] > 0]

        sns.boxplot(
            data=dados,
            x=variavel_alvo,
            y=var,
            hue=variavel_alvo,
            palette=palette,
            legend=False,
            ax=ax
        )

        ax.set_yscale("log")
        ax.set_title(f"{var} (escala log)")
        ax.set_xlabel(variavel_alvo)
        ax.set_ylabel(var)

    # Remove eixos vazios
    for ax in axes[n:]:
        fig.delaxes(ax)

    plt.show()


def categoricas_por_alvo(
    df,
    dicionario,
    variavel_alvo="Credit_Score",
    ncols=2,
    figsize=(18, 8),
    normalize=True,
    cmap="Set2"
):

    variaveis = (
    dicionario
    .query("Tipo == 'categórica'")
    ["Variável"]
    .tolist()
    )
    
    variaveis = [
        v for v in variaveis
        if v not in [variavel_alvo, "Type_of_Loan"]
    ]

    if variavel_alvo in variaveis:
        variaveis.remove(variavel_alvo)

    n = len(variaveis)
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(figsize[0], figsize[1] * nrows),
        constrained_layout=True
    )

    axes = axes.flatten()

    ultimo_ax = None

    for ax, var in zip(axes, variaveis):

        # Ignora Type_of_Loan (ou trate separadamente)
        if var == "Type_of_Loan":
            fig.delaxes(ax)
            continue

        tabela = pd.crosstab(
            df[var],
            df[variavel_alvo],
            normalize="index" if normalize else False
        )

        tabela.plot(
            kind="barh",
            stacked=True,
            ax=ax,
            colormap=cmap,
            legend=False
        )

        ax.set_title(var)
        ax.set_xlabel("Proporção" if normalize else "Quantidade")
        ax.set_ylabel("")

        if normalize:
            ax.set_xlim(0, 1)

        # Adiciona os valores nas barras
        for container in ax.containers:
            labels = []

            for barra in container:
                largura = barra.get_width()

                if largura < 0.03:      # não escreve em segmentos muito pequenos
                    labels.append("")
                else:
                    if normalize:
                        labels.append(f"{largura:.1%}")
                    else:
                        labels.append(f"{int(largura)}")

            ax.bar_label(
                container,
                labels=labels,
                label_type="center",
                fontsize=10,
                color="black"
            )

        ultimo_ax = ax

    # Remove eixos restantes que ficaram vazios
    for ax in axes:
        if not ax.has_data():
            fig.delaxes(ax)

    if ultimo_ax is not None:
        handles, labels = ultimo_ax.get_legend_handles_labels()
        fig.legend(
            handles,
            labels,
            title=variavel_alvo,
            loc="upper right"
        )

    plt.show()


def type_of_loan_por_alvo(
    df,
    variavel="Type_of_Loan",
    variavel_alvo="Credit_Score",
    normalize=True,
    cmap="Set2",
    figsize=(10, 6)
):
    """
    Plota a distribuição de Credit_Score para cada tipo de empréstimo.

    Cada empréstimo presente em uma célula é considerado individualmente.
    """

    dados = (
        df[[variavel, variavel_alvo]]
        .copy()
    )

    # Divide a string em vários empréstimos
    dados[variavel] = dados[variavel].str.split(",")

    # Uma linha para cada empréstimo
    dados = dados.explode(variavel, ignore_index=True)

    # Remove espaços
    dados[variavel] = dados[variavel].str.strip()

    # Remove strings vazias
    dados = dados[dados[variavel] != ""]

    tabela = pd.crosstab(
        dados[variavel],
        dados[variavel_alvo],
        normalize="index" if normalize else False
    )

    # Ordena alfabeticamente
    tabela = tabela.sort_index()

    ax = tabela.plot(
        kind="barh",
        stacked=True,
        figsize=figsize,
        colormap=cmap
    )

    ax.set_xlabel("Proporção" if normalize else "Quantidade")
    ax.set_ylabel("Tipo de empréstimo")
    ax.set_title("Type_of_Loan × Credit_Score")

    if normalize:
        ax.set_xlim(0, 1)

    # Escreve os percentuais
    for container in ax.containers:
        labels = []

        for barra in container:
            largura = barra.get_width()

            if largura < 0.04:
                labels.append("")
            else:
                if normalize:
                    labels.append(f"{largura:.0%}")
                else:
                    labels.append(f"{int(largura)}")

        ax.bar_label(
            container,
            labels=labels,
            label_type="center",
            fontsize=8
        )

    plt.tight_layout()
    plt.show()