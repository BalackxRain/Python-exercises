def busqueda_binaria(vector, elemento):
    inicio = 0
    fin = len(vector) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if vector[medio] == elemento:
            return medio
        elif vector[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Ejemplo de uso
vector = [1, 2, 3, 5, 8]
elemento = 9

# Realizar la búsqueda binaria en el vector
resultado = busqueda_binaria(vector, elemento)

if resultado != -1:
    print("El elemento", elemento, "se encuentra en el índice", resultado)
else:
    print("El elemento", elemento, "no se encontró en el vector.")
