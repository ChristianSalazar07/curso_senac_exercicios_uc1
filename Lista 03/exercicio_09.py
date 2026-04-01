diaria = 150
qtd_clientes = 3
ganho_hotel = 0
clientes = []
for i in range(qtd_clientes):
    nome = input(f"Informe o nome do {i+1}° cliente:")
    diarias = int(input(f"Informe por quantas diárias o {i+1}° cliente ficará:"))
    taxa_servico = 6.3
    if diarias < 15:
        taxa_servico = 8
    elif diarias > 15:
        taxa_servico = 5
    diaria_cliente = diaria + taxa_servico
    ganho_hotel = ganho_hotel + (diaria_cliente * diarias)
    clientes.append(f"Nome:{nome} - Conta:R${diaria_cliente*diarias:.2f}")
for i in range(len(clientes)):
    print(clientes[i])
print(f"O hotel ganhou R${ganho_hotel:.2f}")