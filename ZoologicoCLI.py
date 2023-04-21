from Database import Database
from ZoologicoDAO import ZoologicoDAO
from typing import List
from Animal import Animal
from Habitat import Habitat
from Cuidador import Cuidador


class ZoologicoCLI:
    def __init__(self):
        self.db = Database(database="my_database", collection="my_collection")
        self.ZoologicoDAO = ZoologicoDAO()
        self.cuidador = Cuidador()
        self.habitat = Habitat()
        self.animal = Animal()

    def menu(self):
        print("1 - Criar animal")
        print("2 - Procurar animal")
        print("3 - Atualizar animal")
        print("4 - Deletar animal")
        print("0 - Sair")
        opcao = input("Digite a opção que deseja: ")
        if opcao == "1":
            self.createAnimal()
        elif opcao == "2":
            self.readAnimal()
        elif opcao == "3":
            self.updateAnimal()
        elif opcao == "4":
            self.deleteAnimal()
        elif opcao == "0":
            return None

    def createAnimal(self):

        print("Criar novo cuidador")
        idCuidador = input("id: ")
        nomeCuidador = input("nome: ")
        documentoCuidador = input("documento: ")
        self.cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        habitats: List[Habitat] = []
        while True:
            print("Agora criar novo habitat:")
            idHabitat = input("id: ")
            nomeHabitat = input("nome: ")
            tipoAmbiente = input("tipo de ambiente: ")
            idCuidadorH = input("id cuidador: ")
            self.habitat = Habitat(idHabitat, nomeHabitat, tipoAmbiente, idCuidadorH)
            habitats.append(self.habitat)
            resposta = input("Para criar mais digite 1 para encerrar digite 0: ")
            if resposta.lower() == "0":
                break

        # Cria um objeto do tipo Animal
        print("Por fim, criar novo animal:")
        idAnimal = input("id: ")
        nomeAnimal = input("nome: ")
        especieAnimal = input("especie: ")
        idadeAnimal = int(input("idade: "))
        idHabitatA = input("id do habitat: ")
        self.animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, idHabitatA)
        self.ZoologicoDAOdao.createAnimal(self.animal)

    def readAnimal(self):
            animalId = input("Digite id do animal que deseja pesquisar: ")
            animal = self.Zoologicodao.readAnimal(animalId)
            if animal:
                print(f"id: {animal.id}")
                print(f"nome: {animal.nome}")
                print(f"especie: {animal.especie}")
                print(f"Idade: {animal.idade}")
                for habitat in animal.habitat:
                    print(f"habitat: - {habitat.nome} ({habitat.tipo})")
                return
            else:
                print("animal não encontrado")

    def updateAnimal(self):
        animalId = input("id do animal que deseja atualizar: ")
        animal = self.ZoologicoDAOdao.readAnimal(animalId)
        if animal:
            newNome = input("Novo nome do animal: ")
            newEspecie = input("Nova espécie do animal: ")
            newIdade = int(input("Nova idade do animal: "))

            animal.nome = newNome
            animal.especie = newEspecie
            animal.idade = newIdade
            self.dao.updateAnimal(animal)
            print("animal atualizado com sucesso")
        else:
            print("animal não encontrado")

    def deleteAnimal(self):
        animalId = input("Digite o id do animal que deseja deletar: ")
        animal = self.ZoologicoDAOdao.readAnimal(animalId)
        if animal:
            self.dao.deleteAnimal(animalId)
            print("animal deletado com sucesso")
        else:
            print("animal não encontrado")


