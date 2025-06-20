import random
#Puntaje base: 100 puntos al ganar una partida.
#Penalización por número de jugadas: entre más fichas uses, menos puntos ganas.
#   Se descuentan 2 puntos por cada ficha jugada por el ganador.
#Bonus por usar solo suerte ("S"):
#    Si todas las jugadas del ganador fueron con suerte, +30 puntos.
#    Si usó suerte al menos una vez, +10 puntos.
#Puntaje mínimo garantizado: mínimo 25 puntos por ganar, aunque haya muchas penalizaciones.

#Este codigo es para explicar el funcionamiento de algunas herramientas o funciones de python utilizadas en el codigo del juego de cuatro seguidas.

# --- Explicación del Generador de Números Pseudoaleatorios (PRNG) ---
# La librería 'random' no genera números "verdaderamente" aleatorios a partir de
# fenómenos físicos impredecibles. En su lugar, utiliza un algoritmo determinista
# llamado Generador de Números Pseudoaleatorios (PRNG).
# Funcionamiento básico:
# 1. Semilla (Seed): El PRNG comienza con un valor inicial llamado "semilla".
#    Si no se especifica una semilla, Python utiliza una fuente dependiente del
#    sistema (como la hora actual) para inicializarlo.
#Obtención del tiempo: Python llama a funciones del sistema operativo que le dan una representación numérica del momento actual 
#(Por ejemplo, el número de segundos transcurridos desde una fecha de inicio). Este valor cambia constantemente con el paso del tiempo.
#Uso como semilla: Este valor numérico del tiempo se utiliza como la semilla inicial para el algoritmo del PRNG.
# 2. Algoritmo determinista: A partir de la semilla, el algoritmo aplica una
#    serie de operaciones matemáticas para generar el siguiente número en la
#    secuencia. Cada número generado depende del número anterior.
# 3. Secuencia pseudoaleatoria: La secuencia de números producida por el PRNG
#    parece aleatoria y pasa muchas pruebas estadísticas de aleatoriedad. Sin
#    embargo, debido a su naturaleza determinista, si se utiliza la misma semilla,
#    se generará exactamente la misma secuencia de números.

# --- Funcionamiento de random.randint(a, b) ---
# Genera un número entero aleatorio dentro del rango inclusivo [a, b].
# Internamente, podría funcionar así:
# 1. Obtiene un número decimal aleatorio 'x' a partir de la semilla.
# 2. Calcula el tamaño del rango: (b - a + 1).
# 3. Escala 'x' al rango.
# 4. Desplaza el resultado sumándole el límite inferior.
# 5. Toma la parte entera (piso) del resultado para obtener el entero aleatorio.
# Ejemplo:
dado = random.randint(1, 6)  # Simula lanzar un dado de 6 caras
print(f"Resultado del dado: {dado}")
numero_entre_10_y_20 = random.randint(10, 20)
print(f"Número aleatorio entre 10 y 20: {numero_entre_10_y_20}")

# --- Funcionamiento de random.choice(secuencia) ---
# Selecciona un elemento al azar de una secuencia no vacía (lista, tupla, cadena, etc.).
# Internamente:
# 1. Verifica que la secuencia proporcionada no esté vacía. Si lo está, lanza un IndexError.
# 2. Determina la longitud de la secuencia.
# 3. Genera un índice entero aleatorio que esté dentro del rango de índices válidos
#    de la secuencia (desde 0 hasta longitud - 1).
# 4. Accede al elemento de la secuencia utilizando el índice aleatorio generado.
# 5. Devuelve el elemento seleccionado.
# Ejemplo:
colores = ["rojo", "azul", "verde"]
color_elegido = random.choice(colores)
print(f"Color elegido al azar: {color_elegido}")

