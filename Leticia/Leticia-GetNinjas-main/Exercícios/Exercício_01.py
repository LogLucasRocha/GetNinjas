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
def calcula_media_movel(valores):
    media_movel = []
    for i in range(2, len(valores)):
        media = (valores[i-2] + valores[i-1] + valores[i]) / 3
        media_movel.append(round(media, 2))  # Arredonda para duas casas decimais
    return media_movel

# Definição do tamanho da lista pelo usuário.
tamanho = int(input('Digite o tamanho da lista: '))

# Chamada da função que gera os dados.
dados_ma = gerar_dados_ma(tamanho)

# Chamada da função que calcula a média móvel.
media_movel_resultado = calcula_media_movel(dados_ma)
print("Média Móvel:", media_movel_resultado)


