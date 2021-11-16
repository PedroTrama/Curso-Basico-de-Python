coolPokemon = ["Totodile", "Ralts", "Phanpy", "Kyogre", "Gastly", "Bulbasaur"]          #a lista comeca com indice 0

print(coolPokemon)              #printa toda a lista
print(coolPokemon[0])           #printa o item indexado
print(coolPokemon[4])
print(coolPokemon[-1])          #printa de tras pra frente o item indexado
print(coolPokemon[1:])          #printa todos depois do index
print(coolPokemon[1:4])         #printa todos entre os index (exclusivo)

coolPokemon[2] = "Donpham"      #renomeando um dos itens
print(coolPokemon)

#funcoes para listas
evolutions = ["Feraligatr", "Gardevoir", "Donpham", "Gengar", "Venusaur"]               #definimos outra lista
coolPokemon.extend(evolutions)      #junta duas listas
print(coolPokemon)

coolPokemon.append("Vulpix")        #adiciona um item especifico
print(coolPokemon)

coolPokemon.insert(0, "Litwick")    #adiciona um item no index indicado
print(coolPokemon)

coolPokemon.remove("Vulpix")        #remove um item especifico
print(coolPokemon)

coolPokemon.pop()                   #remove um item (se n especificar, o ultimo)
print(coolPokemon)

coolPokemon.clear()                 #limpa a lista
print(coolPokemon)

coolPokemon = ["Totodile", "Totodile", "Totodile", "Totodile", "Ralts", "Phanpy", "Kyogre", "Gastly", "Bulbasaur"]
evolutions = ["Feraligatr", "Gardevoir", "Donpham", "Gengar", "Venusaur"]
coolPokemon.extend(evolutions)

print(coolPokemon.index("Totodile"))#mostra o indice do elemento pedido
#print(coolPokemon.index("Snive")) -> gera um erro pois snive nao esta na lista

print(coolPokemon.count("Totodile"))#conta quantos itens do mesmo

coolPokemon.sort()                  #coloca em ordem alfabetica
print(coolPokemon)

coolPokemon.reverse()               #coloca em ordem alfabetica de tras pra frente
print(coolPokemon)

nicePokemon = coolPokemon.copy()    #copia uma lista
print(nicePokemon)