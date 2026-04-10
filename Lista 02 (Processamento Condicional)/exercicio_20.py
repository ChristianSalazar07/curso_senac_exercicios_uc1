x = int(input("Informe o primeiro valor:"))
y = int(input("Informe o segundo valor:"))
if x%y == 0:
    print(f"{x:.0f} é múltiplo de {y:.0f}")
elif y%x == 0:
    print(f"{y:.0f} é múltiplo de {x:.0f}")
else:
    print(f"{x:.0f} e {y:.0f} não são múltiplos um do outro")