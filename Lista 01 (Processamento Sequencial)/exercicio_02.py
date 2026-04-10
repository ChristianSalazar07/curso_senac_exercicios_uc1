'''Faça um algoritmo que o usuário informe os valores dos catetos de um
triângulo retângulo e que ao final escreva a sua hipotenusa'''
cateto01 = float(input("Diga o valor do primeiro cateto:"))
cateto02 = float(input("Diga o valor do segundo cateto:"))
hipotenusa = ((cateto01**2) + (cateto02**2))**(0.5)
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")