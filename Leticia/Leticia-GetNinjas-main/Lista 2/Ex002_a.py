import numpy as np
from typing import Tuple

def gera_dados_1(n: int) -> Tuple[np.array, np.array]:
    """Gera vetores para as letras a, b e c.

    :param n: Tamanho do array.
    :type n: int

    :return:
      Tuple[np.array, np.array]: retorna dois arrays para se calcular a similaridade.

    """
    np.random.seed(15)
    array_1 = np.random.normal(size=n)
    array_2 = np.random.normal(size=n)
    return array_1, array_2

def exercicio_2_a(a: np.array, b: np.array) -> float:
    distance = np.linalg.norm(a - b)
    return distance

n = 2  
array_1, array_2 = gera_dados_1(n)
distancia_result = exercicio_2_a(array_1, array_2)
print("Distância Euclidiana:")
print(distancia_result)
