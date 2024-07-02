class Carrinho:
  def __init__(self):
    self._produtos =  []


  def total(self):
    return sum([p.preco for p in self._produtos])
  

  def listar_produtos(self):
    for produto in self._produtos:
      print(produto.nome, produto.preco)


  def inserir_produtos(self, *produtos):
    ([self._produtos.append(produto) for produto in produtos])
      

class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco
  


carrinho = Carrinho()
p1, p2 = Produto("coca-cola", 9), Produto("azeite", 5.50)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()


