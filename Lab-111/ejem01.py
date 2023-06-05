def division_por_restas(dividendo, divisor):
    cociente = 0

    # Si el divisor es cero, no se puede realizar la división
    if divisor == 0:
        return "Error: No se puede dividir por cero."

    # Realizar restas sucesivas hasta que el dividendo sea menor que el divisor
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    # Devolver el cociente como resultado de la división
    return cociente

# Pedir al usuario que ingrese los números
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

# Realizar la división utilizando restas
resultado = division_por_restas(dividendo, divisor)

# Mostrar el resultado
print("El resultado de la división es:", resultado)
