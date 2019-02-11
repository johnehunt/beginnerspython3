import turtle

WIDTH = 640
HEIGHT = 360


def draw_circle(x, y, radius):
    """ Draw a circle at a specific x, y location.
    Then draw four smaller circles recursively"""
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle( radius)
    turtle.penup()
    if radius > 20:
        draw_circle(int(x + radius /2), y, int(radius / 2))
        draw_circle(x - radius / 2, y, radius / 2)
        draw_circle(x, int(y + radius / 2), int(radius / 2))
        draw_circle(x, int(y - radius / 2), int(radius / 2))


turtle.title('My Turtle Animation')
turtle.setup(WIDTH, HEIGHT, 0, 0)
turtle.hideturtle()

# Speed up drawing process
turtle.speed(10)
turtle.penup()

draw_circle(WIDTH / 2, HEIGHT / 2, 200)

turtle.done()