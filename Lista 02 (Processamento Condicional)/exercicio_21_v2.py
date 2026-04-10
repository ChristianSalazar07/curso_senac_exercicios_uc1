a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
lista_valores = []
lista_valores.append(a);lista_valores.append(b);lista_valores.append(c)
lista_valores.sort()
print(f"{lista_valores[0]:.2f},{lista_valores[1]:.2f},{lista_valores[2]:.2f}")