tempo = float(input("Informe o tempo gasto em hora:"))
velocidade_media = float(input("Informe a velocidade média em km/h:"))
gasto = (tempo * velocidade_media) / 12
print(f"Foram gastos {gasto:.2f}L")