import turtle

def hexagon():
    for _ in range(6):
        turtle.forward(50)
        turtle.left(60)

turtle.title('Hexagons')
turtle.setup(200, 200, 0, 0)
turtle.speed(10)
turtle.hideturtle()

turtle.pencolor('blue')

for _ in range (6):
    hexagon()
    turtle.forward(50)
    turtle.right(60)

turtle.done()
