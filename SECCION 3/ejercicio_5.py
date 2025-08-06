def resolver_ejercicio():
    print("Ejercicio 5:")
    print("Expresión: (10 / 2) * (3 + 2) - 4\n")

    # Paso 1: Resolver los paréntesis
    paso1_a = 10 / 2
    paso1_b = 3 + 2
    print(f"Paso 1: 10 / 2 = {paso1_a}")
    print(f"Paso 2: 3 + 2 = {paso1_b}")

    # Paso 2: Sustituir en la expresión
    print(f"Paso 3: {paso1_a} * {paso1_b} - 4")

    # Paso 3: Multiplicación
    paso2 = paso1_a * paso1_b
    print(f"Paso 4: {paso1_a} * {paso1_b} = {paso2}")

    # Paso 4: Resta
    resultado = paso2 - 4
    print(f"Paso 5: {paso2} - 4 = {resultado}")

    print(f"\n✅ Resultado final: {resultado}")


resolver_ejercicio()
