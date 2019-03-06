import turtle
from random import randint


def generate_random_colour():
    """Generates an R,G,B values randomly in range
    0 to 255 """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def setup_screen(title, background = 'white'):
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(640, 600)
    turtle.hideturtle()
    turtle.penup()
    turtle.tracer(200)
    turtle.bgcolor(background)  # Set the background colour of the screen

def draw_snowflake(size):
    """ Draw a picture of a snowflake """
    turtle.penup()
    turtle.forward(10 * size)
    turtle.left(45)
    turtle.pendown()
    turtle.color(generate_random_colour())

    # draw branch 8 times to make a snowflake
    for _ in range(8):
        draw_branch(size)
        turtle.forward(size)
        turtle.left(45)

    turtle.penup()

def draw_branch(size):
    """ Draw an individual branch on a snowflake """
    side_branch_size = size / 3
    for _ in range(3):
        for i in range(3):
            turtle.forward(side_branch_size)
            turtle.backward(side_branch_size)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(side_branch_size)
        turtle.left(45)
    turtle.right(90)


setup_screen('Snowflakes')
turtle.colormode(255)  # Indicates RGB numbers will be in the range 0 to 255

print("Drawing snowflakes at random locations")
for _ in range(30):
    x = randint(-320, 100)
    y = randint(-320, 80)
    snowflake_size = randint(1, 5) * 10
    turtle.goto(x, y)
    turtle.right(15)
    draw_snowflake(snowflake_size)

turtle.update()

print('Done')
turtle.done()
