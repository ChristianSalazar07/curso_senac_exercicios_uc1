a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
lista_lados = []
lista_lados.append(a); lista_lados.append(b); lista_lados.append(c); lista_lados.sort()
lados = "0"
angulos = "0"
if lista_lados[2] < lista_lados[1] + lista_lados[0]:
    if a == b == c:
        lados = "Equilátero"
    elif a == b or a == c or b == c:
        lados = "Isósceles"
    else:
        lados = "Escaleno"
    if lista_lados[2]**2 == lista_lados[1]**2 + lista_lados[0]**2:
        angulos = "Retângulo"
    elif lista_lados[2]**2 > lista_lados[1]**2 + lista_lados[0]**2:
        angulos = "Obtusângulo"
    else:
        angulos = "Acutângulo"
    print(f"O triângulo é {lados} e {angulos}")
else:
    print("Não é triângulo")