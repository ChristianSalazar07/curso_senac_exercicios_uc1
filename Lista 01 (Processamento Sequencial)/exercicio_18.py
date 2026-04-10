import math
altura_degrau = float(input("Informe a altura dos degraus:"))
altura_total = float(input("Informe a altura que será subida:"))
degraus = math.ceil(altura_total/altura_degrau)
print(f"Será necessário subir {degraus:.0f} degraus")