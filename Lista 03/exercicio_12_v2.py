qtd_entrevistados = 0
torcedores_figueirense = 0
torcedores_marcilio = 0
torcedores_outros = 0
salario_figueirense = 0
n_florianopolis_marcilio = 0
n_outros_figueirense = 0
tem_mais_entrevistados = "Sim"
while tem_mais_entrevistados == "Sim" or tem_mais_entrevistados == "sim":
    qtd_entrevistados = qtd_entrevistados + 1
    clube = input("Entre os clubes a seguir, qual o de sua preferência?\n"
                  + "a) Figueirense\n" + "b) Marcílio Dias\n" + "c) Outros clubes\n")
    salario = float(input("Qual o valor de seu salário?"))
    nascimento = input("Qual o local de nascimento?\n"+"a) Florianópolis\n"+"b) Outras cidades\n")
    match clube:
        case "a":
            torcedores_figueirense = torcedores_figueirense + 1
            salario_figueirense = salario_figueirense + salario
            if nascimento == "b":
                n_outros_figueirense = n_outros_figueirense + 1
        case "b":
            torcedores_marcilio = torcedores_marcilio + 1
            if nascimento == "a":
                n_florianopolis_marcilio = n_florianopolis_marcilio + 1
        case "c":
            torcedores_outros = torcedores_outros + 1
    tem_mais_entrevistados = input("Tem mais entrevistados?(Sim ou Não?):")
print(f"Torcedores Figueirense:{torcedores_figueirense}\n"+f"Torcedores Marcílio Dias:{torcedores_marcilio}\n"+f"Torcedores Outros:{torcedores_outros}\n"
      +f"A média salarial dos Torcedores do Figueirense é R${salario_figueirense:.2f}\n"
      +f"O número de pessoas nascidas em Florianópolis e que torcem pelo Marcílio Dias é {n_florianopolis_marcilio}\n"
      +f"O número de pessoas nascidas em outras cidades e que torcem pelo Figueirense é {n_outros_figueirense}")