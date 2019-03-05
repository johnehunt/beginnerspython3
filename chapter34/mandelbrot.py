import turtle

# Set up constants
SCREEN_OFFSET_X = 250
SCREEN_OFFSET_Y = 240

# max iterations allowed
MAX_ITERATIONS = 255

# image size
IMAGE_SIZE_X = 512
IMAGE_SIZE_Y = 512

# Drawing area
MIN_X = -2.0
MAX_X = 1.0
MIN_Y = -1.5
MAX_Y = 1.5


def setup_screen(title, background='white', screen_size_x=640, screen_size_y=320, tracer_size=200):
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    turtle.tracer(tracer_size)
    turtle.bgcolor(background)  # Set the background colour of the screen


setup_screen('Mandelbrot', screen_size_x=IMAGE_SIZE_X, screen_size_y=IMAGE_SIZE_Y, tracer_size=2000)
turtle.colormode(255)  # Indicates RGB numbers will be in the range 0 to 255

# Generate Mandelbrot
for y in range(IMAGE_SIZE_Y):
    zy = y * (MAX_Y - MIN_Y) / (IMAGE_SIZE_Y - 1) + MIN_Y
    for x in range(IMAGE_SIZE_X):
        zx = x * (MAX_X - MIN_X) / (IMAGE_SIZE_Y - 1) + MIN_X
        z = zx + zy * 1j
        c = z
        for i in range(MAX_ITERATIONS):
            if abs(z) > 2.0:
                break
            z = z * z + c
        turtle.color((i % 4 * 64, i % 8 * 32, i % 16 * 16))
        turtle.setposition(x - SCREEN_OFFSET_X, y - SCREEN_OFFSET_Y)
        turtle.pendown()
        turtle.dot(1)
        turtle.penup()

# Ensure that all the drawing is rendered
turtle.update()

print('Done')
turtle.done()
