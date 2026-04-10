nome01 = input("Informe o nome do primeiro produto:")
estoque01 = int(input("Informe o estoque do primeiro produto:"))
nome02 = input("Informe o nome do segundo produto:")
estoque02 = int(input("Informe o estoque do segundo produto:"))
nome03 = input("Informe o nome do terceiro produto:")
estoque03 = int(input("Informe o estoque do terceiro produto:"))
nome04 = input("Informe o nome do quarto produto:")
estoque04 = int(input("Informe o estoque do quarto produto:"))
#Processamento
if estoque01 < 30:
    print(f"{nome01} está abaixo do estoque mínimo")
if estoque02 < 30:
    print(f"{nome02} está abaixo do estoque mínimo")
if estoque03 < 30:
    print(f"{nome03} está abaixo do estoque mínimo")
if estoque04 < 30:
    print(f"{nome04} está abaixo do estoque mínimo")