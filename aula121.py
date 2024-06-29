class Carro:
  ...

  def __init__(self, nome, cor):
    self.nome = nome
    self.cor = cor


  def acelerar(self):
    return f"O {self.nome} está acelerando!"
     



fusca = Carro("Fusca", "Azul")
camaro = Carro("Camaro", "Amarelo")
celta = Carro("Celta", "Branco")


print(fusca.nome)
print(camaro.nome, camaro.cor)
print(celta.nome, celta.cor)

print(fusca.acelerar())
