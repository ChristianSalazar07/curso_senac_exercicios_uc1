segundos_informados = float(input("Informe a quantidade de segundos:"))
minutos = int(segundos_informados / 60)
segundos_informados = segundos_informados - minutos * 60
horas = int(minutos/60)
minutos = minutos - horas *60
dias = int(horas/24)
horas = horas - dias * 24
print(f"Isso equivale a {dias:.2f}d, {horas:.2f}h, {minutos:.2f}min e {segundos_informados:.2f}s")