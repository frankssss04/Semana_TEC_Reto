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
# 🟡 Pacman - Juego Clásico

Este proyecto es una modificación del **Pacman original** en Python (basado en la librería `freegames`).  
Se realizaron cambios para hacerlo más dinámico, con tableros más ajustados y enemigos mejorados.

---

## 📌 Características principales

- Tablero centrado y con el tamaño correcto.  
- Ajustes en la posición inicial de todos los fantasmas.  
- Movimiento más rápido de los fantasmas.  
- Jugabilidad mejorada para hacerlo más desafiante.

---

## 🚀 Cómo ejecutar el juego

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/usuario/proyecto-pacman.git
Entra al directorio del proyecto:

bash
Copiar código
cd proyecto-pacman
Ejecuta el juego:

bash
Copiar código
python pacman.py
🔧 Modificaciones realizadas
Velocidad de los fantasmas:
Se aumentó la velocidad de movimiento de los enemigos para incrementar la dificultad.

Tablero:
Ahora el tablero está centrado en pantalla y todos los fantasmas aparecen dentro del área de juego.

📦 Dependencias
Este proyecto requiere Python 3 y la librería freegames.
Para instalarla, ejecuta:

bash
Copiar código
pip install freegames

## ⚙️ Cambios en el código

---

### 👻 Fantasmas más inteligentes
```python
Antes:

# Movimiento aleatorio de los fantasmas
plan = choice(choices)

Después:

python
# Movimiento estratégico de los fantasmas hacia Pacman con 20% de aleatoriedad
best = min(choices, key=lambda v: abs((point + v) - pacman))
plan = best if random() > 0.2 else choice(choices)
 ```
⚡ Mayor velocidad de juego
```python
Antes:

python
# Actualización de movimiento cada 100ms
ontimer(move, 100)
Después:

python
# Actualización de movimiento cada 60ms para aumentar la velocidad
ontimer(move, 60)
  ```
    



# 🎮 Juego Paint

Este repositorio contiene una versión **modificada** del juego *Paint* de la librería educativa FreeGames. Se trabajó directamente en el código para completar las funcionalidades pendientes y agregar mejoras específicas. A continuación se explica únicamente lo que se añadió o modificó en el código.

---

## 1) Nuevo color: Amarillo

* En la sección de bindings de colores se agregó la línea:

  ```python
  onkey(lambda: color('yellow'), 'Y')
  ```
* Esto permite seleccionar el color amarillo al presionar la tecla **Y**.

---

## 2) Función `circle(start, end)`

* Antes estaba vacía con un `pass`.
* Ahora calcula el radio como la distancia entre `start` y `end`.
* Se mueve la tortuga a `(start.x, start.y - r)` para que el círculo quede centrado.
* Se utiliza `t.circle(r)` para dibujar y se incluye `begin_fill()` / `end_fill()` para rellenar con el color activo.

---

## 3) Función `rectangle(start, end)`

* Antes estaba vacía con un `pass`.
* Ahora se trazan cuatro líneas que unen las esquinas `(x1, y1)`, `(x2, y1)`, `(x2, y2)` y `(x1, y2)`.
* Se usa `begin_fill()` / `end_fill()` para rellenar con el color activo.

---

## 4) Función `triangle(start, end)`

* Antes estaba vacía con un `pass`.
* Ahora dibuja un triángulo isósceles definido por:

  * `A = (start.x, start.y)`
  * `B = (end.x, start.y)`
  * `C = ((start.x + end.x)/2, end.y)`
* Se conecta A → B → C → A y se rellena con `begin_fill()` / `end_fill()`.

---

## 5) Documentación en el código

* Se añadieron **docstrings** a todas las funciones explicando propósito, parámetros y comportamiento.
* Se usaron **type hints** en las funciones principales (`line`, `square`, `circle`, `rectangle`, `triangle`, `tap`, `store`) para mayor claridad.

---

## Resumen de cambios en el código

1. **Color amarillo agregado**.
2. **Función circle** completada.
3. **Función rectangle** completada.
4. **Función triangle** completada.
5. **Docstrings y type hints** añadidos en las funciones.

Estas modificaciones cumplen con los requerimientos del ejercicio y completan el funcionamiento del juego Paint.
