situacao = "sla"
nome = input("Informe o seu nome:")
nota_portugues = float(input("Informe a sua nota de Português:"))
nota_matematica = float(input("Informe a sua nota de Matemática:"))
nota_gerais = float(input("Informe a sua nota de Conhecimentos Gerais:"))
#Processamento
media = (nota_portugues + nota_matematica + nota_gerais)/3
if media >= 5 and nota_portugues > 4 and nota_matematica > 4 and nota_gerais > 4:
    situacao = "Aprovado :D"
else:
    situacao = "Reprovado 👎"
print(f"{nome}\n"
      + f"Nota de Português:{nota_portugues:.2f}\n"
      + f"Nota de Matemática:{nota_matematica:.2f}\n"
      + f"Nota de Conhecimentos Gerais:{nota_gerais:.2f}\n"
      + f"Média final:{media:.2f}\n"+ f"Situação do candidato:{situacao}")