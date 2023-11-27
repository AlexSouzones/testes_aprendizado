def multiplicar(*args):
  total = 1
  for argumento in args:
    total = total * argumento
  print(total)
  return total


def par_ou_impar(valor):
  if valor % 2 == 0:
    print(f"{valor} é um número par!")
  else:
    print(f"{valor} é um número ímpar!")


par_ou_impar(7)
