from Transacao import *

class Historico:
    def __init__(self):
        self.__transacoes = list()

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, transacao: Transacao):
        self.__transacoes.append(f"{transacao.__class__.__name__} | valor: {transacao.valor()}")

    def __str__(self):
        output = ""
        for transacao in self.__transacoes:
            output += f"{transacao}\n"
        
        return output