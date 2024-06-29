class Foo:
  def __init__(self):
    self.public = "Atributo público"
    self.protected = "Atributo protegido"
    self.__private = "Atributo privado"

  def metodo_publico(self):
    return "Metodo público"
  

  def _metodo_protected(self):
    return "Metodo protegido"
  

  def __metodo_private(self):
    return "Metodo privado"
  

f = Foo()
print(f.public)
print(f.metodo_publico())
