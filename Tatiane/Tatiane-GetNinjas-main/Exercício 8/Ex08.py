def obtem_dadosFuncionarios():
    dados_funcionario = {}  # Inicializa um dicionário vazio para armazenar os dados do funcionário

    dados_funcionario["Matrícula"] = input("Matrícula do funcionário: ")
    dados_funcionario["Nome"] = input("Nome do funcionário: ")
    dados_funcionario["Gênero"] = input("Gênero do funcionário: ")
    dados_funcionario["Departamento"] = input("Departamento do funcionário: ")
    dados_funcionario["Tempo de Serviço"] = float(input("Tempo de serviço do funcionário (em anos): "))
    dados_funcionario["Salário"] = float(input("Salário do funcionário: "))

    return dados_funcionario

# Inicializa uma lista vazia para armazenar os dados de vários funcionários
funcionarios = []

n = int(input("Quantos funcionários deseja cadastrar? "))

for i in range(n):
    print(f"Informações do funcionário {i + 1}:")
    funcionario = obtem_dadosFuncionarios()
    funcionarios.append(funcionario)

# Imprime a tabela de funcionários com cabeçalhos
cabecalho = "Matrícula".ljust(12) + "Nome".ljust(20) + "Gênero".ljust(8) + "Departamento".ljust(20) + "Tempo de Serviço".ljust(20) + "Salário".ljust(10)
print("\nTabela de Funcionários:")
print(cabecalho)

for funcionario in funcionarios:
    matricula = funcionario['Matrícula'].ljust(12)
    nome = funcionario['Nome'].ljust(20)
    genero = funcionario['Gênero'].ljust(8)
    departamento = funcionario['Departamento'].ljust(20)
    tempo_servico = str(funcionario['Tempo de Serviço']).ljust(20)
    salario = str(funcionario['Salário']).ljust(10)
    
    print(f"{matricula}{nome}{genero}{departamento}{tempo_servico}{salario}")

