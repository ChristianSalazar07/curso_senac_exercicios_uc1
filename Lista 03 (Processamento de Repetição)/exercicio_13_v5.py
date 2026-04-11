class aluno:
    def __init__(self, nome, notaPortugues, notaMatematica, notaGerais):
        self.nome = nome
        self.notaPortugues = notaPortugues
        self.notaMatematica = notaMatematica
        self.notaGerais = notaGerais
        self.media = 0
        self.aprovacao = "Reprovado"
    def calcularMedia(self):
        self.media = (self.notaPortugues + self.notaMatematica + self.notaGerais)/3
        if self.media >= 4 and self.notaPortugues > 2 and self.notaMatematica > 2 and self.notaGerais > 2:
            self.aprovacao = "Aprovado"
    def __str__(self):
        return f"Nome: {self.nome} - Média: {self.media:.1f} - Aprovação: {self.aprovacao}"
def entrada_alunos():
    alunos = []
    tem_mais_alunos = "Sim"
    qtd_alunos = 0
    while tem_mais_alunos == "Sim" or tem_mais_alunos == "sim":
        qtd_alunos = qtd_alunos + 1
        meuAluno = aluno(input(f"Informe o nome do {qtd_alunos}° aluno:"), 
                     float(input(f"Informe a nota de Português do {qtd_alunos}° aluno:")),
                     float(input(f"Informe a nota de Matemática do {qtd_alunos}° aluno:")),
                     float(input(f"Informe a nota de Conhecimentos Gerais do {qtd_alunos}° aluno:")))
        meuAluno.calcularMedia()
        alunos.append(meuAluno)
        tem_mais_alunos = input("Tem mais alunos?(Sim ou Não?):")
    return alunos
def calcularMediaPortugues(alunos):
    soma_portugues = 0
    for candidato in alunos:
        soma_portugues = soma_portugues + candidato.notaPortugues
    return soma_portugues/len(alunos)
def calcularAprovados(alunos):
    aprovados = []
    for candidato in alunos:
        if candidato.aprovacao == "Aprovado":
            aprovados.append(candidato.nome)
    return aprovados
def calcularAprovadosMatematica(alunos):
    aprovados_matematica_maior_5 = 0
    for candidato in alunos:
        if candidato.notaMatematica > 5 and candidato.aprovacao == "Aprovado":
            aprovados_matematica_maior_5 = aprovados_matematica_maior_5 + 1
    return aprovados_matematica_maior_5
def calcularMediaMaior4_5CGMaior_6(alunos):
    media_maior_4_5_cg_maior_6 = 0
    for candidato in alunos:
        if candidato.media > 4.5 and candidato.notaGerais > 6:
            media_maior_4_5_cg_maior_6 = media_maior_4_5_cg_maior_6 + 1
    return media_maior_4_5_cg_maior_6
def saida_dados():
    for candidato in alunos:
        print(candidato)
    print(f"Alunos aprovados:{alunos_aprovados}\n"
      + f"Média de Português:{media_portugues:.2f}\n"
      + f"O número de candidatos que obtiveram média maior que 4.5 e nota na prova de Conhecimentos Geral maior que 6,0 é: {qtd_media_maior_4_5_cg_maior_6}\n"
      + f"O número de candidatos aprovados que obtiveram nota em Matemática acima de 5,0 é: {qtd_aprovados_matematica_maior_5}")
alunos = entrada_alunos()
media_portugues = calcularMediaPortugues(alunos)
alunos_aprovados = calcularAprovados(alunos)
qtd_aprovados_matematica_maior_5 = calcularAprovadosMatematica(alunos)
qtd_media_maior_4_5_cg_maior_6 = calcularMediaMaior4_5CGMaior_6(alunos)
saida_dados()