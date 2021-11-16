arquivoCores = open("colors.txt", "r")  #a letra indica o que vai fazer: r le, w escreve, a adiciona sem mudar, r+ le e escreve

print(arquivoCores.readable())          #verifica se da pra ler
#print(arquivoCores.read())             #printa TUDO mas ele so passa pelo arquivo de texto uma vez ent se printar uma vez n printa mais
print(arquivoCores.readline())          #printa uma linha de cada vez
print(arquivoCores.readlines())         #printa TODAS LINHAS

arquivoCores.close()