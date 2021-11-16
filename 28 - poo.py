from Classes import Student                         #importa a classse Student do arquivo .py Student
from Classes import GenshinCharacter

student1 = Student("Pedro", 19, "BSI", 2, False)    #cria um objeto student1 dentro da classe Student
student2 = Student("Val", 18, "BSI", 2, False)      #podemos criar quantos objetos quisermos
genshinCharacter = GenshinCharacter("Klee", "Pyro", "Catalista", 5)
genshinCharacter2 = GenshinCharacter("Diona", "Cryo", "Bow", 4)

print(student1.nome)
print(genshinCharacter.nome)
print(student2.curso)
print(genshinCharacter2.visao)