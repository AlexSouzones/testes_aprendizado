class Pessoa:
  ...

  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome


p1 = Pessoa("Alex", "Souza")
p2 = Pessoa("Rebekah", "Souza")

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)