# =========================================================
# Asignación óptima de días de estudio a asignaturas
# Enfoque: PROGRAMACIÓN DINÁMICA (Problema de asignación de recursos)
# =========================================================
# Analogía formal: es una variante del problema de la Mochila
# de Elección Múltiple (Multiple-Choice Knapsack). Cada asignatura
# es un "grupo" y la cantidad de días que se le asignan (0..D)
# es la "elección" dentro de ese grupo. Se debe escoger una
# cantidad de días por asignatura de modo que la suma no supere
# el total de días disponibles y se maximice el beneficio total
# (mejora esperada de nota).
# =========================================================

import time


def beneficio(dias_asignados: int, dificultad: float) -> int:
    """
    Calcula el beneficio (puntos de mejora esperados) de asignar
    'dias_asignados' días de estudio a una asignatura con un nivel
    de 'dificultad' dado (rendimientos marginales decrecientes).
    """
    import math
    return round(20 * (1 - math.exp(-dificultad * dias_asignados)))


def construir_tabla_beneficios(n_asignaturas, dias_totales, dificultades):
    """
    Construye la matriz beneficio[i][d] = beneficio de asignar d días
    a la asignatura i, para d = 0..dias_totales
    """
    tabla = []
    for i in range(n_asignaturas):
        fila = [beneficio(d, dificultades[i]) for d in range(dias_totales + 1)]
        tabla.append(fila)
    return tabla


def asignar_dias_dp(n_asignaturas, dias_totales, tabla_beneficios):
    """
    Programación Dinámica - Asignación de días de estudio.

    dp[i][d] = máximo beneficio total usando las primeras i asignaturas
               y d días de estudio.

    Recurrencia:
        dp[0][d] = 0                                   (caso base)
        dp[i][d] = max( dp[i-1][d-k] + beneficio[i][k] )   para k = 0..d

    Complejidad temporal:  O(N * D^2)
    Complejidad espacial:  O(N * D)
    """
    dp = [[0] * (dias_totales + 1) for _ in range(n_asignaturas + 1)]
    eleccion = [[0] * (dias_totales + 1) for _ in range(n_asignaturas + 1)]

    for i in range(1, n_asignaturas + 1):
        for d in range(dias_totales + 1):
            mejor = 0
            mejor_k = 0
            for k in range(d + 1):
                candidato = dp[i - 1][d - k] + tabla_beneficios[i - 1][k]
                if candidato > mejor:
                    mejor = candidato
                    mejor_k = k
            dp[i][d] = mejor
            eleccion[i][d] = mejor_k

    # Reconstrucción de la solución (cuántos días recibió cada asignatura)
    dias_por_asignatura = [0] * n_asignaturas
    d_restante = dias_totales
    for i in range(n_asignaturas, 0, -1):
        k = eleccion[i][d_restante]
        dias_por_asignatura[i - 1] = k
        d_restante -= k

    return dp[n_asignaturas][dias_totales], dias_por_asignatura


if __name__ == "__main__":
    asignaturas = ["Cálculo", "Física", "Programación", "Bases de Datos", "Inglés"]
    dificultades = [0.35, 0.20, 0.45, 0.30, 0.55]   # más alto = aprende más rápido por día
    dias_totales = 10

    tabla = construir_tabla_beneficios(len(asignaturas), dias_totales, dificultades)

    inicio = time.perf_counter()
    beneficio_total, dias_asignados = asignar_dias_dp(len(asignaturas), dias_totales, tabla)
    fin = time.perf_counter()

    print("=== ASIGNACIÓN ÓPTIMA DE DÍAS DE ESTUDIO (Programación Dinámica) ===")
    print(f"Días disponibles totales: {dias_totales}\n")
    for nombre, dias in zip(asignaturas, dias_asignados):
        print(f"  {nombre:<15} -> {dias} día(s) de estudio")
    print(f"\nBeneficio total esperado (mejora de nota): {beneficio_total} puntos")
    print(f"Tiempo de ejecución: {(fin - inicio) * 1000:.4f} ms")
