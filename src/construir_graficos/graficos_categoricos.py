import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

colors = ["#9467bd", "#057476", "#FF7A00"]
sns.set_theme(style="ticks")
sns.set_palette(sns.color_palette(colors))

def type_of_loan(df):
    emprestimos = (
    df["Type_of_Loan"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    )
    
    contagem = emprestimos.value_counts()
    
    plt.figure(figsize=(6,5))
    
    ax = sns.barplot(
        x=contagem.values,
        y=contagem.index,
        color=colors[0],
        alpha=0.9
    )
    
    ax.bar_label(
        ax.containers[0],
        fmt="%.0f",
        padding=3
    )
    
    plt.title("Distribuição da variável 'Type_of_Loan'")
    plt.xlabel("Quantidade")
    plt.ylabel("Tipo de empréstimo")
    
    sns.despine()
    plt.grid(axis="x", alpha=0.3)
    
    plt.show()


def variaveis_categoricas(df, dicionario):
    
    fig, axes = plt.subplots(2, 2, figsize=(26,15))
    plt.tight_layout(pad=6, w_pad=10, h_pad=5)
    fig.suptitle('Distribuição de variáveis categóricas', fontweight='bold')

    variaveis_categoricas = (
    dicionario
    .query("Tipo == 'categórica' and Variável != 'Type_of_Loan' and Variável != 'Occupation' and Variável != 'Payment_Behaviour'")
    ["Variável"]
    .to_list()
    )
    
    for i, variavel in enumerate (variaveis_categoricas):
        order = df[variavel].value_counts().index
        ax = sns.countplot(
            data=df,
            x=variavel,
            ax=axes.flatten()[i],
            color=colors[0],
            alpha=0.9,
            order=order
        )
        ax.bar_label(
            ax.containers[0],
            fmt='%.0f',
            label_type='center',
            color='white',
            fontweight='bold'
        )
        ax.set(frame_on=False)
        ax.axhline(0, color="k", clip_on=False)
        ax.set_title(f"Distribuição da variável '{variavel}'")
        ax.set_ylabel('Quantidade')
        ax.grid(axis='y', linestyle='-')
    plt.show()


def variavel_categorica(df, variavel, largura, altura):
    contagem = df[variavel].value_counts()
    
    plt.figure(figsize=(largura,altura))

    ax = sns.barplot(
        x=contagem.values,
        y=contagem.index,
        color=colors[0],
        alpha=0.9
    )
    
    ax.bar_label(
        ax.containers[0],
        fmt="%.0f",
        padding=3
    )
    
    plt.title(f"Distribuição da variável '{variavel}'")
    plt.xlabel("Quantidade")
    plt.ylabel(variavel)
    
    sns.despine()
    plt.grid(axis="x", alpha=0.3)
    
    plt.show()