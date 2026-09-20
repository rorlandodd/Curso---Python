numeros = [1, 2, 3]
numerosmas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# primero, segundo, tercero = numeros

# print(segundo, primero, tercero)
primero, *otros = numeros
print(primero)
print(*otros)

pri, segu, *otros, penu, ulti = numerosmas

print(pri, ulti, penu)