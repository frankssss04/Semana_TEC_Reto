# Semana_TEC_Reto
Código para reto semana Tec

# 🐍 Snake - Juego de la Serpiente

Este proyecto es una modificación del juego original **Snake** en Python (de la librería `freegames`).  
Se realizaron cambios para hacerlo más dinámico y desafiante.

---

## 🕹 Controles

- ⬅️ **Izquierda:** tecla `Left`
- ➡️ **Derecha:** tecla `Right`
- ⬆️ **Arriba:** tecla `Up`
- ⬇️ **Abajo:** tecla `Down`

---

## 🔧 Modificaciones realizadas

### 🎨 Colores aleatorios para la serpiente y la comida
Se creó una lista de colores permitidos (excluyendo el rojo) y, al iniciar el juego, se seleccionan dos colores diferentes al azar para la serpiente y la comida:

```python
from random import sample

available_colors = ['blue', 'green', 'yellow', 'purple', 'orange']
snake_color, food_color = sample(available_colors, 2)

```
---

### 🍎 Movimiento aleatorio de la comida
La comida se mueve un paso a la vez de forma aleatoria dentro de los límites de la pantalla:

```python
from random import choice

food_directions = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    possible_moves = []
    for d in food_directions:
        new_pos = food + d
        if -200 < new_pos.x < 190 and -200 < new_pos.y < 190:
            possible_moves.append(d)
    if possible_moves:
        move_dir = choice(possible_moves)
        food.move(move_dir)

```
---

# 🎯 Canon - Juego de Tiro Parabólico

Este proyecto es una modificación del juego original **Cannon** en Python (de la librería `freegames`).  
Se realizaron cambios para hacerlo más dinámico y convertirlo en un juego infinito.

---

## 🔧 Modificaciones realizadas

1. **Velocidad del proyectil (pelota)**
   - Se aumentó la velocidad inicial del proyectil en la función `tap(x, y)`:
     ```python
     speed.x = (x + 200) / 20  # antes era /25
     speed.y = (y + 200) / 20  # antes era /25
     ```
   - Se aumentó el efecto de la gravedad para que el proyectil caiga más rápido:
     ```python
     speed.y -= 0.5  # antes era 0.35
     ```

2. **Velocidad de los targets (balones azules)**
   - Se incrementó la velocidad de desplazamiento horizontal:
     ```python
     target.x -= 2.5  # antes era 0.5
     ```

3. **Juego infinito**
   - Se modificó la lógica para que los targets reaparezcan al salir de la pantalla en una posición aleatoria, en lugar de terminar el juego:
     ```python
     for target in targets:
         if not inside(target):
             target.x = 200
             target.y = randrange(-150, 150)
     ```
Pacman Clásico

Se realizó una versión modificada del clásico juego Pacman para mejorar la jugabilidad y hacerlo más desafiante:

Fantasmas más inteligentes

Los fantasmas ahora persiguen a Pacman de manera estratégica en intersecciones, eligiendo la dirección más cercana a Pacman con un 20% de aleatoriedad, evitando moverse hacia atrás inmediatamente.

Esto se logró modificando la función move() y evaluando opciones válidas en cada paso:

best = min(choices, key=lambda v: abs((point + v) - pacman))
plan = best if random() > 0.2 else choice(choices)


Fantasmas más rápidos

Se redujo el tiempo entre movimientos del juego de 100ms a 60ms usando ontimer(move, 60), haciendo que los fantasmas y Pacman se muevan más rápido y aumentando el nivel de dificultad.

Posiciones iniciales seguras

Se ajustaron las posiciones iniciales de los fantasmas para que aparezcan siempre dentro de los tiles válidos, evitando que algunos no aparecieran en el tablero.

Tablero original y centrado

Se mantuvo el tablero clásico, asegurando que los bordes no generen espacios sobrantes y que Pacman pueda recorrer todo el área disponible.

La puntuación se mantiene visible y se actualiza dinámicamente al recolectar los puntos del tablero.

Game Over

Se añadió un mensaje centrado de “GAME OVER” cuando Pacman colisiona con un fantasma, mejorando la experiencia visual y de feedback para el jugador.

En conjunto, estas modificaciones permiten que el juego sea más dinámico, desafiante y visualmente organizado, logrando una experiencia más entretenida tanto en Cannon como en Pacman.
