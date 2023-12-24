inicio = int(input("Informe o valor de início: "))
fim = int(input("Informe o valor de fim: "))

if fim <= inicio:
    print("O valor de fim deve ser maior que o valor de início. Invertendo os valores.")
    inicio, fim = fim, inicio

print("Valores divisíveis por 5 no intervalo de {} a {}:".format(inicio, fim))
for numero in range(inicio, fim + 1):
    if numero % 5 == 0:
        print(numero)
