def buscar_valor(matriz, valor):
    """Busca un valor en una matriz bidimensional."""
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return True, i, j  # Valor encontrado, fila y columna
    return False, -1, -1  # Valor no encontrado

# Definir la matriz 3x3
matriz = [
    [4, 7, 1],
    [8, 3, 5],
    [9, 2, 6]
]

# Solicitar al usuario ingresar un número
try:
    valor_buscado = int(input("Ingrese un número para buscar en la matriz: "))
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
    exit()

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if encontrado:
    print(f"Valor {valor_buscado} encontrado en la posición ({fila}, {columna}).")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")