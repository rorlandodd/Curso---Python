resultado = 0
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese Operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguinte número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "divi":
        resultado /= n2
    else:
        print("Operacion no valida")

    print (f"El resultado es: {resultado}")