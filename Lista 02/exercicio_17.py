a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
if a < (b+c) and b < (a+c) and c < (a+b):
    if a == b == c:
        print("O triângulo formado é Equilátero")
    elif a == b or a == c or b == c:
        print("O triângulo formado é Isósceles")
    else:
        print("O triângulo formado é Escaleno")
else:
    print("Não é triângulo")