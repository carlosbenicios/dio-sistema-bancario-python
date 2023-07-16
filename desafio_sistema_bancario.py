import textwrap


def menu():
    menu_text = """------ Menu ------
    1\tDepositar
    2\tSacar
    3\tExtrato
    4\tNova Conta
    5\tListar Contas
    6\tNovo usuário
    7\tSair
    """
    return input(textwrap.dedent(menu_text))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito \tR$ {valor:.2f}\n"
        print("\nDepósito Realizado")
    else:
        print("\nValor Inválido!")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque > limite_saque

    if excedeu_saldo:
        print("Operação falhou! Sem saldo suficiente")

    elif excedeu_limite:
        print("Operação falhou! Limite insuficiente")

    elif excedeu_saque:
        print("Operação falhou! Limite de saque excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\tR$ {valor:.2f}\n"

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n********** Extrato **********")
    print("Não há movimentações" if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF em números: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um cadastro com esse CPF")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Rua, Numero - Bairro - Cidade/UF): ")

    usuarios.append(
        {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF em números: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor para saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUES,
            )
            numero_saque += 1

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            break

        else:
            print("Opção inválida")


main()
