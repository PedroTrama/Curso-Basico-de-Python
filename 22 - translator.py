#vamos inventar uma lingua
#essa lingua ira transformar todas vogais do alfabeto em P

def translate(phrase):
    translation = ""
    for letter in phrase:

        if letter.lower() in "aeiou":           #transforma as entradas em minusculas pra poder testar
            if letter.isupper():                #verificando se o input eh maiusculo ou nao
                translation += "P"
            else:
                translation += "p"
        else:
            translation += letter

    return translation

print(translate(input("Digite uma frase: ")))