ganho_total = float(input("Informe os ganhos totais em reais:"))
desconto = 0
if ganho_total <= 500:
    desconto = 0
elif ganho_total <= 1500:
        desconto = 0.1
elif ganho_total <= 2500:
      desconto = 0.15
else:
    desconto = 0.2
print(f"O desconto é de {desconto * 100:.0f}%")
