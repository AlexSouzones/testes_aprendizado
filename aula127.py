import json

caminho = 'aula127.json'

class Pessoa:
  def __init__(self, nome, idade): 
    self.nome = nome
    self.idade = idade


p1 = Pessoa("João", 23)
p2 = Pessoa("Maria", 22)
p3 = Pessoa("Lucas", 30)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]

with open (caminho, 'w') as arquivo:
  json.dump(bd, arquivo, ensure_ascii=False, indent=2)
