qtd_praias = 0
praias_mais_15km = 0
veranistas_nao_asfaltado = 0
praias_asfaltas_menos_1k_veranistas = []
tem_mais_praias = "S"
while tem_mais_praias == "S" or tem_mais_praias == "s":
    qtd_praias = qtd_praias + 1
    nome = input(f"Informe o nome da {qtd_praias}ª praia:")
    distancia = float(input(f"Informe a distância da {qtd_praias}ª praia ao centro em km:"))
    veranistas = int(input(f"Informe a quantidade média de veranistas na {qtd_praias}ª praia:"))
    acesso = bool(input(f"Informe o tipo de acesso à {qtd_praias}ª praia(0 - acesso não asfaltado; 1 - acesso asfaltado):"))
    if distancia > 15:
        praias_mais_15km = praias_mais_15km + 1
    if acesso == 0:
        veranistas_nao_asfaltado = veranistas_nao_asfaltado + veranistas
    if veranistas < 1000 and acesso == 1:
        praias_asfaltas_menos_1k_veranistas.append(f"Nome:{nome} - Distância ao centro:{distancia}km")
    tem_mais_praias = input("Tem mais praias?([S]im ou [N]ão?):")
print(f"{praias_mais_15km} estão a mais de 15km do centro\n"
      +f"{veranistas_nao_asfaltado} veranistas em média foram nas praias sem acesso asfaltado na última temporada")
for i in range(len(praias_asfaltas_menos_1k_veranistas)):
    print(praias_asfaltas_menos_1k_veranistas[i])