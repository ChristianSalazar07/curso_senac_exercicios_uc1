#Entrada
x = float(input("Informe o valor de x:"))
y = float(input("Informe o valor de y:"))
z = float(input("Informe o valor de z:"))
[a,b] = [0,0]
#Processamento
if x > y or z <= 30:
    a = x * 2
else:
    a = x/2
    b = z/5
print(f"a={a:.2f}\nb={b:.2f}")