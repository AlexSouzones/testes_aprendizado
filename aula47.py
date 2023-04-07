"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

tentativa = 0
palavra = "alexe"
segredo = len(palavra) * "*"

while True:
    tentativa += 1
    letra = input("Digite uma letra: ")
    tipo = letra.isalpha()
    tamanho = len(letra)

    if tamanho > 1:
        print("Você apenas pode digitar uma letra!")
        continue

    elif tamanho < 1:
        print("Digite ao menos uma letra!")
        continue

    elif not tipo:
        print("Digite um carácter válido!")
        continue

    letra = letra.lower()


    item = 0
    formando = ""
    for p in palavra:
        if segredo[item] != "*":
            formando += segredo[item]
        elif letra == p:
            formando += letra
        else:
            formando +=  "*"

        
        item += 1

    else:
        segredo = formando

    if segredo == palavra:
        os.system("cls")
        print("Parabéns, você acertou!\n"\
              f"A palavra era {palavra}")
        segredo = len(palavra) * "*"
        print(f"Tentativas: {tentativa}")
        tentativa = 0
    else:
        print(segredo)
