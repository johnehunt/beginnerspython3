import turtle

# Set up 'constants'

# image size
IMAGE_SIZE_X = 500
IMAGE_SIZE_Y = 500
# Determines depth of tree - try 2 and 1.25 as alternatives
FACTOR = 1.45


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
    draw_tree(length / FACTOR, width - 1)
    turtle.right(60)
    draw_tree(length / FACTOR, width - 1)
    turtle.left(30)
    turtle.color(color)
    turtle.width(width)
    turtle.backward(length)


def setup_screen(title, background='white', screen_size_x=640, screen_size_y=320, tracer_size=200):
    """ Sets up Turtle screen with useful defaults """
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    turtle.tracer(tracer_size)
    turtle.bgcolor(background)  # Set the background colour of the screen


print("Starting ...")
setup_screen('Fractal Tree', screen_size_x=IMAGE_SIZE_X, screen_size_y=IMAGE_SIZE_Y, tracer_size=2000)

# Ensure tree is centred and point in the right direction
turtle.setposition(-50, -140)
turtle.left(90)
turtle.down()

# Draw the tree
draw_tree(100)

# Ensure that all the drawing is rendered
turtle.update()

print('Done')
turtle.done()
