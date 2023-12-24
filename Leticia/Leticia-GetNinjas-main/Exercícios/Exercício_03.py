def gerar_features(size: int) -> list:
  """Gera dados do exercicio 3

  :param size: Número de observações
  :type size: int
  :param features: Número de features
  :type features: int

  :return:
    lista: Dicionario com as observações
  """
  import random
  random.seed(15)

  if size <= 2:
    raise Exception('Tamanho deve ser no minimo 3')

  output_list = []
  for k in range(size):
    output_list.append(random.gauss(4, 3))

  return output_list

def calcular_desvio_padrao(valores):
    n = len(valores)
    media = sum(valores) / n
    somatorio = sum((x - media) ** 2 for x in valores)
    desvio_padrao = (somatorio / (n - 1)) ** 0.5
    return desvio_padrao

def transformar_features(valores):
    # Feature original
    feature_original = valores

    # Normalização Z-score
    media = sum(valores) / len(valores)
    desvio_padrao = round(calcular_desvio_padrao(valores), 2)
    feature_z_score = [round((x - media) / desvio_padrao, 2) for x in valores]

    # Normalização Max-Min
    min_valor = min(valores)
    max_valor = max(valores)
    feature_max_min = [round((x - min_valor) / (max_valor - min_valor), 2) for x in valores]

    # Retornar as features
    return [feature_original, feature_z_score, feature_max_min]

# Solicitar o tamanho da feature até que seja válido
while True:
    tamanho_feature = int(input('Digite o tamanho da feature: '))
    if tamanho_feature >= 3:
        break
    else:
        print("O tamanho deve ser no mínimo 3. Por favor, insira um valor válido.")

# Gerar as features usando a função do professor
features = gerar_features(tamanho_feature)

# Transformar as features
features_transformadas = transformar_features(features)

# Imprimir o resultado
print("Features Originais:", features_transformadas[0])
print("Features Z-score:", features_transformadas[1])
print("Features Max-Min:", features_transformadas[2])