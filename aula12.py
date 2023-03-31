nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em KG: "))
imc = peso / (altura * altura)
print(f"{nome}, o seu IMC é igual a {imc}!")

# codigo da aula:

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987