qtd_produtos = 4
estoques_baixos = []
for i in range(qtd_produtos):
    nome = input(f"Informe o nome do {i+1}° produto:")
    estoque = int(input(f"Informe o estoque do {i+1}° produto:"))
    if estoque < 30:
        estoques_baixos.append(nome)
for i in range(len(estoques_baixos)):
    print(f"{estoques_baixos[i]} está abaixo do estoque mínimo")