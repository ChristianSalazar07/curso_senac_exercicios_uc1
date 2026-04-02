dia_semana = input("Informe o dia da semana:")
match dia_semana:
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":print(f"{dia_semana} é dia de Trabalho")
    case "Sábado" | "Domingo":print(f"{dia_semana} é dia de Casa")