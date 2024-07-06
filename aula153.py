from typing import Any


class Teste:
  def __call__(self):
    print("Testando possibilidade de ser chamado sem instancia")


class CallMe:
  def __init__(self, phone):
    self.phone = phone

  
  def __call__(self, nome) -> Any:
    print(f"{nome} está ligando para {self.phone}...")


call1 = CallMe("291391334") 
call1("Alexandre")
Teste()
