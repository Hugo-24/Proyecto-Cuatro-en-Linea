import random

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
quien_inicia = random.choice([jugador1, jugador2])
print(f"La partida la inicia {quien_inicia}\n")

# Mostrar el tablero vacío
print(" 1234567 ")
print("+" + "-" *7 + "+")
print(("|" + "." *7 + "|\n") *6, end = "")
print("+" + "-" *7 + "+")


