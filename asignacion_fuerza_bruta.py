# =========================================================
# Asignación óptima de días de estudio a asignaturas
# Enfoque: FUERZA BRUTA
# =========================================================
# Se generan TODAS las combinaciones posibles de repartir
# 'dias_totales' días entre 'n_asignaturas' (composiciones de un
# entero en n partes, con repetición) y se evalúa el beneficio de
# cada una para quedarse con la mejor.
# Número de combinaciones posibles: C(D + N - 1, N - 1)
# Complejidad temporal: EXPONENCIAL  ->  O(D^N) en el peor caso
# =========================================================

import time
from asignacion_dp import beneficio, construir_tabla_beneficios


def generar_combinaciones(n_asignaturas, dias_totales):
    """
    Genera recursivamente todas las formas de repartir 'dias_totales'
    días entre 'n_asignaturas' asignaturas (fuerza bruta pura).
    """
    if n_asignaturas == 1:
        return [[dias_totales]]

    combinaciones = []
    for dias_para_primera in range(dias_totales + 1):
        sub_combinaciones = generar_combinaciones(
            n_asignaturas - 1, dias_totales - dias_para_primera
        )
        for sub in sub_combinaciones:
            combinaciones.append([dias_para_primera] + sub)
    return combinaciones


def asignar_dias_fuerza_bruta(n_asignaturas, dias_totales, tabla_beneficios):
    """
    Fuerza bruta: evalúa TODAS las combinaciones posibles de asignación
    de días y se queda con la de mayor beneficio total.
    """
    mejor_beneficio = -1
    mejor_combinacion = None

    todas_combinaciones = generar_combinaciones(n_asignaturas, dias_totales)

    for combinacion in todas_combinaciones:
        beneficio_total = sum(
            tabla_beneficios[i][combinacion[i]] for i in range(n_asignaturas)
        )
        if beneficio_total > mejor_beneficio:
            mejor_beneficio = beneficio_total
            mejor_combinacion = combinacion

    return mejor_beneficio, mejor_combinacion, len(todas_combinaciones)


if __name__ == "__main__":
    asignaturas = ["Cálculo", "Física", "Programación", "Bases de Datos", "Inglés"]
    dificultades = [0.35, 0.20, 0.45, 0.30, 0.55]
    dias_totales = 10

    tabla = construir_tabla_beneficios(len(asignaturas), dias_totales, dificultades)

    inicio = time.perf_counter()
    beneficio_total, dias_asignados, n_combinaciones = asignar_dias_fuerza_bruta(
        len(asignaturas), dias_totales, tabla
    )
    fin = time.perf_counter()

    print("=== ASIGNACIÓN ÓPTIMA DE DÍAS DE ESTUDIO (Fuerza Bruta) ===")
    print(f"Días disponibles totales: {dias_totales}")
    print(f"Combinaciones evaluadas: {n_combinaciones}\n")
    for nombre, dias in zip(asignaturas, dias_asignados):
        print(f"  {nombre:<15} -> {dias} día(s) de estudio")
    print(f"\nBeneficio total esperado (mejora de nota): {beneficio_total} puntos")
    print(f"Tiempo de ejecución: {(fin - inicio) * 1000:.4f} ms")
