qtd_alunos = 3
alunos_aprovados = []
soma_portugues = 0
media_maior_4_5_cg_maior_6 = 0
aprovados_matematica_maior_5 = 0
for i in range(qtd_alunos):
    situacao = "sla"
    nome = input(f"Informe o nome do {i+1:.0f}° aluno:")
    nota_portugues = float(input(f"Informe a nota de Português do {i+1:.0f}° aluno:"))
    nota_matematica = float(input(f"Informe a nota de Matemática do {i+1:.0f}° aluno:"))
    nota_gerais = float(input(f"Informe a nota de Conhecimentos Gerais do {i+1:.0f}° aluno:"))
    media = (nota_portugues + nota_matematica + nota_gerais)/3
    if media >= 4 and nota_portugues > 2 and nota_matematica > 2 and nota_gerais > 2:
        alunos_aprovados.append(nome)
        if nota_matematica > 5:
            aprovados_matematica_maior_5 = aprovados_matematica_maior_5 + 1
    soma_portugues = soma_portugues + nota_portugues
    if media > 4.5 and nota_gerais > 6:
        media_maior_4_5_cg_maior_6 = media_maior_4_5_cg_maior_6 + 1
print(f"Alunos aprovados:{alunos_aprovados}\n"
      + f"Média de Português:{soma_portugues/qtd_alunos:.2f}\n"
      + f"O número de candidatos que obtiveram média maior que 4.5 e nota na prova de Conhecimentos Geral maior que 6,0 é: {media_maior_4_5_cg_maior_6:.0f}\n"
      + f"O número de candidatos aprovados que obtiveram nota em Matemática acima de 5,0 é: {aprovados_matematica_maior_5:.0f}")