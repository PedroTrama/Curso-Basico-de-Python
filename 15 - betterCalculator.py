print("\tCALCULADORA\n\t-----------\n")

num1 = float(input("Digite o primeiro valor: "))                #Colocar o float na frente imediatamente transforma a entrada em float
num2 = float(input("Digite o segundo valor: "))
operador = input("Digite a operacao que deseja realizar: ")

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    print(num1 / num2)
elif operador == "^":
    print(pow(num1,num2))
else:
    print("Operação inválida, use apenas os sinais +, -, *, / e ^")

