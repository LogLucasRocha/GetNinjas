import random

n = int(input("Informe a quantidade de números desejados: "))

# Lista de números positivos
numeros_positivos = [random.randint(1, 100) for _ in range(n)]

# Lista de números negativos
numeros_negativos = [-random.randint(1, 100) for _ in range(n)]

print("Números positivos:", numeros_positivos)
print("Números negativos:", numeros_negativos)

soma_positivos = sum(numeros_positivos)
soma_negativos = sum(numeros_negativos)

print("Soma dos números positivos:", soma_positivos)
print("Soma dos números negativos:", soma_negativos)
