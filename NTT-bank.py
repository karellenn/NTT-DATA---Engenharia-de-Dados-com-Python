def mostrar_logo():
    print("""
    =============================
           RNA - BANK
    =============================
    """)

def boas_vindas():
    nome = input("Por favor, informe seu nome: ")
    print(f"\nBem-vindo(a), {nome}!\n")
    return nome

def despedida(nome):
    mostrar_logo()
    print(f"Adeus, {nome}! Obrigado por usar o RNA - BANK.\n")
    satisfacao()

def satisfacao():
    while True:
        try:
            nota = int(input("Por favor, avalie nossa aplicação (1 a 5): "))
            if 1 <= nota <= 5:
                print("Obrigado pela sua avaliação!")
                break
            else:
                print("Por favor, insira um valor entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 5.")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

mostrar_logo()
nome_cliente = boas_vindas()

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        despedida(nome_cliente)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
