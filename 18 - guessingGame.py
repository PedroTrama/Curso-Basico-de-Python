secretWord = "Elefante"
guess = ""
guessCount = 0
guessLimit = 3
out_of_guesses = False

while guess != secretWord and not(out_of_guesses):
    if guessCount < guessLimit:
        guess = input("Sua resposta:")
        guessCount += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Voce Perdeu")

else:
    print("Voce ganhou!")