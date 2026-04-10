primeiro_numero = 85
ultimo_numero = 907
numeros_pares = []
soma = 0
for i in range(primeiro_numero, ultimo_numero):
    if i%2 ==0 and i>primeiro_numero:
        numeros_pares.append(i)
        soma = soma + i
print(f"{numeros_pares}\n"+f"A soma dos números pares é {soma:.0f}")