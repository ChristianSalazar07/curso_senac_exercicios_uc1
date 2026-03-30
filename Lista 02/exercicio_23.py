preco_compra = float(input("Informe o preço de compra do produto:"))
preco_venda = float(input("Informe o preço de venda do produto:"))
lucro_percentual = ((preco_venda-preco_compra)/preco_compra)*100
print(f"O lucro foi de {lucro_percentual:.2f}%")