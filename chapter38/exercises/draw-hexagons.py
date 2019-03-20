import turtle


# Function to draw a hexagon
def hexagon():
    for _ in range(6):
        turtle.forward(50)
        turtle.left(60)

print('Set up')
# Setup window
turtle.title('Hexagons')
turtle.setup(400, 400, 0, 0)
turtle.speed(10)
turtle.hideturtle()
turtle.pencolor('blue')
turtle.tracer(300)
turtle.penup()
turtle.setposition(-30,50)
turtle.pendown()

print('Start to draw hexagons')
# Draw six hexagons
for _ in range(6):
    hexagon()
    turtle.forward(50)
    turtle.right(60)

# Ensure that all the drawing is rendered
turtle.update()

print('Done')
turtle.done()
