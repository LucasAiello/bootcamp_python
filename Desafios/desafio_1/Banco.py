from os import system

saldo = 0
transacoes = []
saques_disponiveis = 3
saque_min = 500
linha = "---------------------"

while(True):
    system('cls')
    texto = """
    Banco
    ---------------------
    d: Depositar
    s: Sacar
    e: Extrato
    x: Sair
    ---------------------
    """
    print(texto)
    print("Digite a entrada:\t")
    entrada = input()
    
    match(entrada):
        case 'd':
            print("Depositar")
            print("Escolha o valor: ")
            valor = int(input())
            if valor > 0:
                print("Depositando...")
                saldo += valor
                transacoes.append(f"Deposito de {valor}R$")
            else:
                print("Valor invalido")

            entrada = input()
        case 's':
            if saques_disponiveis > 0:
                print("Saque")
                print("Digite o valor do saque:\t")
                valor = int(input())
                if valor < 500:
                    print(f"Erro! Saque minimo é de {saque_min}R$")
                else:
                    if valor > saldo:
                        print("Erro! Saldo insuficiente")
                    else:
                        print("Sacando...")
                        saldo -= valor
                        saques_disponiveis -= 1
                        transacoes.append(f"Saque de {valor}R$")
            else:
                print("Saques diarios ja foram utilizados")
            entrada = input()

        case 'e':
            print(linha)
            print("Extrato")
            print(linha)
            print(f"Saldo:\t{saldo}")
            for transacao in transacoes:
                print(transacao)
            entrada = input()
        case 'x':
            print("Saindo...")
            break;
        