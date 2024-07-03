from abc import ABC, abstractmethod


class Notificacao(ABC):
  def __init__(self, mensagem) -> None:
    self.mensagem = mensagem


  @abstractmethod
  def enviar(self) -> bool:
    ...

  
class Email(Notificacao):
  def enviar(self) -> bool:
    print(f"E-mail: enviando - {self.mensagem}")
    return True


class SMS(Notificacao):
  def enviar(self) -> bool:
    print(f"SMS: enviando - {self.mensagem}")
    return True


def notificar(notificacao: Notificacao):
  mensagem_enviada = notificacao.enviar()
  if mensagem_enviada:
    print("mensagem foi enviada")
  else:
    print("mensagem não foi enviada")


notificacao_sms = SMS("Olá")
n1 = notificar(notificacao_sms)


notificacao_Email = Email("Olá")
n2 = notificar(notificacao_Email)
