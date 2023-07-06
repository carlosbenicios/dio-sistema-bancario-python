menu = '''
********* Escolha a Opção *********
1 - Depositar
2 - Sacar 
3 - Extrato
4 - Sair
'''

saldo = 0.0
valor_limite_saque = 500.0
extrato = ""
contador_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("*****Realizar Depósito*****")
        valor = float(input("Informe o valor do depósito: "))
        if valor >= 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
            print(f"O valor de R$ {valor} foi adicionado a conta")
        else:
            print("Valor Inválido")

    elif opcao == "2":
        print("*****Realizar Saque*****")
        valor = float(input("Informe o valor do saque: "))
        sem_saldo = valor > saldo
        sem_limite = valor >= valor_limite_saque
        sem_saque = contador_saque >= LIMITE_SAQUE

        if sem_saldo:
            print(
                f"Você não tem valor suficiente para essa operação. Saldo atual R${saldo}.")
        elif sem_limite:
            print("Você excedeu o valor de limite de saque")
        elif sem_saque:
            print("Você excedeu o número de saques diários")
        elif valor > 0:
            saldo -= valor
            print(f"Saque realizado, saldo disponível R$ {saldo}")
            extrato += f"Saque: R$ {valor:.2f}\n"
            contador_saque += 1
    elif opcao == "3":
        print("*****Extrato*****")
        print(extrato)
        print(f"Saldo: R${saldo}")

    elif opcao == "4":
        break
