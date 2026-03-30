import math
#Entrada
custo_espetaculo = float(input("Informe o custo do espetaculo em reais:"))
custo_ingresso = float(input("Informe o valor do ingresso em reais:"))
#Processamento
vendas_necessarias = math.ceil(custo_espetaculo / custo_ingresso)
vendas_necessarias_lucro_23 = math.ceil(((custo_espetaculo * 100)/77) / custo_ingresso)
#Saída
print(f"A quantidade de vendas necessárias para cobrir o custo do espetáculo é:{vendas_necessarias:.0f}\n"+
      f"A quantidade de vendas necessárias para haver 23% de lucro é:{vendas_necessarias_lucro_23:.0f}")