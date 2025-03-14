class Cachorro:
    def __init__(self, nome, raca, comida, idade):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.idade = idade
        self.acordado = False
        self.feliz = False
        self.energia = 100  # Novo atributo 'energia', inicializado com 100

    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}, Energia: {self.energia}"

    def latir(self):
        print(f"{self.nome} está latindo: AU AU!")

    def brincar(self):
        if self.energia >= 20:  # Verifica se o cachorro tem energia suficiente para brincar
            print(f"{self.nome} está brincando no gramado!")
            self.energia -= 20  # Reduz a energia em 20 ao brincar
        else:
            print(f"{self.nome} está sem energia para brincar! Precisa descansar.")

    def dormir(self):
        print(f"{self.nome} está dormindo no sofá!")
        self.energia = 100  # Restaura a energia para 100 ao dormir

    def comer(self, comer):
        self.comida -= 1
        print(f"{self.nome} está comendo: {comer}.")

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos!")

# Cachorros
cachorro1 = Cachorro("Bob", "Shitzu", 6, 6)
cachorro2 = Cachorro("Rex", "Labrador", 3, 2)
cachorro3 = Cachorro("Bolt", "Pastor Alemão", 7, 9)

# Interagindo com os cachorros
cachorro1.latir()
cachorro1.comer("ração")
cachorro1.envelhecer()
cachorro1.brincar()  # O cachorro brinca, reduzindo a energia
cachorro1.dormir()  # O cachorro dorme, restaurando a energia

print()

# Interagindo com os cachorros
cachorro2.latir()
cachorro2.comer("ração")
cachorro2.envelhecer()
cachorro2.brincar()  # O cachorro brinca, reduzindo a energia
cachorro2.dormir()  # O cachorro dorme, restaurando a energia

print()

# Interagindo com os cachorros
cachorro3.latir()
cachorro3.comer("ração")
cachorro3.envelhecer()
cachorro3.brincar()  # O cachorro brinca, reduzindo a energia
cachorro3.dormir()  # O cachorro dorme, restaurando a energia