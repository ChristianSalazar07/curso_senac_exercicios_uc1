qtd_alunos = 45
soma_idade_menos_1_70 = 0
alunos_menos_1_70 = 0
soma_altura_mais_20 = 0
alunos_mais_20 = 0
for i in range(qtd_alunos):
    altura_aluno = float(input(f"Informe a altura do {i+1}° aluno:"))
    idade_aluno = int(input(f"Informe a idade do {i+1}° aluno:"))
    if altura_aluno < 1.7:
        alunos_menos_1_70 = alunos_menos_1_70 + 1
        soma_idade_menos_1_70 = soma_idade_menos_1_70 + idade_aluno
    elif idade_aluno >= 20:
        alunos_mais_20 = alunos_mais_20 + 1
        soma_altura_mais_20 = soma_altura_mais_20 + altura_aluno
print(f"A idade média dos alunos com altura menor que 1,70 m é de {soma_idade_menos_1_70/alunos_menos_1_70:.2f}\n"
      +f"A altura média dos alunos com mais de vinte anos é de {soma_altura_mais_20/alunos_mais_20:.2f}m")