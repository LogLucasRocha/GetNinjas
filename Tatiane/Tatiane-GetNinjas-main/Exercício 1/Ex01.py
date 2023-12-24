nome = input("NOME DO LUTADOR: ")
peso = float(input("PESO: "))

if peso < 65:
    print("O lutador {} pesa {}Kg e se enquadra na categoria pena".format(nome, peso))
elif peso < 72:
    print("O lutador {} pesa {}Kg e se enquadra na categoria leve".format(nome, peso))
elif peso < 79:
    print("O lutador {} pesa {}Kg e se enquadra na categoria ligeiro".format(nome, peso))
elif peso < 86:
    print("O lutador {} pesa {}Kg e se enquadra na categoria meio-médio".format(nome, peso))
elif peso < 93:
    print("O lutador {} pesa {}Kg e se enquadra na categoria médio".format(nome, peso))
elif peso < 100:
    print("O lutador {} pesa {}Kg e se enquadra na categoria meio-pesado".format(nome, peso))
else: 
    print("O lutador {} pesa {}Kg e se enquadra na categoria pesado".format(nome, peso))
