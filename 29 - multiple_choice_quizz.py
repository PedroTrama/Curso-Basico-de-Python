from Question import Question

questoes = [
    "1)Quanto é 1+1?\n(a) 11\n(b) 2\n(c) 1\n",
    "\n2)Quanto é 3*27\n(a) 9\n(b) 30\n(c) 81\n",
    "\n3)Quanto é 10/0\n(a) Impossivel\n(b) 10\n(c) 0\n"        #podemos criar infinitar perguntas
]

questions = [
    Question(questoes[0],"b"),
    Question(questoes[1],"c"),
    Question(questoes[2],"a"),                                  #basta adiciona-las aqui
]

def quizz(questions):
    acertos = 0
    for question in questions:                                  #o parametro question fica rodando todas as questoes

        resposta = input(question.numero + "Sua resposta: ")

        if resposta == question.gabarito:
            acertos += 1
            print("Correto")
        else:
            print("Errado")

    print("\nVocê acertou " + str(acertos) + " de " + str(len(questions)) + " questões!")

quizz(questions)