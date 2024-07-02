class Endereco:
  def __init__(self, rua, numero):
    self.numero = numero
    self.rua = rua


class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.enderecos = []

  
  def inserir_enderecos(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))


  def listar_enderecos(self):
    ([print(endereco.rua, endereco.numero) for endereco in self.enderecos])
    
    
cliente = Cliente("Maria")
cliente.inserir_enderecos("25 de março", 56)
cliente.inserir_enderecos("Belarmino", 63)
cliente.listar_enderecos()
