while True:
    n = float(input("FORNEÇA UM NÚMERO (ou digite 0 para sair): "))
    
    if n == 0:
        print("Encerrando o programa.")
        break
    
    print("A tabuada do número {} é:".format(int(n)))
    for i in range(1, 11):
        result = n * i
        print("{} x {} = {}".format(int(n), int(i), int(result)))
    
    continuar = input("Deseja continuar o programa? (Digite 'sim' para continuar, ou qualquer outra coisa para parar): ")
    if continuar.lower() != 'sim':
        print("Encerrando o programa.")
        break
