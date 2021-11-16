def elevando(base, potencia):
    result = 1

    for index in range(potencia):
        result *= base
    return result

print(elevando(2,3))
