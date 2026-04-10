primeiro_numero = 85
ultimo_numero = 907
numeros_pares = []
soma = 0
if primeiro_numero % 2 == 0:
    numero_atual = primeiro_numero + 2
else:
    numero_atual = primeiro_numero + 1
for numero_atual in range(numero_atual,ultimo_numero,2):
    numeros_pares.append(numero_atual)
    soma = soma + numero_atual
print(f"{numeros_pares}\n"+f"A soma dos números pares é {soma:.0f}")