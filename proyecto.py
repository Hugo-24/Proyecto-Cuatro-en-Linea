import random
from datetime import datetime  # Para guardar fecha y hora de las partidas

# Función para imprimir el tablero actual
def imprimir_tablero(): 
    print(" 1234567 ")
    print("+-------+")
    print("|" + fila1 + "|")
    print("|" + fila2 + "|")
    print("|" + fila3 + "|")
    print("|" + fila4 + "|")
    print("|" + fila5 + "|")
    print("|" + fila6 + "|")
    print("+-------+")

# Función para insertar una ficha en la fila indicada
def poner_ficha(fila, columna, ficha):
    col = int(columna) - 1
    nueva_fila = ""
    for i in range(7):
        if i == col:
            nueva_fila += ficha
        else:
            nueva_fila += fila[i]
    return (nueva_fila)

# Función que actualiza el tablero colocando la ficha en la primera fila libre
def actualizar_tablero(columna, ficha):
    global fila1, fila2, fila3, fila4, fila5, fila6
    col = int(columna) - 1
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

# Función para verificar si hay 4 fichas consecutivas en línea
def hay_ganador():
    tablero = [fila1, fila2, fila3, fila4, fila5, fila6]

    # Horizontal
    for fila in tablero:
        for col in range(4):
            segmento = fila[col:col+4]
            if segmento == "XXXX" or segmento == "OOOO":
                return segmento[0]

    # Vertical
    for col in range(7):
        for fila in range(3):
            f1 = tablero[fila][col]
            f2 = tablero[fila+1][col]
            f3 = tablero[fila+2][col]
            f4 = tablero[fila+3][col]
            if f1 == f2 == f3 == f4 and f1 in "XO":
                return f1

    # Diagonal ↘
    for fila in range(3):
        for col in range(4):
            f1 = tablero[fila][col]
            f2 = tablero[fila+1][col+1]
            f3 = tablero[fila+2][col+2]
            f4 = tablero[fila+3][col+3]
            if f1 == f2 == f3 == f4 and f1 in "XO":
                return f1

    # Diagonal ↙
    for fila in range(3):
        for col in range(3, 7):
            f1 = tablero[fila][col]
            f2 = tablero[fila+1][col-1]
            f3 = tablero[fila+2][col-2]
            f4 = tablero[fila+3][col-3]
            if f1 == f2 == f3 == f4 and f1 in "XO":
                return f1

    return None

