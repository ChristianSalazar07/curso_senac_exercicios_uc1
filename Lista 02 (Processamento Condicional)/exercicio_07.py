salario = 0
valor_vendas = float(input("Informe o valor total das vendas em reais:"))
if valor_vendas > 20000:
    salario = valor_vendas * 0.1
else:
    salario = valor_vendas * 0.075
print(f"O salário é de R${salario:.2f}")