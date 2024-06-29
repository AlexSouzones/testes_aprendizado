class Animal:

  def __init__(self, nome):
    self.nome = nome

    variavel = "valor"
    print(variavel)

  def comendo(self, alimento):
    return f"O {self.nome} está comendo {alimento}!"
  
  def executando(self, *args, **kwargs):
    return self.comendo(*args, **kwargs)


leao = Animal("Leão")
print(leao.nome)
print(leao.executando("carne"))