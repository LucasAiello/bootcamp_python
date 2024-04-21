import Historico
import Cliente

class Conta:
    def __init__(self, cliente: Cliente, numero: int):
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = 0.0
        self.__agencia = "001"
        self.__historico = Historico()

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def historico(self):
        return self.__historico
    
    def nova_conta(self, cliente: Cliente, numero = 1):
        return Conta(cliente, numero)
    
    def sacar(self, valor: float):
        if valor <= self.saldo() and valor > 0:
            self.__saldo -= valor
            return True
        return False
    
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, limite: float, limite_saques: int):
        super.__init__(cliente, numero)
        self.__limite = limite
        self.__limite_saques = limite_saques

    def sacar(self, valor: float):
        if valor > 0:
            if self.__limite_saques > 0:
                if valor <= self.saldo():
                    self.__saldo -= valor
                    self.__limite_saques -= 1
                    return True
                else:
                    sobra = valor - self.__saldo
                    if sobra <= self.__limite:
                        self.__saldo = 0
                        self.__limite -= sobra
                        self.__limite_saques -= 1
                        return True
        return False
    
    def depositar(self, valor: float):
        return super().depositar(valor)
    