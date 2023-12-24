import seaborn as sns
import pandas as pd

# Carregue o conjunto de dados 'penguins'
df = sns.load_dataset('penguins')

columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']

# Análise 1
print("**********Análise 1**********")

columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
df_analise1 = df[columns]

media_analise1 = df_analise1.mean().round(2)
variancia_analise1 = df_analise1.var().round(2)

print("Média de cada coluna (Análise 1):")
print(media_analise1)
print("\nVariância de cada coluna (Análise 1):")
print(variancia_analise1)

# Análise 2
print("**********Análise 2**********")

columns_analise2 = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
df_analise2 = df[columns_analise2]

def zscore(column):
    return (column - column.mean()) / column.std()

df_zscore = df_analise2.apply(zscore, axis=0)

print("DataFrame com colunas normalizadas por Z-score (Análise 2):")
print(df_zscore)

# Análise 3
print("**********Análise 3**********")

def zscore_with_sex(column):
    return (column - column.mean()) / column.std()

df_zscore = df[columns_analise2].apply(zscore_with_sex, axis=0)
df_zscore['sex'] = df['sex']

estatisticas_por_sexo = df_zscore.groupby('sex').agg(['mean', 'var', 'max', 'min']).round(2)

print("Média, Variância, Máximo e Mínimo de cada informação normalizada por sexo (Análise 3):")
print(estatisticas_por_sexo)
