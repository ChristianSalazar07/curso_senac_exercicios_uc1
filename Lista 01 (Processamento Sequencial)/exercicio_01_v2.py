''' Faça um algoritmo que leia quatro números informados pelo usuário e
que depois imprima a média ponderada, sabendo-se que os pesos são
respectivamente: 1, 2, 3 e 4.'''
#Entrada
qtd_valores = 4
soma = 0
divisor = 0
for i in range(4):
    valor = float(input(f"Diga o {i+1}° valor:"))
#Processamento
    soma = soma + valor * (i+1)
    divisor = divisor + (i+1)
media = soma / divisor
#Saída
print(f"A média ponderada é:{media:.2f}")