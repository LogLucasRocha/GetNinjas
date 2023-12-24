import numpy as np

numero_sorteado_1 = np.random.randint(1, 16)
numero_sorteado_2 = np.random.randint(1, 16)
np.random.seed(numero_sorteado_1) 
entrada = np.random.rand(numero_sorteado_2).astype(float)

print("Entrada original:")
print(entrada)

def exercicio_1_a(array):
    for i in range(len(array)):
        valor = array[i]
        if 0.6 <= valor <= 1:
            array[i] = valor * 0.8
        elif 0.2 <= valor < 0.6:
            array[i] = valor * 0.85
        elif 0 <= valor < 0.2:
            array[i] = valor * 0.9

# Chamar a função
exercicio_1_a(entrada)

def exercicio_1_b(array):
    # Condição para o intervalo [0.6, 1]
    condicao_1 = (array >= 0.6) & (array <= 1)
    array[condicao_1] *= 0.8

    # Condição para o intervalo [0.2, 0.6]
    condicao_2 = (array >= 0.2) & (array < 0.6)
    array[condicao_2] *= 0.85

    # Condição para o intervalo [0, 0.2]
    condicao_3 = (array >= 0) & (array < 0.2)
    array[condicao_3] *= 0.9

# Chamar a função
exercicio_1_b(entrada)

print("Entrada modificada (Exercício_1_a):")
print(entrada)
print("Entrada modificada (Exercício_1_b):")
print(entrada)
