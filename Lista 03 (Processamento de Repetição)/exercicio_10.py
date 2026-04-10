qtd_praias = 3
praias_mais_15km = 0
veranistas_nao_asfaltado = 0
praias_asfaltas_menos_1k_veranistas = []
for i in range(qtd_praias):
    nome = input(f"Informe o nome da {i+1}ª praia:")
    distancia = float(input(f"Informe a distância da {i+1}ª praia ao centro em km:"))
    veranistas = int(input(f"Informe a quantidade média de veranistas na {i+1}ª praia:"))
    acesso = bool(input(f"Informe o tipo de acesso à {i+1}ª praia(0 - acesso não asfaltado; 1 - acesso asfaltado):"))
    if distancia > 15:
        praias_mais_15km = praias_mais_15km + 1
    if acesso == 0:
        veranistas_nao_asfaltado = veranistas_nao_asfaltado + veranistas
    if veranistas < 1000 and acesso == 1:
        praias_asfaltas_menos_1k_veranistas.append(f"Nome:{nome} - Distância ao centro:{distancia}km")
print(f"{praias_mais_15km} estão a mais de 15km do centro\n"
      +f"{veranistas_nao_asfaltado} veranistas em média foram nas praias sem acesso asfaltado na última temporada")
for i in range(len(praias_asfaltas_menos_1k_veranistas)):
    print(praias_asfaltas_menos_1k_veranistas[i])