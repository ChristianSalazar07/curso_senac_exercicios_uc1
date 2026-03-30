desconto = 0
valor_compra = float(input("Informe o valor da compra em reais:"))
if valor_compra >= 5000:
    desconto = 0.2
else:
    desconto = 0.15
valor_final = valor_compra * (1-desconto)
print(f"O valor final é R${valor_final:.2f}")