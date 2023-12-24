n = int(input("Digite a quantidade de ingressos: "))
dia = input("Digite o dia da semana para os ingressos: ")

idades = [] # Inicializa uma lista vazia para armazenar as idades
valores = [] # Inicializa uma lista vazia para armazenar os valores
i = 1 # Inicializa o contador

#Contadores
descontos = 0
infantil = 0
idoso = 0
normal = 0

while i <= n:
    idade = int(input("Digite a idade do ingresso {}: ".format(i)))
    idades.append(idade)  # Adiciona a idade à lista
    if idade <= 12:
        ingresso = float(25.00)
        infantil += 1
    elif idade >= 61:
        ingresso = float(20.00)
        idoso += 1
    else :
        if dia == "segunda" or dia == "segunda-feira" or dia == "Segunda" or dia == "Segunda-feira" or dia == "Segunda-Feira" or dia == "segunda feira" or dia == "Segunda Feira":
            ingresso = float(25.00)
            normal += 1
            descontos += 1
        else: 
            ingresso = float(40.00)
            normal += 1
    valores.append(ingresso)  # Adiciona o valor à lista
    i += 1 

subtotal = (infantil * 25.00) + (idoso * 20.00)  + (normal * 40.00)
print("O subtotal da compra de {} ingressos é de R$ {:.2f}.".format(n, subtotal))

descontos = (descontos * 15.00)
print("O total de descontos é de R$ {:.2f}.".format(descontos))

total = subtotal - descontos
print("O total a pagar é de R$ {:.2f}.".format(total))
