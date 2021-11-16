#os loops de for sao muito poderosos, vale a pena usa-los em programas
for letras in "Letras ! ":                      #printa todas as letras da strig
    print(letras)

cores = ["Vermelho", "Amarelo", "Azul"]
for cores in cores:                             #printa todos elementos da lista
    print(cores)

for indice in range(10):                        #printa todos os numeros de 0 a 9
    print(indice)

for indice2 in range(5, 10):                    #printa todos os numeros de 5 a 9
    print(indice2)

colors = ["Verde", "Laranja", "Roxo"]
for index in range(len(colors)):                #como o tamanho da lista eh 3, ele printa as cores da lista em seus respectivos indices
    print(colors[index])

for controle in range(5):                       #printa tudo ate controle ir de 0 a 4
    if controle == 0:
        print("Primeira iteracao")
    else:
        print("Nao eh a primeira")