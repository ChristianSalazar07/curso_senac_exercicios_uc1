desconto = float(input("Informe o valor do desconto em porcentagem:"))
preco = float(input("Informe o preço do produto em reais:"))
nome = (input("Informe o nome do produto:"))
if desconto < 25 and preco > 25000:
    print(nome)