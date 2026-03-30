salario_bruto = float(input("Informe o valor do salário bruto em reais:"))
inss = salario_bruto * 0.08
ir = salario_bruto * 0.1
filiacao_sindical = (salario_bruto-(inss + ir))*0.005
desconto_total = inss + ir + filiacao_sindical
salario_liquido = salario_bruto - desconto_total
print(f"INSS:R${inss:.2f}\n"
      +f"IR:R${ir:.2f}\n"
      +f"Filiação Sindical:R${filiacao_sindical:.2f}\n"
      +f"Total dos descontos:R${desconto_total:.2f}\n"
      +f"Salario Líquido:R${salario_liquido:.2f}")