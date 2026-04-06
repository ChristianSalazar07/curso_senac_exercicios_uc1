#Entrada
salario_bruto = float(input("Informe o salário: "))
#Processamento
desconto = 0.2
salario_liquido = salario_bruto * (1 - desconto)
#Saída
print(f"Salario líquido:{salario_liquido:.2f}")