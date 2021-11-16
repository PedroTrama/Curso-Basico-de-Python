#formato de uma classe
class Student:

    def __init__(self, nome, idade, curso, semestre, deDP):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.semestre = semestre
        self.deDP = deDP

    def ehVeterano(self):
        if self.semestre > 2:
            return True
        else:
            return False

#podemos fazer outras classes nesse mesmo arquivo
class GenshinCharacter:

    def __init__(self, nome, visao, arma, raridade):
        self.nome = nome
        self.visao = visao
        self.arma = arma
        self.raridade = raridade