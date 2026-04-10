segundos = float(input("Informe a quantidade de segundos:"))
minutos = int(segundos / 60)
segundos = segundos - minutos * 60
horas = int(minutos/60)
minutos = minutos - horas *60
dias = int(horas/24)
horas = horas - dias * 24
print(f"Isso equivale a {dias:.0f}d, {horas:.0f}h, {minutos:.0f}min e {segundos:.2f}s")