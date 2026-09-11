animal = "Chanchito feliz"
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.strip().capitalize())  # Convierte la primera letra a mayúscula
print(animal.title())  # Convierte la primera letra de cada palabra a mayúscula
print(animal.strip())  # Elimina espacios en blanco al inicio y al final
print(animal.replace("Chanchito", "Gatito"))  # Reemplaza una subcadena por otra
print(animal.split())  # Divide la cadena en una lista de palabras
print(animal.find("feliz"))  # Busca la posición de una subcadena
print(animal.count("i"))  # Cuenta cuántas veces aparece una subcadena
print("chito" in animal)  # Verifica si una subcadena está presente
print("chito" not in animal)  # Verifica si una subcadena no está presente
print(animal.startswith("Chan"))  # Verifica si la cadena comienza con una subcadena
print(animal.endswith("feliz"))  # Verifica si la cadena termina con una sub