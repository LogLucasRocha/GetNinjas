import random

codigo_produto = random.randint(10000, 99999)

a, b, c, d, e = [int(digito) for digito in str(codigo_produto)]

# Aplica os fatores de multiplicação
a *= 2
b *= 3
c *= 4
d *= 5
e *= 6

soma_resultados = a + b + c + d + e
digito_verificador = soma_resultados % 7

codigo_formatado = f"{codigo_produto}-{digito_verificador}"

print("Código de Produto com Dígito Verificador:", codigo_formatado)
