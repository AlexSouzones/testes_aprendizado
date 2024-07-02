class Fabricante:
  def __init__(self, nome):
    self.nome = nome


class Motor:
  def __init__(self, nome):
    self.nome = nome


class Carro:
  def __init__(self, nome):
    self.nome = nome
    self._fabricante = None
    self._motor = None


  @property
  def motor(self):
    return self._motor
  

  @motor.setter
  def motor(self, valor):
    self._motor = valor


  @property
  def fabricante(self):
    return self._fabricante
  

  @fabricante.setter
  def fabricante(self, valor):
    self._fabricante = valor
  


fusca = Carro("Fusca")
ford = Fabricante("Ford")
v_oito = Motor("V8")
fusca.fabricante = ford
fusca.motor = v_oito

print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)

camaro = Carro("Camaro")
ferrari = Fabricante("Ferrari")
motor_7_0 = Motor("7.0")
camaro.fabricante = ferrari
camaro.motor = motor_7_0

print(camaro.nome, camaro.motor.nome, camaro.fabricante.nome)
