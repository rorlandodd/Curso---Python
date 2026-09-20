lista = [1 ,2 ,3 ,4]
print(1, 2, 3, 4)
print(*lista)


def n(n1,n2,n3):
    pass

lista2 = [5, 6]
combinada = ["Hola", *lista, *lista2]
print(combinada)

punto1 = {"x":19}
punto2 = {"y":15}
nuevoPunto = {**punto1, **punto2, "z":"Hola mundo"} 
print(nuevoPunto)
