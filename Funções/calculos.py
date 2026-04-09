def media_ponderada(valores, pesos):
    soma = 0
    soma_pesos = 0
    if (pesos or valores) == []:
        pass
    elif type(pesos) != list or type(valores) != list:
        pass
    elif len(valores) == len(pesos):
        for i in range(len(valores)):
            valor = valores[i]
            peso = pesos[i]
            soma = soma + valor * peso
            soma_pesos = soma_pesos + peso
        return soma/soma_pesos
    else: pass
def media_simples(valores):
    soma = 0
    for numero in valores:
        soma = soma + numero
    return soma/len(valores)
print(media_ponderada(4,[3]))