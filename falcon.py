import pandas as pd
import openpyxl
import os

# Caminho relativo ao projeto
base_path = os.path.join(os.path.dirname(__file__), "data", "Falcon.xlsx")

# Carregar base
df = pd.read_excel(base_path)

# Ajustar coluna Status
df['Status'] = df['Status'].replace({
    'NÃO FOI POSSÍVEL CONFIRMAR NÃO FRAUDE': 'INDEF.NF',
    'NÃO FOI POSSÍVEL CONFIRMAR FRAUDE': 'INDEF.F',
})

# Ajustar nomes de Fila para ficarem mais curtos
df['Fila'] = df['Fila'].replace({
    'CARTÕES APROVADAS': 'CAR.APROV.',
    'CARTÕES RECUSADAS': 'CAR.RECUS.'
})

# Verifica se colunas necessárias existem
expected_cols = {'Status', 'Fila'}
missing = expected_cols - set(df.columns)
if missing:
    raise KeyError(f"Colunas faltando na base: {missing}")

# Contagens gerais (não filtradas)
status_counts = df['Status'].value_counts(dropna=False)
fila_counts = df['Fila'].value_counts(dropna=False)
