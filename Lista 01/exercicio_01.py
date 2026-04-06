# Faça um algoritmo que leia quatro números informados pelo usuário e
#que depois imprima a média ponderada, sabendo-se que os pesos são
#respectivamente: 1, 2, 3 e 4.
#Entrada
valor01 = float(input("Diga o primeiro valor:"))
valor02 = float(input("Diga o segundo valor:"))
valor03 = float(input("Diga o terceiro valor:"))
valor04 = float(input("Diga o quarto valor:"))
#Processamento
media_ponderada = ((valor01 * 1) + (valor02 * 2) + (valor03 * 3) + (valor04 * 4))/10
#Saída
print(f"A média ponderada é:{media_ponderada:.2f}")
