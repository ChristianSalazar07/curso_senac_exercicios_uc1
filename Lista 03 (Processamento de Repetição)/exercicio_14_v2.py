#Entrada
qtd_alunos = 0
soma_renda_alimentacao_mais_300 = 0
qtd_alunos_alimentacao_mais_300 = 0
media_gasto_aluguel = 0
nomes = []
p1 = []
p2 = []
tem_mais_alunos = "Sim"
while tem_mais_alunos == "Sim" or tem_mais_alunos == "sim":
        qtd_alunos = qtd_alunos + 1
        nome = input(f"Informe o nome do {qtd_alunos}° aluno:")
        renda_mensal = float(input(f"Informe a renda mensal da {qtd_alunos}ª família:"))
        gasto_alimentacao = float(input(f"Informe a quantidade gasta em alimentação pela {qtd_alunos}ª família:"))
        gasto_vestimenta = float(input(f"Informe a quantidade gasta em vestimenta pela {qtd_alunos}ª família:"))
        gasto_aluguel = float(input(f"Informe a quantidade gasta em aluguel pela {qtd_alunos}ª família:"))
#Processamento
        if gasto_alimentacao > 300:
                soma_renda_alimentacao_mais_300 = soma_renda_alimentacao_mais_300 + gasto_alimentacao
                qtd_alunos_alimentacao_mais_300 = qtd_alunos_alimentacao_mais_300 + 1
        media_gasto_aluguel = media_gasto_aluguel + gasto_aluguel
        p1.append(gasto_alimentacao/renda_mensal)
        nomes.append(nome)
        p2.append(gasto_vestimenta/renda_mensal)
        tem_mais_alunos = input("Tem mais alunos?(Sim ou Não?):")
#Saída
if qtd_alunos_alimentacao_mais_300 != 0:
        print(f"A renda média familiar dos alunos que gastam acima de R$300,00 com alimentação é: R${soma_renda_alimentacao_mais_300/qtd_alunos_alimentacao_mais_300:.2f}\n"
      + f"O gasto médio com aluguel é: R${media_gasto_aluguel/qtd_alunos:.2f}")
else:
        print(f"Nenhum aluno teve gastos com alimentação superiores a R$300,00\n"
              +f"O gasto médio com aluguel é: R${media_gasto_aluguel/qtd_alunos:.2f}")
for i in range(len(nomes)):
        print(f"Nome:{nomes[i]} -=- P1:{p1[i]:.2f} -=- P2:{p2[i]:.2f}")