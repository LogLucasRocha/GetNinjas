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

def exercicio_2_c(a: np.array, b: np.array) -> float:

    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    similarity = dot_product / (norm_a * norm_b)
    return similarity

n = 2  
array_1, array_2 = gera_dados_1(n)
similaridade_result_cosseno = exercicio_2_c(array_1, array_2)
print("Similaridade de Cosseno:")
print(similaridade_result_cosseno)
