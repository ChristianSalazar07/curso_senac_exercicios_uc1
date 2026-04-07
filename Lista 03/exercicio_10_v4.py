qtd_praias = 0
praias_mais_15km = 0
veranistas_nao_asfaltado = 0
qtd_praias_nao_asfaltado = 0
praias_asfaltas_menos_1k_veranistas = []
tem_mais_praias = "S"
praias = {}
while tem_mais_praias == "S" or tem_mais_praias == "s":
    qtd_praias = qtd_praias + 1
    nome = input(f"Informe o nome da {qtd_praias}ª praia:")
    distancia = float(input(f"Informe a distância da {qtd_praias}ª praia ao centro em km:"))
    veranistas = int(input(f"Informe a quantidade média de veranistas na {qtd_praias}ª praia:"))
    acesso = float(input(f"Informe o tipo de acesso à {qtd_praias}ª praia(0 - acesso não asfaltado; 1 - acesso asfaltado):"))
    praias[nome] = [distancia, veranistas, acesso]
    tem_mais_praias = input("Tem mais praias?([S]im ou [N]ão?):")
lista_nomes = praias.keys()
for praia in lista_nomes:
    elemento = praias.get(praia)
    distancia = elemento[0]
    veranistas = elemento[1]
    acesso = elemento[2]
    if distancia > 15:
        praias_mais_15km = praias_mais_15km + 1
    if acesso == 0:
        veranistas_nao_asfaltado = veranistas_nao_asfaltado + veranistas
        qtd_praias_nao_asfaltado = qtd_praias_nao_asfaltado + 1
    if veranistas < 1000 and acesso == 1:
        praias_asfaltas_menos_1k_veranistas.append(f"Nome:{praia} - Distância ao centro:{distancia}km")
print(f"{praias_mais_15km} estão a mais de 15km do centro\n")
if qtd_praias_nao_asfaltado != 0:
    print(f"{veranistas_nao_asfaltado/qtd_praias_nao_asfaltado} foi a média de veranistas nas praias sem acesso asfaltado na última temporada")
for i in range(len(praias_asfaltas_menos_1k_veranistas)):
    print(praias_asfaltas_menos_1k_veranistas[i])