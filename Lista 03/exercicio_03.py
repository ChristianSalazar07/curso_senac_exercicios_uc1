qtd_numeros = 50
numeros_negativos = []
soma = 0
qtd_negativos = 0
for i in range(qtd_numeros):
    numero_atual = int(input(f"Informe o {i+1:.0f}° número:"))
    if numero_atual < 0:
        numeros_negativos.append(numero_atual)
        qtd_negativos = qtd_negativos + 1
    else:
        soma = soma + numero_atual
print(f"Soma dos positivos = {soma:.0f}\n"
      + f"{qtd_negativos:.0f} Numeros Negativos = {numeros_negativos}")