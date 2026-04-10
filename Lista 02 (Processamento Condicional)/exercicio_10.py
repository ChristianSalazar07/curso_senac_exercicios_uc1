a = float(input("Informe o primeiro valor:"))
b = float(input("Informe o segundo valor:"))
c = float(input("Informe o terceiro valor:"))
if a > b and a > c:
    print(f"{a} é o maior número")
    if b < c:
        print(f"{b} é o menor número")
    else:
        print(f"{c} é o maior número")
else:
    print(f"{a} é o menor número")
    if b > c:
        print(f"{b} é o maior número")
    else:
        print(f"{c} é o maior número")