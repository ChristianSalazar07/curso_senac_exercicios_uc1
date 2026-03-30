a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
valor_maior = 0
valor_central = 0
valor_menor = 0
if a > b and a > c:
    valor_maior = a
    if b < c:
        valor_menor = b
        valor_central = c
    else:
        valor_menor = c
        valor_central = b
elif a > b or a > c:
    valor_central = a
    if b > c:
        valor_maior = b
        valor_menor = c
    else:
        valor_maior = c
        valor_menor = b
else:
    valor_menor = a
    if b > c:
        valor_maior = b
        valor_central = c
    else:
        valor_maior = c
        valor_central = b
print(f"{valor_menor},{valor_central},{valor_maior}")