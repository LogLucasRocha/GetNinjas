while True:
    entrada = input("Digite um número inteiro positivo (ou 'X' para sair): ")
    
    if entrada == 'X':
        break  
    
    try:
        numero = int(entrada)
        if numero > 0:
            divisivel_por_2 = numero % 2 == 0
            divisivel_por_3 = numero % 3 == 0

            print(f"Número: {numero} {', Divisível por 2' if divisivel_por_2 else ''} {', Divisível por 3' if divisivel_por_3 else ''}")
        else:
            print("Por favor, digite um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo ou 'X' para sair.")
