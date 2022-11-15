menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_CHEQUE_ESPECIAL = 300
cheque_especial = LIMITE_CHEQUE_ESPECIAL

while True:
    opcao = input(menu)
    
    cheque_especial = LIMITE_CHEQUE_ESPECIAL if saldo >= 0 else LIMITE_CHEQUE_ESPECIAL + saldo
    
    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor a sacar: "))

        excedeu_saldo = valor > ((saldo + cheque_especial) if saldo >= 0 else cheque_especial)
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada. Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação não realizada, limite diário excedido.")
        elif excedeu_saques:
            print("Operação não realizada, limite de saques diários excedido")
        elif valor > 0:
            saldo -= valor
            
            extrato += f"Saque realizado de R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação não realizada. Valor informado incorretamente.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Conta sem movimentos a exibir." if not extrato else extrato)
        print(f"Saldo atual é de: R$ {saldo:.2f}")
        print(f"Cheque especial disponível R$ {cheque_especial:.2f} de R$ {LIMITE_CHEQUE_ESPECIAL:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário.")
        break

    else:
        print("Operação inválida, favor selecionar uma dentre as operações do menu acima.")