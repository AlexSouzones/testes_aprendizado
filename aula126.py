class Pessoa:
  ano_atual = 2024

  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade


  def get_ano_nascimento(self):
    print(f"{self.nome} nasceu em {self.ano_atual - self.idade}")


p1 = Pessoa("Maria", 20)

p2 = Pessoa("Joao", 40)

p2.nome = "Carlos"

p2.signo = "Leão"
print(p2.__dict__)
print(vars(p1))
