# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

estados = ['BA', 'SP', 'MG', 'RJ']

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

def unir_listas(lista1, lista2):
  lista_unida = zip(lista1, lista2)
  print(tuple(lista_unida))


unir_listas(estados, cidades)
