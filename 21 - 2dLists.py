numberGrid = [                  #assim que criamos matrizes
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numberGrid[2][1])         #printamos os elementos das linhas e colunas (comeca no 0 sempre)

for linha in numberGrid:        #printa todas as linhas
    print(linha)
    
for linha in numberGrid:
    for coluna in linha:
        print(coluna)           #printa todos elementos
