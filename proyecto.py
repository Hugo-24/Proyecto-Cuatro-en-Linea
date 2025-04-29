import random
# Función para imprimir el ejemplo del juego
def imprimir_ejemplo(): #Todavia no tengo lista la funcion, es intentando entender lo que debo entregar
    print(" 1234567 ")
    print("+" + "-" *7 + "+")
    print(("|" + "." *7 + "|\n") *6, end = "")
    print("+" + "-" *7 + "+")

# Inicializar el juego
print("\n")
print("*** CUATRO SEGUIDAS ***\n")
print("Bienvenidos al juego de CUATRO SEGUIDAS\n")
print("El juego consiste en colocar cuatro fichas en línea, ya sea horizontal, vertical o diagonal.\n")            

# Pedir nombres de los jugadores
jugador1 = input("Por favor indique nombre de participante #1: ")
ficha1 = ""

while ficha1 not in ["X", "O"]:  # Validar la ficha elegida.
    ficha1 = input(f"\n{jugador1}, por favor indica con qué ficha deseas jugar [X] o [O]: ")
    if ficha1 not in ["X", "O"]:
        print("Ficha no válida. Por favor elige 'X' o 'O'.")

# Pedir nombre del jugador 2
jugador2 = input("\nPor favor indique nombre de participante #2: ")

# Asignar automáticamente la otra ficha
if ficha1 == "X":
    ficha2 = "O"
else:
    ficha2 = "X"

# Mostrar las fichas elegidas
print(f"\n{jugador2}, te toca jugar con la siguiente ficha: {ficha2}\n")

# Sorteo de quién inicia la partida
print("Lanzando una moneda al aire para determinar quién inicia la partida...\n")
quien_inicia = random.choice([jugador1, jugador2]) #random.choice(lista): elige aleatoriamente un elemento de una lista.
print(f"La partida la inicia {quien_inicia}\n")

# Mostrar el tablero vacío
print(" 1234567 ")
print("+" + "-" *7 + "+")
print(("|" + "." *7 + "|\n") *6, end = "")
print("+" + "-" *7 + "+")
#Ver el turno actual
turno_actual = quien_inicia
ficha_actual = ficha1 if quien_inicia == jugador1 else ficha2

# Pedir columna para poner ficha
columna = ""
while columna not in ["1", "2", "3", "4", "5", "6", "7", "S"]:
    columna = input(f"\n{turno_actual}, indica un número de columna o pulsa [S] para tentar a la suerte: ")
    
    if columna == "S":
        columna = str(random.randint(1, 7)) #random.randint(a, b): genera un número entero aleatorio entre 'a' y 'b' incluidos.
        print(f"\nSuerte con eso, se eligió aleatoriamente la columna {columna} para tu ficha\n")

# Intento pa ver ejemplo
ejemplo = ""    
while ejemplo not in ["Y", "N"]:
    ejemplo = input("¿Deseas ver el ejemplo brindado para el proyecto? Ingresa 'Y' para sí o 'N' para no: ")
    if ejemplo == "Y":
        imprimir_ejemplo()
    elif ejemplo == "N":
        print("\nHas elegido no mostrar el ejemplo.\n")
    else:
        print("\nOpción no válida. Continuando sin mostrar el ejemplo.\n")