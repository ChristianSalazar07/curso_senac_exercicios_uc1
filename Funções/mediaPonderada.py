def media_ponderada(valores, pesos):
    soma = 0
    soma_pesos = 0
    if len(valores) == len(pesos):
        for i in range(len(valores)):
            valor = valores[i]
            peso = pesos[i]
            soma = soma + valor * peso
            soma_pesos = soma_pesos + peso
        return soma/soma_pesos
    else: pass
'''print(f"{media_ponderada([100,6,200],[1,1,1])}")
print(f"{media_ponderada([100,6,200],[2,3])}")
print(media_ponderada([2],[3,4]))
print(media_ponderada([2,4,6,8,10],[]))'''