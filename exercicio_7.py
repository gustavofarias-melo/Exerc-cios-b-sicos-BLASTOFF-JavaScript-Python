lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = []

for num in lista:
    if( num == 0 ):
        continue
    elif (num % 2 == 0):
        numeros.append(num)

print(numeros)
