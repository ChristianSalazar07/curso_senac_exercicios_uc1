nome = input("Informe o seu nome:")
sexo = input("Informe o seu sexo(M ou F)):")
estado_civil = input("Informe o seu estado civil(S ou C):")
idade = int(input("Informe a sua idade:"))
salario_pai = float(input("Informe o salário do seu pai ou cônjuge:"))
pensao = 0
#Processamento
match sexo:
    case "M":
        if estado_civil == "S" and idade < 18:
            pensao = salario_pai * 0.15
    case "F":
        if estado_civil == "S" and idade < 21:
            pensao = salario_pai * 0.2
        elif estado_civil == "C":
            pensao = salario_pai * 0.3
print(f"{nome} tem direito a R${pensao:.2f} de pensão")