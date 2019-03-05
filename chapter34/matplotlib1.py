import matplotlib.pyplot as pyplot

print('Set up data')
x = [1, 2, 3, 4, 5, 6, 7, 8, 10]
y = [3, 4, 4.75, 5, 4.6, 4.12, 4, 4.25, 3.75]

print('Configure graph)')
pyplot.ylabel('y values', fontsize=11)
pyplot.xlabel('x values', fontsize=11)
pyplot.title("Simple Plot")

print('Plot the graph and display')
pyplot.plot(x, y)
pyplot.show()
