def say_hi():                #aqui definimos uma funcao que sera usada. IDENTACAO IMPORTA MUITO. SE SAIR DA IDENTACAO, SAI DA FUNCAO
    nome = input("Qual o seu nome? ")
    print("Ola! " + nome)

say_hi()                     #aqui rodamos a funcao

def say_hi2(name, age):      #nessa funcao colocamos um parametro, se marcarmos ele na hora de chamar a funcao ela pode muder conforme o parametro (podemos colcoar quantos parametros quisermos
    print("Ola! " + name + " Sua idade eh: " + age)

say_hi2("Pedro", "10")
say_hi2("Lucas", "15")
say_hi2("Gabriel", "20")
