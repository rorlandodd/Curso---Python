numeros = [3,6,34,56,3,2,8,3,634,54]
numeros2 = sorted(numeros) #Va a general nueva lista sin modificar la que saca copia
print(numeros2)

numeros.sort(reverse=True)
print(numeros)

usuarios =[[7, "Rene"], [6, "Camila"], [8, "Matias"], [5, "Natalia"]]

def ordena(elemento):
    return elemento[1]

print(usuarios)
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)