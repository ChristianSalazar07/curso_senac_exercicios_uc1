qtd_numeros = 3
valores = []
for i in range(qtd_numeros):
      n = float(input(f"Informe o {i+1}° valor:"))
      valores.append(n)
valores.sort()
print(f"{valores[len(valores)-1]} é o maior número\n"
      + f"{valores[0]} é o menor número")