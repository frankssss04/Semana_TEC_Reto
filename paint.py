"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
"""Juego Paint modificado.

Funcionalidades añadidas (equipo de 2):
- Nuevo color: Amarillo (tecla "Y").
- Dibujar círculo (tecla "c").
- Completar rectángulo (tecla "r").
- Completar triángulo (tecla "t").

Uso:
- Click 1: marca punto inicial.
- Click 2: marca punto final y dibuja la figura seleccionada.
- Teclas de color: K=negro, W=blanco, G=verde, B=azul, R=rojo, Y=amarillo.
- Teclas de figura: l=línea, s=cuadrado, c=círculo, r=rectángulo, t=triángulo.
- "u" deshace el último trazo.

Requisitos:
- Python 3.x
- turtle (incluido en la biblioteca estándar)
- freegames: `pip install freegames`

Estandar de documentación:
- Cada función tiene docstring con propósito, parámetros y efecto lateral.
"""

from turtle import *  # API principal de dibujo
import turtle as t  # para acceder a t.circle sin colisión con nuestra función circle()
from freegames import vector


def line(start: vector, end: vector) -> None:
    """Dibuja una línea del punto start al punto end.

    Args:
        start: Vector con coordenadas (x, y) iniciales.
        end: Vector con coordenadas (x, y) finales.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start: vector, end: vector) -> None:
    """Dibuja un cuadrado usando start como origen y end para calcular el lado.

    El lado se calcula con la diferencia en x (end.x - start.x) como en el
    ejercicio original de FreeGames.

    Args:
        start: Vector con coordenadas (x, y) iniciales.
        end: Vector con coordenadas (x, y) finales.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start: vector, end: vector) -> None:
    """Dibuja un círculo centrado en start con radio = distancia start→end.

    Se posiciona la tortuga en (start.x, start.y - r) para que `t.circle(r)`
    dibuje un círculo centrado en (start.x, start.y).

    Args:
        start: Centro del círculo.
        end: Punto para calcular el radio.
    """
    # Calcular radio como distancia euclidiana entre start y end
    dx = end.x - start.x
    dy = end.y - start.y
    r = (dx ** 2 + dy ** 2) ** 0.5

    up()
    goto(start.x, start.y - r)
    down()
    begin_fill()
    t.circle(r)  # usar alias del módulo para evitar colisión con esta función
    end_fill()


def rectangle(start: vector, end: vector) -> None:
    """Dibuja un rectángulo dado por las esquinas opuestas start y end.

    Traza el polígono en sentido horario: (x1, y1) → (x2, y1) → (x2, y2) →
    (x1, y2) → (x1, y1), y lo rellena con el color activo.

    Args:
        start: Esquina superior-izquierda o inferior-izquierda (no importa).
        end: Esquina opuesta a `start`.
    """
    x1, y1 = start.x, start.y
    x2, y2 = end.x, end.y

    up()
    goto(x1, y1)
    down()
    begin_fill()
    goto(x2, y1)
    goto(x2, y2)
    goto(x1, y2)
    goto(x1, y1)
    end_fill()


def triangle(start: vector, end: vector) -> None:
    """Dibuja un triángulo isósceles dentro del rectángulo definido por start/end.

    Vértices:
        A = (start.x, start.y)
        B = (end.x,   start.y)
        C = ((start.x + end.x) / 2, end.y)

    Args:
        start: Primer vértice y esquina de referencia.
        end: Punto que fija base y altura.
    """
    a = (start.x, start.y)
    b = (end.x, start.y)
    c = ((start.x + end.x) / 2, end.y)

    up()
    goto(*a)
    down()
    begin_fill()
    goto(*b)
    goto(*c)
    goto(*a)
    end_fill()


def tap(x: float, y: float) -> None:
    """Almacena punto inicial o dibuja la figura seleccionada.

    Si aún no hay punto inicial en el estado, guarda (x, y) como inicio.
    En el segundo click, dibuja `state['shape'](start, end)` y limpia el inicio.

    Args:
        x: Coordenada x del click.
        y: Coordenada y del click.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key: str, value) -> None:
    """Guarda `value` en el diccionario de estado bajo la clave `key`."""
    state[key] = value


# --- Configuración de ventana y bindings ---
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Colores (incluye el nuevo color Amarillo: 'Y')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  # NUEVO COLOR

# Figuras
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Inicia el bucle principal de turtle
done()


