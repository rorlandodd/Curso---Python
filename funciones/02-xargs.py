def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


print(suma(5, 2))
print(suma(3, 7, 5))
print(suma(45, 3, 7, 79))