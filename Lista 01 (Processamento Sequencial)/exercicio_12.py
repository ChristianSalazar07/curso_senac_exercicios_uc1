custo_fabrica = float(input("Informe o custo de fábrica:"))
porcentagem_distribuidor = 0.28
porcentagem_impostos = 0.45
custo_consumidor = (custo_fabrica * (1+porcentagem_impostos)) * (1+porcentagem_distribuidor)
print(f"O custo ao consumidor é de R${custo_consumidor:.2f}")