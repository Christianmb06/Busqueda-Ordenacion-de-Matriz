def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Definir la matriz 3x3
matriz = [
    [4, 7, 1],
    [8, 3, 5],
    [9, 2, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = int(input("Ingrese el número de fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
if 0 <= fila_a_ordenar < len(matriz):
    matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
else:
    print("Número de fila fuera de rango.")

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
