pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)

uiltimoElemento = pila.pop()
pila.pop()
pila.pop()
print(uiltimoElemento)
print(pila)


if not pila:
    print("Pila Vacia")