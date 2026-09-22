#Filas Fifo
from collections import deque

lista = [1, 2, 3, 4]
lista1 = list(range(1000))

fila = deque([1,2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)

fila.popleft()
fila.popleft()
fila.popleft()


print(fila)

if not fila:
    print("Lista vacia")