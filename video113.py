def multiplicar(*args):
  total = 1
  for numero in args:
    total *= numero
  print(total)


def descobrir(numero):
  if numero % 2 == 0:
    print("Número par!")
  else:
    print("Número ímpar!")


multiplicar(2, 4, 10)
descobrir(81)
