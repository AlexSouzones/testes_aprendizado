cpf = "746824890"
soma = 0
contagem = 10

for digito in cpf:
    soma += int(digito) * contagem
    contagem -= 1

calculo = (soma * 10) % 11

primeiro_digito = calculo if calculo <= 9 else 0
print(primeiro_digito)
