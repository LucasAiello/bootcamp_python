from datetime import date
import textwrap
import datetime
import abc as ABC

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

    def adicionar_conta(self, conta):
        self.__contas.append(conta.nova_conta(self))
        
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, data_nascimento: date, nome: str):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def __str__(self):
        return f"""
                   =======================================
                   Nome:       {self.__nome}
                   CPF:        {self.__cpf}
                   Endereco:   {super().endereco}
                   Data nasc.  {self.__data_nascimento}
                   Contas:     {len(super().contas)}
                   ======================================="""             

class Transacao():

    @ABC.abstractmethod
    def __init__(self, valor: float):
        ...
    
    @ABC.abstractmethod
    def registrar(self, conta):
        ...

    @property
    @ABC.abstractmethod
    def valor(self):
        ...

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor
    
    def registrar(self, conta):
        if conta.depositar(self.__valor):
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self.__valor

class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor
    
    def registrar(self, conta):
        if conta.sacar(self.__valor):
            conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self.__valor

class Historico:
    def __init__(self):
        self.__transacoes = list()

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, transacao: Transacao):
        self.__transacoes.append(f"{transacao.__class__.__name__} | valor: {transacao.valor}")

    def __str__(self):
        output = ""
        for transacao in self.__transacoes:
            output += f"{transacao}\n"
        
        return output

class Conta:
    def __init__(self, cliente: Cliente, numero: int):
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = 0.0
        self.__agencia = "001"
        self.__historico = Historico()

    def __str__(self):
        return f"Saldo: {self.__saldo} | Cliente: {self.__cliente.endereco}"

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def historico(self):
        return self.__historico
    
    def nova_conta(self, cliente: Cliente, numero = 1):
        return Conta(cliente, numero)
    
    def sacar(self, valor: float):
        if valor <= self.saldo and valor > 0:
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

def buscar_cliente(cpf: str, clientes: list):
    if len(clientes) == 0:
        print("\nNao ha nenhum cliente\n")
        return -1
    for posi in range(len(clientes)):
        if clientes[posi].cpf == cpf:
            return posi
        
    print("Nao ha nenhum cliente com o CPF informado")
    return False

def depositar(clientes: list):
    print("\tDEPOSITO\t")
    print("Informe o CPF:\t")
    cpf = input()
    posi  = buscar_cliente(cpf, clientes)
    if posi != -1:
        print("Selecione a conta: \t")
        conta = int(input())
        if len(clientes[posi].contas) == 0:
            print("Cliente nao possui conta")
            return False
        if len(clientes[posi].contas) <= posi:
            print("Conta invalida")
            return False
        print("\nInforme o valor:\t")
        valor = float(input())
        deposito = Deposito(valor)
        deposito.registrar(clientes[posi].contas[conta]) 

def sacar(clientes: list):
    print("\tSacar\t")
    print("Informe o CPF:\t")
    cpf = input()
    posi  = buscar_cliente(cpf, clientes)
    if posi != -1:
        print("Selecione a conta: \t")
        conta = int(input())
        if len(clientes[posi].contas) == 0:
            print("Cliente nao possui conta")
            return False
        if len(clientes[posi].contas) <= posi:
            print("Conta invalida")
            return False
        print("\nInforme o valor:\t")
        valor = float(input())
        saque = Saque(valor)
        saque.registrar(clientes[posi].contas[conta]) 

def novo_usuario(clientes: list):
    mascara_ptbr = "%d/%m/%Y"

    print("\tCriando novo usuario\t")
    print("Informe o seu endereco:\t")
    endereco = input()
    print("Informe o seu CPF:\t")
    cpf = input()
    print("Informe o seu nome:\t")
    nome = input()
    while(True):
        print("Informe a sua data de nascimento (dd/mm/aaaa):\t")
        data = input()

        data = datetime.datetime.strptime(data, mascara_ptbr)
        break

    
    novo_cliente = PessoaFisica(endereco, cpf, data, nome)
    clientes.append(novo_cliente)

def nova_conta(clientes: list):
    print("\tCRIANDO NOVA CONTA")
    cpf = input("Informe o CPF:\t")
    posi = buscar_cliente(cpf, clientes)
    if posi != -1:
        nova_conta = Conta(clientes[posi], 1)
        clientes[posi].adicionar_conta(nova_conta)

def listar_contas(clientes: list):
    print("\tLISTAR CONTAS")
    cpf = input("Informe o CPF:\t")
    posi = buscar_cliente(cpf, clientes)
    if posi != -1:
        for conta in clientes[posi].contas:
            print(conta)

def extrato(clientes: list):
    print("\tEXTRATO")
    cpf = input("Informe o CPF:\t")
    posi = buscar_cliente(cpf, clientes)
    if posi != -1:
        print("Selecione a conta: \t")
        conta = int(input())
        if len(clientes[posi].contas) == 0:
            print("Cliente nao possui conta")
            return False
        if len(clientes[posi].contas) <= posi:
            print("Conta invalida")
            return False
        print(clientes[posi].contas[conta].historico)

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    print(menu)
    op = input()
    return op

def main():
    clientes = []

    while(True):
        op = menu()

        match(op):

            case 'd':
                depositar(clientes)
            case 's':
                sacar(clientes)
            case 'e':
                extrato(clientes)
            case 'nc':
                nova_conta(clientes)
            case 'lc':
                listar_contas(clientes)
            case 'nu':
                novo_usuario(clientes)
            case 'q':
                exit()
            
main()