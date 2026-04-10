altura = float(input("Informe a sua altura em metros:"))
sexo = input("Informe o seu sexo (M ou F):")
peso_ideal = 0
match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        print("Sexo inválido.")
print(f"O seu peso ideal é:{peso_ideal:.2f}kg")