x = int(input("Informe o valor inteiro:"))
faixa = "Faixa X"
if x < 100:
    faixa = "Faixa A"
elif x <= 150:
    faixa = "Faixa B"
elif x <= 300:
    faixa = "Faixa C"
print(f"{x:.0f} pertence a {faixa}")