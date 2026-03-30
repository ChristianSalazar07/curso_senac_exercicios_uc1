nome = input("Informe o nome do cliente:")
quantidade_diarias = int(input("Informe a quantidade de diárias:"))
diaria = 80
taxa = 8
if quantidade_diarias > 15:
    taxa = 5,5
elif quantidade_diarias == 15:
    taxa = 6
valor_total = (taxa + diaria) * quantidade_diarias
print(f"{nome} tem que pagar R${valor_total:.2f}")