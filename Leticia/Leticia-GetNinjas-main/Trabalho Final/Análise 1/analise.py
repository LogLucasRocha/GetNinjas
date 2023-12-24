import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crie uma lista de Product_Code de P1 até P819
product_codes = ['P' + str(i) for i in range(1, 820)]

# Crie uma lista de colunas de W1 até W51
w_columns = [f'W{i}' for i in range(1, 52)]

# Combine as colunas Product_Code e as colunas W
columns_to_read = ['Product_Code'] + w_columns

# Leia o arquivo CSV com as colunas selecionadas
dados_de_vendas = 'Sales_Transactions_Dataset_Weekly.csv'
data_frame = pd.read_csv(dados_de_vendas, usecols=columns_to_read)

# Defina uma semente para a seleção de 3 produtos aleatórios
np.random.seed(42)

# Seleção de 3 produtos aleatórios
produtos_selecionados = np.random.choice(data_frame['Product_Code'].unique(), 3, replace=False)
df_filtrado = data_frame[data_frame['Product_Code'].isin(produtos_selecionados)]

# Encontre as semanas com valores diferentes de zero em qualquer produto
semanas_com_dados = df_filtrado.iloc[:, 1:].columns[df_filtrado.iloc[:, 1:].sum() > 0]

# Gráfico de Valor da Transação
plt.figure(figsize=(8, 4))
for produto in produtos_selecionados:
    df_produto = df_filtrado[df_filtrado['Product_Code'] == produto]
    valores = df_produto.iloc[:, 1:][semanas_com_dados].values.flatten()
    
    plt.plot(semanas_com_dados, valores, label=produto)

plt.xlabel('Semana')
plt.ylabel('Valor de Transação')
plt.title('Valor de Transação ao Longo do Tempo para Produtos Selecionados')
plt.legend()
plt.grid(True)

plt.show()

# Gráfico de Diferença das Séries Temporais
plt.figure(figsize=(8, 4))
for produto in produtos_selecionados:
    df_produto = data_frame[data_frame['Product_Code'] == produto]
    semanas = df_produto.columns[1:]
    
    # Calcule as diferenças apenas para as semanas com valores
    diferencas = df_produto.iloc[:, 1:][semanas_com_dados].diff(axis=1).values.flatten()
    
    plt.plot(semanas_com_dados, diferencas, label=produto)

plt.xlabel('Semana')
plt.ylabel('Diferença Semanal')
plt.title('Série Temporal das Diferenças por Produto ao Longo das Semanas')
plt.legend()
plt.grid(True)

plt.show()

# Inicialize listas vazias para armazenar os máximos e mínimos de todos os produtos
maximos_por_produto = []
minimos_por_produto = []
desvio_padrao_por_produto = []
media_por_produto = []
mediana_por_produto = []

# Itere por todos os produtos no DataFrame original
for produto in data_frame['Product_Code'].unique():
    df_produto = data_frame[data_frame['Product_Code'] == produto]
    valores = df_produto.iloc[:, 1:][semanas_com_dados].values.flatten()
    
    maximo_produto = np.max(valores)  # Calcula o máximo
    minimo_produto = np.min(valores)  # Calcula o mínimo
    desvio_padrao_produto = np.std(valores)  # Calcula o desvio padrão
    media_produto = np.mean(valores)  # Calcula a média
    mediana_produto = np.median(valores)  # Calcula a mediana
    
    maximos_por_produto.append(maximo_produto)
    minimos_por_produto.append(minimo_produto)
    desvio_padrao_por_produto.append(desvio_padrao_produto)
    media_por_produto.append(media_produto)
    mediana_por_produto.append(mediana_produto)

# Imprima os dados estatísticos de todos os produtos
for i, produto in enumerate(data_frame['Product_Code'].unique()):
    print(f"Produto: {produto} - Máximo: {maximos_por_produto[i]}, Mínimo: {minimos_por_produto[i]}, Desvio Padrão: {desvio_padrao_por_produto[i]}, Média: {media_por_produto[i]}, Mediana: {mediana_por_produto[i]}")


produto_p1 = data_frame[data_frame['Product_Code'] == 'P1']

# Crie uma lista para armazenar as médias móveis de intervalo 3
medias_moveis = []

# Itere pelas semanas a partir da semana W1 até a semana W(len(produto_p1.columns) - 2)
for i in range(1, len(produto_p1.columns) - 1):
    # Calcule a média das vendas nas 3 semanas consecutivas
    media_movel = produto_p1.iloc[:, i:i+3].mean(axis=1)
    medias_moveis.extend(media_movel)

# Crie uma lista de números de semana correspondentes às médias móveis
semanas = list(range(1, len(medias_moveis) + 1))

# Crie um gráfico de linha das médias móveis em relação às semanas
plt.figure(figsize=(10, 6))
plt.plot(semanas, medias_moveis, marker='o', linestyle='-', color='b')
plt.xlabel('Semana')
plt.ylabel('Média Móvel de Vendas (Intervalo 3 semanas)')
plt.title('Média Móvel de Vendas do Produto P1 com Intervalo 3 semanas (Começando em W1)')
plt.grid(True)
plt.show()

