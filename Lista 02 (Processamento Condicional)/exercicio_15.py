id_conta = int(input("Informe o número da sua conta:"))
tipo_operacao = input("Informe o tipo de operação(D ou R):")
valor_operacao = float(input("Informe o valor da operação em reais:"))
saldo_conta = 0
match id_conta:
    case 1:
        saldo_conta = 15000
    case 2:
        saldo_conta = 991823
    case 3:
        saldo_conta = 988123
    case _:
        saldo_conta = 0
if tipo_operacao == "R":
    saldo_conta = saldo_conta - valor_operacao
elif tipo_operacao == "D":
    saldo_conta = saldo_conta + valor_operacao
else:
    print("Operação inválida")
print(f"O novo saldo da conta é: R${saldo_conta:.2f}")
if saldo_conta < 0:
    print("Conta abaixo do limite de crédito")