def calcular_puntaje_total():
    print("\n1. Puntaje total del jugador")
    n1 = int(input("Puntos nivel 1: "))
    n2 = int(input("Puntos nivel 2: "))
    n3 = int(input("Puntos nivel 3: "))
    print("Puntaje total:", n1 + n2 + n3)

def calcular_tiempo_total_en_segundos():
    print("\n2. Tiempo total de juego en segundos")
    h = int(input("Horas jugadas: "))
    m = int(input("Minutos jugados: "))
    s = int(input("Segundos jugados: "))
    total = h * 3600 + m * 60 + s
    print("Tiempo total en segundos:", total)

def calcular_dano_total():
    print("\n3. Daño total causado")
    a1 = int(input("Daño ataque 1: "))
    a2 = int(input("Daño ataque 2: "))
    a3 = int(input("Daño ataque 3: "))
    print("Daño total:", a1 + a2 + a3)

def calcular_experiencia_total():
    print("\n4. Experiencia total ganada")
    e1 = int(input("Exp misión 1: "))
    e2 = int(input("Exp misión 2: "))
    e3 = int(input("Exp misión 3: "))
    print("Experiencia total:", e1 + e2 + e3)

def calcular_porcentaje_vida():
    print("\n5. Porcentaje de vida restante")
    vida_max = int(input("Vida máxima: "))
    vida_actual = int(input("Vida actual: "))
    porcentaje = (vida_actual / vida_max) * 100
    print("Vida restante: {:.2f}%".format(porcentaje))

def calcular_oro_total():
    print("\n6. Oro total recolectado")
    o1 = int(input("Oro misión 1: "))
    o2 = int(input("Oro misión 2: "))
    o3 = int(input("Oro misión 3: "))
    print("Oro total:", o1 + o2 + o3)

def calcular_velocidad_promedio():
    print("\n7. Velocidad promedio")
    distancia = float(input("Distancia recorrida (km): "))
    tiempo = float(input("Tiempo (horas): "))
    velocidad = distancia / tiempo
    print("Velocidad promedio: {:.2f} km/h".format(velocidad))

def calcular_costo_mejoras():
    print("\n8. Costo total de mejoras")
    c1 = int(input("Costo mejora 1: "))
    c2 = int(input("Costo mejora 2: "))
    c3 = int(input("Costo mejora 3: "))
    print("Costo total:", c1 + c2 + c3)

def calcular_tiempo_restante():
    print("\n9. Tiempo restante de misión")
    total = int(input("Tiempo total (min): "))
    transcurrido = int(input("Tiempo transcurrido (min): "))
    restante = total - transcurrido
    print("Tiempo restante:", restante, "minutos")

def calcular_nivel_promedio():
    print("\n10. Nivel promedio del equipo")
    l1 = int(input("Nivel jugador 1: "))
    l2 = int(input("Nivel jugador 2: "))
    l3 = int(input("Nivel jugador 3: "))
    promedio = (l1 + l2 + l3) / 3
    print("Nivel promedio: {:.2f}".format(promedio))

def calcular_dano_critico():
    print("\n11. Daño crítico")
    base = int(input("Daño base: "))
    crit = float(input("Multiplicador crítico: "))
    total = base * crit
    print("Daño crítico:", total)

def calcular_tiempo_horas_minutos():
    print("\n12. Tiempo total en horas y minutos")
    total_min = int(input("Minutos totales: "))
    horas = total_min // 60
    minutos = total_min % 60
    print(f"Tiempo total: {horas} horas y {minutos} minutos")

def calcular_porcentaje_misiones():
    print("\n13. Porcentaje de misiones completadas")
    total = int(input("Total de misiones: "))
    completadas = int(input("Misiones completadas: "))
    porcentaje = (completadas / total) * 100
    print("Porcentaje completado: {:.2f}%".format(porcentaje))

def calcular_costo_total_objetos():
    print("\n14. Costo total de objetos comprados")
    o1 = int(input("Costo objeto 1: "))
    o2 = int(input("Costo objeto 2: "))
    o3 = int(input("Costo objeto 3: "))
    print("Costo total:", o1 + o2 + o3)

def calcular_tiempo_promedio_partida():
    print("\n15. Tiempo promedio de partida")
    t1 = int(input("Duración partida 1 (min): "))
    t2 = int(input("Duración partida 2 (min): "))
    t3 = int(input("Duración partida 3 (min): "))
    promedio = (t1 + t2 + t3) / 3
    print("Tiempo promedio: {:.2f} minutos".format(promedio))

def calcular_porcentaje_enemigos_derrotados():
    print("\n16. Porcentaje de enemigos derrotados")
    total = int(input("Total enemigos: "))
    derrotados = int(input("Enemigos derrotados: "))
    porcentaje = (derrotados / total) * 100
    print("Porcentaje derrotados: {:.2f}%".format(porcentaje))


# Ejecutar todos los ejercicios
if __name__ == "__main__":
    calcular_puntaje_total()
    calcular_tiempo_total_en_segundos()
    calcular_dano_total()
    calcular_experiencia_total()
    calcular_porcentaje_vida()
    calcular_oro_total()
    calcular_velocidad_promedio()
    calcular_costo_mejoras()
    calcular_tiempo_restante()
    calcular_nivel_promedio()
    calcular_dano_critico()
    calcular_tiempo_horas_minutos()
    calcular_porcentaje_misiones()
    calcular_costo_total_objetos()
    calcular_tiempo_promedio_partida()
    calcular_porcentaje_enemigos_derrotados()
