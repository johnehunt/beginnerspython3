more = 100


def increase(num):
    return num + more


print(increase(10))
more = 50
print(increase(10))


def increment(num):
    return num + 1


def reset_function():
    global increment
    addition = 50
    increment = lambda num: num + addition


print(increment(5))

reset_function()

print(increment(5))
