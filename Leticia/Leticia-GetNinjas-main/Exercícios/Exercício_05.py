from typing import Tuple
def gerar_listas(size: int, users: int) -> Tuple[list, list]:
  """Gera dados do exercicio 4

  :param size: Número de observações
  :type size: int
  :param users: Número de usuários
  :type features: int

  :return:
    Tuple[list, list]: Lista com o identificador dos usuários e lista com o valor da compra.
  """
  import random
  random.seed(15)

  if size <= users * 4:
    raise Exception('Amostra deve ser 4 vezes maior que o número de usuarios')



  id_user = []
  receita = []

  for k in range(size):
    id_user.append(random.randint(0, users))
    receita.append(random.gammavariate(10, 200))


  return id_user, receita

def calcular_valor_maximo_compras(id_user, receita):
    if len(id_user) != len(receita):
        raise ValueError("As listas de IDs e valores de compras devem ter o mesmo tamanho.")

    valor_maximo_por_usuario = {}

    for id_usuario, valor_compra in zip(id_user, receita):
        if id_usuario in valor_maximo_por_usuario:
            # Se o usuário já está no dicionário, atualiza o valor máximo se o novo valor for maior
            valor_maximo_por_usuario[id_usuario] = round(max(valor_maximo_por_usuario[id_usuario], valor_compra), 2)
        else:
            # Se o usuário não está no dicionário, adiciona com o valor atual
            valor_maximo_por_usuario[id_usuario] = round(valor_compra, 2)

    return valor_maximo_por_usuario

# Exemplo de uso
id_user, receita = gerar_listas(100, 10)
dic_valor_maximo_compras = calcular_valor_maximo_compras(id_user, receita)
print("Dicionário Valor Máximo de Compras:", dic_valor_maximo_compras)
