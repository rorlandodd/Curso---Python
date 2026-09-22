from pprint import pprint
string = "Hola mundo como estan!!"

def quita_espacios(texto):
    return [char for char in texto if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def ordena(dict):
    return sorted(
        dict.items(),
        key = lambda key: key[1],
        reverse = True,
    )

def mayores_tuplas(lista):
    maximo = lista [0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden [1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)


#pprint(contados, width=1)
#print(sin_espacios)
#print(ordenados)
print(mayores)