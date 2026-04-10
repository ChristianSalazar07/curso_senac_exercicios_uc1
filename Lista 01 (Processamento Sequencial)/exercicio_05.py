aplicacao_mensual = float(input("Informe o valor da aplicação mensual:"))
taxa = float(input("Informe o valor da taxa, em porcentagem:"))
meses = float(input("Informe a quantidade de meses:"))
valor_acumulado = (aplicacao_mensual*(1+(taxa/100))**(meses-1))/taxa
print(f"O valor acumulado é: {valor_acumulado:.2f}")