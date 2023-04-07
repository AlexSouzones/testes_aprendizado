"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# n1 = input("Digite um número inteiro: ")
# try:
#     if int(n1) % 2 == 0:
#         print(f"{n1} é um número par!")
#     else:
#         print(f"{n1} é um número ímpar!")

# except:
#     print("Isso não é um número inteiro!!!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Que horas são? ")

# try:
#     hora = int(hora)
#     if hora >= 11 and hora <= 11:
#         print("Bom dia!")
#     elif hora > 11 and hora < 18:
#         print("Boa tarde!")
#     elif hora >= 18 and hora <= 23:
#         print("Boa noite!")
#     else:
#         print("Essa hora não existe!")
# except:
#     print("Isso não é uma hora!!!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Qual o seu primeiro nome? ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")