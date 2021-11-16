#podemos trabalhar com varios tipos de numeros
print(2)                #naturais
print(2.0987)           #decimais
print(-2.0987)          #numeros negativos

#temos todas operacoes basicas
print(3 + 4.5)
print(3 - 4.5)
print(3 * 4.5)
print(3 / 4.5)
print(3 * (4 + 5))      #a ordem importa, podemos usar parenteses!
print(10 % 3)           #mostra o resto

#inclusive usar como variaveis
meuNumero = 29
print(meuNumero)
print(str(meuNumero))   #ou transforma-lo em strinh! usamos isso para printar numeros junto de strings tipo:
#print(meuNumero + (" eh meu numero favorito")) -> Isso da erro pq o numero esta como int e nao como string
print(str(meuNumero) + (" eh meu numero favorito")) #agora deu certo ;)

#outras funcoes uteis
print(abs(-72))         #aqui temos o valor absoluto do numero da variavel
print(pow(3,2))         #assim, elevamos ao quadrado ou aa potencia que quisermos
print(2**3)             #assim, tbm podemos fazer um numero elevado a outro
print(max(12,69,4,59))  #printa o maior numero
print(min(12,69,4,59))  #printa o menor numero
print(round(3.98))      #arredonda o numero

#podemos importar uma biblioteca de matematica e ganhar novas funcoes:
from math import *

print(floor(3.14))      #retira tudo depois da virgula
print(ceil(3.14))       #arredonda pra cima de qq jeito
print(sqrt(81))         #raiz quadrada com uma casa decimal
#tem muitas outras funcoes!



