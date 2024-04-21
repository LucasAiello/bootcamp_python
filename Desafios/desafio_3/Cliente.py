from datetime import date
import Conta
import Transacao

class Cliente:
    def __init__(self, endereco: str):
        self.__endereco = endereco
        self.__contas = list()

    @property
    def endereco(self):
        return self.__endereco

    @property
    def contas(self):
        return self.__contas

    def adicionar_conta(self, conta: Conta):
        self.__contas.append(conta.nova_conta(self))
        
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, data_nascimento: date):
        super.__init__(endereco)
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    