import numpy as np

# Ejercicio 1: Array de 10 ceros.
array_ceros = np.zeros(10)
print("Ejercicio 1:", array_ceros)

# Ejercicio 2: Array con números del 1 al 20.
array_1_20 = np.arange(1, 21)
print("Ejercicio 2:", array_1_20)

# Ejercicio 3: Números pares del 2 al 50.
array_pares = np.arange(2, 51, 2)
print("Ejercicio 3:", array_pares)

# Ejercicio 5: Matriz 4x4 con valores aleatorios entre 0 y 1.
matriz_aleatoria = np.random.rand(4, 4)
print("Ejercicio 5:\n", matriz_aleatoria)

# Ejercicio 6: suma de arrays a=[1,2,3], b=[4,5,6].
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
suma = a + b
print("Ejercicio 6:", suma)

# Ejercicio 7: multiplicación de matrices 3x3.
matriz1 = np.random.randint(1, 11, (3, 3))
matriz2 = np.random.randint(1, 11, (3, 3))

producto = np.dot(matriz1, matriz2)
print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)
print("Ejercicio 7 - Producto:\n", producto)

# Ejercicio 8: array de 15 valores aleatorios entre 1 y 100.
array_aleatorio = np.random.randint(1, 101, 15)
maximo = np.max(array_aleatorio)
minimo = np.min(array_aleatorio)
promedio = np.mean(array_aleatorio)

print("Ejercicio:", array_aleatorio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Promedio:", promedio)

# Ejercicio 9: matriz 5x5 con valores del 1 al 25.
matriz_5x5 = np.arange(1, 26).reshape(5, 5)
diagonal = np.diag(matriz_5x5)

print("Ejercicio 9:\n", matriz_5x5)
print("Diagonal:", diagonal)

# Ejercicio 10: matriz 5x5 de enteros aleatorios entre 1 y 20.
matriz_aleatoria = np.random.randint(1, 21, (5, 5))
suma_filas = matriz_aleatoria.sum(axis=1)
suma_columnas = matriz_aleatoria.sum(axis=0)

print("Ejercicio 10:\n", matriz_aleatoria)
print("Suma de filas:", suma_filas)
print("Suma de columnas:", suma_columnas)
