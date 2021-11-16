arquivoCores = open("colors.txt", "a")      #adiciona so ao final do arquivo

arquivoCores.write("\nDourado")             #escreve Dourado e pula uma linha ao fim do arquivo

arquivoCores.close()

arquivoCores = open("colors.txt", "w")      #reescreve tudo no arquivo

arquivoCores.write("Dourado\n")               #escreve Dourado e pula uma linha ao fim do arquivo

arquivoCores.close()