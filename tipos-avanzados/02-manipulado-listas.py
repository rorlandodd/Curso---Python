mascotas = ["Copito", "Cola de palo", "Pili", "Mila"]

i=0
while i < len(mascotas):
    print(f"{i}: {mascotas[i]}")
    i +=1
print(mascotas[1:2])
print(mascotas[-1])
print(mascotas[::2])
print(mascotas[2:])
print(mascotas[1::2])

numeros = list(range(21))
print(numeros[1::2])
print(numeros[::2])
