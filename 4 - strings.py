print("TESTANDO STRINGS\n________________")     #\n pula lina. \\ printa uma barra \" printa aspas
phrase = "Olha que frase GRANDE"                #variavel string
print(phrase + (", muuuuito GRANDE"))           #printa variavel + string
print(phrase.upper())                           #deixa tudo upper case
print(phrase.lower())                           #deixa tudo lower case
print(phrase.lower().islower())                 #primeiro deixa em lower e dps verifica se esta em lower, retornando true ou false
print(len(phrase))                              #mostra o numero de caracteres
print(phrase[0])                                #mostra o primeiro caractere
print(phrase[20])                               #mostra o vigesimo primeiro caractere
print(phrase.index(" "))                        #printa o primeiro caractere ou string com o valor entre parenteses
print(phrase.replace("GRANDE", "pequena"))      #troca uma string por outra

