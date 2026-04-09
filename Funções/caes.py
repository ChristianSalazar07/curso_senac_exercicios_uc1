class Cao:
    def __init__(self, peso, raca):
        self.peso = peso
        self.raca = raca
    def __str__(self):
        return f"O meu {self.raca} pesa {self.peso:.2f}kg"
    def latir(self):
        for i in range(round(self.peso/4)):
            print("🐕Au!"+"!"*i)
class Golden(Cao):
    def __init__(self, peso, cor_pelo):
        super().__init__(peso, "Golden")
        self.cor_pelo = cor_pelo
    def __str__(self):
        return f"O meu {self.raca} pesa {self.peso:.2f}kg e tem pelo {self.cor_pelo}"
    def latir(self):
        for i in range(round(self.peso/4)):
            print("🐕🐕Auf!"+"!!"*i)
    def sentar(self):
        print("🐕‍🦺Sentado")
class Poodle(Cao):
    def __init__(self, peso, cor_pelo):
        super().__init__(peso, "Poodle")
        self.cor_pelo = cor_pelo
    def __str__(self):
        return f"🐩 O meu {self.raca} pesa {self.peso:.2f}kg e tem pelo {self.cor_pelo}"
    def latir(self):
        for i in range(round(self.peso/3)):
            print("🐩🐩 Arf!"+"!!"*i)
    def sentar(self):
        print("🐩🐕‍🦺Sentado")