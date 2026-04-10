nome01 = input("Informe o nome do primeiro corretor:")
venda01 = float(input("Informe o valor das vendas do primeiro corretor em reais:"))
nome02 = input("Informe o nome do segundo corretor:")
venda02 = float(input("Informe o valor das vendas do segundo corretor em reais:"))
nome03 = input("Informe o nome do terceiro corretor:")
venda03 = float(input("Informe o valor das vendas do terceiro corretor em reais:"))
#Processamento 1
if venda01 > 50000:
    comissao01 = venda01 * 0.12
elif venda01 >= 30000:
    comissao01 = venda01 * 0.095
else:
    comissao01 = venda01 * 0.075
#Processamento 2
if venda02 > 50000:
    comissao02 = venda02 * 0.12
elif venda02 >= 30000:
    comissao02 = venda02 * 0.095
else:
    comissao02 = venda02 * 0.075
#Processamento 3
if venda03 > 50000:
    comissao03 = venda03 * 0.12
elif venda03 >= 30000:
    comissao03 = venda03 * 0.095
else:
    comissao03 = venda03 * 0.075
#Resultado
print(f"O corretor {nome01} vendeu R${venda01:.2f} e recebeu R${comissao01}\n"
      + f"O corretor {nome02} vendeu R${venda02:.2f} e recebeu R${comissao02}\n"
      + f"O corretor {nome03} vendeu R${venda03:.2f} e recebeu R${comissao03}\n"
      + f"O valor total de vendas da empresa foi de R${venda01 + venda02 + venda03:.2f}")