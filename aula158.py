"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Cliente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia:str, n_conta:str, saldo:float):
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        return f"depositou {valor}"
      

    @abstractmethod
    def sacar(self, valor):
        ...
   
   
class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta


class ContaCorrente(Conta):
  
  def sacar(self, valor):
      if self.saldo < valor:
          msg = f"Você apenas tinha {self.saldo} e o banco te emprestou {valor - self.saldo} para seu saque"
          self.saldo = 0
          return msg
      else:
          self.saldo = self.saldo - valor
          return f"sacou {valor} e ficou com {self.saldo}"
      

class ContaPoupanca(Conta):
  def sacar(self, valor):
      if self.saldo < valor:
          return f"Saldo insuficiente"
      else:
          self.saldo = self.saldo - valor
          return f"sacou {valor} e ficou com {self.saldo}"


class Banco:
    def __init__(self, nome: str, agencia: str):
        self.nome = nome
        self.agencia = agencia
        self.contas = []
        self.clientes = []



    



c1 = ContaCorrente("0001", "5533", 200.5) 
p1 = Cliente("Alexandre", 22, c1)
    
nubank = Banco("Nubank", "0001")

print(p1.conta.sacar(300))