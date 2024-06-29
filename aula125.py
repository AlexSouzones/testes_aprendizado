class Pessoa:
  ano_atual = 2024

  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade


  def get_ano_nascimento(self):
    print(f"{self.nome} nasceu em {self.ano_atual - self.idade}")


p1 = Pessoa("Maria", 20)

p1.get_ano_nascimento()

p2 = Pessoa("Joao", 40)

p2.get_ano_nascimento()
