def nombreCompleto (nombre, apellido = "Diaz"): #Parametro por defecto
    return f"bienvenido {nombre} {apellido}"

print(nombreCompleto("rene"))
print(nombreCompleto("Orlando", "Duartes"))
print(nombreCompleto(apellido="Diaz", nombre="Matias"))