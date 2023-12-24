import pandas as pd
import random
import matplotlib.pyplot as plt

# Defina o nome do arquivo CSV
visitas = 'visitas.csv'
receitas = 'receita.csv'

# Carregue os arquivos CSV em DataFrames
df_visitas = pd.read_csv(visitas)
df_receitas = pd.read_csv(receitas)

# Unifique os DataFrames usando o campo 'id_visita'
df_unificado = df_visitas.merge(df_receitas, on='id_visita', how='outer')

# Preencha os dados faltantes com 0
df_unificado = df_unificado.fillna(0)

# Calcule a média das receitas por 'id_cliente' incluindo visitas sem receita
media_receitas_a = df_unificado.groupby('id_cliente')['receita'].mean()

# Filtrar visitas com receita maior que 0
df_com_receita = df_unificado[df_unificado['receita'] > 0]

# Calcule a média das receitas por 'id_cliente' excluindo visitas sem receita
media_receitas_b = df_com_receita.groupby('id_cliente')['receita'].mean()

# Calcule o percentual de visitas com receita por cliente
total_visitas_por_cliente = df_unificado.groupby('id_cliente').size()
total_visitas_com_receita_por_cliente = df_com_receita.groupby('id_cliente').size()
percentual_com_receita_por_cliente = (total_visitas_com_receita_por_cliente / total_visitas_por_cliente) * 100

# Formate o percentual com símbolo "%" e duas casas decimais
percentual_com_receita_por_cliente = percentual_com_receita_por_cliente.map("{:.2f}%".format)

# Visualize as médias de receitas e o percentual de visitas com receita por cliente
print("Média incluindo visitas sem receita:")
print(media_receitas_a)

print("Média excluindo visitas sem receita:")
print(media_receitas_b)

print("Percentual de visitas com receita por cliente:")
print(percentual_com_receita_por_cliente)

# Agora, vamos adicionar a funcionalidade de gerar amostras, calcular médias de receita e criar um DataFrame com os valores de B e as médias.
n_max_iteracoes = 1000  # Defina o número máximo de iterações (B indo de 1 até 1000)
tamanho_do_banco = len(df_unificado)  # Defina o tamanho do banco de amostras

valores_de_B = []
medias_de_receita = []

# Loop de 1 a 1000
for B in range(1, n_max_iteracoes + 1):
    # Gere uma amostra com reposição do dataframe original
    amostra = df_unificado.sample(n=tamanho_do_banco, replace=True)
    
    # Calcule a média de receita da amostra
    media_amostra = amostra['receita'].mean()
    
    # Armazene os valores de B e as médias
    valores_de_B.append(B)
    medias_de_receita.append(media_amostra)

# Crie um DataFrame com os valores de B e as médias de receita
df_resultado = pd.DataFrame({'B': valores_de_B, 'Média de Receita': medias_de_receita})

# Visualize o DataFrame resultante
print(df_resultado)

# Crie um histograma da distribuição das médias de receita
plt.hist(df_resultado['Média de Receita'], bins=30, edgecolor='k')
plt.title('Distribuição das Médias de Receita')
plt.xlabel('Média de Receita')
plt.ylabel('Frequência')
plt.show()
