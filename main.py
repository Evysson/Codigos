class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False
    def comer (self, comendo):
        if self.comendo == False:
            print(f"{self.nome} Foi comer")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo.")
        self.comendo = True
        print(f"{self.nome} Está comendo")
    def pararComer (self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo")
    def andar (self, andando):
        if self.andando == False:
            print(f"{self.nome} foi andar")
            self.andando = True
        else:
            print(f"{self.nome} Já está andando")
    def paraAndar (self):
        if self.andando == True:
            print(f"{self.nome} parou de andar")
            self.andando == False
        else:
            print(f"{self.nome} não está andando")
        print(f"{self.nome}foi caminhar {self.andando}")
    def dormi (self, dormindo):
        if self.dormindo == False:
            print(f"{self.nome} está dormindo")
            self.dormindo = True
        else:
            print(f"{self.nome} já está dormindo")
    def paraDormi (self):
        if self.dormindo == True:
            print(f"{self.nome} Acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} já está acordado")

p1 = Pessoa( "Evysson", 78, 27)
p1.comer("Arroz")
p1.dormi("na cama")
p1.andar("na rua")





























