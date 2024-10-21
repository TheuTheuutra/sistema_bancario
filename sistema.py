menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")
    
    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! Você excedeu o limite de saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você excedeu o limite de saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido")
    
    elif opcao == "e":
        print(f"Saldo: R$ {saldo:.2f}")
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
        


