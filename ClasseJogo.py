class Heroi:
    def __init__(self, nome: str, idade: int, tipo: str):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "Mago":
            print(f"o {self.tipo} atacou usando Magia")
        elif self.tipo == "Guerreiro":
            print(f"o {self.tipo} atacou usando Espada")
        elif self.tipo == "Monge":
            print(f"o {self.tipo} atacou usando Artes Marciais")
        elif self.tipo == "ninja":
            print(f"o {self.tipo} atacou usando shuriken")

novo_heroi = Heroi(nome="Micael", idade=18, tipo="Mago")
novo_heroi.atacar()
