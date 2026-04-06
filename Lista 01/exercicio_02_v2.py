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