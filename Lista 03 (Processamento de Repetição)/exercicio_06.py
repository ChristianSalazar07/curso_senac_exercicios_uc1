qtd_alunos = int(input("Informe quantos alunos foram questionados:"))
alunos_menos_10 = 0
alunos_10_a_15 = 0
alunos_mais_15 = 0
for i in range(qtd_alunos):
    vezes_restaurante = int(input(f"Informe quantas vezes o {i+1}° aluno foi ao restaurante da universidade:"))
    if vezes_restaurante < 10:
        alunos_menos_10 = alunos_menos_10 + 1
    elif vezes_restaurante > 15:
        alunos_mais_15 = alunos_mais_15 + 1
    else:
        alunos_10_a_15 = alunos_10_a_15 + 1
print(f"{(alunos_menos_10/qtd_alunos)*100:.2f}% foram ao restaurante menos de 10 vezes\n"
      + f"{(alunos_10_a_15/qtd_alunos)*100:.2f}% foram ao restaurante entre 10 a 15 vezes\n"
      + f"{(alunos_mais_15/qtd_alunos)*100:.2f}% foram ao restaurante mais de 15 vezes")