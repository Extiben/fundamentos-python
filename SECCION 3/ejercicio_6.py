def resolver_ejercicio():
    print("Ejercicio 6:")
    print("Expresión: 2 + 3 * (4 - 1)\n")

    # Paso 1: Resolver el paréntesis
    parentesis = 4 - 1
    print(f"Paso 1: 4 - 1 = {parentesis}")

    # Paso 2: Multiplicación
    multiplicacion = 3 * parentesis
    print(f"Paso 2: 3 * {parentesis} = {multiplicacion}")

    # Paso 3: Suma
    resultado = 2 + multiplicacion
    print(f"Paso 3: 2 + {multiplicacion} = {resultado}")

    print(f"\n✅ Resultado final: {resultado}")


resolver_ejercicio()
