x = int(input("Digite la cantidad de números: "))

suma = 0
promedio = 0

for i in range(0,x):
        numeros = int(input("Digite los números: "))
        suma += numeros

promedio = suma/x

print("La suma de los números es {} y el promedio de los numeros es {}.".format(suma,promedio))