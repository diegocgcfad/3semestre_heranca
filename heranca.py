class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def dieta(self):
        print("Carnívoro")

class dataNascimento(Animal): #Indicação da superclasse entre parênteses
    def __init__(self, nome, especie, data): #Adição da propriedade data
        Animal.__init__(self, nome, especie) #Mantendo a herança das outras propriedades
        self.data = data
    def nascimento(self):
        print(f"Nome do animal: {self.nome}\nEspécie: {self.especie}\nData de Nascimento: {self.data}")
x = dataNascimento("Simba","Leão Africano","1994-07-08")
x.nascimento()
