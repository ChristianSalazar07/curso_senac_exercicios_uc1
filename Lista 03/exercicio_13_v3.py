qtd_alunos = 0
alunos_aprovados = []
alunos = []
class aluno:
    def __init__(self, nome, notaPortugues, notaMatematica, notaGerais):
        self.nome = nome
        self.notaPortugues = notaPortugues
        self.notaMatematica = notaMatematica
        self.notaGerais = notaGerais
        self.media = 0
        self.aprovacao = "sla"
    def calcular_media(self):
        self.media = (self.notaPortugues + self.notaMatematica + self.notaGerais)/3
    def __str__(self):
        return f"{self.nome}"
soma_portugues = 0
media_maior_4_5_cg_maior_6 = 0
aprovados_matematica_maior_5 = 0
tem_mais_alunos = "Sim"
while tem_mais_alunos == "Sim" or tem_mais_alunos == "sim":
    qtd_alunos = qtd_alunos + 1
    meuAluno = aluno(input(f"Informe o nome do {qtd_alunos}° aluno:"), 
                     float(input(f"Informe a nota de Português do {qtd_alunos}° aluno:")),
                     float(input(f"Informe a nota de Matemática do {qtd_alunos}° aluno:")),
                     float(input(f"Informe a nota de Conhecimentos Gerais do {qtd_alunos}° aluno:")))
    meuAluno.calcular_media()
    if meuAluno.media >= 4 and (meuAluno.notaPortugues) > 2 and meuAluno.notaMatematica > 2 and meuAluno.notaGerais > 2:
        alunos_aprovados.append(meuAluno.nome)
        if meuAluno.notaMatematica > 5:
            aprovados_matematica_maior_5 = aprovados_matematica_maior_5 + 1
    soma_portugues = soma_portugues + meuAluno.notaPortugues
    if meuAluno.media > 4.5 and meuAluno.notaGerais > 6:
        media_maior_4_5_cg_maior_6 = media_maior_4_5_cg_maior_6 + 1
    alunos.append(meuAluno)
    tem_mais_alunos = input("Tem mais alunos?(Sim ou Não?):")
print(f"Alunos aprovados:{alunos_aprovados}\n"
      + f"Média de Português:{soma_portugues/qtd_alunos:.2f}\n"
      + f"O número de candidatos que obtiveram média maior que 4.5 e nota na prova de Conhecimentos Geral maior que 6,0 é: {media_maior_4_5_cg_maior_6}\n"
      + f"O número de candidatos aprovados que obtiveram nota em Matemática acima de 5,0 é: {aprovados_matematica_maior_5}")
print()