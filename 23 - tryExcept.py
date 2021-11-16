#esse tipo de estrutura previne que o programa quebre por causa de erros bestas
try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("Dividiu por zero")
except ValueError:
    print("Entrada invalida")