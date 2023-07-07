import os

lista_compras = []

while True:
    comando = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ").lower()
    os.system("cls")
    if comando == "l":
        if lista_compras:
            for indice, produto in enumerate(lista_compras):
                print(indice, produto)
        else:
            print("Nada para listar")
    elif comando == "i":
        valor = input("Valor: ")
        while not valor:
            print("Digite um nome!")
            valor = input("Valor: ")
        else:
            lista_compras.append(valor)
    elif comando == "a":
        item = input("Escolha o indice para apagar: ")
        if item.isdigit():
            while len(lista_compras) <= int(item):
                print("Digite um indice válido!")
                item = input("Escolha o indice para apagar: ")
                while not item.isdigit():
                    print("Digite um indice númerico!")
                    item = input("Escolha o indice para apagar: ")
            lista_compras.pop(int(item))
        else:
            print("Isso não é um indice!")
    else:
        print("Digite um comando válido!")


            