preco_custo = float(input("Informe o preço custo do produto:"))
percentual = float(input("Informe o percentual de acrescimo:"))
valor_venda = preco_custo * (1 + (percentual/100))
print(f"O valor de venda é R${valor_venda:.2f}")