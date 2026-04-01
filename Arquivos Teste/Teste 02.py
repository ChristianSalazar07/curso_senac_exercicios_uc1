lista_clientes = []
tem_mais_clientes = "Sim"
while tem_mais_clientes == "Sim" or tem_mais_clientes == "sim":
    informacoes_clientes = {"nome" : input(f"Informe o nome do {len(lista_clientes)+1}° cliente:"),
                         "id" : int(input(f"Informe o ID {len(lista_clientes)+1}° cliente:"))
                           }
    lista_clientes.append(informacoes_clientes)
    tem_mais_clientes = input("Tem mais clientes?(Sim ou Não):")
for i in range(len(lista_clientes)):
    print(f"{lista_clientes[i]}")