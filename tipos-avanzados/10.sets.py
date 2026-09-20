# Set ignifica grupo o conjunto
primer = {1,1,2,2,3,4}
print(primer) 
primer.add(0)
print(primer)
#primer.remove()
print(primer)

segundo = [3,4,5]
segundo = set(segundo)
print(segundo)

#print(primer | segundo) #union
#print(primer & segundo) #devuleve solos los repetidos en cada set
#print(primer - segundo) #Mostrar los datos
print(primer ^ segundo)