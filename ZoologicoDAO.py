from bson import ObjectId

from Animal import Animal
from Habitat import Habitat


class ZoologicoDAO:
    def __init__(self, database):
        self.db = database

    def createAnimal(self, animal: Animal):
        try:
            result = self.db.collection.insert_one({
                "nome": animal.nome,
                "especie": animal.especie,
                "habitat": animal.habitat
            })
            animal_id = str(result.inserted_id)
            print(f"Id do animal: {animal_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Nao inseriu o animal {e}")
            return None

    def readAnimal(self, id: str) -> Animal:
        try:
            animais = self.db.collection.find_one({"_id": id})
            habitats = animais["habitat"]
            habitat = Habitat(habitats["id"], habitats["nome"], habitats["tipoAmbiente"])
            animal = Animal(animais["id"], animais["nome"], animais["especie"], animais["idade"],
                            habitat)
            print(f"Animal encontrado: {animais}")
            return animal
        except Exception as e:
            print(f"Animal não encontrado {e}")
            return None

    def updateAnimal(self, animal: Animal) -> None:
        try:
            result = self.db.collection.update_one({"_id": ObjectId(animal.id)},
                                                   {"$set": {"nome": animal.nome, "especie": animal.especie,"habitat": animal.habitat}})
            print(f"Animal atualizado: {result.modified_count}")
            return result.modified_count
        except Exception as e:
            print(f"ERRO AO ATUALIZAR ANIMAL {e}")
            return None

    def deleteAnimal(self, id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Animal: {result.deleted_count} deletado")
            return result.deleted_count
        except Exception as e:
            print(f"ERRO AO DELETAR ANIMAL {e}")
            return None
