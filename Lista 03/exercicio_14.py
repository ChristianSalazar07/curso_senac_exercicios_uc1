#Entrada
qtd_alunos = 3
soma_renda_alimentacao_mais_300 = 0
qtd_alunos_alimentacao_mais_300 = 0
media_gasto_aluguel = 0
nomes = []
p1 = []
p2 = []
for i in range(qtd_alunos):
        nome = input(f"Informe o nome do {i+1}° aluno:")
        renda_mensal = float(input(f"Informe a renda mensal da {i+1}ª família:"))
        gasto_alimentacao = float(input(f"Informe a quantidade gasta em alimentação pela {i+1}ª família:"))
        gasto_vestimenta = float(input(f"Informe a quantidade gasta em vestimenta pela {i+1}ª família:"))
        gasto_aluguel = float(input(f"Informe a quantidade gasta em aluguel pela {i+1}ª família:"))
#Processamento
        if gasto_alimentacao > 300:
                soma_renda_alimentacao_mais_300 = soma_renda_alimentacao_mais_300 + gasto_alimentacao
                qtd_alunos_alimentacao_mais_300 = qtd_alunos_alimentacao_mais_300 + 1
        media_gasto_aluguel = media_gasto_aluguel + gasto_aluguel
        p1.append(gasto_alimentacao/renda_mensal)
        nomes.append(nome)
        p2.append(gasto_vestimenta/renda_mensal)
#Saída
if qtd_alunos_alimentacao_mais_300 != 0:
        print(f"A renda média familiar dos alunos que gastam acima de R$300,00 com alimentação é: R${soma_renda_alimentacao_mais_300/qtd_alunos_alimentacao_mais_300:.2f}\n"
      + f"O gasto médio com aluguel é: R${media_gasto_aluguel/qtd_alunos:.2f}")
else:
        print(f"Nenhum aluno teve gastos com alimentação superiores a R$300,00\n"
              +f"O gasto médio com aluguel é: R${media_gasto_aluguel/qtd_alunos:.2f}")
for i in range(len(nomes)):
        print(f"Nome:{nomes[i]} -=- P1:{p1[i]:.2f} -=- P2:{p2[i]:.2f}")
