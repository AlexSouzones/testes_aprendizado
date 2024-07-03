class Trabalhador:
  def __init__(self, nome, job):
    self.nome = nome
    self.job = job
    self.__cpf = None


  @property
  def cpf(self):
    return self.__cpf
  

  @cpf.setter
  def cpf(self, valor):
    self.__cpf = valor



p1 = Trabalhador("Carlos", "Bombeiro")
p1.cpf = ("1231412")
print(p1.cpf)
print(p1.__cpf)
