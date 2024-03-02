def somar_listas(lista1, lista2):

  somas = []
  lista_unificada = list(zip(lista1, lista2))

  for tupla in lista_unificada:
    somas.append(tupla[0]+tupla[1])

  return somas

l1 = [1, 2, 3, 4]

l2 = [1, 2, 3]

print(somar_listas(l1, l2))
