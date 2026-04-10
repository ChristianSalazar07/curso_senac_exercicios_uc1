salario_minimo = float(input("Informe o salario minimo em real:"))
quantidade_consumida = float(input("Informe a quantidade de energia consumida em kW:"))
valor_kw = salario_minimo/5
valor_pago = quantidade_consumida * valor_kw
valor_pago_desconto = valor_pago * 0.85
print(f"O valor de cada kW é R${valor_kw:.2f}\n"+
      f"O valor pago pela residência foi de R${valor_pago:.2f}\n"+
      f"O valor a ser pago com 15% de desconto é de R${valor_pago_desconto:.2f}")