qtdCorretores = 3
class corretor:
    def __init__(self, nome, venda):
        self.nome = nome
        self.venda = venda
        self.comissao = 0
    def calcularComissao(self):
        if self.venda > 50000:
            self.comissao = self.venda * 0.12
        elif self.venda >= 30000:
            self.comissao = self.venda * 0.095
        else:
            self.comissao = self.venda * 0.075
    def __str__(self):
        return f"O corretor {self.nome} vendeu R${self.venda:.2f} e recebeu R${self.comissao:.2f}"
def entradaCorretores():
    corretores = []
    for i in range(qtdCorretores):
        meuCorretor = corretor(input(f"Informe o nome do {i+1}° corretor:"),
                               float(input(f"Informe o valor das vendas do {i+1}° corretor em reais:")))
        meuCorretor.calcularComissao()
        corretores.append(meuCorretor)
    return corretores
def calcularTotalVendas(corretores):
    vendasTotal = 0
    for corretor in corretores:
        vendasTotal = vendasTotal + corretor.venda
    return vendasTotal
def saida():
    for corretor in listaCorretores:
        print(corretor)
    print(f"O valor total de vendas da empresa foi de R${totalVendas:.2f}")
listaCorretores = entradaCorretores()
totalVendas = calcularTotalVendas(listaCorretores)
saida()
