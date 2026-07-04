import pandas as pd

def resumo_nulos(df, nome_df):
    print(f'Valores nulos para o dataset de {nome_df}:')
    nulos = df.isnull().sum()
    porcentagem = (nulos / len(df) * 100).round(2)

    resumo = pd.DataFrame({
        "Quantidade de nulos": nulos,
        "Porcentagem (%)": porcentagem
    })
    
    # Mantém apenas colunas com pelo menos um valor nulo
    resumo = resumo[resumo["Quantidade de nulos"] > 0]
    
    return resumo.sort_values("Quantidade de nulos", ascending=False)