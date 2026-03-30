desconto = 25
diaria = float(input("Informe o valor da diária:"))
apartamentos = int(input("Informe o número de apartamentos:"))
diaria_promocional = diaria * (1-desconto)
arrecadacao_ocupacao_total = diaria_promocional * apartamentos
arrecadacao_ocupacao_70 = diaria_promocional * (apartamentos*0.7)
diferenca_promocao = (diaria*apartamentos) - arrecadacao_ocupacao_total
print(f"O valor promocional da diária será de R${diaria_promocional:.2f}\n O valor arrecadado em caso de ocupação total é de R${arrecadacao_ocupacao_total:.2f}\n O valor arrecadado em caso de 70% de ocupação é de R${arrecadacao_ocupacao_70:.2f}\n O valor que o hotel deixará de arrecadar devido à promoção é de R${diferenca_promocao:.2f}")