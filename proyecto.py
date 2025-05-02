import random

# Función para imprimir el ejemplo del juego
def imprimir_tablero(): 
    print(   " 1234567 "    )
    print(   "+-------+"    )
    print("|" + fila1 + "|")
    print("|" + fila2 + "|")
    print("|" + fila3 + "|")
    print("|" + fila4 + "|")
    print("|" + fila5 + "|")
    print("|" + fila6 + "|")
    print(   "+-------+"    )

# Función para poner una ficha en la fila correspondiente.
def poner_ficha(fila, columna, ficha):
    col = int(columna) - 1
    nueva_fila = ""
    for i in range(7):
        if i == col:
            nueva_fila += ficha
        else:
            nueva_fila += fila[i]
    return (nueva_fila)

# Función para encontrar la primera fila disponible en una columna (de abajo hacia arriba)
def actualizar_tablero(columna, ficha):
    global fila1, fila2, fila3, fila4, fila5, fila6  # Necesario para modificar variables globales
    col = int(columna) - 1  # Convertir columna a índice (0-6)
    # Revisar desde la fila de abajo hacia arriba
    if fila6[col] == ".":
        fila6 = poner_ficha(fila6, columna, ficha)
        return True
    elif fila5[col] == ".":
        fila5 = poner_ficha(fila5, columna, ficha)
        return True
    elif fila4[col] == ".":
        fila4 = poner_ficha(fila4, columna, ficha)
        return True
    elif fila3[col] == ".":
        fila3 = poner_ficha(fila3, columna, ficha)
        return True
    elif fila2[col] == ".":
        fila2 = poner_ficha(fila2, columna, ficha)
        return True
    elif fila1[col] == ".":
        fila1 = poner_ficha(fila1, columna, ficha)
        return True
    else:
        print("La columna está llena. No se puede poner ficha.")
        return False
    
# Variable de control para repetir el juego
seguir_jugando = True

while seguir_jugando == True:
    # Inicializar el juego
    print("*** CUATRO SEGUIDAS ***\n")
    print("\nBienvenidos al juego de CUATRO SEGUIDAS\n")
    print("El juego consiste en colocar cuatro fichas en línea, ya sea horizontal, vertical o diagonal.\n")            

    # Pedir nombres de los jugadores
    jugador1 = input("Por favor indique nombre de participante #1: ")
    ficha1 = ""

    while ficha1 not in ["X", "O"]:  # Validar la ficha elegida.
        ficha1 = input(f"\n{jugador1}, por favor indica con qué ficha deseas jugar [X] o [O]: ") 
        if ficha1 not in ["X", "O"]:
            print("Ficha no válida. Por favor elige 'X' o 'O'.")

    # Pedir nombre del jugador 2
    # Validar que el nombre no sea el mismo
    jugador2 = jugador1
    while jugador2 == jugador1: 
        jugador2 = input("\nPor favor indique nombre de participante #2: ")
        if jugador2 == jugador1:
            print("El nombre del segundo jugador no puede ser el mismo que el del primero. Por favor, elige otro nombre.") 

    # Asignar automáticamente la otra ficha
    if ficha1 == "X":
        ficha2 = "O"
    else:
        ficha2 = "X"

    # Mostrar las fichas elegidas
    print(f"\n{jugador2}, te toca jugar con la siguiente ficha: {ficha2}\n") 

    # Sorteo de quién inicia la partida
    print("Lanzando una moneda al aire para determinar quién inicia la partida...\n")
    quien_inicia = random.choice([jugador1, jugador2]) 
    print(f"La partida la inicia {quien_inicia}\n")

    # Crear filas del tablero como strings
    fila1 = "......."
    fila2 = "......."
    fila3 = "......."
    fila4 = "......."
    fila5 = "......."
    fila6 = "......."

    # Mostrar el tablero vacío
    imprimir_tablero() 

    # Ver el turno actual
    turno_actual = quien_inicia
    if quien_inicia == jugador1:
        ficha_actual = ficha1  
    else: 
        ficha_actual = ficha2
    contador_fichas = 0
    fichas_max = 42  # 6 filas * 7 columnas

    # Comienza la partida y el conteo de los turnos
    while contador_fichas < fichas_max:
        columna = ""
        while columna not in ["1", "2", "3", "4", "5", "6", "7", "S"]:
            columna = input(f"\n{turno_actual}, indica un numero de columna o pulsa [S] para tentar a la suerte: ")
            if columna == "S":
                columna = str(random.randint(1, 7)) 
                print(f"\nSe eligió aleatoriamente la columna {columna} para tu ficha\n")
            if columna not in ["1", "2", "3", "4", "5", "6", "7", "S"]:
                print("Columna no válida. Por favor elige un número entre 1 y 7 o 'S' para elegir aleatoriamente.")

        # Lógica para insertar la ficha en el tablero real
        if actualizar_tablero(columna, ficha_actual):
            contador_fichas += 1
            imprimir_tablero()
            print(f"\nSe ha puesto la ficha {ficha_actual} en la columna {columna}. Fichas jugadas: {contador_fichas}")
        else:
            print("Intenta de nuevo con otra columna.")
            continue  # Repite el turno si no pudo poner ficha

        # Cambiar turno
        if (turno_actual == jugador1):
            turno_actual = jugador2
            ficha_actual = ficha2
        else:
            turno_actual = jugador1
            ficha_actual = ficha1

    # Cuando se llena el tablero y nadie gana
    print("\nEl tablero está lleno. ¡Nadie ganó esta vez!")

    # Mostrar tabla de posiciones (por ahora fija)
    print("\n*** TABLA DE POSICIONES ***")
    print("1. Andrea - 110 puntos acumulados. Última partida en 2022-08-16 a las 13:50")
    print("2. Camilo - 80 puntos acumulados. Última partida en 2021-02-25 a las 10:15")
    print("3. Tatiana - 75 puntos acumulados. Última partida en 2022-08-16 a las 13:50")
    print("4. Juana - 70 puntos acumulados. Última partida en 2022-05-10 a las 14:00")
    print("5. Johana - 60 puntos acumulados. Última partida en 2022-05-11 a las 14:00")

    # Preguntar si desean jugar otra vez
    respuesta = ""
    while respuesta not in ["S", "N"]:
        respuesta = input("\n¿Desean jugar otra vez? [S/N]: ")
        if respuesta not in ["S", "N"]:
            print("Respuesta no válida. Por favor elige 'S' para sí o 'N' para no.")
    if respuesta == "N":
        seguir_jugando = False
        print("¡Gracias por jugar!")