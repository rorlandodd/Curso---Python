# and, or, not
# and: devuelve True si ambos operandos son True
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# or: devuelve True si al menos uno de los operandos es True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
# not: devuelve True si el operando es False y viceversa
print(not True)  # False
print(not False)  # True

gas = False
encendido = True
edad = 13

# Se ejecuta de izquierda a derecha la menos que este dentro de parentecis que eso se ejecuta primero
if not gas and encendido and edad > 18:
    print("Puede avanzar")