# --- Funcionamiento del print(f"...") (f-strings o string literales formateados) ---
# Los f-strings (introducidos en Python 3.6) son una forma concisa y legible de
# insertar expresiones Python dentro de cadenas de texto para su formateo.
# Comienzan con una 'f' antes de la comilla inicial de la cadena.
# Internamente, cuando Python encuentra un f-string:
# 1. **Analiza** la cadena, identificando texto estático y expresiones entre llaves `{}`.
# 2. **Evalúa** cada expresión dentro de las llaves en el contexto actual del programa.
# 3. **Convierte a cadena** el resultado de cada expresión (usando str()).
# 4. **Formatea** opcionalmente el valor si se especifica un formato después de dos puntos
#    dentro de las llaves (ej: {:.2f}).
# 5. **Combina** todas las partes para formar la cadena final.
# Sintaxis básica:
# print(f"Texto fijo {variable} más texto {expresión}")

# --- Funcionamiento del for ---
# El ciclo 'for' en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena de texto o rango de números) 
# y ejecutar un bloque de código para cada elemento de esa secuencia.
# La función poner_ficha recorre la fila con un ciclo for
# El for i in range(7) significa: "haz esto para cada posición de 0 a 6"
# En cada posición, si es igual a la columna elegida, pone la ficha (X u O)
# Si no, copia el mismo carácter que ya estaba en la fila
# Así se construye una nueva fila con la ficha puesta en la posición correcta
#Ejemplos:
# 1 Iterar sobre una lista.
# Itera sobre cada elemento de la lista
lista = [1, 2, 3, 4]
for elemento in lista:
    print(elemento)
# 2 Usar un rango de números con range()
# Itera desde 0 hasta 4 (range(5) genera los números: 0, 1, 2, 3, 4)
for i in range(5):
    print(i)
# 3 También puedes especificar un inicio, un fin y un paso:
# Itera desde 2 hasta 8 con un paso de 2 (el limite superior es excluyente)
for i in range(2, 9, 2):
    print(i)
# 4 Iterar sobre una cadena de texto
# Itera sobre cada carácter de la cadena
texto = "hola"
for letra in texto:
    print(letra)
# 5 Iterar sobre un diccionario
# 5.1 Itera sobre las claves del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in diccionario:
    print(clave)  # Imprime las claves: 'a', 'b', 'c'
# 5.2 Itera sobre los valores del diccionario
for valor in diccionario.values():
    print(valor)  # Imprime los valores: 1, 2, 3
# 5.3 Itera sobre las claves y valores del diccionario
for clave, valor in diccionario.items():
    print(clave, valor)  # Imprime las parejas clave-valor: ('a', 1), ('b', 2), ('c', 3)

# --- Operadores de asignacion ----
# 'nueva_fila = nueva_fila + ficha' crea una nueva lista que contiene los elementos de 'nueva_fila' y 'ficha',
# y reasigna 'nueva_fila' a esta nueva lista. Es menos eficiente porque se crea una nueva lista en memoria.
# nueva_fila = nueva_fila + ficha
# 'nueva_fila += ficha' agrega los elementos de 'ficha' directamente a la lista 'nueva_fila', modificando la lista 
# original en lugar de crear una nueva. Es más eficiente porque no se crea una nueva lista, solo se modifica la existente.
# nueva_fila += ficha
# Cuando usas '+' en lugar de '+=', aunque estés usando el mismo identificador (por ejemplo, 'nueva_fila'),
# lo que realmente ocurre es que se crea una nueva lista con los elementos combinados,
# y esa nueva lista se asigna al mismo identificador.

# --- Variables locales y globales ---
# En Python, una variable puede ser "local" o "global", dependiendo de dónde y cómo se define.
# VARIABLE GLOBAL:
# Es una variable que se define fuera de cualquier función.
# Está disponible para todo el programa y puede ser usada por cualquier función.
# Si una función necesita *modificar* una variable global, se debe usar la palabra clave 'global'.
# Ejemplo:
x = 5  # variable global
def cambiar_valor_global():
    global x  # Indica que se va a usar la variable global 'x'
    x = 10
cambiar_valor_global()
print(x)  # Imprime 10
# VARIABLE LOCAL:
# Es una variable que se define *dentro* de una función.
# Solo puede ser usada dentro de esa función.
# No existe fuera de la función, ni otras funciones pueden acceder a ella directamente.
# Ejemplo:
def ejemplo_local():
    y = 3  # variable local
    print(y)  # Solo existe dentro de esta función
ejemplo_local()
# print(y)  # Esto daría error porque 'y' no existe fuera de la función