qtd_clientes = 10
clientes = []
arrecadacao = 0
for i in range(qtd_clientes):
    nome_cliente = input(f"Informe o nome do {i+1}° cliente:")
    valor_compra = float(input(f"Informe o valor da compra do {i+1}° cliente:"))
    if valor_compra >= 250:
        desconto = 0.2
        valor_final = valor_compra * (1-desconto)
    else:
        desconto = 0.15
        valor_final = valor_compra * (1-desconto)
    arrecadacao = arrecadacao + valor_final
    clientes.append(f"Nome = {nome_cliente} - Valor Original = R${valor_compra:.2f} - Desconto = {desconto*100:.0f}% - Valor Final = R${valor_final:.2f}")
for i in range(len(clientes)):
    print(clientes[i])
print(f"A loja arrecadou R${arrecadacao:.2f}")