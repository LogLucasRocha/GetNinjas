def gerar_features_dict(size: int, features: int) -> dict:
    """Gera dados do exercicio 4

    :param size: Número de observações
    :type size: int
    :param features: Número de features
    :type features: int

    :return:
        dict: Dicionário com as observações
    """
    import random
    random.seed(15)

    output_dict = {}
    mean = 3
    sd = 1

    for j in range(features):
        output_dict[f'feature_{j}'] = []
        for k in range(size):
            output_dict[f'feature_{j}'].append(random.gauss(mean, sd))
        mean += 0.5
        sd *= 1.1

    return output_dict

def calcular_desvio_padrao(valores):
    n = len(valores)
    media = sum(valores) / n
    somatorio = sum((x - media) ** 2 for x in valores)
    desvio_padrao = (somatorio / (n - 1)) ** 0.5
    return desvio_padrao

def padronizar_features_dict(dados, tipo_padronizacao):
    if tipo_padronizacao not in ['z-score', 'max-min']:
        raise ValueError('O tipo de padronização deve ser "z-score" ou "max-min".')

    features_padronizadas = {}

    for chave, valores in dados.items():
        if tipo_padronizacao == 'z-score':
            media = sum(valores) / len(valores)
            desvio_padrao = calcular_desvio_padrao(valores)
            features_padronizadas[chave] = [round((x - media) / desvio_padrao, 2) for x in valores]
        elif tipo_padronizacao == 'max-min':
            min_valor = min(valores)
            max_valor = max(valores)
            features_padronizadas[chave] = [round((x - min_valor) / (max_valor - min_valor), 2) for x in valores]

    return features_padronizadas

# Solicitar informações do usuário com validação
while True:
    tamanho_amostra = int(input('Digite o tamanho da amostra (deve ser no mínimo 3): '))
    num_features = int(input('Digite o número de features (deve ser no mínimo 2): '))

    if tamanho_amostra >= 3 and num_features >= 2:
        break
    else:
        print('Valores inválidos. Por favor, tente novamente.')

# Gerar o dicionário de features
output_dict = gerar_features_dict(tamanho_amostra, num_features)

# Escolher o tipo de padronização
tipo_padronizacao = input('Escolha o tipo de padronização ("z-score" ou "max-min"): ')

# Padronizar as features utilizando o output_dict
features_padronizadas = padronizar_features_dict(output_dict, tipo_padronizacao)

# Imprimir o resultado
print("Features Padronizadas:")
print(features_padronizadas)
