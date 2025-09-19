"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice, sample
from turtle import *

from freegames import square, vector


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores permitidos (sin rojo)
available_colors = ['blue', 'green', 'yellow', 'purple', 'orange']
# Elegir dos colores diferentes al azar
snake_color, food_color = sample(available_colors, 2)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Mover la comida aleatoriamente un paso a la vez
    food_directions = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    possible_moves = []
    for d in food_directions:
        new_pos = food + d
        if -200 < new_pos.x < 190 and -200 < new_pos.y < 190:
            possible_moves.append(d)
    if possible_moves:
        move_dir = choice(possible_moves)
        food.move(move_dir)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
