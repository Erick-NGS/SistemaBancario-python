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
        valor_deposito = float(input("Informe o valor a ser depositado: R$"))

        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("Valor inserido inválido! Por favor, digite um valor válido.")


    elif opcao.lower() == "s":
        valor_saque = float(input("Informe o valor do saque: R$"))

        excedeu_num_saques = numero_saques >= LIMITE_SAQUES
        excedeu_valor_saque = valor_saque > limite_valor_saque
        sem_saldo = valor_saque > saldo_conta

        if excedeu_num_saques:
            print("Falha na operação: Você chegou ao limite de saques do dia.")

        elif excedeu_valor_saque:
            print("Falha na operação: Valor informado para saque é maior do que o valor disponível na conta.")

        elif sem_saldo:
            print("Falha na operação: Saldo insuficiente na conta.")

        elif valor_saque > 0:
            saldo_conta -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação: Valor informado inválido.")

    elif opcao.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("==========================================")

    elif opcao.lower() == "q":
        break

    else:
        print("Opção inválida! Selecione uma opção válida para realizar uma operação!")