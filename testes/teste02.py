class Login:
  def __init__(self, nome):
    self.nome = nome
    self.__senha = None


  @property
  def senha(self):
    return self.__senha
  

  @senha.setter
  def senha(self, senha):
    self.__senha = senha


u1 = Login("Angelica")
u1.senha = "Miau"
print(u1.senha)
