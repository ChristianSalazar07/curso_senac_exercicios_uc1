qtd_corretores = 3
comissoes = []
nomes = []
vendas = []
#Processamento
for i in range(qtd_corretores):
    nome = input(f"Informe o nome do {i+1}° corretor:")
    venda = float(input(f"Informe o valor das vendas do {i+1}° corretor em reais:"))
    if venda > 50000:
         comissao = venda * 0.12
    elif venda >= 30000:
        comissao = venda * 0.095
    else:
        comissao = venda * 0.075
    nomes.append(nome)
    comissoes.append(comissao)
    vendas.append(venda)
#Resultado
for i in range(len(comissoes)):
    print(f"O corretor {nomes[i]} vendeu R${vendas[i]:.2f} e recebeu R${comissoes[i]}")
print(f"O valor total de vendas da empresa foi de R${vendas[0] + vendas[1] + vendas[2]:.2f}")