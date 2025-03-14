class Cachorro:
    def __init__(self, nome, raca, comida, idade):
        self .nome = nome
        self .raca = raca
        self .comida = comida
        self .idade = idade
        self .acordado = False
        self .feliz = False 

    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"


    def latir (self):
        print(f"{self.nome} está latindo: AU AU!")

    def brincar (self):
        print(f"{self.nome} está brincando no gramado!")

    def dormir (self):
        print (f"{self.nome} está dormindo no sofá!")

    def comer (self, comer):
        self.comida -= 1
        print (f"{self.nome} está comendo: {comer}.")

    def envelhecer (self):
        self.idade += 1
        print (f"{self.nome} agora tem {self.idade} anos!")

    # Cachorros
cachorro1 = Cachorro("bob","shitzu", 6, 6)
cachorro2 = Cachorro("Rex","labrador" ,3, 2)
cachorro3 = Cachorro("Bolt","pastor alemão", 7, 9)

    # Interagindo com os cachorros 
cachorro1.latir()
cachorro1.comer("ração")
cachorro1.envelhecer()


print()

    # Interagindo com os cachorros 
cachorro2.latir()
cachorro2.comer("ração")
cachorro2.envelhecer()


print()

    # Interagindo com os cachorros 
cachorro3.latir()
cachorro3.comer("ração")
cachorro3.envelhecer()