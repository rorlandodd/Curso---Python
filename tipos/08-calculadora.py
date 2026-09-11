numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if (operacion == "+"):
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {int(resultado)}")
elif (operacion == "-"):
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {int(resultado)}")
elif (operacion == "*"):
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {int(resultado)}")
elif (operacion == "/"):
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {int(resultado) }")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida. Por favor, ingrese una operación válida (+, -, *, /).")