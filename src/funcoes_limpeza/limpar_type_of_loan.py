import pandas as pd
import numpy as np

def limpar_type_of_loan(valor):
    if pd.isna(valor):
        return valor

    # Padroniza o separador
    valor = valor.replace(" and ", ", ")

    # Divide em itens, remove espaços, itens vazios e "Not Specified"
    emprestimos = [
        item.strip()
        for item in valor.split(",")
        if item.strip() and item.strip() != "Not Specified"
    ]

    # Se não sobrou nenhum empréstimo
    if not emprestimos:
        return np.nan

    return ", ".join(emprestimos)