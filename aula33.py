"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
letra = 0

nova_string = ''
#nova_string += '*L*u*i*z* *O*t*á*v*i*o'

while letra < tamanho_nome:
    nova_string += f"*{nome[letra]}*"
    letra += 1

print(nova_string)