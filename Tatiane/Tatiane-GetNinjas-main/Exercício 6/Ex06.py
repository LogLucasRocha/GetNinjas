import random

while True:
    la = int(input("Informe o tamanho da lista A: "))
    lb = int(input("Informe o tamanho da lista B: "))
    
    if la == lb:
        print("Os tamanhos das listas devem ser diferentes. Por favor, informe novos tamanhos.")
    else:
        break

listaA = [random.randint(1, 100) for _ in range(la)]
print("Lista A:", listaA)

listaB = [random.randint(1, 100) for _ in range(lb)]
print("Lista B:", listaB)

lista_intercalada = []

while listaA or listaB:  # Enquanto pelo menos uma das listas tiver elementos
    if listaA:
        lista_intercalada.append(listaA.pop(0))
    if listaB:
        lista_intercalada.append(listaB.pop(0))

print("Lista Intercalada:", lista_intercalada)
