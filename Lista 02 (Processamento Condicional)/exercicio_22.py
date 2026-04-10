a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
valor_maior = 0
valor_central = 0
valor_menor = 0
lados = "0"
angulos = "0"
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
if valor_maior < valor_central + valor_menor:
    if a == b == c:
        lados = "Equilátero"
    elif a == b or a == c or b == c:
        lados = "Isósceles"
    else:
        lados = "Escaleno"
    if valor_maior**2 == valor_central**2 + valor_menor**2:
        angulos = "Retângulo"
    elif valor_maior**2 > valor_central**2 + valor_menor**2:
        angulos = "Obtusângulo"
    else:
        angulos = "Acutângulo"
    print(f"O triângulo é {lados} e {angulos}")
else:
    print("Não é triângulo")