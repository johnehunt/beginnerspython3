double = lambda i: i * i

print(double(10))

func0 = lambda: print('no args')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))
