Algoritmo AsignacionDiasEstudio_ProgramacionDinamica
	Definir N, Dias, i, d, k, mejor, mejorK, dRestante Como Entero
	Definir beneficioTotal Como Entero
	Dimension dificultad[10]
	Dimension beneficio[10,50]
	Dimension dp[11,51]
	Dimension eleccion[11,51]
	Dimension diasAsignados[10]
	Dimension nombreAsignatura[10]
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
	// --- Construccion de la tabla de beneficios (rendimientos decrecientes) ---
	Para i <- 1 Hasta N Hacer
		Para d <- 0 Hasta Dias Hacer
			beneficio[i,d] <- Trunc(20 * (1 - Exp(-dificultad[i] * d)) + 0.5)
		FinPara
	FinPara
	// --- Inicializacion de la tabla de Programacion Dinamica ---
	Para i <- 0 Hasta N Hacer
		Para d <- 0 Hasta Dias Hacer
			dp[i,d] <- 0
			eleccion[i,d] <- 0
		FinPara
	FinPara
	// --- Llenado de la tabla DP ---
	// dp[i,d] = maximo beneficio usando las primeras i asignaturas y d dias
	Para i <- 1 Hasta N Hacer
		Para d <- 0 Hasta Dias Hacer
			mejor <- 0
			mejorK <- 0
			Para k <- 0 Hasta d Hacer
				Si (dp[i-1, d-k] + beneficio[i,k]) > mejor Entonces
					mejor <- dp[i-1, d-k] + beneficio[i,k]
					mejorK <- k
				FinSi
			FinPara
			dp[i,d] <- mejor
			eleccion[i,d] <- mejorK
		FinPara
	FinPara
	beneficioTotal <- dp[N,Dias]
	// --- Reconstruccion de la solucion optima ---
	dRestante <- Dias
	Para i <- N Hasta 1 Con Paso -1 Hacer
		diasAsignados[i] <- eleccion[i, dRestante]
		dRestante <- dRestante - diasAsignados[i]
	FinPara
	Escribir ""
	Escribir "=== ASIGNACION OPTIMA DE DIAS DE ESTUDIO (Programacion Dinamica) ==="
	Para i <- 1 Hasta N Hacer
		Escribir nombreAsignatura[i], " -> ", diasAsignados[i], " dia(s) de estudio"
	FinPara
	Escribir "Beneficio total esperado (mejora de nota): ", beneficioTotal, " puntos"
FinAlgoritmo