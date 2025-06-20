# CUATRO SEGUIDAS

Proyecto final del curso **Fundamentos de Programación** – Juego interactivo desarrollado en Python.

## Descripción

**Cuatro Seguidas** es un juego de dos jugadores en el que cada uno intenta ubicar **cuatro fichas iguales en línea** (horizontal, vertical o diagonal) dentro de un tablero de 6 filas por 7 columnas.

Este proyecto aplica conceptos clave de programación como:

- Control de flujo
- Funciones
- Manejo de cadenas y estructuras de datos
- Validación de entradas
- Manejo de archivos para persistencia

## Funcionalidades principales

- Ingreso de nombres y elección de fichas (X u O)
- Sorteo aleatorio para decidir quién inicia
- Tablero en modo texto, actualizado en tiempo real
- Turnos alternos entre jugadores
- Opción de jugar “a la suerte” (columna aleatoria)
- Fichas apiladas correctamente en cada columna
- Detección automática de victoria por línea:
  - Horizontal
  - Vertical
  - Diagonal (↘ y ↙)
- Empate cuando el tablero se llena sin ganador
- Registro de puntajes acumulativos por jugador
- Visualización del **Top-5** del historial
- Posibilidad de repetir la partida al terminar

## Sistema de Puntajes

El nuevo sistema de puntajes recompensa tanto la estrategia como el azar de forma justa:

- **100 puntos base por victoria**
- **Penalización**: se descuentan 2 puntos por cada ficha jugada (entre más rápido ganes, mejor)
- **Bonificación por suerte:**
  - +30 puntos si el jugador ganó **usando solo la opción de suerte**
  - +10 puntos si **al menos una jugada fue con suerte**
- **Puntaje mínimo garantizado**: 25 puntos por ganar

Los puntajes se almacenan en un archivo `puntajes.txt` y se acumulan a lo largo del tiempo.

## Requisitos

- Python 3.x
- No se requieren librerías externas

## Cómo jugar

1. Ejecuta el archivo Python (`cuatro_seguidas.py`)
2. Ingresa los nombres y selecciona fichas
3. Realiza jugadas escribiendo un número de columna (1 a 7) o la letra `S` para “tentar a la suerte”
4. El juego terminará si alguien gana o el tablero se llena
5. Visualiza el Top-5 de puntajes y elige si deseas volver a jugar

## Archivos importantes

- `cuatro_seguidas.py` – Código principal del juego
- `puntajes.txt` – Archivo generado automáticamente que guarda el historial de puntajes

## Autor

Desarrollado como parte del proyecto final para el curso **Fundamentos de Programación**  
Universidad / Colegio – 2025
