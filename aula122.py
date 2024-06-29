class Carro:
  ...

  def __init__(abc, nome, cor):
    abc.nome = nome
    abc.cor = cor


  def acelerar(self):
    print(f"O {self.nome} está acelerando!")
     



fusca = Carro("Fusca", "Azul")
camaro = Carro("Camaro", "Amarelo")
celta = Carro("Celta", "Branco")

Carro.acelerar(celta)
# print(fusca.nome)
# print(camaro.nome, camaro.cor)
# print(celta.nome, celta.cor)

# print(fusca.acelerar())

