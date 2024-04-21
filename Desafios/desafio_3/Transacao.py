import abc as ABC
from Conta import *

class Transacao(ABC):

    @ABC.abstractmethod
    def __init__(self, valor: float):
        ...
    
    @ABC.abstractmethod
    def registrar(self, conta: Conta):
        ...

    @property
    @ABC.abstractmethod
    def valor(self):
        ...

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor
    
    def registrar(self, conta: Conta):
        if conta.depositar(self.__valor):
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self.__valor

class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self.__valor):
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self.__valor
    