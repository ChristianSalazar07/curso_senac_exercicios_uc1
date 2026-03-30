x = float(input("Informe o número:"))
if x > 0:
    resultado = "positivo"
elif x < 0:
    resultado = "negativo"
else:
    resultado = "nulo"
print(f"O número é {resultado:.2f}")