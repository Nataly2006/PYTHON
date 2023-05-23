# Codigo 1
def cuenta(n):
    return list(range(n))

for i in range(151):
    print(i)

# Básico: imprime todos los números enteros del 0 al 150.

# Codigo 2
for num in range(5, 1001, 5):
    print(num)

# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

# Codigo 3
for i in range(1, 101):
    if i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
# Contar a la manera del Dojo 

# Codigo 4
suma_impares = 0

for num in range(1, 500001, 2):
    suma_impares += num

print("La suma de los enteros impares del 0 al 500,000 es:", suma_impares)

# agregar los enteros impares del 0 al 500,000
# e imprime la suma final

# Codigo 5
num = 2018

while num >= 0:
    print(num)
    num -= 4

# imprimir números positivos comenzando desde el 2018
# en cuenta regresiva de 4 en 4  

# Codigo 6
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
# Contador flexible

lista = [5,7,20,3]
promedio = sum(lista) / len(lista)
print(promedio)  # Output: 3.0