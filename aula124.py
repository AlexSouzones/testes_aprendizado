class Camera:

  def __init__(self, nome, filmando=False):
    self.nome = nome
    self.filmando = filmando

  
  def filmar(self):
    if self.filmando:
      print(f"{self.nome} já está filmando!")
      return
    print(f"{self.nome} está filmando. . .")
    self.filmando = True


  def fotografar(self):
    if self.filmando:
      print(f"{self.nome} não pode fotografar, está filmando!")
      return
    
    print(f"{self.nome} fotografou este momento!")


  def parar_filmar(self):
    if not self.filmando:
      print(f"{self.nome} não está filmando!")
      return
    
    print(f"{self.nome} parou de filmar!")
    self.filmando = False

  
tekpix = Camera("TekPix")
canon = Camera("Canon")
tekpix.filmar()
print(tekpix.filmando)
print(canon.filmando)
tekpix.filmar()
canon.parar_filmar()
tekpix.parar_filmar()
