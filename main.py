menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_conta = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        pass

    elif opcao.lower() == "s":
        pass

    elif opcao.lower() == "e":
        pass

    elif opcao.lower() == "q":
        break

    else:
        print("Opção inválida! Selecione uma opção válida!")