# Función para guardar el puntaje del jugador
def guardar_puntaje(nombre, puntos):
    nombre = nombre.strip()
    puntajes = {}

    try:
        with open("puntajes.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 3:
                    n, p, fecha = partes
                    puntajes[n] = (int(p), fecha)
    except FileNotFoundError:
        pass

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
    if nombre in puntajes:
        puntos_totales = puntajes[nombre][0] + puntos
    else:
        puntos_totales = puntos
    puntajes[nombre] = (puntos_totales, ahora)

    with open("puntajes.txt", "w") as archivo:
        for n, (p, fecha) in puntajes.items():
            archivo.write(f"{n}|{p}|{fecha}\n")

# Función para mostrar los 5 mejores puntajes
def mostrar_top5():
    print("\n*** TABLA DE POSICIONES ***")
    try:
        with open("puntajes.txt", "r") as archivo:
            registros = []
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 3:
                    nombre, puntos, fecha = partes
                    registros.append((int(puntos), nombre, fecha))

            registros.sort(reverse=True)

            for i, (puntos, nombre, fecha) in enumerate(registros[:5], start=1):
                print(f"{i}. {nombre} - {puntos} puntos acumulados. Última partida en {fecha}")
    except FileNotFoundError:
        print("No hay puntajes registrados aún.")

# Variable de control para repetir el juego
seguir_jugando = True

while seguir_jugando == True:
    print("*** CUATRO SEGUIDAS ***\n")
    print("\nBienvenidos al juego de CUATRO SEGUIDAS\n")

    jugador1 = input("Por favor indique nombre de participante #1: ")
    ficha1 = ""
    while ficha1 not in ["X", "O"]:
        ficha1 = input(f"\n{jugador1}, por favor indica con qué ficha deseas jugar [X] o [O]: ") 

    jugador2 = jugador1
    while jugador2 == jugador1: 
        jugador2 = input("\nPor favor indique nombre de participante #2: ")

    ficha2 = "O" if ficha1 == "X" else "X"
    print(f"\n{jugador2}, te toca jugar con la siguiente ficha: {ficha2}\n") 

    print("Lanzando una moneda al aire para determinar quién inicia la partida...\n")
    quien_inicia = random.choice([jugador1, jugador2]) 
    print(f"La partida la inicia {quien_inicia}\n")

    fila1 = "......."
    fila2 = "......."
    fila3 = "......."
    fila4 = "......."
    fila5 = "......."
    fila6 = "......."

    imprimir_tablero() 

    turno_actual = quien_inicia
    ficha_actual = ficha1 if turno_actual == jugador1 else ficha2
    contador_fichas = 0
    fichas_max = 42

    # Rastrear si alguien usó suerte y cuántas veces
    jugador1_usó_s = False
    jugador2_usó_s = False
    jugador1_usó_solo_s = True
    jugador2_usó_solo_s = True

    while contador_fichas < fichas_max:
        columna = ""
        columna_original = ""
        while columna not in ["1", "2", "3", "4", "5", "6", "7"]:
            columna = input(f"\n{turno_actual}, indica un numero de columna o pulsa [S] para tentar a la suerte: ")
            if columna == "S":
                columna_original = "S"
                columna = str(random.randint(1, 7))
                print(f"\nSe eligió aleatoriamente la columna {columna} para tu ficha\n")
                if turno_actual == jugador1:
                    jugador1_usó_s = True
                else:
                    jugador2_usó_s = True
            elif columna in ["1", "2", "3", "4", "5", "6", "7"]:
                columna_original = columna
                if turno_actual == jugador1:
                    jugador1_usó_solo_s = False
                else:
                    jugador2_usó_solo_s = False
            else:
                print("Columna no válida.")

        if actualizar_tablero(columna, ficha_actual):
            contador_fichas += 1
            imprimir_tablero()
            print(f"\nSe ha puesto la ficha {ficha_actual} en la columna {columna}. Fichas jugadas: {contador_fichas}")

            ganador = hay_ganador()
            if ganador:
                jugador_ganador = jugador1 if ganador == ficha1 else jugador2

                # Calcular puntaje
                puntaje_base = 100
                penalizacion = contador_fichas * 2
                puntaje = puntaje_base - penalizacion

                # Bonos por suerte
                if jugador_ganador == jugador1:
                    if jugador1_usó_solo_s:
                        puntaje += 30
                    elif jugador1_usó_s:
                        puntaje += 10
                else:
                    if jugador2_usó_solo_s:
                        puntaje += 30
                    elif jugador2_usó_s:
                        puntaje += 10

                if puntaje < 25:
                    puntaje = 25

                print(f"\n¡Felicidades, {jugador_ganador}, has ganado la partida!")
                print(f"Has sumado {puntaje} puntos en esta partida\n")
                guardar_puntaje(jugador_ganador, puntaje)
                break
        else:
            print("Intenta de nuevo con otra columna.")
            continue

        turno_actual = jugador2 if turno_actual == jugador1 else jugador1
        ficha_actual = ficha2 if ficha_actual == ficha1 else ficha1

    if not hay_ganador():
        print("\nEl tablero está lleno. ¡Nadie ganó esta vez!")

    mostrar_top5()

    respuesta = ""
    while respuesta not in ["S", "N"]:
        respuesta = input("\n¿Desean jugar otra vez? [S/N]: ")
    if respuesta == "N":
        seguir_jugando = False
        print("¡Gracias por jugar!")