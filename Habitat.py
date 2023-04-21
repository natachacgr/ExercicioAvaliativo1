import Cuidador

class Habitat:
    def __init__(self, id: str, nome: str, tipoAmbiente: str, cuidador: Cuidador):
        self.id = id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador