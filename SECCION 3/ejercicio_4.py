def resolver_ejercicio():
    print("Ejercicio 4:")
    print("Expresión: 10 - 4 + 2 * 3\n")

    # Paso 1: Multiplicación primero
    paso1 = 2 * 3
    print(f"Paso 1: 2 * 3 = {paso1}")

    # Paso 2: Sustituir el resultado en la expresión
    print(f"Paso 2: 10 - 4 + {paso1}")

    # Paso 3: Resolver de izquierda a derecha (suma/resta)
    paso2 = 10 - 4
    print(f"Paso 3: 10 - 4 = {paso2}")
    resultado = paso2 + paso1
    print(f"Paso 4: {paso2} + {paso1} = {resultado}")

    print(f"\n✅ Resultado final: {resultado}")


resolver_ejercicio()
