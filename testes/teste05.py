class Login:
  def __init__(self, inst, matricula, password):
    self.inst = inst
    self.matricula = matricula
    self.password = password


  def logar(self):
    print(f"logando como {self.inst}")


uninassau = Login("Uninassau", "01412923", "01291239")
uninama = Login("Uninama", "54435346", "23131212")
uninama.logar()
