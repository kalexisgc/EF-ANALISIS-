Algoritmo AsignacionDiasEstudio_FuerzaBruta
	Definir N, Dias, i, d, mejorBeneficio, totalCombinaciones Como Entero
	Dimension dificultad[10]
	Dimension beneficio[10,50]
	Dimension nombreAsignatura[10]
	Dimension combinacionActual[10]
	Dimension mejorCombinacion[10]
	Escribir "Ingrese el numero de asignaturas:"
	Leer N
	Escribir "Ingrese el total de dias disponibles para estudiar:"
	Leer Dias
	Para i <- 1 Hasta N Hacer
		Escribir "Nombre de la asignatura ", i, ":"
		Leer nombreAsignatura[i]
		Escribir "Dificultad de aprendizaje (0.1 a 0.9) de la asignatura ", i, ":"
		Leer dificultad[i]
	FinPara
	Para i <- 1 Hasta N Hacer
		Para d <- 0 Hasta Dias Hacer
			beneficio[i,d] <- Trunc(20 * (1 - Exp(-dificultad[i] * d)) + 0.5)
		FinPara
	FinPara
	mejorBeneficio <- -1
	totalCombinaciones <- 0

	GenerarYEvaluar(1, Dias, N, beneficio, combinacionActual, mejorCombinacion, mejorBeneficio, totalCombinaciones)
	Escribir ""
	Escribir "=== ASIGNACION OPTIMA DE DIAS DE ESTUDIO (Fuerza Bruta) ==="
	Escribir "Combinaciones evaluadas: ", totalCombinaciones
	Para i <- 1 Hasta N Hacer
		Escribir nombreAsignatura[i], " -> ", mejorCombinacion[i], " dia(s) de estudio"
	FinPara
	Escribir "Beneficio total esperado (mejora de nota): ", mejorBeneficio, " puntos"
FinAlgoritmo

SubProceso GenerarYEvaluar(asignaturaActual, diasRestantes, N, beneficio, combinacionActual, mejorCombinacion Por Referencia, mejorBeneficio Por Referencia, totalCombinaciones Por Referencia)
	Definir dias, j, beneficioActual Como Entero
	Si asignaturaActual > N Entonces
		Si diasRestantes = 0 Entonces
			totalCombinaciones <- totalCombinaciones + 1
			beneficioActual <- 0
			Para j <- 1 Hasta N Hacer
				beneficioActual <- beneficioActual + beneficio[j, combinacionActual[j]]
			FinPara
			Si beneficioActual > mejorBeneficio Entonces
				mejorBeneficio <- beneficioActual
				Para j <- 1 Hasta N Hacer
					mejorCombinacion[j] <- combinacionActual[j]
				FinPara
			FinSi
		FinSi
	SiNo
		Para dias <- 0 Hasta diasRestantes Hacer
			combinacionActual[asignaturaActual] <- dias
			GenerarYEvaluar(asignaturaActual + 1, diasRestantes - dias, N, beneficio, combinacionActual, mejorCombinacion, mejorBeneficio, totalCombinaciones)
		FinPara
	FinSi
FinSubProceso