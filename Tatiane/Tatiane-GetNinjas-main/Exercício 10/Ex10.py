N = int(input("Digite um número inteiro entre 1 e 50: "))

if N < 1 or N > 50:
    print("Número fora do intervalo válido.")
else:
    import random
    lista_A = [random.uniform(-100, 100) for _ in range(N)]

    # Separa os valores em listas NEG e POS
    NEG = [valor for valor in lista_A if valor < 0]
    POS = [valor for valor in lista_A if valor >= 0]

    # Apresenta as duas listas e a quantidade de elementos em cada uma
    print("Lista de valores negativos (NEG):", NEG)
    print("Quantidade de elementos em NEG:", len(NEG))
    print("Lista de valores positivos e zero (POS):", POS)
    print("Quantidade de elementos em POS:", len(POS))
