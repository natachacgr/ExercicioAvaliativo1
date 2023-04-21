import Habitat

class Animal:
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: Habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat