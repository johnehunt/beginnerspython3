def my_function():
    a_variable = 100
    print(a_variable)


a_variable = 25
my_function()
print(a_variable)

max = 100
def print_max():
    global max
    max = max + 1
    print(max)


print_max()
print(max)


def outer():
    title = "original title"

    def inner():
        nonlocal title
        title = "another title"
        print("inner:", title)

    inner()
    print("outer:", title)


outer()
