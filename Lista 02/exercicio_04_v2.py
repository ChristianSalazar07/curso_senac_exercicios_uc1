qtd_numeros = 4
valores_divisiveis_3_e_2 = []
for i in range(qtd_numeros):
      n = int(input(f"Informe o {i+1}° valor:"))
      if n%(3*2) == 0:
        valores_divisiveis_3_e_2.append(n)
print(f"{valores_divisiveis_3_e_2} são divisiveis por 3 e 2")