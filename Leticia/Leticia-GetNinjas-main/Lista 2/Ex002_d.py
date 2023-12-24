import numpy as np
from typing import Tuple


def gera_dados_2(n: int) -> Tuple[np.array, np.array]:
    """Gera vetores para a letra d

    :param n: Tamanho do array
    :type n: int

    :return:
        Tuple[np.array, np.array]: retorna dois arrays para se calcular a similaridade.

    """
    np.random.seed(15)

    array_1 = np.random.choice([0, 1], size=(n,), p=[0.25, 0.75])
    array_2 = np.random.choice([0, 1], size=(n,), p=[0.5, 0.5])
    return array_1, array_2

n = 5
array_1, array_2 = gera_dados_2(n)

print("Array 1:")
print(array_1)

print("\nArray 2:")
print(array_2)

def indice_jaccard(array_1, array_2):
    intersection = np.sum(np.logical_and(array_1, array_2))
    union = np.sum(np.logical_or(array_1, array_2))

    jaccard_index = intersection / union
    return jaccard_index

jaccard_result = indice_jaccard(array_1, array_2)
print("Índice de Jaccard:")
print(jaccard_result)
