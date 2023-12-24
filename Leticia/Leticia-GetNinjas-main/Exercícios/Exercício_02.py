def gerar_dados_ma(size:int) -> list:
  """Gera dados do exercicio 1 e 2

  :param size: Número de observações
  :type size: int

  :return:
    lista: Lista com as observações
  """

# Todo o código desse bloco é apenas para gerar os dados.

  import random
  random.seed(15)

  if size <= 2:
    raise Exception('Tamanho deve ser no minimo 3')

  output_list = []
  output_list.append(random.gauss(0, 2))

  output_list.append(random.gauss(0, 2))
  for k in range(2, size):
    new_obs = 0.8*output_list[k-1] - 0.5*output_list[k-2] + random.gauss(0, 2)
    output_list.append(new_obs)

  return output_list

# Definição da função que calcula a média móvel.
def calcula_media_movel_parametros(valores, dias_media_movel):
    if len(valores) < dias_media_movel:
        raise ValueError("O volume de dados deve ser maior ou igual ao número de dias para a média móvel.")

    media_movel = []
    for i in range(dias_media_movel - 1, len(valores)):
        media = sum(valores[i - dias_media_movel + 1:i + 1]) / dias_media_movel
        media_movel.append(media)

    return media_movel

# Definição do tamanho da lista pelo usuário.
tamanho = int(input('Digite o tamanho da lista: '))

# Chamada da função que gera os dados.
dados_ma = gerar_dados_ma(tamanho)

parametro_media_movel = int(input('Digite o parâmetro da média móvel: '))

# Chamada da função que calcula a média móvel com parâmetro
media_movel_resultado_parametro = calcula_media_movel_parametros(dados_ma, parametro_media_movel)
print("Média Móvel com Parâmetro:", media_movel_resultado_parametro)
