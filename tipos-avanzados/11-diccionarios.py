usuarios = {"id": 2, "nombre": "Rene", "edad": 38}

print (usuarios)
print (usuarios["nombre"])
usuarios["sexo"] = "hombre"
print(usuarios)
print(usuarios, usuarios["edad"])
if "nombre" in usuarios:
    print(usuarios["nombre"])
else:
    print(f"No se encontro")

print(usuarios.get("nombr", "No se encontro"))
print(usuarios.get("nombre"))

del usuarios["sexo"]
print(usuarios)

for llave,valor in usuarios.items():
    print(llave, valor)

users= [
    {"id":1, "nombre": "Rene"},
    {"id":2, "nombre": "Matias"},
    {"id":3, "nombre": "Camila"}
]

for user in users:
    print(user["nombre"])