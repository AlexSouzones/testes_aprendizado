# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0

for pergunta in perguntas:
  print(pergunta["Pergunta"])

  for i, escolha in enumerate(pergunta["Opções"]):
    print(f"{i}) {escolha}")
  resposta = int(input("Digite uma alternativa: "))

  if resposta < len(pergunta["Opções"]):

    if pergunta["Resposta"] == pergunta["Opções"][resposta]:
      print("Você Acertou!")
      respostas_certas += 1
      
  else:
    print("Você errou!")

else:
  print(f"Você acertou {respostas_certas} de 3")