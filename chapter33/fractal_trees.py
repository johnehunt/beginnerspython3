import turtle
import math

# image size
IMAGE_SIZE_X = 500
IMAGE_SIZE_Y = 500

FACTOR = 1.45

def setup_screen(title, background='white', screen_size_x=640, screen_size_y=320, tracer_size=200):
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    turtle.tracer(tracer_size)
    turtle.bgcolor(background)  # Set the background colour of the screen


setup_screen('Fractal Tree', screen_size_x=IMAGE_SIZE_X, screen_size_y=IMAGE_SIZE_Y, tracer_size=2000)
turtle.colormode(255)  # Indicates RGB numbers will be in the range 0 to 255
turtle.left(90)


def draw_tree(length, width=9):
    color = 'brown'
    if length < 1:
        return
    elif length < 3:
        color = 'green'

    if width < 1:
        width = 1

    turtle.color(color)
    turtle.width(width)
    turtle.forward(length)
    turtle.left(30)
    draw_tree(length / FACTOR, width-1)
    turtle.right(60)
    draw_tree(length / FACTOR, width-1)
    turtle.left(30)
    turtle.color(color)
    turtle.width(width)
    turtle.backward(length)

# Ensure tree is centred
turtle.setposition(-50,-140)

turtle.down()
draw_tree(100)

# Ensure that all the drawing is rendered
turtle.update()

print('Done')
turtle.done()
