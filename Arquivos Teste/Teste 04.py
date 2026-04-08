def media(valores):
    soma = 0
    for numero in valores:
        soma = soma + numero
    return soma/len(valores)
print(media([1,3,5,7]))
print(media([5,10,15,20,25]))