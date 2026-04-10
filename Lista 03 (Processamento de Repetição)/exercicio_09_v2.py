diaria = 150
ganho_hotel = 0
clientes = []
tem_mais_cliente = "Sim"
qtd_clientes = 0
while tem_mais_cliente == "Sim" or tem_mais_cliente == "sim":
    qtd_clientes = qtd_clientes + 1
    nome = input(f"Informe o nome do {qtd_clientes}° cliente:")
    diarias = int(input(f"Informe por quantas diárias o {qtd_clientes}° cliente ficará:"))
    taxa_servico = 6.3
    if diarias < 15:
        taxa_servico = 8
    elif diarias > 15:
        taxa_servico = 5
    diaria_cliente = diaria + taxa_servico
    ganho_hotel = ganho_hotel + (diaria_cliente * diarias)
    clientes.append(f"Nome:{nome} - Conta:R${diaria_cliente*diarias:.2f}")
    tem_mais_cliente = input("Tem mais clientes?(Sim ou Não?):")
for i in range(len(clientes)):
    print(clientes[i])
print(f"O hotel ganhou R${ganho_hotel:.2f}")