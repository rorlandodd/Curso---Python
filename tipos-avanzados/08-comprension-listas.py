usuarios =[[7, "Rene"], [6, "Camila"], [8, "Matias"], [5, "Natalia"]]

nombres = []
for usuario in usuarios:
    nombres.append(usuarios[0])
#print(nombres)

nombres1 = [usuario[1] for usuarios in usuarios]
#print(nombres1)

#filtrar y transformada
nombres2 = [usuario[1] for usuario in usuarios if usuario[0] > 5]
#print(nombres2)

nombres3 = list(map(lambda usuario: usuario[1], usuarios))
print(nombres3)

nombres4 = list(filter(lambda usuario: usuario[0] >2, usuarios))
print(nombres4)