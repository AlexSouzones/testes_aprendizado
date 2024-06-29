class Pessoa:
  ano_atual = 2024 # -> atributo

  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade

  @classmethod
  def metodo_classe(cls):
    print("Hey")

  @classmethod
  def criar_com_50(cls, nome):
    return cls(nome, 50)
  

  @classmethod
  def criar_sem_nome(cls, idade):
    return cls("anonimo", idade)


p1 = Pessoa.criar_com_50("João")
print(p1.nome, p1.idade)
p2 = Pessoa.criar_sem_nome(20)
print(p2.nome, p2.idade)
