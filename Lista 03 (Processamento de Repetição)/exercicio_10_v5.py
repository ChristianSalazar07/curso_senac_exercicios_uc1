class Praia:
    def __init__(self, nome, distancia, veranistas, acesso):
        self.nome = nome
        self.distancia = distancia
        self.veranistas = veranistas
        self.acesso = acesso
def entradaDados():
    qtd_praias = 0
    tem_mais_praias = "S"
    praias = []
    while tem_mais_praias == "S" or tem_mais_praias == "s":
        qtd_praias = qtd_praias + 1
        minhaPraia = Praia(input(f"Informe o nome da {qtd_praias}ª praia:"),
                      float(input(f"Informe a distância da {qtd_praias}ª praia ao centro em km:")),
                      int(input(f"Informe a quantidade média de veranistas na {qtd_praias}ª praia:")),
                      float(input(f"Informe o tipo de acesso à {qtd_praias}ª praia(0 - acesso não asfaltado; 1 - acesso asfaltado):")))
        praias.append(minhaPraia)
        tem_mais_praias = input("Tem mais praias?([S]im ou [N]ão?):")
    return praias
def processamentoDados(praias):
    dados = {"qtdPraiasMais15km": 0,
             "veranistasNaoAsfaltado": 0,
             "qtdVeranistasNaoAsfaltado": 0,
             "praiasAsfaltasMenos1kVeranistas": []}
    for praia in praias:
        if praia.distancia > 15:
            dados["qtdPraiasMais15km"] = dados["qtdPraiasMais15km"] + 1
        if praia.acesso == 0:
            dados["veranistasNaoAsfaltado"] = dados["veranistasNaoAsfaltado"] + praia.veranistas
            dados["qtdVeranistasNaoAsfaltado"] = dados["qtdVeranistasNaoAsfaltado"]
        if praia.veranistas < 1000 and praia.acesso == 1:
            dados["praiasAsfaltasMenos1kVeranistas"].append(f"Nome:{praia.nome} - Distância ao centro:{praia.distancia}km")
    return dados
def saidaDados(praias, dados):
    print(f"{dados["qtdPraiasMais15km"]} estão a mais de 15km do centro\n")
    if dados["qtdVeranistasNaoAsfaltado"] != 0:
        print(f"{dados["veranistasNaoAsfaltado"]/dados["qtdVeranistasNaoAsfaltado"]} foi a média de veranistas nas praias sem acesso asfaltado na última temporada")
    for i in range(len(dados["praiasAsfaltasMenos1kVeranistas"])):
        print(dados["praiasAsfaltasMenos1kVeranistas"])
listaPraias = entradaDados()
dadosPraias = processamentoDados(listaPraias)
saidaDados(listaPraias, dadosPraias)