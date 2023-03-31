primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor = '{primeiro_valor}' é "
          f"maior que o segundo valor = '{segundo_valor}'")

elif segundo_valor > primeiro_valor:
    print(f"O segundo valor = '{segundo_valor}' é "
          f"maior que o primeiro valor = '{primeiro_valor}'")

else:
    print(f"O primeiro valor = '{primeiro_valor}' é "
         f" igual ao segundo valor = '{segundo_valor}'")